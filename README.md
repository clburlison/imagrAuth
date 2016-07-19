# imagrAuth

![example](/resources/example.png)

**Another not finished project.** Using @pudquick's [nibbler](https://gist.github.com/pudquick/f27efd1ddcbf57be0d14031a5e692015) project to display a simple python app from an nib. The idea behind this project is to run it as a script component inside of an [Imagr](https://github.com/grahamgilbert/imagr) workflow. This script will check for authorization via a LDAP lookup and if everything is hunky dory will exit(0) to continue the imaging workflow.

When playing with this you'll need to make sure `/usr/bin/ldapsearch` is present on your system. More NetInstall environments will not have this by default.

**Did I mention this isn't finished?** The concept is finished but sticking it into Imagr and working isn't.