__author__ = 'Guruguha'

# Command line args

import sys
for x in sys.argv:
    print(x)
print(sys.path)

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

