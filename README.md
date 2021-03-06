# MyGram

MyGram is a web application where different users can upload their pictures and can also like  and comment on other people's posts.To use any of the features of the app ,a user must me registered and logged into the app.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. 

 #### Prerequisites

* Virtual environment
* Python3.6
* Postgres
* pip
* Django 1.11

#### Cloning
 * In your terminal<br>
 ```
   $ git clone https://github.com/Anabella1109/MyGram.git
   $ cd MyGram
```

#### Activate virtual environment

```
$ python3.6 -m venv --without-pip virtual 
$ source venv/bin/activate
``` 

 #### Installing

Install dependancies that will create an environment for the app to run
```
 pip3 install -r requirements.txt
 ```
#### Create Database
```
$ psql
CREATE DATABASE mygram
```
#### .env file
Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'<br>
DBNAME = 'mygram'<br>
USER = '&lt;Username&gt;'<br>
PASSWORD = '&lt;password&gt;'<br>
DEBUG = True 

 #### Run initial Migrations
```
$ python manage.py makemigrations mygram 
$ python3.6 manage.py migrate
```

#### Running the app
```
$ python3.6 manage.py runserver
```

## Running the tests

```
$ python3.6 manage.py test mygram
```



## Deployment

Add additional notes about how to deploy this on a live system

## Built With 

* [Django](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
<!-- * [Maven](https://maven.apache.org/) - Dependency Management -->
<!-- * [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds -->

 <!--## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. -->

<!-- ## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  -->

## Authors

* **TUYISENGE Anabella** 

## Support and contact details

Having any issues?
Email:bellaxbx1109@gmail.com
Slack:TUYISENGE Anabella


<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

## License


[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2019 **TUYISENGE Anabella**


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
 
