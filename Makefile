PROJECT := BatchY
ROOT := .
PACKAGE := batchy
TESTS := $(ROOT)/test
PYTHON := python
PIP := pip
PEP8 := pep8
PEP_IGNORE := E501
DEPENDS := pep8 nose coverage
NOSE := nosetests

# Install ####################################################################

.PHONY: all
all: 
	$(MAKE) install
	$(MAKE) clean-all
	$(MAKE) test

.PHONY: install
install: $(PACKAGE) .depends
	$(PYTHON) setup.py install

.PHONY: .depends
.depends:
	$(PIP) install $(DEPENDS) --use-mirrors

# Clean-up ###################################################################

.PHONY: .clean-dist
.clean-dist:
	rm -rf dist build *.egg-info

.PHONY: clean
clean:
	$(PYTHON) setup.py clean
	find $(ROOT) -name "*.pyc" -delete

.PHONY: clean-all
clean-all: clean .clean-dist

# Test #######################################################################

.PHONY: test
test: $(PACKAGE) pep8
	$(NOSE)


# Static Analysis ############################################################

.PHONY: pep8
pep8: $(PACKAGE)
	pep8 $(PACKAGE) --ignore=$(PEP_IGNORE)
