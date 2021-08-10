# "BlogProject" is my sample project where I apply what I have learned

#### Add your "RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY" in "BlogProject/settings.py (RECAPTCHA_PUBLIC_KEY = "..." and RECAPTCHA_PRIVATE_KEY = "...")
```
RECAPTCHA_PUBLIC_KEY = "..."
RECAPTCHA_PRIVATE_KEY = "..."
```

#### To use reCAPTCHA:
```
https://www.google.com/recaptcha/about/
```

### To install what is required for the project:

[Django==3.2.6](https://www.djangoproject.com/download/)

[django-ckeditor==6.1.0](https://pypi.org/project/django-ckeditor/)

[django-cleanup==5.2.0](https://pypi.org/project/django-cleanup/)

[django-crispy-forms==1.12.0](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

[django-recaptcha==2.0.6](https://pypi.org/project/django-recaptcha/)

[Pillow==8.3.1](https://pypi.org/project/Pillow/)

### Please don't forget to execute these commands:
```
python3 manage.py migrate --run-syncdb
python3 manage.py makemigrations
python3 manage.py migrate
```