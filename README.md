# fsclient

This is a client application for searching venues with Foursquare API.

## Installation
Create a virtual environment.
```
$ virtualenv myenv
```

Activate the created environment.
```
$ ./myenv/bin/activate
```

Run the following command to install pip packages.
```
$ pip install -r requirements.pip
```

Rung migration commands to creating sqlite database.
```
$ python manage.py makemigrations
$ python manage.py migrate

```

Finally run the following command to starting application.
```
$ python manage.py runserver

```


## Configuration
*CLIENT_ID*:Client identifier value.
*CLIENT_SECRET*:Secret key value for authenticating to API.


