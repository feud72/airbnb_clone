# Airbnb Clone

Cloning Airbnb with Python, Django, Tailwind and more...

## Installation

### pipenv

```bash
$ sudo -H pip install pipenv
```

```bash
$ pipenv install --python $(which python3.7)
```

### Pillow install - Prerequisites

https://pillow.readthedocs.io/en/stable/installation.html

on Ubuntu 16.04 LTS

```bash
$ sudo apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
    libharfbuzz-dev libfribidi-dev
```

### Initialize

```bash
<<<<<<< HEAD
python manage.py createsuperuser

python manage.py makemigrations

python manage.py migrate
=======
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
>>>>>>> 1e67093d14d65f168920ce0c611f04902c938559
```

### Seeding fake items

```bash
python manage.py seed_amenities
<<<<<<< HEAD

python manage.py seed_facilities

=======
python manage.py seed_facilities
>>>>>>> 1e67093d14d65f168920ce0c611f04902c938559
python manage.py seed_roomtypes
```

```bash
python manage.py seed_users --number 50
<<<<<<< HEAD

=======
>>>>>>> 1e67093d14d65f168920ce0c611f04902c938559
python manage.py seed_rooms --number 150
```

```bash
python manage.py seed_reviews --number 50
<<<<<<< HEAD

python manage.py seed_lists --number 50

=======
python manage.py seed_lists --number 50
>>>>>>> 1e67093d14d65f168920ce0c611f04902c938559
python manage.py seed_reservations --number 50
```
