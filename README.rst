Demo project for django-linkcheck
=================================

A very simple project intended to demonstrate use of the django-linkcheck_ app. Users can post links along with a descriptive title and comment, and django-linkcheck will make it easy to monitor dead links.

.. _django-linkcheck: https://github.com/andybak/django-linkcheck

Requirements
------------

* Django_ 1.3
* django-linkcheck_

.. _Django: https://www.djangoproject.com/
.. _django-linkcheck: https://github.com/andybak/django-linkcheck

Basic usage
-----------

#. Make sure that django and django-linkcheck are on your Python path

#. ``cd`` into the project root directory

#. Run ``cp local_settings_example.py local_settings.py``

#. Change the contents of ``local_settings.py`` as necessary

#. Run ``./manage.py syncdb``

#. Run ``./manage.py collectstatic``

#. Run ``./manage.py runserver``

#. Visit ``localhost:8000`` from your browser

#. Add some posts at ``http://localhost:8000/add/``

#. View ``http://localhost:8000/admin/linkcheck/`` to see linkcheck in action
