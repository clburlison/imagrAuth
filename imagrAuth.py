#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
imagrAuth is an authorization prompt that can be loaded into an Imagr script
component. When authorization fails an error message will be displayed on
screen and will prevent future components from running. This is accomplished by
exit 20 if authorization fails.

Referenced code:
https://gist.github.com/pudquick/f27efd1ddcbf57be0d14031a5e692015
http://everythingisgray.com/2014/01/02/querying-ad-group-membership-status-with-ldapsearch/
'''

import subprocess
import os
from nibbler import *

ADGROUP = "imagrusers"
DOMAIN = "example.com"
SEARCH_BASE = "DC=example,DC=com"

try:
    script_path = os.path.dirname(os.path.realpath(__file__))
    n = Nibbler(os.path.join(script_path, 'imagrAuth.nib'))
except IOError, ImportError:
    print "Unable to load nib!"
    exit(20)


def exitScript():
    '''Exit imagrAuth and don't continue the imagr workflow'''
    print "Goodbye!"
    n.quit()
    exit(1)


def reboot():
    '''Reboot the machine. This keeps whatever is currently blessed'''
    subprocess.call(['/sbin/reboot'])


def getADGroup(username, password):
    '''This checks to see if the user in question is part of the AD Group.'''
    try:
        cmd = subprocess.check_output(['/usr/bin/ldapsearch', '-LLL', '-h',
                                       DOMAIN, '-x', '-D',
                                       '{0:}@{1:}'.format(username, DOMAIN),
                                       '-w', password, '-b', SEARCH_BASE,
                                       'sAMAccountName={0:}'.format(username),
                                       'memberOf'])
        if cmd.find(ADGROUP) == -1:
            print "Not found in the AD Group"
            return False
        else:
            print "Found in the AD Group"
            return True
    except Exception as e:
        print e
        return False


def runner():
    '''Wrapper to call the getADGroup method on button click. Handles feedback
    to feedback_result text field.'''
    username = n.views['username_input'].stringValue()
    password = n.views['password_input'].stringValue()
    feedback = n.views['feedback_result']

    if getADGroup(username, password):
        # User has the correct username/password and they are authroized
        feedback.setStringValue_(u"✅ Valid user")
        exit(0)
    else:
        feedback.setStringValue_(u"❌ Invalid user or not authorized")


def main():
    '''Main method.'''
    n.attach(runner, 'continueButton')
    n.attach(reboot, 'restartButton')
    n.attach(exitScript, 'exitButton')

    n.hidden = True
    n.run()

if __name__ == '__main__':
    main()
