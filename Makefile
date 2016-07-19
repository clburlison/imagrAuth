# Makefile for imagrAuth related tasks
# hdiutil formats http://superuser.com/a/146053

PROJECT="imagrAuth"

#################################################

##Help - Show this help menu
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

##  dmg - Wrap the scripts inside a dmg
dmg:
	rm -f ./${PROJECT}.dmg
	rm -rf /tmp/${PROJECT}-build
	mkdir -p /tmp/${PROJECT}-build/
	cp -R {README.md,imagrAuth.nib,imagrAuth.py,nibbler.py} /tmp/${PROJECT}-build
	hdiutil create -srcfolder /tmp/${PROJECT}-build -volname "${PROJECT}" -format UDRW -o ${PROJECT}.dmg
	rm -rf /tmp/${PROJECT}-build
