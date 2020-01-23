# Rugby World XV

## By Stephen Whittington

Rugby World XV is a single page application built with the flask
web framework along with Mongodb for data storage. It allows users
to import their favorite players and create an allstar/rugby world cup squad,
which they can edit anytime and add as many players as they want.
The site is easy to navigate with a simple layout and is responsive on
mobile and desktop.

## UX Process

[Link to my figma mockup](https://github.com/StephenWhittington/rugby-world-xv/blob/master/static/images/Pick%20Your%20World%20XV.png)

I started with a desktop mockup using figma by focusing on the core aspects
of what the user should experience, a well responsive and easy to use webpage.
With easy navigation,forms and input fields for the user to experience, The user results
then returned for them to read update or delete. The website is aimed at the fanbase of rugby
but it is easily navigated by anyone.

The user wants to be able to add players of their choice and create a team
that is unique to them. And this webpage helps them do that with its simple layout
and navigation, Also with its easy to use forms and input fields.

### User Stories

#### **list of user stories.**

* **Add A Player**: The user clicks on the Add Players nav bar and it takes them to a page
where they can add a player of their choice. The form consists of player name, country, club team,
position and height. After the user has filled in the form they can then click on the add player button
which then takes them to the create team page and the player they entered can be found
by the position.

* **Creating A Team**: After the user has added 15 players they want, They can then create their team by
clicking on the Create Team nav link which takes them to another page to enter the players
they have added into a full 1-15 rugby squad. Once the user has selected a full squad they can then
click on the Add Team button which then takes them to the home page where they can view
the created team.

* **Delete A Team**: The user can delete a team by clicking on the DEL
button, If the user selects delete it will remove that team from the database but the players
will still be available to anyone else creating a team.

* **Edit/Update A Team**: After the user clicks on the EDIT button it takes them to another
Create Team page only this one shows the players in that team already. The user can then select 
any player they want to replace with another then hit the edit team button,
which then updates their team with the information selected and returns them
to the home page to view the updated team.

# Features 

## Existing Features

* **Responsive nav/sidebar** - A responsive and easy to use navbar that collapses into a side bar when screen is viewed
on mobile.

* **Collapsible Accordion** - A collapisble accordion that drops down and shows the users team
with a rugby positons layout. 

* **Forms/Input fields** - Easy to read and understand forms and input fields for the user to navigate and enter
their information. 

* **Buttons** - Buttons when selected that either save/edit/delete or add to the database, also taking the user to the correct
path.

* **Background Image** - A background image of the most recent rugby world cup logo to add to the sites design.

## Features Left To Implement 

* Adding a flask session login for user security.

* Add another page showing more information on players/teams

# Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
  
    * The website uses Semantic Markup Language as its foundation.   

* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

    * The website uses Cascading Style Sheets to implement design and customization.
    
* [Python3](https://www.python.org/download/releases/3.0/)

    * The website uses python3 a high-level, interpreted, interactive and object-oriented scripting language,
    which is highly readable and uses English keywords frequently whereas the other languages use punctuations.
    
* [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))

    * The website uses the Flask web framework to compile modules and libraries, and it helps develop
    the web application without any low-level code.
    
* [MongoDB](https://www.mongodb.com/)

    * The website uses MongoDB for its cross-platform and open-source document-oriented database.
    I have used this easy to use database to create,update,store and delete all of the information.
    
* [Materialize](https://materializecss.com/)

    * For this website i decided to use Materialize instead of bootstrap, for its
    reusable UI components that help in constructing attractive, consistent, 
    and functional web pages and web apps while adhering to modern web design.
    
* [jQuery](https://jquery.com/)

    * The website uses JQuery The Document Object Model (DOM) to simplify manipulation.
    
* [Jinja2](https://en.wikipedia.org/wiki/Jinja_(template_engine))

    * The website uses Jinja2 a web template engine for the Python programming language which
    provides Python-like expressions while ensuring that the templates are evaluated in a sandbox.

# Testing 

### User Story Tests Completed   
    
1. **Collapsible-Accordion**:
    1. Click on the arrow next to the del/edit buttons.
    2. A callapsible body element showing the users selected team in a rugby 15 set up appears.
    3. Confirmed that the when the user selects the arrow the information is shown.

1. **Del/Edit Buttons**:
    1. If the user selects the del or edit buttons.
    2. A team is deleted when the delete button is selected, when the edit button is selected
    the user can update any position with another player and update their team.
    3. Confirmed that when the user selects any of the buttons it updates or deletes from the database.

1. **Add Players Form**:
    1. When the user fills in the required form.
    2. Once the user has entered the player information they want, They can then click
    on the add player button which then saves the player to the database and takes them to the create team page.
    3. Confirmed that the player is added to the database and forwards the user to the create team page.

1. **Create Team Form**:
    1. The user fills out a form with a team name and the positions with the players they want in the team.
    2. After the user has named a team and selected the players they want in the specific positions, They can
    select save team which then saves the team to the database and the user is taken to the home page to view the results.
    3. Confirmed that when form is filled in and the save team button is selected, it adds the result to the database
    and takes the user to the home page.

1. **Side Navbar**:
    1. Click on the nav icon when in mobile or tablet view.
    2. A side bar showing the links is shown to the user and they can select which page they want to
    visit.
    3. Confirmed that the webpage has a responsive sidebar that is easy to use and goes to the correct paths.

### How it looks/works on different browsers and screen sizes

Testing my project on different screen sizes was easy with Meterialize, I started with
a desktop layout and added styling for mobile towards the end of the project. I tested the page
on the three most common web browsers Chrome/IE and Mozzila Firefox and i am happy
with how it looks on all of them. The only things i had to change were the columns for
the create team and update team pages to look better responsive on mobile and tablet.

## Bugs And Problems

I havent found any major bugs or issues with my project it works as it is supposed, but there
is a minor issue with users being able to update delete or change others information.

    * I understand that this can be fixed with a flask session/login that is linked to the
    users username, that then will store that users data but only they can make changes to it.
    
## Compatibility

To make sure users have a broad range of accessibility, i have tested my project on 3 major browsers in both desktop and mobile size.

* Chrome
* Mozilla Firefox
* Internet Explorer

## Testing my code via validation

I ran all my code through both a CSS/HTML5 and Python-tester validator i had a few errors but my page works regardless of them. 
I understand that most of the errors are due to jinja/python being used inside my html templates, which doesn't effect the project
overall.

* **base.html** -  I ran this page through [https://validator.w3.org/](https://validator.w3.org/) and encounterd 8 errors and 1 warning.
* **addplayers.html** -  I ran this page through [https://validator.w3.org/](https://validator.w3.org/) and encounterd 3 errors and 1 warning.
* **editteam.html** -  I ran this page through [https://validator.w3.org/](https://validator.w3.org/) and encounterd 66 errors and 1 warning.
* **manageteam.html** -  I ran this page through [https://validator.w3.org/](https://validator.w3.org/) and encounterd 15 errors and 1 warning.
* **team.html** -  I ran this page through [https://validator.w3.org/](https://validator.w3.org/) and encounterd 65 errors and 1 warning.

* **style.css** -  I ran my code through [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) and had 0 errors.
* **app.py** -  I ran my code through [https://extendsclass.com/python-tester.html](https://extendsclass.com/python-tester.html) the result was 0 syntax erros.

# Deployment

My source code was all done via GitHub, You can find my repository here:
    
* **Repository**:[https://github.com/StephenWhittington/rugby-world-xv](https://github.com/StephenWhittington/rugby-world-xv)

The deployment and live version is hosted via Heroku:

* **Heroku**:[https://rugby-world-xv.herokuapp.com/](https://rugby-world-xv.herokuapp.com/)
    
    * First I created a new app and named it and set the region. 
    
    * Then I logged into heroku via git with "heroku login" and connected git to the new app location using
    git remote.

    * I then created a `requirements.txt` and `Procfile`:
        
        * `sudo pip3 freeze > requirements.txt`
        * `echo web: python3 app.py > Procfile`
    
    * Then added all my project files using `git add .` and commited with `git commit -am "make it better"`
    
    * The project was then pushed using `git push heroku master` and scaled the app dynos using `heroku ps:scale web=1`.
    
    * I then went to Heroku settings clicked on Config Vars and added my IP and PORT.
    
    * I then did the same with my **MONGO URI and SECRET KEY** which are linked and hidden with a '.env' file in my repository.
    
I can confirm that there are no differences from the deployed and the development version.

## How Developers can download and work on my project

    * Click on Clone or Download on my repository.
    * Create an enviorment variable  
    * Clone the project in your workspace using git clone
    * Then add your own MONGO_URI and SECRET_KEY
    * Make sure MONGO_URI and SECRET_KEY are added to a gitignore file.

# Credits
 
 **Content**
 
 In this project I used a lot of materialize templates and forms which then i made my own by linking them to my
 MongoDB database via key value pairs. Python and Jinja2 code was used to create easy for loops and if statements to access the correct
 data for the user from the backend. My CSS styling was simple this time as i wanted to focus on the core aspect of being able to implement
 the CRUD functionality, but maintain a responsive and easy readable page. Any problms i encounterd during the project I went to slack contacted
 the tutors or sorced the answers myself.
 
 **Media**
 
 * The only media used in this project was the background image of the most recent rugby world cup logo, This image
 is for educational purposes only.

 **Acknowledgements**

I received inspiration for this project from the flask mini project during the data centric module, I decided to use materialize
instead of bootstrap for the layout as i like the simplicity of it. I then built the project using my own idea instead of the examples given
and i feel like i understand python and jinja a lot better now using it based off my own inspiration.

A huge thanks to my mentor Ignatius Ukwuoma for his time, suggestions, and constructive feedback for this project!