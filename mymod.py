# this is a module  - I want it to stop people to executing it directly
# when imported , the value of __name__ will be the module name (not '__main__').

import sys

if __name__ == '__main__':
    sys.exit()

def myfunc():
    pass



print(__name__)
