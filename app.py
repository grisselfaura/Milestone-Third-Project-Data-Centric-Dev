# -----Imported modules ----- #
import os
import math
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo, DESCENDING
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env


# -----Declaring app name ----- #

app = Flask(__name__)

# -----Config environmental variables saved on the env.py ----- #

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# secret key needed to create session cookies
app.secret_key = os.environ.get("SECRET_KEY")

# -----Creating an instance of Mongo ----- #
mongo = PyMongo(app)


# -----Pagination and sorting params variables ----- #
PAGE_SIZE = 6
KEY_PAGE_SIZE = 'page_size'
KEY_PAGE_NUMBER = 'page_number'
KEY_TOTAL = 'total'
KEY_PAGE_COUNT = 'page_count'
KEY_ENTITIES = 'items'
KEY_NEXT = 'next_uri'
KEY_PREV = 'prev_uri'
KEY_SEARCH_TERM = 'search_term'
KEY_ORDER_BY = 'order_by'
KEY_ORDER = 'order'


# Funcion to perform paginations.
# In the video below I learned how to do paginations using pagination modules
# https://www.youtube.com/watch?v=PSWf2TjTGNY&feature=youtu.be

# -----Pagination macro from my mentor ----- #
def get_paginated_items(entity, query={}, **params):  # function
    page_size = int(params.get(KEY_PAGE_SIZE, PAGE_SIZE))
    page_number = int(params.get(KEY_PAGE_NUMBER, 1))
    order_by = params.get(KEY_ORDER_BY, '_id')
    order = params.get(KEY_ORDER, 'asc')
    order = pymongo.ASCENDING if order == 'asc' else pymongo.DESCENDING

    # If statement to avoid any pagination issues
    if page_number < 1:
        page_number = 1
    offset = (page_number - 1) * page_size
    items = []

    # Updated section allow user to paginate a filtered/sorted "query"
    search_term = params.get(KEY_SEARCH_TERM, '')
    if bool(query):
        items = entity.find(query).sort(order_by, order).skip(
            offset).limit(page_size)
    else:
        if search_term != '':
            entity.create_index([("$**", 'text')])
            result = entity.find({'$text': {'$search': search_term}})
            items = result.sort(order_by, order).skip(offset).limit(page_size)
        else:
            items = entity.find().sort(
                order_by, order
            ).skip(offset).limit(page_size)

    total_items = items.count()

    if page_size > total_items:
        page_size = total_items
    if page_number < 1:
        page_number = 1
    if page_size:
        page_count = math.ceil(total_items / page_size)
    else:
        page_count = 0
    if page_number > page_count:
        page_number = page_count
    next_uri = {
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number + 1
    } if page_number < page_count else None
    prev_uri = {
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_NUMBER: page_number - 1
    } if page_number > 1 else None

    return {
        KEY_TOTAL: total_items,
        KEY_PAGE_SIZE: page_size,
        KEY_PAGE_COUNT: page_count,
        KEY_PAGE_NUMBER: page_number,
        KEY_NEXT: next_uri,
        KEY_PREV: prev_uri,
        KEY_SEARCH_TERM: search_term,
        KEY_ORDER_BY: order_by,
        KEY_ORDER: order,
        KEY_ENTITIES: items
    }


# ---------------- #
#    APP ROUTES    #
# ---------------- #


# ----- HOME ----- #
@app.route('/')
@app.route('/home')
def home():
    categories = list(mongo.db.categories.find())
    return render_template('home.html', categories=categories)


# ----- Read all recipes ----- #
@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    # Page to view all recipes
    recipes = get_paginated_items(
        mongo.db.recipes,
        **request.args.to_dict())  # dictionary
    return render_template('recipes.html', recipes=recipes)


# ----- Filters for categories in home page ----- #
@app.route('/get_recipes_by_category/<category_name>', methods=['GET'])
def get_recipes_by_category(category_name):
    # Page to view all recipes
    recipes = get_paginated_items(mongo.db.recipes, query={
        'category_name': category_name},
        **request.args.to_dict())
    categories = list(mongo.db.categories.find())
    return render_template(
        'recipes.html', title='category_name', recipes=recipes,
        categories=categories, category_name=category_name)


# ----- Page to view individual card recipes ----- #
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=recipe)


# ----- Search functionality in the Home page ----- #
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("query")

    # Search result
    recipes = get_paginated_items(mongo.db.recipes, {
        '$text': {'$search': query}})

    # Page to view all recipes from the search result
    if recipes['total'] > 0:
        return render_template('recipes.html', recipes=recipes)

    # Messages when search yield cero results
    flash("0 matches for \"{}\"".format(query))
    return render_template('recipes.html', recipes=recipes)


# ----- Register a new user ----- #
@app.route('/join_free', methods=['GET', 'POST'])
def join_free():
    if request.method == 'POST':
        # Checks if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please choose a different name.")
            return redirect(url_for('join_free'))

        # Check passwords and match against each other
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if password == password2:
            join_free = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(join_free)

            # put the new user into "session" cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration successful!")
            return redirect(url_for('myrecipes', username=session["user"]))

        else:
            flash("Password does not match")
            return redirect(url_for('join_free'))

    return render_template('join_free.html')


# ----- Sign In to the app ----- #
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensures hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    'myrecipes', username=session["user"]))

            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for('sign_in'))

        else:
            # Username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for('sign_in'))

    return render_template('sign_in.html')


# ----- User's account displayin own recipes ----- #
@app.route('/myrecipes/<username>', methods=['GET', 'POST'])
def myrecipes(username):
    # Grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Use params variables from pagination to sort by "created_date"
    params = request.args.to_dict()
    params[KEY_ORDER_BY] = "created_date"

    # Page user's recipes sorted by "created_date"
    user_myrecipe_paginated = get_paginated_items(mongo.db.recipes, query={
        "created_by": username},
        **params)  # dictionary

    if session["user"] == username:
        return render_template(
            'myrecipes.html', username=username,
            total_user_recipes=user_myrecipe_paginated[KEY_TOTAL],
            title='created_by',
            user_myrecipe_paginated=user_myrecipe_paginated)

    flash("You need to sign in!")
    return redirect(url_for('sign_in'))


# ----- Sign Out from account ----- #
@app.route('/sign_out')
def sign_out():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for('sign_in'))


# ------------------------------------------- #
#    CRUD: Create | Read | Update | Delete    #
# ------------------------------------------- #


# ----- Create own recipes ----- #
@app.route('/add_recipe',  methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        share_recipe = "on" if request.form.get("share_recipe") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "cooking_time": request.form.get("cooking_time"),
            "basic_ingredients": request.form.getlist("basic_ingredients[]"),
            "complementary_ingredients": request.form.getlist(
                "complementary_ingredients[]"),
            "recipe_method": request.form.getlist("recipe_method[]"),
            "recipe_images": request.form.get("recipe_images"),
            "closing_line": request.form.get("closing_line"),
            "share_recipe": share_recipe,
            "created_by": session["user"],
            "created_date": datetime.now().strftime("%d/%m/%Y")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for('myrecipes', username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulty = mongo.db.difficulty.find().sort("sort_difficult", 1)
    return render_template(
        'add_recipe.html', categories=categories, difficulty=difficulty)


# ----- Update user's recipes ----- #
@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if request.method == 'POST':
        share_recipe = "on" if request.form.get("share_recipe") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "cooking_time": request.form.get("cooking_time"),
            "basic_ingredients": request.form.getlist("basic_ingredients[]"),
            "complementary_ingredients": request.form.getlist(
                "complementary_ingredients[]"),
            "recipe_method": request.form.getlist("recipe_method[]"),
            "recipe_images": request.form.get("recipe_images"),
            "closing_line": request.form.get("closing_line"),
            "share_recipe": share_recipe,
            "created_by": session["user"],
            "created_date": datetime.now().strftime("%d/%m/%Y")
        }
        mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for('view_recipe', recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulty = mongo.db.difficulty.find().sort("sort_difficult", 1)
    return render_template(
        'edit_recipe.html', recipe=recipe, categories=categories,
        difficulty=difficulty)


# ----- Delete user's recipes ----- #
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for('myrecipes', username=session["user"]))


# ----- Read all Categories ----- #
@app.route('/get_categories')
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template('categories.html', categories=categories)


# ------------------------------------------- #
#    CRUD: Create | Read | Update | Delete    #
# ------------------------------------------- #


# ----- Add Categories ----- #
@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for('get_categories'))

    return render_template('add_category.html')


# ----- Edit Categories [only admin] ----- #
@app.route('/edit_category/<category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "category_image": request.form.get("category_image")
        }
        mongo.db.categories.update({'_id': ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({'_id': ObjectId(category_id)})
    return render_template('edit_category.html', category=category)


# ----- Delete Categories [only admin] ----- #
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for('get_categories'))


# -----Correct running of the app file  ----- #
# -----In terms of Environmental Variables in Heroku ----- #
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
