

# 3D Print Central

3D Print Central is a small web app to help queue and manage print jobs for 3D printers. It is designed for use by Leighton Park School students and therefore new user registrations are limited to the '@leightonpark.com' domain, however this is easily changed by the `ALLOWED_EMAIL_DOMAINS` setting.

**This version is live [here][2]**.   Sign up with `anything@leightonpark.com` as the mailer is disabled and will not send out emails :)


This project is incomplete and therefore errors could occur, although I like to think I've ironed the majority out :p.

It is built with [Python][0] using the [Django Web Framework][1].

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv print_queue`
    2. `$ . print_queue/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate
    python manage.py makemigrations
    python manage.py migrate

Run the same as all Django projects:
    
    python manage.py runserver 8000
    
Or deploy using your favourite WSGI solution :p

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://testbed.aliakseipilko.com/3dprintcentral/
