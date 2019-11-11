import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)



@app.route('/')
@app.route('/create_team')
def view_team():
    return render_template("base.html",
                            team=mongo.db.team.find())
                            
@app.route('/new_team')
def new_team():
    return render_template("addplayers.html",
                            players=mongo.db.players.find())

@app.route('/add_player', methods=['POST'])
def add_player():
    players =  mongo.db.players
    players.insert_one(request.form.to_dict())
    return redirect(url_for('create_team'))
    
@app.route('/create_team')
def create_team():
    return render_template("team.html",
                            team=mongo.db.team.find())
                            
@app.route('/create_team', methods=['POST'])
def add_team():
    team =  mongo.db.players
    team.insert_one(request.form.to_dict())
    return redirect(url_for('create_team'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)