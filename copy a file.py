# copyfile() = copies contents of a file
# copy () = cpoyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (files creation and modification times)

#example

import shutil

shutil.copyfile('text.txt', 'copy.txt')# copy content of text.txt to copy.txt in visual studio , add path if you wanna store somewhere else
