import os

directories = os.popen("ls").read()

for directory in directories.split("\n"):
    if not directory:
        continue
    
    os.chdir(directory)
    os.system("zip -r " + directory + ".zip plots")
    os.chdir("..")
    
