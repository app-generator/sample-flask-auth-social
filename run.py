# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from flask import Flask, jsonify, redirect, render_template, url_for
from flask_dance.contrib.github import github
from flask_dance.contrib.twitter import twitter
from flask_login import logout_user, login_required

from app.models import db, login_manager
from app.oauth import github_blueprint, twitter_blueprint


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(github_blueprint, url_prefix="/login")
app.register_blueprint(twitter_blueprint, url_prefix="/login")

db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/ping")
def ping():

    if github.authorized:
        return github.get("/user").json()
    
    if twitter.authorized:
        return twitter.get("account/settings.json").json()

    return jsonify(ping="not authenticated")

@app.route("/")
def homepage():

    provider       = None 
    social_account = None
    
    if github.authorized:
        
        social_account = github.get("/user").json()['html_url']
        provider       = 'Github' 
    
    if twitter.authorized:

        social_account = 'https://twitter.com/' + twitter.get("account/settings.json").json()['screen_name']
        provider       = 'Twitter' 

    return render_template("index.html", social_account=social_account, provider=provider)

@app.route("/login/github")
def login_github():
    
    if not github.authorized:
        return redirect(url_for("github.login"))
    res = github.get("/user")
    username = res.json()["login"]
    return f"You are @{username} on GitHub"

@app.route("/login/twitter")
def login_twitter():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    res = twitter.get("account/settings.json")
    username = res.json()["screen_name"]
    return f"You are @{username} on Twitter"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run(debug=True)
