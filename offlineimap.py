#!/usr/bin/python
import re, subprocess
def get_keychain_pass(server=None):
    params = {
        'server': server
    }
    command = "return lpass show $(server)s" % params
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    outtext = [l for l in output.splitlines()
               if l.startswith('Password: ')][0]
    return re.match(r'Password: "(.*)"', outtext).group(1)
