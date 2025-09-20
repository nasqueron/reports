.. secretsmith documentation main file, created by
   sphinx-quickstart on Sat Sep 20 20:04:12 2025.

secretsmith
===========

Introduction
------------

The secretsmith package is a high-level wrapper on the top of hvac
to connect to a Vault or OpenBao server.

secretsmith has been written to avoid to repeat boilerplate code
about connections details like authentication method or namespace.

One of the strength of secretsmith is to allow the Vault connection
to be configured by a YAML file instead of having to take decisions
in code, and repeat local configuration parsing in each project.

Contents
--------

.. toctree::
   :maxdepth: 3

   getting-started
   connect
   kv2

Appendices
----------

* :ref:`search`
