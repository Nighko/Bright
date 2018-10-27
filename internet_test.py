# This is taken from Quora: https://www.quora.com/How-can-you-check-if-there-is-an-internet-connection-using-a-Python-script
# Modified by  me :D

#!/usr/bin/env python


def ping(verbose=False):
    """
    True if host responds to a ping request
    """
    import os
    import sys
    import subprocess
    import platform

    # some standard reliable targets
    # Level 3 anycast (default)
    host = "8.8.4.4"

    ping_str = "-c 1"  # just one ping
    need_sh = True    # for Linux

    # platform specifics  "Windows" "Linux" "Darwin" #
    platfrm = platform.system()
    if platfrm == "Windows":
        ping_str = "-n 1"
        need_sh = False

    # build a command
    cmd = "ping " + " " + ping_str + " " + host

    result = ""

    # do not show ping output
    if not verbose:
        # output suppressed to bit bucket
        devnul = open(os.devnull, 'w')
        result = subprocess.call(cmd, stdout=devnul, shell=need_sh)
    else:
        # show ping results
        result = subprocess.call(cmd,  shell=need_sh)

    # call returns 0 on success
    if result == 0:
        return True
    else:
        return False
