
SHELL                                   := /bin/bash

PWD 									?= pwd_unknown

TIME 									:= $(shell date +%s)
export TIME

# PROJECT_NAME defaults to name of the current directory.
ifeq ($(project),)
PROJECT_NAME							:= $(notdir $(PWD))
else
PROJECT_NAME							:= $(project)
endif
export PROJECT_NAME

#GIT CONFIG
GIT_USER_NAME							:= $(shell git config user.name)
export GIT_USER_NAME
GIT_USER_EMAIL							:= $(shell git config user.email)
export GIT_USER_EMAIL
GIT_SERVER								:= https://github.com
export GIT_SERVER
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

.PHONY: help
help: report
	@echo ""
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

.PHONY: docs
docs:
	@echo 'docs'
	bash -c "if pgrep MacDown; then pkill MacDown; fi"
	bash -c 'cat $(PWD)/HEADER.md                >  $(PWD)/README.md'
	bash -c 'cat $(PWD)/COMMANDS.md              >> $(PWD)/README.md'
	bash -c 'cat $(PWD)/FOOTER.md                >> $(PWD)/README.md'
	bash -c "if hash open 2>/dev/null; then open README.md; fi || echo failed to open README.md"

TIME := $(shell date +%s)
export TIME

BASENAME := $(shell basename -s .git `git config --get remote.origin.url`)
export BASENAME

ifeq ($(kbuser),)
# My default change to your keybase user name
KB_USER := randymcmillan
else
KB_USER = $(kbuser)
endif
export KB_USER

ifeq ($(ghuser),)
# My default change to your keybase user name
GITHUB_USER := randymcmillan
else
GITHUB_USER = $(ghuser)
endif
export GITHUB_USER

# Force the user to explicitly select public - public=true
# export KB_PUBLIC=public && make keybase-public
ifeq ($(public),true)
KB_PUBLIC  := public
else
KB_PUBLIC  := private
endif
export KB_PUBLIC

ifeq ($(libs),)
LIBS  := $(PWD)/libs
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

.PHONY: depends
depends: #touch-time
																	#????
	#sudo rm -f /usr/bin/python
	#pip3 install sphinx sphinx_rtd_theme glpi sphinx-reload blockcypher groundwork-sphinx-theme --user blockcypher
	./install-depends.sh
	sudo -H pip3 install --upgrade --target=$(LIBS) sphinx sphinx_rtd_theme glpi sphinx-reload blockcypher groundwork-sphinx-theme sphinx-glpi-theme
#export PYTHONPATH=$(PYTHONPATH):$(PWD)/$(LIBS)
	#pip  install sphinx sphinx_rtd_theme glpi sphinx-reload blockcypher groundwork-sphinx-theme --user blockcypher
	#make depends public=true
	bash -c "[ -d '~/$(GITHUB_USER).github.io' ] && echo  || rm -rf ~/$(GITHUB_USER).github.io"
	git clone git@github.com:$(GITHUB_USER)/$(GITHUB_USER).github.io.git ~/$(GITHUB_USER).github.io

.PHONY:
git-remote-add-keybase:
	git remote add keybase keybase://$(KB_PUBLIC)/$(KB_USER)/$(KB_USER).keybase.pub

.PHONY: install-depends
install-depends: 
	bash -c "./install-depends.sh"

.PHONY: all
.ONESHELL:
all: touch-time make-kb-gh

.PHONY: make-kb-gh
.ONESHELL:
make-kb-gh: touch-time singlehtml keybase gh-pages
	curl https://api.travis-ci.org/bitcoin-core/gui.svg?branch=master --output _static/gui.svg
	curl https://api.travis-ci.org/bitcoin/bitcoin.svg?branch=master  --output _static/bitcoin.svg

.PHONY: push-all
.ONESHELL:
push-all: touch-time make-kb-gh
	bash -c "git add -f _build _static * && \
		git commit -m 'update from $(BASENAME) on $(TIME)'"
	git push -f origin	+master:master
	echo if error run 
	echo make git-remote-add-keybase
	git push -f keybase	+master:master
	#bash -c "pushd ~/$(GH_USER).github.io && git add * && git pull -f https://github.com/randymcmillan/randymcmillan.keybase.io && git push -f origin +master:master"
	bash -c "pushd ~/$(GITHUB_USER).github.io && git add * && git commit -m 'update from $(BASENAME) on $(TIME)' && git push -f origin +master:master"

.PHONY: reload
.ONESHELL:
reload:
	sphinx-reload .

.PHONY: rebuild
.ONESHELL:
rebuild: touch-time clean keybase gh-pages
	make make-kb-gh

.PHONY: clean
.ONESHELL:
clean: touch-time
	bash -c "rm -rf 1618*"
	bash -c "rm -rf $(BUILDDIR)"

.PHONY: serve
.ONESHELL:
serve: keybase gh-pages
	bash -c "python3 -m http.server 8000 -d _build/$(KB_USER).keybase.pub &"

.PHONY: singlehtml
singlehtml: touch-time
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/$(GITHUB_USER).github.io
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/$(KB_USE/R).keybase.pub
#	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) /keybase/$(KB_PUBLIC)/$(KB_USER)
#	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) /keybase/public/$(KB_USER)
#	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) /keybase/private/$(KB_USER)
#	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) ~/$(GH_USER).github.io
	@echo
	#bash -c "keybase sign -i $(PWD)/$(BUILDDIR)/singlehtml/index.html -o $(PWD)/$(BUILDDIR)/singlehtml/index.sig"
	#bash -c "git add _build _static . && git commit -m 'update from $(BASENAME) on $(TIME)' && git push -f origin +master:master"
	@echo "Build finished. The HTML page is in $(PWD)/$(BUILDDIR)/singlehtml"

.PHONY: keybase
keybase: touch-time singlehtml
	@echo keybase
	@echo if error ensure these files exist...
	@echo	
	bash -c "keybase sign -i			keybase.txt -o keybase.txt.sig"
	bash -c "install -v					keybase.txt     $(BUILDDIR)/$(KB_USER).keybase.pub/keybase.txt"
	bash -c "install -v					keybase.txt.sig $(BUILDDIR)/$(KB_USER).keybase.pub/keybase.txt.sig"
	bash -c "keybase sign -i			$(BUILDDIR)/$(KB_USER).keybase.pub/index.html -o  $(BUILDDIR)/$(KB_USER).keybase.pub/index.html.sig"
	bash -c "install -v					$(BUILDDIR)/$(KB_USER).keybase.pub/index.html      /keybase/$(KB_PUBLIC)/$(KB_USER)/index.html"
	bash -c "install -v					$(BUILDDIR)/$(KB_USER).keybase.pub/index.html.sig  /keybase/$(KB_PUBLIC)/$(KB_USER)/index.html.sig"
	bash -c "install -v					$(BUILDDIR)/$(KB_USER).keybase.pub/keybase.txt     /keybase/$(KB_PUBLIC)/$(KB_USER)/keybase.txt"
	bash -c "install -v					$(BUILDDIR)/$(KB_USER).keybase.pub/keybase.txt.sig /keybase/$(KB_PUBLIC)/$(KB_USER)/keybase.txt.sig"
	bash -c "touch $(TIME)"
	@echo	
	bash -c "git status"
	make push-keybase
	@echo "Build finished. The HTML page is in $(BUILDDIR)/$(KB_USER).keybase.pub"
	@echo "Build finished. The HTML page is in /keybase/$(KB_PUBLIC)/$(KB_USER).keybase.pub"
ifneq ($(public),true)
	@echo "make keybase public=true #will push to the your /keybase/public/$(KB_USER).keybase.pub"
endif

.PHONY: push-keybase
.ONESHELL:
push-keybase: touch-time
	bash -c "git add -f $(BUILDDIR) _static * && \
		git commit -m 'update from $(BASENAME) on $(TIME)' && \
		git push -f origin +master:master && \
		git push -f keybase +master:master"

.PHONY: gh-pages
.ONESHELL:
gh-pages: touch-time singlehtml
ifeq ($(public),true)
	@echo gh-pages
	bash -c "install -v $(BUILDDIR)/$(KB_USER).keybase.pub/*.html ~/$(GITHUB_USER).github.io"
	bash -c "install -v $(BUILDDIR)/$(KB_USER).keybase.pub/keybase.txt ~/$(GITHUB_USER).github.io"
	bash -c "install -v $(BUILDDIR)/$(KB_USER).keybase.pub/*.sig ~/$(GITHUB_USER).github.io"
	bash -c "install -d $(BUILDDIR)/$(KB_USER).keybase.pub/_* ~/$(GITHUB_USER).github.io/_*"
	make push-keybase
	make push-gh-pages
	@echo "Build finished. The HTML page is in ~/$(GITHUB_USER).github.io"
endif

.PHONY: push-gh-pages
.ONESHELL:
push-gh-pages: touch-time
ifeq ($(public),true)
	bash -c "cd ~/$(GITHUB_USER).github.io && \
		git status && \
		git add -f * && \
		git commit -m 'update from $(BASENAME) on $(TIME)' && \
		git push -f origin +master:master"
endif

.PHONY: failure
failure:
	@-/bin/false && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"
.PHONY: success
success:
	@-/bin/true && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"

