# import packA.subA.sa2 # works when run python3 packA/a2.py
# from packA.subA import sa2 # works when run python3 packA/a2.py
# from subA import sa2 # works when run python3 a2.py and python3 packA/a2.py

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# now this works, even when a2.py is run directly
from packA.subA import sa2

print('Hello from packA/a2.py')