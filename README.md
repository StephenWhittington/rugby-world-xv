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
    

* [MongoDB](https://www.mongodb.com/)

    * The website uses MongoDB for its cross-platform and open-source document-oriented database.
    I have used this easy to use database to create,update,store and delete all of the information.
    
* [Materialize](https://materializecss.com/)

    * For this website i decided to use Materialize instead of bootstrap, for its
    reusable UI components that help in constructing attractive, consistent, 
    and functional web pages and web apps while adhering to modern web design.
    
* [jQuery](https://jquery.com/)

    * The website uses JQuery The Document Object Model (DOM) to simplify manipulation.

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