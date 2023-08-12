# This is a small Python file to automatically move my backed up files to proper directories.
# In case of reseting my PC or system crash.  
# And this is my 1st code that can be used for practical/real-life Problems.😇
# Run python3 -u "<Path to this file>"
# IF YOU WANNA USE IT, PLEASE MAKE SURE THAT YOU ARE USING FRESH INSTALL.
# BECAUSE THIS SCRIPT WILL CRASH OR DELETE YOUR OLD FILES IN DIRECTORIES.

import os, shutil               # importing modules



# Paths:
Root= "/home"                     # root directory
Home= f"{Root}/sd/2"                # home directory. pattern: /{Root_folder}/<your username>
BackupPath="/mnt/sdb1/SDD BACKUP" # where Backup is located
Path2=f"{Home}/.config"           # path to .Config Dict.  also can be added directly instead of using variable.

# Directories:
Dicts = {
    ".mozilla": f'{Home}',       # Pattern: "<directory name>":f'<path>',
    ".themes": f'{Home}',
    ".vscode-oss": f'{Home}',
    "V-environment": f'{Home}',
    # "Documents": f'{Home}',
    ".librewolf": f'{Home}',
                                 # space for clarity between separate Paths.
    "libreoffice": f'{Path2}',
    "mpv": f'{Path2}',
    "syncthing": f'{Path2}',
    # "VSCodium": f'{Path2}'
}





# Making  directories if they don't exist:-
def CheckPaths(Dict):
    print('|\n|-☢️  Directory check Started:-\n|\n|')
    for k,v in Dict.items():
        split = v.split(f'{Home}')
        sp= split[1]
        print('|')
        if(not os.path.exists(f'{v}/{k}')):
            os.makedirs(f"{v}/{k}/", exist_ok=True)
            print(f"|- Created [~{sp}/{k}] as it didn't exist.")
        else:
            print(f'|- (~{sp}/{k}) exists.')



# moving files to appropiate directories:
def copy(src, dst, symlinks=False, ignore=None): # symlinks will be copied as regular file/directory 
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        print(f"Copying from: {s} to: {d}")      # Print source and destination. for testing purpose.
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def copytree(Dict):
    for k,v in Dict.items():
        print(f'|- [{k}] started.')
        copy(f'{BackupPath}/{k}',f'{v}/{k}')
        print(f'|- Done.\n|')


# Restoring:-
def restore(Directory):
    print('|------------------------\n|-⏳  Restoring Backup..\n|\n|\n|')    # for some reason, terminal log needs two spaces to display one space...
    CheckPaths((Directory))
    print('|\n|\n|\n|-☢️  Directory check completed.\n|\n|-ℹ️  Proceeding to next step.')
    print('|\n|-☢️  Starting to move backed-up folders.\n|\n|')
    copytree((Directory))
    print('|\n|\n|\n|-⌛  Backup Restored..\n|------------------------')




# Trigarring restoration process:-
if(__name__=="__main__"): # for safety
    restore(Dicts)