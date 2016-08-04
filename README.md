# OCD Action
	
# Content

1. [Description](#description)
2. [Setup](#setup)
3. [Contributing](#contributing)


# Description
A collaborative, youth­led project aiming to make use of digital technology to provide mental health support to children & adolescents suffering with anxiety.

[More Info](https://github.com/womenhackfornonprofits/whfnp-wiki/wiki/Current-Projects#ocd-action)


## Tech
- Python + Django
- JavaScript for some interactions/ lazy loading images etc
- Sass + HTML
- Github
- Slack for group chats/standups etc

## Team
- [Lili](https://github.com/lili2311) - Full Stack
- [Jen](https://github.com/jsms90) - Backend
- [Lola](https://github.com/LolaPwa) - Full Stack (Training)
- [Elizabeth](https://github.com/elizabethvenner) - Front end

# Setup
## Tools
1. **Terminal**: [iTerm2](https://www.iterm2.com/) (MacOSX), [Terminator](http://gnometerminator.blogspot.co.uk/p/introduction.html) (Linux) or use your preffered one.
2. **Text Editor**: [Sublime Text](http://www.sublimetext.com/) or you preffered one.

## Dev Enviroment Setup
1. [Install Git](http://git-scm.com/download/mac)
2. Clone the repo: `git clone git@github.com:womenhackfornonprofits/ocdaction.git`


1. Install [virtualenv](https://virtualenv.pypa.io/en/stable/): 

	```sudo pip install virtualenv```

2. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):

3. Source the `virtualenvwrapper`:
	```source /usr/local/bin/virtualenvwrapper.sh```
	
	**NOTE**: To help do this automatically on every new shell you open add the line above to your `.bash_profile` or  `.bashrc`

4. Create a new env for the project:
 
	 ```mkvirtualenv ocdaction```
6. Get the code: 

	```git clone git@github.com:womenhackfornonprofits/ocdaction.git```
	
6. Go inside the `ocdaction` directory:
	
	```cd ocdaction```

7. Activate the virtual enviroment:
 
	 ```workon ocdaction``` 
	 
	 This will now ensure anything you install is within this enviroment.

8. You will need to have [Postgres installed](https://www.postgresql.org/download/) and up and running. You can onstall it via:
	- Homebrew ```brew install postgresql```
	- OR Download the [Postgress App](http://postgresapp.com/)

9. Make sure the Postgres Server is up and running:
	- If using the App simply start the server from there
	- If using command line: ``brew services start postgresql``

9. Install the requirements:

	 ```pip install -r requirements.txt``` 
	 
	 This will get all the dependencies.

9. Create a database locally for the project to run:
	
	```createdb ocdaction```

10. Go inside frontend folder: 
	
	```cd frontend```

11. Install all the dependencies:

	 ```npm install```

	 This will get all the dependencies

	
## Running the project locally
1. Go inside the django app directory: 

	```cd ocdaction```
2. Run django server:
	
	```python manage.py runserver```
	
3. The project is now running on `http://127.0.0.1:8000/`, go to that address in your browser. 
4. You may see a message that you have unapplied migrations, when you see this simply run the command below which will create any tables and fields in the database:

	```python manage.py migrate```


## Front End changes
1. Make css and javascript changes in the ```frontend``` folder
2. Make any HTML changes in the Django templates located in `ocdaction/templates`
3. Use `grunt default` in the frontend folder to build, watch and copy all the required files automatically into the Django static folder.

## Deploying to Heroku
1. Create a Heroku Account
2. Get added to the app in the Heroku Dashboard
3. In the terminal `heroku login`
4. Within you project directory `heroku git:remote -a staging-ocdactin`
5. Once you are ready to deploy, from master branch you can run `git push heroku master` make sure you have commited all the changes before running this and the `git status` is clean.
6. Go to https://staging-ocdaction.herokuapp.com/ to view the live site.

# Contributing
Please follow a few guidelines in order to contribute to the project set out in the [Contributing file](https://github.com/womenhackfornonprofits/ocdaction/blob/master/CONTRIBUTING.md)

