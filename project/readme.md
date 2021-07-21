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
$ pip install django==3.2.5 djangorestframework==3.12.4 django-allauth==0.45.0 django-cors-headers==3.7.0 django-filter==2.4.0
$ source djangoenv/bin/activate
```