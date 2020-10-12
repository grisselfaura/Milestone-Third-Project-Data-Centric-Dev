# B a s e - F o o d - RECIPE MANAGER (Milestone Project 3) * to be updated

Welcome to my Stream Third Project: Data Centric Development Milestone Project  - Code Institute!

The goal was to create an application that allows users to store and easily access vegan cooking recipes online.
This app also allows the users to share their recipes with other users or just app viewers.
The recipes are built on the Flask framework using MongoDB database which can be filtered by a user on the website using the categories href but also searching for a specific ingredient (if available).
It is a (data-driven) application, and the target audience is any user targeted towards athletes working out for their competition. 

This website is part of my portfolio to present to prospective employers.

Please note this is merely a course project, and then the information on the side is used for that purpose alone. I only use publicly available data for this purpose.
Recipe Data used on this app was provided by Tom Van Oijen in attempt to help him share his experience as turning vegan!
All the photos available in this app were taken by photographer Gaby Van Ingen so please DO ASK permission to use them as they have been share for the solely use of this project.
Recipes can be filtered by category or thorugh the searchbox for example:  ingredients or method words.
One disadvantage is that the recipes where provided using a pdf format in Dutch language and had to be manually entered to test the funcionality of this app. 
When more time is available it would be my wish to attempt to generate a json file database and load this directly to the db Mongo.


## Demo

You can check out the website [here]( https://griss-milestone-3-project.herokuapp.com/)!
[Responsive mockup](http://ami.responsivedesign.is/?url=https://griss-milestone-3-project.herokuapp.com/)!
![Responsive mockup](https://i.ibb.co/Gs6qG2x/Mockups.png "Responsive mockup")


## UX

- My goal on the website design was to make it as easy as possible for the potential users to upload, share and access the information on the site while striving for a simple layout approach.
The website can also be used by people who are only interested in finding recipes to get inspired. 

- For the basic viewers:
* view the recipes from any device (mobile, tablet, desktop).
* view all recipes as a Guest.
* see recipes from other users to get new ideas (unless user's restricted view).
* search any specific recipe, ingredients, methods.
* search recipes by different category.
* easily navigate through the recipes by various main filters.

- For advance viewers:
* Register as a user
* Login and add recipes.[Creatre]
* Add recipes for their account without sharing to other users.
* Easily see all of the recipes submitted under their Profile.
* Get the instruction to make a dish from this site.[Read]
* Edit the recipes they have added.[Edit]
* Delete the recipes they have submitted.[Delete]
* Adm user also to manage the categories where the recipes will become allocated for the filter functionality.

### Design
- The design color scheme choice was keep a simple and elegant combination in order to create a consistent and visual impactful yet straighforward easy-for-the-eye feeling. 

#### Framework

* **[Materialize 1.0.0] = To get a modern and clean layout, I used Materialize as a framework.
* **[jQuery 3.5.1] = Used to manipulate the DOM, for example buttons, and showing / hiding elements
* **[Flask 1.1.2] = Flask is the micro web framework that runs the application

#### Database

For the database, I choose MongoDB following the example from the course. 
The database is made up of the following collections : categories / difficulty / recipes/ users.

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

- Wireframes available.

## Features

- ### Existing Features 
In this section I will describe the front-end features of my project:
1. [Navbar]: consists of the PREPARE FOR YOUR RACE logo which also returns the user to the "Home" page of the application.
             My navbar also has links to "All Recipes", "Your Suggestion", "Contact Us", "Dashboard", "Login". The navbar will appear in all pages
             with the same functions for all links. with an extra feature which highlights the nav bar that is being selected by the user.
         
2. [Home]: consists of one background image along with some information on contacting the webmaster and a link to the contact us page of the site. 
    
3. [All_Recipes]: directs the user to the "All Recipes" page which displays ALL recipes from ALL users which have been entered on the site. 
                The user can then filter or browse through the recipes.
                The can view more information on each recipe by selectign the "See Recipe Description" link which delivers the user to the "Recipe Detail" page. 

4. [Recipe_Detail]: provides users with the recipe details containg a recipe name, description, image (if available), flavour, meal type, race day, sport type, nutrition wise type of meal, author and date posted.

5. [My_Recipes]: provides the user with the recipes that they have added themselves. The user's recipes can be edited and deleted by using the buttons displayed under the recipes.

6. [Login]: when first selected the user will be prompted to create a username to login to the application so that they can add recipes to the database.

7. [Register]:

8. [Dashboard]: once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 4 data charts depicting the number of favourite meal type, favourite sport type, favourite race day and meal associated for the vegan.

9. [Contact_Us]: delivers the user to the contact page. This page displays a blank form, which allows users to contact the website developers to offer feedback and suggestions (not currently wired up to an email address as this is not a real business). 
              Their are also 4 social media buttons so that the user may interact on social networks.

10. [Social_Links]: provides users with links to the website social media pages.

- This site uses the Scrolling Nav feature in Bootstrap  Further work is need to maintained highlighted the tab that has been accessed.
- The navbar is fixed to the top and includes an dropdown Menu for the md-screen that collapses when selected. 

- ### Features Left to Implement

8. [Dashboard]: once logged in the user will be presented with their dashboard which provides a count of their recipes, along with 4 data charts depicting the number of favourite meal type, favourite sport type, favourite race day and meal associated for the vegan.

* In the future i would like to add a a choropath map direcly using dc.js instead of generated using d3.js so as multiple charts can be quickly drawn (code is already started under test_script_chloro_DC_worldmap.html) but due to time limitation is yet pending to integrate all the functions to generate the infographic). 
Fixed with the help from mentor during last session. However the generated map is not centered on the div and cant not be target via css.
* In addition the "About us" and links from the footnote are yet to be constructed.
* Furthermore the links to social media are not linked for the purpose of this exercise.
* Lastly, I would like to be able to have real life data feeding the info-charts. The Database choosed only contained CO2 data for the purpose of this exercise. However on a real case scenario will be more graphics showing additional parameters like temperature and water melting. 



## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

1. HTML
2. CSS
3. Bootstrap (4.4.1)
3.1. Scrolling Nav
3.2. Landing Page
4. Font-awesome (4.7.0) and fonts.googleapis.com used.
5. [JQuery](https://jquery.com) The project uses **JQuery** to simplify DOM manipulation.
6. JavaScript to embedd facebook videos in both the Home and reduce tabs.
7. Dc.js, crossfilter, queue, topojson and D3.js for the data visualization (graph and world data map)
* this website is only available in english
8. Email.js to send Email Directly From JavaScript

## Testing
HTML and CSS code checked for coding errors.
CSS prefixes were checked against https://autoprefixer.github.io/

By clicking on the links in the navbar, the background effect will confirm to the user which tab has been selected. All tabs can be independently accessed without having to go back to the HOME tab. 
*The footnote and social media links as well as the "About us" tab are pending to be developed (future construction) as for the purpose of this project they will not add any further skill . 

1. HOME TAB
-If you try to click on the embeded facebook link it will start displaying and can be paused from the same screen.
-All navigations link work and will redirect you to the desire tab.
-If you try to do a quick sign up for news from the quick CALL TO ACTION FORM, it will redirect you to the Sign up Tab and will prefill you email to the new form.
*Country was by default showing Afghanistan as the country form is being shown in alfabetical display. (Fixed to show a choose value instead)

2. DASHBOARD TAB
-The infographics is interactive. The user can search for any given country from the database.
-In addition hover feature has been added to the charts to highlight user interaction with potential action. The hover over on any pie slice/bar chart/country will display detailed data information.

3. REDUCE TAB
-If you try to click on the embeded facebook link it will start displaying and can be paused from the same screen.
-A color scale map was also added for easy and fun visualization comparing the data of all countries in one single view.

4. SIGN UP TAB
-If you try to submit the contact form with an invalid email address, there will be an error noting the invalid email address. 
-Furthermore, the 'required' attribute is added to all the fields, so if those fields are not filled in, the form will not submit. There will be an error indicating to the user what it is missing.
-When form is submitted a loading gif will be show to indicate the user that the website is loading. Furthermore when submission is successfull the user will see an alert message confirming that submission was or not successfull.

All links will open in a new tab using 'target="_blank" except for the ones that are not yet developed further as previously indicated. 
All links have been manually tested to ensure that they are pointing to the correct destination with exception to the links that are not yet developed/connected as aboved indicated.

-This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness. 
In addition, the site  was tested via  http://ami.responsivedesign.is/ to review how the project looks and works on different screen sizes.

Tabs and sections with interesting bugs or problems discovered during testing:
- Section padding was to big for the UX desing of this project. This was fixed by modifying the scrolling css from Bootstraap as per our needs (fixed).
- * Further work is need to add feature that highlights active pages for example using similar system than the scrollSpy which highlights activated sections (fixed all taps except HOME). 
- The required attribute with the select element in a single choice form needs an empty value attribute or first child element with no text for our sign-in form (fixed).
- Footnote on dashboard was not centered. This was achieved with using the correct grid option from Bootstraap (fixed).
- Showcase and reduce images were all different sizes and therefore dificult to scale up for responsiveness design without using targetting images individually. Aspect ratio strategy was not a successful approach to scale them up at once (fixed when added as images).
- WordlMap responsiveness needs to be address and removed from the header div to avoid shadow bug inside the worldmap div (fixed). Centering WordMap remains pending to be address.
- Facebook embeeded videos are loading are taking very long time to load in the REDUCE TAB (fixed). Error in the console was found when uploading more than one video. Still needs to be further explored however all videos are reachable and react to play/pause. 
- Charts delay a few seconds to load.


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

Go Humongous With MongoDB Atlas
### Content
Most of the text was provided by Tom Van Oijenor and translated from me.
This is only an educational exercise. They can be share upon requested as it is the wish of the writer these recipes reach as many as possible.

### Media
The recipe photos were provided by photographer Gaby Van Ingen so please DO ASK permission to use them as they have been share for the solely use of this project.
Other images used in this site were taken from already published website as this is only an educational exercise.

### Acknowledgements
Special thanks to my Code Institute mentor, for his mentoring during this project and also helping me to sort pagination issues and the javascript behind the form input for the ingredients and methods.
Regarding my desicion to choose for a vegan recipe app, it is my personal passion to promote any kind of projects that promote the care and respect for the animals and resources available in this planet.
.
For the project itself I received inspiration from my tutor and also from other students via Slack. 
The Bootstrap Nav tutorial was found through this tutorial [here](https://startbootstrap.com/templates/scrolling-nav/).
The Bootstrap landing page and footer inspiration [here](https://startbootstrap.com/themes/landing-page/).
The sign up form was inspired on this model [here](https://www.climaterealityproject.org/joinreality?promo_name=Join%20Reality&promo_creative=navig%20ation&promo_position=homepage_top).


## License
[MIT](https://choosealicense.com/licenses/mit/)