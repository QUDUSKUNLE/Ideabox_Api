### Ideabox API

Server side implementation of IdeaBox

### Introduction

Ideabox is a simple application that allows users to create a pool of ideas and promote collaboration.

### Technologies

* [Flask](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application) - Python web framework
* [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - an extension for Flask that adds support for SQLAlchemy to your application
* [PostgreSQL](https://www.postgresql.org/) - an open source object-relational database system.

### Development setup

- Clone this repository and navigate into the project directory
```
$ git clone https://github.com/QUDUSKUNLE/Ideabox__api && cd ideabox
```

- Create a python3 virtual environemnt for the project and activate it
```
$ mkvirtualenv --py=python3 ideabox
```

- Install the project dependencies
```
pip install -r requirements.txt
```
- Copy .env.sample into .env in the learning_map_api which is the base folder of the project. You should adjust it according to your own local settings. To set up postgres database locally you can follow this.

- Export the environment variables in the .env
```
export $(cat .env)
```
### Run the app:
```
$ python manage.py runserver
```
- The app should now be available from your browser at http://127.0.0.1:5000

- Run database upgrade
```
flask db upgrade
```

### Making Changes to the Model
- After making a change on the model, apply the database migration to make the change in the database before pushing the code on Github:
```
$ flask db migrate -m “message indicating change made”
```
```
$ flask db upgrade
```

- Check migrations history to confirm change is made.
```
$ flask db history
```

### Installing Git hooks
```
$ sh setup_hooks.sh
```
### Authors

* **Qudus Yekeen** - *Initial work* 

See also the list of [contributors](https://github.com/QUDUSKUNLE/Ideabox__api/graphs/contributors) who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/QUDUSKUNLE/Ideabox__api/blob/master/LICENSE) file for details