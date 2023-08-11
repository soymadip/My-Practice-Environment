# This is a small Python file to automatically move my backed up files to proper directories. 
# In case of reseting my PC or system crash.  
# Run python3 -u "<Path to this file>"
# IF YOU WANNA USE IT, PLEASE MAKE SURE THAT YOU ARE USING FRESH INSTALL.
# BECAUSE THIS SCRIPT WILL DELETE YOUR OLD DIRECTORIES.

import os, shutil


# Paths:
BackupPath= "/mnt/sdb1/SDD BACKUP" # where Backup is located
RootPath= "/home/sd/2"             # your root directory
ConfigPath="/home/sd/2/.config"    # path to ConfigDicts
# Directories:
RootDicts= ["Documents",".mozilla",".themes",".vscode-oss","V-environment",".librewolf"]
ConfigDicts= ["libreoffice","mpv","syncthing","VSCodium"]



# Making  directories if they don't exist:-

# For root:-
def CheckRootPaths(paths):
    print('|\n|-☢️  Directory check Started:-\n|\n|')
    for path in paths:
        print('|')
        if(not os.path.exists(f'{RootPath}/{path}')):
            os.mkdir(f"{RootPath}/{path}")
            print(f"|- Created [~/{path}] as it didn't exist.")
        else:
            print(f'|- [~/{path}] exists.')

# For .config:-
def CheckConfigPaths(paths):
    if(not os.path.exists(f'{ConfigPath}/')):
        os.mkdir(f'{ConfigPath}/')
    for path in paths:
        print('|')
        if(not os.path.exists(f'{ConfigPath}/{path}')):
            os.mkdir(f"{ConfigPath}/{path}")
            print(f"|- Created [~.config/{path}] as it didn't exist.")
        else:
            print(f'|- [~/.config/{path}] exists.')
    print('|\n|\n|\n|-☢️  Directory check completed.\n|\n|-ℹ️  Proceeding to next step.')




#moving files to appropiate directories:

def copytree(src, dst, symlinks=False, ignore=None): # symlinks will be copied as regular file/directory 
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)




# Now starting Process:

print('|------------------------\n|-⏳  Restoring Backup..\n|\n|\n|')

CheckRootPaths(RootDicts)
CheckConfigPaths(ConfigDicts)
print('|\n|-☢️  Starting to move directories.\n|\n|')

for src in RootDicts:
    if(src == '.librewolf'):
      print("|\n|- [.librewolf] skipped as it's causing crash.")
      continue
    else:
     copytree(f'{BackupPath}/{src}',f'{RootPath}/{src}')
     print(f'|- [{src}] Done.')
print('|')

for k in ConfigDicts:
    copytree(f'{BackupPath}/{k}',f'{ConfigPath}/{k}')
    print(f'|- [.config/{k}] Done.')
print('|\n|\n|\n|-⌛  Backup Restored..\n|------------------------')



