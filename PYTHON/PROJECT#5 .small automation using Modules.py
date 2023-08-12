# This is a small Python file to automatically move my backed up files to proper directories.
# In case of reseting my PC or system crash.  
# And this is my 1st code that can be used for practical/real-life Problems.😇
# Run python3 -u "<Path to this file>"
# IF YOU WANNA USE IT, PLEASE MAKE SURE THAT YOU ARE USING FRESH INSTALL.
# BECAUSE THIS SCRIPT WILL CRASH OR DELETE YOUR OLD FILES IN DIRECTORIES.

import os, shutil               # importing modules


#____________________ User configs ________________________________________________

# Paths:
Root= "/home"                     # root directory
Home= f"{Root}/sd/"               # home directory. pattern: /{Root_folder}/<your username>
# Home= f"{Root}/sd/2"            # This one is for testing.
BackupPath="/mnt/sdb1/SDD BACKUP" # where Backup is located.
Path2=f"{Home}/.config"           # path to .Config Dict.  also can be added directly instead of using variable.

# Directories:
Dicts = {
    ".mozilla": f'{Home}',       # Pattern: "<directory name>":f'<path>',
    ".themes": f'{Home}',
    ".vscode-oss": f'{Home}',
    "V-environment": f'{Home}',
     "Documents": f'{Home}',
    ".librewolf": f'{Home}',
                                 # space for clarity between separate Paths.
    "libreoffice": f'{Path2}',
    "mpv": f'{Path2}',
    "syncthing": f'{Path2}',
     "VSCodium": f'{Path2}'
}


#__________________ All Restore Functions _____________________________________________


# Making  directories if they don't exist:-
def CheckPaths(Dict):
    print('|\n|-\033[1;32m☢️  Directory check Started:-\033[0m\n|\n|')
    for k,v in Dict.items():
        split = v.split(f'{Home}')
        sp= split[1]
        print('|')
        if(not os.path.exists(f'{v}/{k}')):
            os.makedirs(f"{v}/{k}/", exist_ok=True)
            print(f"|- Created [~{sp}/{k}] as it didn't exist.")
        else:
            print(f'|- (~{sp}/{k}) exists.')
    print('|\n|\n|\n|-\033[1;32m☢️  Directory check completed.\033[0m')



# moving files to appropiate directories:
def copy(src, dst, symlinks=False, ignore=None): # symlinks will be copied as regular file/directory 
    for item in os.listdir(src):
        if(item=='lock'):
            pass
            print(f'|-\033[91m SKIPPED [{src}/{item}].\n|- Move it manually.\033[0m')  # causing crash
            continue
        else:
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
#       print(f"Copying from: {s} to: {d}")      # Print source and destination. for testing purpose. 
        if os.path.isdir(s):
            if symlinks:
                shutil.copytree(s, d, symlinks, ignore)
            else:
                copy(s, d, symlinks, ignore)
        else:
            if not (symlinks and os.path.islink(s) and os.path.exists(os.readlink(s))):
                os.makedirs(os.path.dirname(d), exist_ok=True)
                shutil.copy2(s, d)

def copytree(Dict):
    print('|\n|-\033[1;32m☢️  Starting to move backed-up folders.\033[0m\n|\n|')
    for k,v in Dict.items():
        print(f'|- [{k}] started.')
        copy(f'{BackupPath}/{k}',f'{v}/{k}')
        print(f'|- Done.\n|')
    print('|\n|\n|-\033[1;32m☢️  Finished Moving.\033[0m')

# Restoring:-
def restore(Directory):
    print('|------------------------\n|-⏳\033[1;33m  Restoring Backup..\033[0m\n|\n|\n|')    # for some reason, terminal log needs two spaces to display one space...
    CheckPaths((Directory))
    print('|\n|-ℹ️  Proceeding to the next step.')
    copytree((Directory))
    print('|\n|\n|\n|-⌛\033[1;33m  Backup Restored..\033[0m\n|------------------------')



#__________________ Triggar ______________________________________________________


# Triggaring restoration process:-
if(__name__=="__main__"): # for safety
    restore(Dicts)