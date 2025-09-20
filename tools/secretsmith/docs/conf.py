#   -------------------------------------------------------------
#   Rhyne-Wyse :: Sphinx documentation
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        Trivial work, not eligible to copyright
#   Reference:      https://www.sphinx-doc.org/en/master/usage/configuration.html
#   -------------------------------------------------------------

#   -------------------------------------------------------------
#   Project information
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

project = "secretsmith"
copyright = "2025, Nasqueron | Released under CC-BY 4.0 license."
author = "Sébastien Santoro aka Dereckson"

#   -------------------------------------------------------------
#   General configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build"]

#   -------------------------------------------------------------
#   HTML output
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

html_theme = "haiku"
html_static_path = ["_static"]
