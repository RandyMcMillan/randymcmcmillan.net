TIME := $(shell date +%s)
export TIME
#GIT CONFIG
GIT_USER_NAME							:= $(shell git config user.name)
export GIT_USER_NAME
GIT_USER_EMAIL							:= $(shell git config user.email)
export GIT_USER_EMAIL
GIT_SERVER								:= https://github.com
export GIT_SERVER
GIT_PROFILE								:= bitcoincore-dev
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

.PHONY: report
report: touch-time
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
push: touch-time
	bash -c "git add -f * && \
		git commit -m 'update from $(GITHUB_USER_NAME) on $(TIME)'"
	git push -f origin	+master:master

.PHONY: automate
automate: touch-time
	./.github/workflows/automate.sh

.PHONY: touch-time
.ONESHELL:
touch-time:
	touch 1
	touch $(TIME)
	$(shell git rm -f 16*)
	rm -f 16*
	touch $(TIME)
	echo $(TIME) $(shell git rev-parse HEAD) > $(TIME)
	touch 1

.PHONY: failure
failure: touch-time
	@-/bin/false && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"
.PHONY: success
success:
	@-/bin/true && ([ $$? -eq 0 ] && echo "success!") || echo "failure!"
