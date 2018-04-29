import os
import shutil, sys
from shutil import copyfile


def attach(path_in, path_in_labels, path_out, path_out_labels):
	filelist=os.listdir(path_in_labels)
	for f in filelist:
	    shutil.copy2(path_in_labels+f  , path_out_labels)
	filelist1=os.listdir(path_in)
	for f in filelist1:
	    shutil.copy2(path_in+f  , path_out )

if __name__ == '__main__':
    var1 = sys.argv[1]
    var2 = sys.argv[2]
    var3 = sys.argv[3]
    var4 = sys.argv[4]
    var5 = sys.argv[5]
    if var5=='train':
	    print('start attaching train data')
	    attach(var1, var2, var3, var4)
    if var5=='val':
	    print('start attaching val data')
		attach(var1, var2, var3, var4)
