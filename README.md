# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more...

## Installation

### pipenv

```bash
$ sudo -H pip install pipenv
```

```bash
$ pipenv install --python $(which python)
```

### Pillow install - Prerequisites

https://pillow.readthedocs.io/en/stable/installation.html

on Ubuntu 16.04 LTS

```bash
$ sudo apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
    libharfbuzz-dev libfribidi-dev
```

on termux

```bash
$ pkg install libtiff libwebp openjpeg
$ LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pipenv install Pillow
```

https://wiki.termux.com/wiki/Image_Editors

### Initialize

```bash
python manage.py makemigrations users

python manage.py makemigrations rooms

python manage.py makemigrations reviews

python manage.py makemigrations reservations

python manage.py makemigrations lists

python manage.py createsuperuser 

python manage.py migrate
```

### Seeding fake items

```bash
python manage.py seed_amenities

python manage.py seed_facilities

python manage.py seed_roomtypes
```

```bash
python manage.py seed_users --number 50

unzip photos_seed.zip

mv photos_seed room_photos

mkdir uploads

mv room_photos uploads/

python manage.py seed_rooms --number 150
```

https://github.com/Brobin/django-seed/issues/65

```bash
python manage.py seed_reviews --number 50

python manage.py seed_lists --number 50

python manage.py seed_reservations --number 50
```
