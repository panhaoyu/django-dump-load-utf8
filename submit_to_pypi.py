import os
import shutil


def submit():
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('django_dump_load_utf8.egg-info')


if __name__ == '__main__':
    submit()
