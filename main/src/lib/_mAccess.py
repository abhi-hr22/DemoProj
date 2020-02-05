### Adding access Control of each module to other Modules

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir_1 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir_1) 