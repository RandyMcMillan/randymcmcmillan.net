SHELL                                   := /bin/bash
PWD 									?= pwd_unknown
TIME 									:= $(shell date +%s)
export TIME

ifeq ($(project),)
PROJECT_NAME							:= $(notdir $(PWD))
else
PROJECT_NAME							:= $(project)
endif
export PROJECT_NAME

#GIT CONFIG
GIT_USER_NAME							:= $(shell git config user.name)
export GIT_USER_NAME
GH_USER_NAME							:= $(shell git config user.name)
#MIRRORS
GH_USER_REPO    						:= $(GH_USER_NAME).github.io
KB_USER_REPO   	        				:= $(GH_USER_NAME).keybase.pub
#GITHUB RUNNER CONFIGS
ifneq ($(ghuser),)
GH_USER_NAME := $(ghuser)
GH_USER_REPO := $(ghuser).github.io
endif
ifneq ($(kbuser),)
KB_USER_NAME := $(kbuser)
KB_USER_REPO := $(kbuser).keybase.pub
endif
export GIT_USER_NAME
export GH_USER_REPO
export KB_USER_REPO

GIT_USER_EMAIL							:= $(shell git config user.email)
export GIT_USER_EMAIL
GIT_SERVER								:= https://github.com
export GIT_SERVER
GIT_SSH_SERVER							:= git@github.com
export GIT_SSH_SERVER
GIT_PROFILE								:= $(shell git config user.name)
export GIT_PROFILE
GIT_BRANCH								:= $(shell git rev-parse --abbrev-ref HEAD)
export GIT_BRANCH
GIT_HASH								:= $(shell git rev-parse --short HEAD)
export GIT_HASH
GIT_PREVIOUS_HASH						:= $(shell git rev-parse --short master@{1})
export GIT_PREVIOUS_HASH
GIT_REPO_ORIGIN							:= $(shell git remote get-url origin)
export GIT_REPO_ORIGIN
GIT_REPO_NAME							:= $(PROJECT_NAME)
export GIT_REPO_NAME
GIT_REPO_PATH							:= $(HOME)/$(GIT_REPO_NAME)
export GIT_REPO_PATH

BASENAME := $(shell basename -s .git `git config --get remote.origin.url`)
export BASENAME

# Force the user to explicitly select public - public=true
# export KB_PUBLIC=public && make keybase-public
ifeq ($(public),true)
KB_PUBLIC  := public
else
KB_PUBLIC  := private
endif
export KB_PUBLIC

ifeq ($(libs),)
LIBS  := ./libs
else
LIBS  := $(libs)
endif
export LIBS

SPHINXOPTS            =
SPHINXBUILD           = sphinx-build
PAPER                 =
BUILDDIR              = _build
PRIVATE_BUILDDIR      = _private_build

# Internal variables.
PAPEROPT_a4           = -D latex_paper_size=a4
PAPEROPT_letter       = -D latex_paper_size=letter
ALLSPHINXOPTS         = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
PRIVATE_ALLSPHINXOPTS = -d $(PRIVATE_BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help
help: report
	@echo ""
	@echo "  make docs"
	@echo "  make push"
	@echo ""
	@echo ""
	@echo "Keybase usage:"
	@echo ""
	@echo "  make depends"
	@echo "  make all"
	@echo "  make push-all"
	@echo "  make reload"
	@echo "  make rebuild"
	@echo "  make serve"
	@echo ""
	@echo "  make singlehtml"
	@echo ""
	@echo "Example:"
	@echo ""
	@echo "make push-all public=true"
	@echo ""
	@echo ""

.PHONY: report
report: 
	@echo ''
	@echo '	[ARGUMENTS]	'
	@echo '      args:'
	@echo '        - TIME=${TIME}'
	@echo '        - PROJECT_NAME=${PROJECT_NAME}'
	@echo '        - GIT_USER_NAME=${GIT_USER_NAME}'
	@echo '        - GH_USER_REPO=${GH_USER_REPO}'
	@echo '        - KB_USER_REPO=${KB_USER_REPO}'
	@echo '        - GIT_USER_EMAIL=${GIT_USER_EMAIL}'
	@echo '        - GIT_SERVER=${GIT_SERVER}'
	@echo '        - GIT_PROFILE=${GIT_PROFILE}'
	@echo '        - GIT_BRANCH=${GIT_BRANCH}'
	@echo '        - GIT_HASH=${GIT_HASH}'
	@echo '        - GIT_PREVIOUS_HASH=${GIT_PREVIOUS_HASH}'
	@echo '        - GIT_REPO_ORIGIN=${GIT_REPO_ORIGIN}'
	@echo '        - GIT_REPO_NAME=${GIT_REPO_NAME}'
	@echo '        - GIT_REPO_PATH=${GIT_REPO_PATH}'

.PHONY: push
.ONESHELL:
push: docs touch-time
	bash -c "git add -f * .github && \
		git commit -m 'update from $(GIT_USER_NAME) on $(TIME)'"
	git push -f origin	+master:master

.PHONY: branch
.ONESHELL:
branch: docs touch-time
	bash -c "git add -f * .github && \
		git commit -m 'update from $(GIT_USER_NAME) on $(TIME)'"
	git push -f origin	+$(TIME):$(TIME)

.PHONY: automate
automate: touch-time
	./.github/workflows/automate.sh

.PHONY: touch-time
.ONESHELL:
touch-time:
	touch 0 && echo 0 > 0
	touch 1 && echo 1 > 1
	touch $(TIME)
	#$(shell git rm -f 16*)
	#git rm -f 16*
	touch $(TIME)
	echo $(TIME) $(shell git rev-parse HEAD) > $(TIME)
	echo $(TIME) > TIME
	touch 1

.PHONY: global
.ONESHELL:
global: 
	#$(shell git rm -f 16*)
	#git rm -f 16*
	touch GLOBAL
	echo $(TIME) $(shell git rev-parse HEAD) > GLOBAL
	echo $(TIME) > GLOBAL
	bash -c 'make push'

.PHONY: docs
docs:
	@echo 'docs'
	bash -c "if pgrep MacDown; then pkill MacDown; fi"
	bash -c 'cat $(PWD)/HEADER.md                >  $(PWD)/README.md'
	bash -c 'cat $(PWD)/COMMANDS.md              >> $(PWD)/README.md'
	bash -c 'cat $(PWD)/FOOTER.md                >> $(PWD)/README.md'
	bash -c "if hash open 2>/dev/null; then open README.md; fi || echo failed to open README.md"

.PHONY: clean
.ONESHELL:
clean: touch-time
	bash -c "rm -rf 1618*"
	bash -c "rm -rf $(BUILDDIR)"

.PHONY: serve
.ONESHELL:
serve:
	bash -c "python3 -m http.server 8000 -d . &"

.PHONY: failure
failure:
	@-/bin/false && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"
.PHONY: success
success:
	@-/bin/true && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"

