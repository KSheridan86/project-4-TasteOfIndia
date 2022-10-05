# Taste Of India

## Introduction
Taste of India is a website built in Django using Python, JavaScript, CSS and HTML. It centers around the very popular Indian cuisine. It enables users to create and share recipes with other users from around the world. It is targetted towards users who enjoy their food and would like to share their recipes with others. Users have the ability to create recipes, and their own profile. They can upload images for use on their recipe or on their profile, link their personal accounts and websites, leave comments on recipes and private message other users.

This is the fourth project for the Code Institute Diploma in Software Development with eCommerce.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication and Full CRUD functionality for Recipes and User Profiles.

![Screenshot of homepage]()

[View the live website on Heroku](https://pp4tasteofindia.herokuapp.com/)


## Table of Contents
* [User Experience Design](#user-experience-design)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Epics](#Epics)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Database Schema](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### The Strategy Plane
*  Taste of India is intended to be a friendly community site for users to create and share their own recipes with others. Users will also be able to find recipes created by other users from around the world. The graphical elements and overall design of the site provide the user with a fun and enjoyable environment.

##### The Sites Ideal User
* Food lover looking to share their favourite recipes with others
* Someone looking to expand their recipe knowledge
* Someone looking for inspiration for new things to try

#### Site Goals

* To provide users with a place to find recipes
* To provide users with a place to share their own recipes
* To provide users with a place to discover new meals

#### Epics

8 Epics were created which were then further developed into 25 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/users/KSheridan86/projects/3)

1. User Profile [#1](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/1)
2. Sign in/out [#2](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/2)
3. Recipes [#3](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/3)
4. Recipe Interaction [#4](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/4)
5. Search Recipes [#5](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/5)
6. Landing page [#6](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/6)
7. Messaging [#7](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/7)
8. Authorisation [#8](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/8)

### User Stories

From the Epics, 25 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Nice-to-Have or Won't Have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. A number of these stories were created based on an ideal scenario of building out the project whilst I knew in the time available it would be unlikely I would complete those stories. The full list of User Stories is available on the project [kanban board](https://github.com/users/KSheridan86/projects/3).

These are the user stories that were completed within the projects first release, by Epic.

	
1. User Profile
	*  Create a User Account - As a User, I would like to be able to create an account, so that I can create and save recipes
	*  Users can view their profile - As a User, I would like to be able to see the details in my user profile, so that I can see what  information other users can see about me
	*  Users can edit their profile - As a User, I would like to be able to edit my profile, so that I can keep the information upto date
	*  Users can delete their account - As a User, I can delete my account, so that I can remove my details and recipes at my request

2. User sign in or sign out
	*  User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can keep my account secure
	*  Features restricted to signed in users - As a Site Owner, I would like to restrict some features of the site to registered users, so that it encourages people to sign up to the site

3. User recipes
	*  Create a Recipe - As a User, I would like to be able to share my own recipes, with family and friends so they can teach them to their own children and have fun experiences together baking
	*  View Recipes - As a User, I can access the recipes on the site.
	*  Update a recipe - As a user, I can update a recipe that I have created, so that I can correct any mistakes I may have made
	*  Delete a recipe - As a user, I can delete a recipe that I have created, so that I can remove it from the site

4. Recipe Interaction
	*  Leave Comments - As a User I can leave comments/feedback on Recipes I like/don't like
	*  Respond to Comments - as a user I can respond to comments left on my or others Users Recipes

5. Recipe searching
	*  Recipe Searching - As a User, I would like to be able to find Recipes, so that I can increase the variety of meals we consume.
	*  Recipe Search - Advanced - As a User, I would like to be able to search the Recipes by title, ingredients or author, so that I can find the ones that match my fancy at that point in time

6. Landing page
	*  As a User I would like to be brought to the landing page upon first visiting the site so that I can see what options are available to me
    *  As a User from the landing page I should have the option to view the Recipes or the Users
    *  As a User on the landing page I should be easily able to Log in or Register for an account

7. Messaging
    *  As a User I would like to be able to send private messages to other Users
    *  As a User I would like to be able to reply to received private messages
    *  As a User I should be able to delete received private messages
    *  As a User access to my inbox should be easy and straight forward

8. Authorisation
	*  As the site developer I would like to restrict Recipe CRUD functionality to logged in Users
    *  As the site developer I would like to restrict User Crud functionality to logged in Users 


[Back to the Top](#table-of-contents)
### The Scope Plane

**Features planned:**
* User Profile - Create, Read, Update and Delete
* Recipes - Users can create, read, update and delete their own recipes
* Other Users Recipes - Users can read and comment on other users recipes
* Profiles - Users can read other users profiles
* Users can login to their account
* Users can logout of their account
* Users need to be registered and logged in to access recipe creation and account editing.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access a recipe site



### The Structure Plane

User Story:

> Create a User Account - As a User, I would like to be able to create an account, so that I can create and save recipes

Acceptance Criteria:
* Given that I am an unregistered user, When I am on the homepage, Then I can see a button to sign up, And, When I click on the button, Then I am taken to the user registration page
* Given that I am an unregistered user, And, I am on the user registration page, When I enter my username, email address and password, And, I click on the register button, Then The system creates me an account, And, signs me in.
* Given that I have an account, And, I am signed into the account, When I have an option to create a recipe, And, when I click on that option, Then I am taken to a page where I can provide the details of my recipe

Implementation:
* Clearly accessible call to action on homepage to register for an account
* Clearly accessible link to login or register within main navigation bar
* Easy to use User registration process
* Clear UX design, prevent unnecessary links to register as a user, if user is already logged in.

User Story:

> Users can view their profile - As a User, I would like to be able to see the details in my user profile, so that I can see what information other users can see about me

Acceptance Criteria:
* Given that I am logged into my user account I can access an option to view my profile

Implementation:
* 

User Story:

> Users can edit their profile - As a User, I would like to be able to edit my profile, so that I can keep the information upto date

Acceptance Criteria:
* Given that I am logged into my account when I am viewing my profile then I should be able to edit the details
* Given that I am logged into my account when I click on the edit button on my profile page then I should be taken to a page to edit the details
* Given that I am not logged into my account when I view my profile page, or anyone elses then I should not be able to see the edit button
* Given that I am not logged into my account when I type in the address to edit my profile, or anyone elses then I should be redirected to the log in page.

Implementation:
* Provide a clearly accessible button on a user's profile for the profile owner only, so they can edit their profile
* Provide a simple and clear edit profile form, linked from the edit profile button

User Story:

Users can delete their account - As a User, I can delete my account, so that I can remove my details and recipes at my request 

Acceptance Criteria:
* Given that I am a registered user when I navigate to my account then I have an option to delete my account
* Given that I am a registered user viewing my account details when I click on the option to delete my account then I am requested to confirm the request
* Given that I am a registered user viewing my account details when I click on the option to delete my account
And, When I confirm the request then My account and the recipes that I have created are deleted
* Given that I am a registered user when I delete my account then I should receive confirmation of the account deletion

Implementation:
* Provide users with an easily accessible option to delete their account
* Provide users with a secure confirmation process to confirm account deletion requests to prevent accidents
* Link all user created elements so that when a user deletes their account, all associated records are deleted.
* Provide the user with confirmation that their account has been deleted.

User Story:

> User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can keep my account secure

Acceptance Criteria:
* Given that I am a registered user, who is not logged in when I navigate to the sign in page and I enter my credentials correctly and press sign in then I am signed into my account
* Given that I am a registered user, who is currently logged in when I click on the sign out link then I am signed out of my account
* Given that I am a registered user, who has signed out of my account when I use the browser navigation buttons such as back button then I can not access information which requires me to be signed in

Implementation:
* Provide login and logout functionality
* Secure restricted pages from access when a user is not signed in.

User Story:

> Features restricted to signed in users - As a Site Owner, I would like to restrict some features of the site to registered users, so that it encourages people to sign up to the site

Acceptance Criteria:
* Given that a user is not registered or signed in, when they look at a recipe then they do not have the ability to create a recipe
* Given that a user is not registered or signed in, when they look at a recipe then they are unable to leave a comment
* Given that a user is not registered or signed in, when they encounter functionality that requires them to be signed in then they are redirected to the login or register page.

Implementation:
* Restrict the ability to save a recipe to authenticated users
* Restrict the ability to create a recipe to authenticated users
* Restrict the ability to like a recipe to authenticated users
* Redirect users who make a request for functionality that requires them to be authenticated users to the login page

User Story:

> Create a Recipe - As a User, I would like to be able to share my own recipes, with family and friends

Acceptance Criteria:
* Given that I am a logged in user when I navigate to the recipe section then I have the option to create a recipe
* Given that I have created a recipe as a logged in user when I save the completed recipe then it is available to other users to view

Implementation:
* Provide authenticated users with a clear option to create a recipe
* Make saved recipes available to other users to view

User Story:

> View Recipes - As a User, I can access the recipes on the site, so that I can follow them at home

Acceptance Criteria:
* Given that I am a user on the site when I navigate to the recipes page then I am presented with a list of the recipes available
* Given that I am a user on the site when I navigate to the recipes page And When I click on a recipe then I am presented with the full recipe details

Implementation:
* Provide users of the site with the ability to access all recipes
* Provide users of the site with the ability to access the full recipe details from the recipe summary card

User Story:

>  Update a recipe - As a user, I can update a recipe that I have created, so that I can correct any mistakes I may have made

Acceptance Criteria:
* Given that I am a registered user who has created a recipe when I navigate to my profile page then I have the option to edit the details of my recipes
* Given that I am a registered user when I navigate to someone else's recipe then I do not get the edit option

Implementation:
* Provide easy access to recipe owners to edit recipes.
* Prevent other users from editing a recipe they did not create
* Provide a method for recipe owners to edit the recipe details - form
* Ensure recipe edits are saved to the database and users are informed of changes

User Story:

> Delete a recipe - As a user, I can delete a recipe that I have created, so that I can remove it from the site

Acceptance Criteria:
* Given that I am a registered user who is logged in, and has created a recipe when I navigate to my profile page then I have the option to delete my recipes
* Given that I am a registered user who is logged in, has created a recipe and I am viewing the recipe I wish to delete when I click the delete recipe button then I receive a confirmation window to confirm that I really want to delete the recipe
* Given that I am a registered user who is logged in, has created a recipe, navigated to that recipe and clicked on the delete recipe button when the confirmation window appears and I confirm the deletion then the recipe is deleted from the system
* Given that I am a registered user, or a non registered user when I navigate to a recipe page that I did not create then I do not have the option to delete the recipe

Implementation:
* Provide recipe owners with the option to delete their recipe
* Provide recipe deletion requests with a confirmation window to prevent mistakes
* Ensure confirmed deletion requests are processed on the database correctly.
* Prevent unauthorised access to recipe deletion functionality

User Story:

> US#33 - Recipe Searching - As a User, I would like to be able to find recipes, so that I can increase the variety of meals we consume.

Acceptance Criteria:
* Given that I am a user of the website when I navigate to the homepage then I can access a link to all the recipes
* Given that I am a user of the website when I want to view a specific recipe then I can access the full recipe details by clicking on the recipe

Implementation:
* Provide ease of access to full recipe list
* Provide users with the ability to access full recipe details from the summary card

User Story:

> Recipe Search - Advanced - As a User, I would like to be able to search the recipes, so that I can find the ones that match my fancy at that point in time

Acceptance Criteria:
* Given that I am a user of the website when I navigate to the site then I can access a search function to access related recipes
* Given that I am a user of the website when I search the recipes then the search results show relevant recipes

Implementation:
* Provide all users the ability to search the recipes
* Enable search query to match with recipe title and recipe author

User Story:

> Clear Recipe Layout - As a User, I would like clear instructions on how to make each recipe, so that I am able to follow along as an inexperienced cook


Acceptance Criteria:
* Given that I am a user when I click on a recipe to view the details then The instructions on how to make the recipe are clearly accessible
* Given that I am a user accessing the recipe details when I access a recipe instructions then they should be easily to identify the order in which they should be followed

Implementation:
* Provide users with a clean and simple recipe detail page layout
* Provide users with a easy to follow instruction list 

User Story:

> Responsive Templates - As a Site Owner, I would like my site to be fully responsive, so that Users accessing the site from different devices have an enjoyable experience

Acceptance Criteria:
* Given that I am a user accessing the site on my smartphone when I navigate through the site then all pages should be formatted to my device
* Given that I am a user accessing the site on my tablet when I navigate through the site then all pages should be formatted to my device
* Given that I am a user accessing the site on my laptop when I navigate through the site then all pages should be formatted to my device screen
* Given that I am a user accessing the site on my desktop computer when I navigate the site then all pages should be formatted to suit my screen size

Implementation:
* Provide users with a fully responsive site that responds to mobile, tablet, laptop and desktop sized devices


#### Opportunities

Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide users the ability to create an account ** | 5 | 5 |
| ** Provide users the ability to create recipes ** | 5 | 5 |
| ** Provide users the ability to edit recipes ** | 5 | 5 |
| ** Provide users the ability to view recipes ** | 5 | 5 |
| ** Provide users the ability to delete recipes ** | 5 | 5 |
| ** Provide users the ability to edit their account ** | 5 | 5 |
| ** Provide users the ability to view other accounts ** | 5 | 5 |
| ** Provide users the ability to delete their account ** | 5 | 5 |
| ** Provide users the ability to access the site on any device ** | 5 | 5 |
| ** Provide users the ability to search the site for recipes ** | 4 | 5 |

### The Skeleton Plane
#### Wireframe mock-ups

Home page: The home page provides the user with a clear understanding as to the purpose of the site. The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using.

![Home Page Wireframe]()

Users have the ability to create recipes to share with other users. The emphasis of the design is to provide a clear recipe layout that can adapt to any size device. Clearly seperating general information, ingredients and steps.

![Recipe Detail Desktop Wireframe]()

Users also have the ability to create a personal profile. From this profile users can access the recipes they have created and those that they have liked quickly and easily. They can also control the information they share with other users.

![User Profile Desktop Wireframe]()

Users will have the ability to search for recipes based on a search query of their choice. To aid in the discovery of different recipes, each recipe will be displayed in the form of a summary card from which the user can access the full recipe details.

![Recipe search page with results desktop wireframe]()

Users will have the ability to search for other users, so if there is a user who's recipes they like regularly, they can access their profile to find out more information about them.

![Profile search page with results desktop wireframe]()

Wireframes were also produced for each major page for both mobile and tablet devices. With the intention of the site being fully responsive so that no matter the device size the user is viewing the site on, it will display accordingly.

* [Home page mobile wireframe]()
* [Home page tablet wireframe]()
* [Recipe detail page mobile wireframe]()
* [Recipe search page mobile wireframe]()
* [Recipe search page tablet wireframe]()
* [User profile search results page mobile wireframe]()
* [User profile search results page tablet wireframe]()

#### Database Schema

Several custom models were predicted to be required when building the site. A Profile Model was included. In order for the users to create Recipes a custom recipe model was required, which would be linked to the User Profile through using the profile as a foreign key. The database schema was planned using [DrawSQL app](https://drawsql.app/). Limitations of the app prevented labelling the field types correctly, it did not include the option to override the types available and did not include textarea, cloudinary fields or url fields. The models in the app reflect the true field choice.

![Database Schema Diagram]()

### The Surface Plane

#### Design

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected the colour scheme using the adobe colour selector. The colour schemes were checked for colour contrast to ensure that the appropriate colours were used for a high level of colour contrast to maximise accessibility for users.

##### Typography 


##### Images


## Features
#### Home page
A welcoming homepage was built to welcome the user to the site and clearly convey the sites purpose. The call to action for the user to search for recipes is at the top of the main page, with a large, hero like welcome message appearing just below. At the bottom of the page a clear comparison showing users the benefits of signing up to the site is displayed.

![Home Page]()

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require.

![Logged in User Nav Bar]()

A secondary user menu is available to users who are logged into the site, users who are not logged in receive a login/register link in its place

![logged in user nav bar user menu open]()

The navigation bar and the user menu are fully responsive.


#### Footer
A common footer is utilised through out the site to encourage users to visit the social media sites of the main site. They currently direct users to the generic social media sites, all external links open in a new tab.

![footer]()

#### Recipe Search
Users have the ability to search the database of recipes against the recipe title, ingredients and the author of the recipes username.

![Recipe search Desktop]()

#### Recipe Cards
Search results appear in the form of recipe summary cards. The cards show the user the title of the recipe, the featured image of the recipe, and the author of the recipe, if they have chosen to create a username. This allows the users to quickly identify the recipes they would like to look at in more detail.

##### Standard Recipe Card
![Standard Recipe Card]()

#### User Profile
Users have the ability to create a profile. If they choose not to complete the profile, the area they choose not to complete lets the user know what would appear in that section, it also informs them if other users can see the message or not. The user profile page provides the profile owner with quick access to edit and delete functionality.

![Owner Profile Page]()

Users can also access their own recipes easily.

![Easy Access to own and liked recipes]()

#### Edit Profile Page
Users have the ability to edit their profiles on the site. The edit profile page is clearly laid out. The current profile image is displayed with the user having the ability to change the image.

![Edit profile page]()

#### Create/Edit Recipe Page
Users have the ability to create and edit their recipes. The create recipe and edit recipe page is clearly laid out.

##### Recipe Form
![Recipe Form]()

#### Access to Edit Recipe and Delete Recipe Functionality
Only the users that create the recipe can edit it or delete it. If the authorised user is the recipe author, then the edit recipe and delete recipe buttons will appear on the recipe detail page. 

##### Own recipe detail card

##### Other users recipe detail card



## Future Enhancements
There are several items of functionality that I would like to add in the future. I have left the original user stories that were developed in the project kanban board as future enhancement opportunities.
The key areas I would like to add to the site in the future are:

* The ability for users to login via social networks such as google or facebook

## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here]().
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the acceptance criteria of the user stories listed above were met. The commit at which the functionality requirements for each user story were met is listed in the issues section of the repo. It was applied to each issue before it was closed and marked as completed.


#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.

[Testing Schedule Overview](/assets/testing/test-schedule.pdf)

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing
All code files were validated using suitable validators for the specific language. The full details can be found in the testing.md file.
All code passed the validation, with only code generated by other parties producing errors or warnings.
* Django built in code within the settings file produced five line length errors. 
* Bootstrap code produced 260 warnings in the CSS validation. 
* Fontawesome cdn produced 6 HTML validation errors relating to css variables within the cdn css code. 

#### Notable Bugs

The use of CloudinaryFields for the images in the recipe and profile models does not enforce input validation to image file types. I could also not find anything related to enforcing the file types within the cloudinary documentation. This enabled users to attempt to upload non-image file types. To combat this issue, within the view that handles the form submission, I utilised a try, except statement that attempts to upload the file, but if the upload fails due to the file type error on the cloudinary servers, it gracefully handles the error and provides the user with an error message informing them what happened and why. This prevents users from breaking the functionality of the site, whilst still enabling them to correct the file they are trying to upload.

No other bugs of note were found during development of the site. Several minor bugs were encountered due to small logic mistakes or scenario's unaccounted for, however these were found during the several rounds of testing and corrected. There are no known bugs left in the site.

#### Technologies Used

* Python
* Django
    * Django was used as the main python framework in the development of this project
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* JavaScript
    * Custom JavaScript was utilised to allow Users to close site messages
* Bootstrap 5
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* VS Code was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project
* Balsamiq was utilised to develop wireframes for the site from which the design was based
* DrawSQL.app was used to develop the database schema during development

#### Resources Used

* The Django documentation was used extensively during development of this project
* The Cloudinary documentation was used extensively during development to setup the configuration between django and the cloudinary apis
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.


##### Other Libraries Used

## Deployment

The site was deployed via Heroku, and the live link can be found here - [TasteOfIndia](https://pp4tasteofindia.herokuapp.com/)

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    * Log into GitHub or create an account.
    * Locate the repository at https://github.com/MattBCoding/pp4-the-pantry .
    * At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/MattBCoding/pp4-the-pantry
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

## Acknowledgements

I would like to acknowledge the help and support given by my mentor Chris Quinn, he is never short of good ideas. 
All of the students in my own study group aswell as all the students in the wider Code Institute Slack channels. My cohort Facilitator [Kasia](https://github.com/bezebee) and all of the staff at Code Institute. The sense of comraderie among all of these individuals has helped me to feel at home on my journey to a new career in programming.

## Author Info

- [GitHub](https://github.com/KSheridan86)
- [Linkedin](https://www.linkedin.com/in/kensheridan86/)


[Back to the Top](#table-of-contents)