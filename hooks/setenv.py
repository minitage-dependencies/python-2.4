import os, sys
import re
def getpythonenv(options,buildout):
    """Where python looks to get its cflags."""
    if os.uname()[0] == 'Darwin':
        cwd = os.getcwd()
        os.chdir(options['compile-directory'])
        os.system('autoconf -v -f')
        os.chdir(cwd)
    # holly hack to make cflags/ldflags from minitage always in compilation statements
    os.environ['OPT'] = os.environ['CFLAGS']


def patchincludes(options,buildout):
    """Where python looks to get its cflags."""
    u, v = os.uname()[0],os.uname()[3]
    if u == 'Darwin' and v == '9.8.0':
        cmyfile = [l for l in open(
                        os.path.join(
                                options['compile-directory'],
                                'pyconfig.h'),
                        'r'
                     ).readlines() if not 'SETPGRP_HAVE_ARG' in l]
        cmyfile = open(
                        os.path.join(
                                options['compile-directory'],
                                'pyconfig.h'),
                        'w'
                     ).writelines(cmyfile + ['\n#define SETPGRP_HAVE_ARG 1\n'])
# vim:set ts=4 sts=4 et  :
