# Portfolio

## Overview
This project is a website showing past projects I have been working on. It shows

+ Revision History
+ Files in the project
+ Make comments for specific project

It is mainly built on Flask. I also uses Angular to build the comment feature. 

## Usage

#### Install dependency 
	pip install -r requirements.txt
	
#### Run 
Go to portfolio directory

	python app.py
#### Deployment on Heroku
Just create a new heroku application, and push the code to heroku
	
	heroku create
	git push heroku
	heroku ps:scale web=1

## Credit
+ [Angularjs](https://angularjs.org/)
+ [Bootflat](http://bootflat.github.io/)
+ [Flask](http://flask.pocoo.org/)
+ [Flask-Assets](https://github.com/miracle2k/flask-assets)
+ [Flask-mongoengine](https://github.com/mongoengine/flask-mongoengine)
+ [Jinja](http://jinja.pocoo.org/)
+ [xmltodict](https://github.com/martinblech/xmltodict)
