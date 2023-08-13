# This is a small Python file to automatically move backed up files(dotfiles) to proper directories,
# In case of reseting my PC or system crash.
# And this is my 1st code that has real-life use case.😇
# IF SOMEONE WANNA USE IT, MAKE SURE THAT YOU ARE USING AFTER FRESH OS INSTALL.
# BECAUSE THIS SCRIPT CAN CRASH OR DELETE YOUR OLD FILES IN DIRECTORIES.
# Run sudo python3 -u "<Path to this file>"

#____________________ User configs ________________________________________________

# Paths:
Root= "/home"                        # root directory
Home= f"{Root}/sd"                   # home directory. pattern: /{Root_folder}/<your username>
Pck_Mger= "nala"                     # The package manager your OS is using. I am using Nala as apt.
BckpPath="/mnt/sdb1/SDD BACKUP"    # where Backup folder is located.
Rest_flname="restore.py"             # This file's name. CHANGE IT YOU YOU'VE CHANGED THIS FILE'S NAME.
CPath=f"{Home}/.config"              # path to .Config Dict.  also can be added directly instead of using variable.

# Backed up directories: 
Dicts = {
    ".mozilla": f'{Home}',           # Pattern: "<directory name>":f'<path>',
    ".themes": f'{Home}',
    ".vscode-oss": f'{Home}',
    "Documents": f'{Home}',
    ".librewolf": f'{Home}',
    ".antigen": f'{Home}',
                                     # space for clarity between separate Paths.
    "libreoffice": f'{CPath}',
    "mpv": f'{CPath}',
    "syncthing": f'{CPath}',
    "VSCodium": f'{CPath}',
    "neofetch": f'{CPath}',
    "kdedefaults": f'{CPath}',
#    "plasmaConfSaver": f'{CPath}',  # Don't need. just for reminder.
    "menus": f'{CPath}',
    "gtk-4.0": f'{CPath}'
}


# Use  'Ctrl+s' & 'meta+x' to save,quit this file.

# ------------- DON'T TOUCH ANYTHING AFTER THIS --------------------------------------

#__________________ All Restore Functions ____________________________________________

import os, shutil                        # Gotta know more abput this 'shutil' module. 


# start with 'ask-edit' wizard:-
def get_user_choice(inp):
    global wpath                  
    wpath= os.getcwd()                    # this is global
    if(inp=='y'):
        os.system(f'nano "{wpath}/{Rest_flname}"')


# For making  directories if they don't exist:-
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
            print(f'|- [~{sp}/{k}] exists.')
    print('|\n|\n|\n|-\033[1;32m☢️  Directory check completed.\033[0m')



# For moving files to appropiate directories:
def copy(src, dst, symlinks=False, ignore=None): # symlinks will be copied as regular file/directory
    for item in os.listdir(src):
        if(item=='lock'):
            pass
            print(f'|-\033[91m SKIPPED [{src}/{item}].\033[0m\n|-\033[91m Move it manually.\033[0m')  # causing crash
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


# For Restoring:-
def copytree(Dict):
    print('|\n|-\033[1;32m☢️  Starting to move backed-up folders.\033[0m\n|\n|')
    for k,v in Dict.items():
        print(f'|- [{k}] started.')
        copy(f'{BckpPath}/{k}',f'{v}/{k}')
        print(f'|- Done.\n|')
    print('|\n|\n|-\033[1;32m☢️  Finished Moving.\033[0m')

def restore(Directory):
    print('|------------------------\n|-⏳\033[1;33m  Restoring Backup..\033[0m\n|\n|\n|')    # for some reason, terminal log needs two spaces to display one space...
    CheckPaths((Directory))
    print('|\n|-ℹ️  Proceeding to the next step.')
    copytree((Directory))
    print('|\n|\n|\n|-⌛\033[1;33m  Backup Restored..\033[0m\n|________________________')




#__________________ Triggar ______________________________________________________

#Triggaring restoration process:-

if(__name__=="__main__"): # for safety
    os.system('clear')    # clear terminal screen
    ans= input('Do you wanna change default configs? [y/n]\n>>> ')
    get_user_choice(ans)
    os.system('clear')
    restore(Dicts)
