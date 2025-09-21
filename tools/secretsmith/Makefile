#   -------------------------------------------------------------
#   Secretsmith
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        Trivial work, not eligible to copyright
#   -------------------------------------------------------------

PYTHON=python3
BUILD_PACKAGE=$(PYTHON) -m build
RM=rm -rf

#   -------------------------------------------------------------
#   Main targets
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

build:

test:
	cd tests && make test

package:
	$(BUILD_PACKAGE)

documentation: docs/_build/html

clean:
	$(RM) dist docs/_build/html

full: test package documentation

#   -------------------------------------------------------------
#   Documentation
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

docs/_build/html:
	cd docs && make html
