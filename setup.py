from distutils.core import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='DBans',
      version='1.8',
      description='Discord Bans Python',
      long_description=long_description,
      url='https://github.com/JustMaffie/dbanspy',
      author='JustMaffie',
      author_email='jori@jorivanee.me',
      license='MIT',
      packages=['dbans'],
      zip_safe=False)