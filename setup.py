import setuptools

import django_dump_load_utf8

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="django-dump-load-utf8",
    version=django_dump_load_utf8.__version__,
    author=django_dump_load_utf8.__author__,
    author_email=django_dump_load_utf8.__email__,
    description="Django command dumpdatautf8 and loaddatautf8",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panhaoyu/django-dump-load-utf8",
    project_urls={
        "Bug Tracker": "https://github.com/panhaoyu/django-dump-load-utf8/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=['demo*']),
    python_requires=">=3.8",
)
