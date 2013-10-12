
jcfg: jinja templates for your configuration files
==================================================

Overview
--------

**jcfg** is a simple script which uses `Jinja <http://jinja.pocoo.org/>`_ templates to generate
configuration files. My motivation was to replace some no-so-good-looking M4 configuration files
with something that was more friendly to use.


Usage
-----

::

    jcfg --input template_file --output out_file.cfg --context settings.py

The file passed as the content must be a valid Python module, with an attribute called "context".


Author
------

Saúl Ibarra Corretgé <saghul@gmail.com>


License
-------

Unless stated otherwise on-file jcfg uses the MIT license, check the LICENSE file.


Contributing
------------

If you'd like to contribute, fork the project, make a patch and send a pull
request. Have a look at the surrounding code and please, make yours look
alike :-) If you intend to contribute a new feature please contact the maintainer
beforehand in order to discuss the design.

