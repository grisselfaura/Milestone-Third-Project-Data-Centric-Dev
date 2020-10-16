# B a s e - F o o d - RECIPE MANAGER (Milestone Project 3)

Welcome to my Stream Third Project: Data Centric Development Milestone Project - Code Institute!

The goal was to create a (data-driven) application that allows users to store and easily access VEGAN cooking recipes online.
A friend of mine has recently become vegan and he wrote a pdf of easy to make vegan recipes which he would like to share with many others.
For this reason i decided to contribute to this nice cause by using his recipe database for my project. It is our future wish to be able 
to share this amoung relatives, friends and whoever is interested.
This app will allows the users to share their recipes with other users or just to view the recipes as guests.
The recipes are built on the Flask framework using MongoDB database which can be filtered by a user on the website using the categories images carrousel [link] 
and also to retrieve recipes by searching for specific ingredients (when a match is available).

This website is part of my portfolio to present to prospective employers.

Please note that this is merely a course project, and the information on the site is used for such purpose. I only used publicly available data in combination with 
the recipe data with the consent of the authors.
The recipe data used on this (data-driven) application was provided by Tom Van Oijen in attempt to help him share his experience as becoming vegan!
All the photos shared through this app were taken by photographer Gaby Van Ingen so please DO ASK permission to use them as they have been share for the solely use of this project.
Recipes can be filtered by category link or thorugh the searchbox for example using: ingredients or method words.
One large disadvantage is that the recipes where provided in a pdf format in Dutch language and had to be manually entered in order to test the funcionality of this application. 
In the future it is my wish convert this file to a json file database and load this directly to the db Mongo.


## Demo

You can check out the website [here]( https://griss-milestone-3-project.herokuapp.com/)!
[Responsive mockup](http://ami.responsivedesign.is/?url=https://griss-milestone-3-project.herokuapp.com/)!
![Responsive mockup](https://i.ibb.co/Gs6qG2x/Mockups.png "Responsive mockup")


## UX

- My goal for this application was to make simple easy to use design for the potential users to upload, share and access the information on the site.
The website can also be used by people who are only interested in finding recipes to get inspired. 

- For the basic viewers:
* view the recipes from any device (mobile, tablet, desktop).
* view all recipes as a Guest.
* see recipes from other users to get new ideas (unless user has restricted the recipe access).
* search any specific recipe by name, ingredients, methods.
* easily navigate through the recipes using the categories filters.

- For advance viewers:
* Register as a user
* Login and add recipes. [Create]
* Login and add categories for ADMIN user.[Create]
* Add recipes for their account without sharing to other users. [Create + extra feature]
* Easily see all of the recipes submitted under their Profile. [Read]
* Easily see all of the recipes submitted to this site. [Read]
* Edit their own recipes. [Edit]
* Delete their own recipes for admin. [Delete]
* Admin user also to manage the categories where the recipes will become allocated for the filter functionality.

### Design
- The design color scheme choice was keeping a simple and elegant combination in order to create a consistent and visual impactful yet straighforward easy-for-the-eye feeling. 

#### Typography

The following fonts were used:

* **Fredericka** was used for the recipe names.
* **Open Sans Condensed** was used for the Form: description/subheading.
* **Caveat & family Indie Flower** was used for the Form: Ingredients.
* **Architects Daughter familyIndie+Flower** was used for the Form: Methods.
* **Indie Flower** was used for the Form: closing line.
* **Gloria Hallelujah** was used for the general text in myrecipes.html.
* **Josefin Slab** was used for the general text in myrecipes.html.

#### Icon

A combination of [Materialize icons] & [Fontawesome] has been used for this project.

- Wireframes are available [here](https://github.com/grisselfaura/Milestone-Third-Project-Data-Centric-Dev/blob/master/static/wireframes)

## Features

- ### Existing Features 
In this section I will describe the front-end features of my project:
1. [Navbar]: consists of the application logo which also returns the user to the "Home" page of the application.
            My navbar also has links to "Recipes", "Login" and "Join-free. 
            The navbar will appear in all pages and comes with an extra feature which highlights the nav bar that is being selected by the user.
            In addition, there is a side **Mobile Collapse Button* for mobile view.
            Visitors to the site who are not logged in, can only access the links above.
         
2. [Home]: consists of one background image along with some information regarding "why to become vegan" and a carrousal showing the recipes categories available in the application. 
    
3. [Recipes]: directs the guest or registered user to the "All Recipes" page which displays ALL the available recipes from ALL the users which have been entered and marked as SHARE
            in the application. 
            The ADMIN user can view all the recipes irrespectively of the "shared" bottom.
            The guest or registered user can use the search functionality to find a specific recipe.
            The guest or registered user can browse through all the recipes via the pagination links or can simply select an specific recipe.
            The guest or registered user can view more information on each recipe by selecting the reveal plus-circle button for example: the "See Recipe Description" link which 
            delivers the viewer
            to the "Recipe Detail" card. 

4. [View_recipe]: the viewer can access the view_recipe card by clicking in the image of the recipe. The user will be able to acccess the edit/delete buttons only when it is the 
                recipe_owner. 
                The recipe card provides the viewer with the recipe details: the recipe name, description, image (if available), category, difficulty, cook time, ingredients, 
                methods, author and date posted. The registered user can also view their own recipes via the myrecipes nav (when logged in).

5. [My_Recipes]: provides the user with the recipes that they have added themselves. The user's recipes can ONLY be modified by the recipe_owner by editing and deleting via the 
                buttons displayed under the recipes. Recipes are sorted by created date.

6. [Register]:  guest users can use the site as a guest, but some features are not available unless logged in.
                A built-in authentication and authorization to check certain criterias had been incorporated before an account is validated. 
                All passwords are hashed for security purposes!

7. [Login]: registered users can logged in by entering their username and password. Checks has been incorporated to verify that the username exists and the username/password is 
            correct.

8. [Logout]: registered user can logged out of their account.

8. [Add_Recipe] [Edit_Recipe] [Delete_Recipe]: registered users can add recipes using the recipe form available. In addition recipe_owners can edit or delete their recipes and 
                                                decide if they would to make their recipe available for public display.

9. [FlashMessages]: The application uses the flask messages method to communicate important events to the user and make it more user friendly.


- ### Features Left to Implement & Updates

1. [Dashboard]: in future once user is logged in : the user will be presented with their dashboard which provides the total number of their recipes, along with data charts with 
    their favourite meal, the most liked recipes, how many times did other users view or liked their own recipes.
2. [Social_Links]: provisional links to the social media pages.
3. [Nav]: Further work is needed to maintain highlighted the current nav that has been accessed.
4. [Add/delete button from recipe form] Javascript was targeting the wrong div for adding/removing ingredients/steps. The add plus button was cloning all the lines entered 
    during the add_recipe and delete button was not possible on the lines added during the add_recipe. Error has been fixed and now is targeting the correct elements.
5. [Translation]: google translation button feature to be added. Failed attempt as Google translation built-in functionality is overrided by the css from Materialize.
6. [Search]: was affected by the introduction of pagination function but the bug has been repaired with help from Tutor.
7. [Search functionality & filters]: discussion to add more filters. To be implemented in the future when database is expanded.
8. [Pagination]: paging errors when viewing from category filter. The search_term parameters from pagination were breaking the code code when moving through pages. 
    This was fixed with help from Tutor. 
9. [Pagination]: pending to be added for the myrecipes nav. This has now been implemented.
10. "Created_date" needs to be blocked in the edit_recipe. To be implemented in the future.
11. Image responsivesize is offsetting the cards panel sizes. Cards height had been set to reduce the offsetting.
12. Category hrefs from the view_recipe cards are not conected to the categories database. To be implemented in the future with a larger database.
13. Errors 404: locate potential error for non-exisitng pages. To be implemented in the future.
14. Change debug to FALSE.


## Technologies Used

#### Languages

* **[HTML] used as the mark-up language.
* **[CSS] used as the base for cascading styles.
* **[JavaScript] used mostly for DOM manipulation.
* **[Python3] used to run the backend application.
* This website is only available in English.

#### Libraries

* **[Google_Fonts] provided the fonts used throughout the project.
* **[Font_Awesome] provided the the icon set.
* **[Materialize] used as the CSS framework for the project.
* **[jQuery] used as the primary JavaScript functionality to simplify DOM manipulation.
* **[Flask] is the micro web framework that runs the application.
* **[Jinja] is the default templating language for Flask and it is used to display data from the python application in the frontend html pages.
* **[PyMongo] enable the python application to access the Mongo database.
* MATH and datetime were also used for basic math operations and datetime to obtain recipe creation_date.

#### Tools

* **[GitHub]** provides the hosting for software development control version using Git.
* **[Am I Responsive]** to test responsiveness and to create the images portrait in this readme file.

#### Framework

* **[Materialize] = To get a modern and clean layout, I used Materialize as a framework.
* **[jQuery] = Used to manipulate the DOM, for example buttons, and showing / hiding different elements.
* **[Flask] = Flask is the micro web framework that runs the application.

#### Database

For the database, I choose to work with MongoDB [MongoDB Atlas] following the example provided from the course. 
The database is made up of the following collections: categories / difficulty / recipes/ users.

## Testing
### Validation

- **HTML:** I have used https://validator.w3.org/ in order to validate the HTML code.

- **CSS:** I have used https://jigsaw.w3.org/css-validator/ in order to validate the CSS code & CSS prefixes were checked against with https://autoprefixer.github.io/

- **JavaScript:** I have used https://jshint.com/ in order to check the JavaScript code.

- **[PEP8 Online]:** (http://pep8online.com/) was used to validate Python.

# Manual Testing
By clicking on the links in the navbar, the background effect will confirm to the user which tab has been selected. All tabs can be independently accessed without having to go 
back to the HOME tab. 
*The social media links are pending to be developed (future construction) as for the purpose of this project they will not add any further skills. 

 * **REGISTER** 
I've created my own account, and 3 other accounts to confirm that the authentication and validation for creating account worked as expected.

* **LOG IN AND LOG OUT** * Logging To An Existing Account
The accounts created were tested by attempting log in and out. No issues found or expected. Using a non-existing user or incorrect password yield errors. Flash messages confirmed
the user if attempts to log in/out were successful.

* **Add | View | Edit | Delete a Recipe**
I've created more than 30 recipes from 4 different accounts in order to:
    Show the application functionality.
    Test pagination displaying 6 cards for page from allrecipes and myrecipes. Test the prev and next pagination buttons.
    Test share_recipe button and search database.
    The data validation in the add recipe form is solid and only accepts input in the correct format.
    * Recipes has been modified in several ocassion to test the functionality of updating/deleting a recipe to the database and for a user-friendly display. 
    Tested edit and delete recipe buttons were available for the owner of the recipes, and disabled for non-owners (message display via tooltips). 
    To prevent user from deleting a card mistake extra checks were added. When the delete button is pressed, a modal asks the owner to confirm deletion. 
    If the recipe_owner selects cancel, they are taken back to all the recipes and recipe_owner selects confirm the recipe gets deleted.

**Known Issues**

Pagination - Pagination was not working from the search result. For setting the pagination for search result and the recipes, my mentor Guido guided me and
together we solved the pagination issues using the pdb debugger.

All the social links will open in a new tab using 'target="_blank". 
All links have been manually tested to ensure that they are pointing to the correct destination.

-This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) 
to ensure compatibility and responsiveness. 
In addition, the site  was tested via  http://ami.responsivedesign.is/ to review how the project looks and works on different screen sizes.

Tabs and sections with interesting bugs or problems discovered during testing:
- images size were uploaded in different sizes and responsiveness was out of proportion.
Aspect ratio strategy was not a successful approach to scale them up at once (image size might vary depending on selected image). Testing has been done with similar size images.


## Deployment

To run locally, you can clone this repository directly into the editor of your choice by pasting
```
 `git clone  https://github.com/grisselfaura/Milestone-Third-Project-Data-Centric-Dev.git` into your terminal. 
```
To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.


The following section describes the process to deploy this project to Heroku.

1. Ensure all required technologies are installed locally, as per the [requirements.txt] file.
2. Login to Heroku, using 'heroku login' command. Input Heroku login details.
3. Create new Heroku app, using 'heroku apps:create appname' command.
4. Push project to Heroku, using 'push -u heroku master' command.
5. Create scale, using 'heroku ps:scale web=1' command.
6. Login to Heroku and select newly created app.
7. Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
8. From 'More' menu on the top right, select 'Restart all dynos'.
9. View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
10. Deployed via Heroku:..............


## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 

## Credits
Go Humongous With MongoDB Atlas course tutorial 

### Content
Most of the text was provided by Tom Van Oijenor and translated by me.
This is only an educational exercise. Recipes can be share upon requested.

### Media
The recipe photos were provided by photographer Gaby Van Ingen so please DO ASK permission to use them as they have been share for the solely use of this project.
Other images used in this site were taken from already published website as this is only an educational exercise.

### Acknowledgements
Special thanks to Tim, Steven and Xavier from the tutor support. Thanks a mil to Michael for helping me with the javascript issues behind the form input for the 
ingredients and methods and to my Code Institute mentor, for his support during this project and also helping with the pagination issues and introducing me to pdb debugger.
Regarding my desicion to choose for a vegan recipe app, it is my personal passion to colaborate with any kind of projects that promote the care and respect for the animals 
and resources available in this planet.

For the project itself I received inspiration from my tutor and also from other students via Slack. 
The pagination tutorial gave me a basic understanding on pagination to understand different templates approaches [here](https://www.youtube.com/watch?v=PSWf2TjTGNY&feature=youtu.be).
The javascript for the recipe form was based and improved version from [here](https://github.com/stephyraju/spiceworld/blob/master/static/js/main.js).
The recipe app functionality was based on the task flask tutorial - The Flask Framework Lessons provided by Tim.


## License
[MIT](https://choosealicense.com/licenses/mit/)