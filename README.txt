Introduction
============

This is django project for pushstrength.com.

Overview
--------

It's provides welcome page with a possibility to subscribe to newsletter.
Newsletter is built on top of mailchimp service.
Client side is built with twitter bootstrap.


Test Setup
----------

* install python 2.6 or higher
* install django 1.5 into your python directly or better virtual environment
* install django-mailchimp, see docs for details:
    https://github.com/ojii/django-mailchimp
* unzip this django project
* run root project folder manage.py module with command runserver, use above
  installed python or it's virtual environment
* in your browser visit 127.0.0.1:8000 to check the application


MailChimp Configuration
-----------------------

* create account at mailchimp.com
* create Subscribers List:
    http://kb.mailchimp.com/article/how-can-i-find-my-list-id
* generate API key:
    http://kb.mailchimp.com/article/where-can-i-find-my-api-key
* paste generate API key into MAILCHIMP_API_KEY variable in settings.py module
* paste Subscribers List id into setting.py module


Twitter Button Configuration
----------------------------

* set required Twitter Username in TWITTER_USERNAME setting.py module
