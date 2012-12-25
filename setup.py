"""
Flask-Reggie
------------

Quickly and Easily enable Regex Routes within your Flask Application

"""

from setuptools import setup

setup(
    name='Flask-Reggie',
    version='0.0.1',
    url='https://github.com/rhyselsmore/flask-reggie',
    license='BSD',
    author='Rhys Elsmore',
    author_email='me@rhys.io',
    description='Flask Regex Routes.',
    long_description=__doc__,
    py_modules=['flask_reggie'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
