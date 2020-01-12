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


