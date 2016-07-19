# imagrAuth

![example](/resources/example.png)

**Another unfinished project.** Using @pudquick's [nibbler](https://gist.github.com/pudquick/f27efd1ddcbf57be0d14031a5e692015) project to display a simple python app from an nib. The idea behind this project is to run it as a script component inside of an [Imagr](https://github.com/grahamgilbert/imagr) workflow. This script will check for authorization via a LDAP lookup and if everything is hunky dory will exit(0) to continue the imaging workflow.

When playing with this you'll need to make sure `/usr/bin/ldapsearch` is present on your system. Most NetInstall environments will not have this by default.

**Did I mention this isn't finished?** The concept is finished but sticking it into Imagr and working isn't.


---

## What all these files?

* `imagrAuth.nib` - This is the window that contains the view, buttons, and text fields. Use Xcode for modications.
* `imagrAuth.py` - This is the python backend that does the actual account lookup to verify that the user has permissions to move forward with the imagr workflow.
    * Make sure and modify the three variables.
    
        ```python
        ADGROUP = "imagrusers"
        DOMAIN = "example.com"
        SEARCH_BASE = "DC=example,DC=com"
        ```

* `launchImagrAuth.sh` - A simple wrapper that mounts a DMG containing all the resources for `imagrAuth.py` to work. This is the script that your `imagr_config.plist` will call. See `imagr_config_example.plist` for more info.
* `nibbler.py` - @pudquick's creation to use nib files within python
* `Makefile` - run `make dmg` to create a dmg that you'll add to your 
* `imagr_config_example.plist` - An example imagr workflow to help connect the dots.

## How do I make this work in NetInstall?

**UNTESTED** Since `/usr/bin/ldapsearch` is likely not included in your NetInstall nbi you will need to add the frameworks for it yourself. The included `ldapsearch_NetInstall_Frameworks` directory will help you create a package with those frameworks (untested at this time). You should run that against a full OS and then install the output package in your NetInstall.