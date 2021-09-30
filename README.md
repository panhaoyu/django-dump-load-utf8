# Django Dump Load UTF-8

Django provides great database management, however, the `dumpdata` and `loaddata` commands do not use `utf-8` encoding.
Thus, many data are not able to dump and load.

Feel sorry that I'm not able to provide Django a patch, for the contribution guide is too long to read. If anyone has
time, please help me to merge it to Django.

## Installation

```shell
pip install django-dump-load-utf8
```

## Usage

### Add to `INSTALLED_APPS`

```python
# settings.py
INSTALLED_APPS = [
    '...',
    'django_dump_load_utf8',
    '...',
]
```

### Use as a `manage.py` command

```shell
manage.py dumpdatautf8 --output data.json

# In another database
manage.py loaddatautf8 data.json
```

## About

If this is useful, please give me a star!

If you have time, please help me merge this to django!

The project currently only supports python 3.8+, if you have time, please make it more competitive.