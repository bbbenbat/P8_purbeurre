# PUR BEURRE  APPLICATION

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Application created to find the products with the best nutriscore.

## Getting Started

These instructions will get you to install the application on heroku.

### Prerequisites

You have to create an account to Heroku (https://signup.heroku.com) and AWS
(https://portal.aws.amazon.com/billing/signup#/start).

Download the 'purbeurre' file from the github repository
(https://github.com/bbbenbat/purbeurre.git).

### Installing

#### Heroku
Create the application:
- 'New'
- 'Create new app'
- Enter the name's application.

Create the database:
- click on the application
- 'Resources'
- 'Add-ons'
- Enter 'Heroku Postgres' in the search bar
- Click on 'Heroku Postgres' to install it


#### Local

Add the project from your virtual environment :
```
> heroku git:remote -a yourApp 
```

Add the application url in the 'purbeurre\prod_settings.py' file of the 'purbeurre' project:
ALLOWED_HOSTS = ['urlApp']
Change the parameters in the 'purbeurre\settings.py' file of the 'purbeurre' project:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'p8purbeurre',
        'USER': 'p8purbeurreuser',
        'PASSWORD': 'Python2021',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Updating the database:
- creation of tables
- creation of a super-user
- feeding tables from the Openfoodfacts API

```
> git push heroku master
> heroku run bash -a yourApp
>> python manage.py makemigrations accounts
>> python manage.py migrate accounts
>> python manage.py makemigrations researches
>> python manage.py migrate researches
>> python manage.py migrate
>> python manage.py createsuperuser
>>> email address : ...
>>> password : ...
>>> password : ...
>> exit
> heroku run python researches/start_db.py
```

#### AWS

Go to 'S3':
- activate the bucket
- create a user who will be part of "Amazon S3 FullAccess".
- copy the contents of the media folder into the bucket.

#### Heroku

Creation of environment variables.
- setting
- config var

AWS_ACCESS_KEY_ID : yourAWSUserIdKey

AWS_S3_REGION_NAME : eu-west-3

AWS_SECRET_ACCESS_KEY : yourAWSUserAccessKey

AWS_STORAGE_BUCKET_NAME : yourAWSBucketName

DATABASE_URL HerokuDatabaseURI

DJANGO_SETTINGS_MODULE : purbeurre.prod_settings

SECRET_KEY : DjangoSecretKey


## How to use

Enter a product in the search bar.

Several proposals for better quality products will be offered to you
(classified by nutritional score).

You can create a user account.

Once logged in, you will be able to save your favorite products.

You can remove a product from your favorites, from the 'favorites' page.

## Built With

* [OpenFoodFacts](https://wiki.openfoodfacts.org) - The web API used.
* [Heroku](https://www.heroku.com) - The website host.
* [AWS](https://aws.amazon.com) - The web host for 'media' content.

## Contributing

Please go [CONTRIBUTING.md](https://github.com/bbbenbat/purbeurre/pulls) for submitting pull requests to us.

## Versioning

Version 0.1

## Authors

* **Ben Bessayah** - *PurBeurre* - [bbbenbat](https://github.com/bbbenbat)




