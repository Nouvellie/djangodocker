# INSTALL
## Preparing pip

```sh
$ python3 -m pip install --upgrade pip -y
$ pip3 install virtualenv -y
```

## Create env

```sh
$ virtualenv djangoenv
$ source djangoenv/bin/activate
```

## Libs

```sh
$ pip install django==3.2.5 djangorestframework==3.12.4 django-allauth==0.45.0 django-cors-headers==3.7.0 django-filter==2.4.0 django-rest-auth==0.9.5 gunicorn==20.1.0 djangorestframework_simplejwt==4.7.2 django-environ==0.4.5 django-rest-registration==0.6.3
$ source djangoenv/bin/activate
```

#### Save libs list:

```sh
$ pip3 freeze > requirements.txt
```

#### Install from requirements.txt:

```sh
$ pip3 install -r requirements.txt
```

## Deactivate

```sh
$ deactivate
```