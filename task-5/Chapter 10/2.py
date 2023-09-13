# The function used to rename the files in 'os.rename' which belongs to the 'os' module.
# It allows us to change the name of the file by specifying its current path name and the new path name we want to assign to it.
# Here is how it is done.......

import os

old_name = 'old_file.txt'
new_name = 'new_file.txt'

os.rename(old_name, new_name)
