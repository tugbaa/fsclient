# fsclient

This is a client application for searching venues with Foursquare API.

## Installation
Create a virtual environment.
```shell
$ virtualenv myenv
```

Activate the created environment.
```shell
$ ./myenv/bin/activate
```

Run the following command to install pip packages.
```shell
$ pip install -r requirements.pip
```

Rung migration commands to creating sqlite database.
```shell
$ python manage.py makemigrations
$ python manage.py migrate

```

Finally run the following command to starting application.
```shell
$ python manage.py runserver

```


## Configuration
**CLIENT_ID** : Client identifier value. <br />
**CLIENT_SECRET** : Secret key value for authenticating to API. <br />

[link test] (www.google.com)

