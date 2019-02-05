#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import sys
import os

debug = True

stderr = sys.stderr
stdout = sys.stdout

def clean(arg, dirname, names):
    for fn in names:
        
        if fn[-1] == '~' or fn.startswith('#') or fn.startswith('.#'):
            fp = os.path.join(dirname, fn)
            print('rm:', fp)
            os.remove(fp)


def execute():
    dirname = os.getcwd()
    print('clean', dirname)
    for path, dirs, files in os.walk(dirname):
        for fn in files:
            if fn[-1] == '~' or fn.startswith('#') or fn.startswith('.#'):
                fp = os.path.join(path, fn)
                print('rm:', fp)
                os.remove(fp)
            


if __name__ == '__main__':
    """
    main
    
    """
    execute()
