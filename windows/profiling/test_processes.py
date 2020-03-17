import glob
import os
import subprocess
import tkinter as tk
import win32clipboard # requires pywin32

import scandir_rs # requires scandir_rs

copy_pasta = tk.Tk()
copy_pasta.withdraw()
def return_list(func):
    def to_list(*args, **kwargs):
        return list(func(*args, **kwargs))
    return to_list

##########################
### Built-in Functions ###
##########################
@return_list
def glob_search(base_dir, search_term):
    return glob.iglob(f"{base_dir}\\**\\*{search_term}*", recursive=True)

@return_list
def scandir_search(base_dir, search_term):
    for entry in os.scandir(base_dir):
        if entry.is_file() and search_term in entry.name:
            yield os.path.join(base_dir, entry.name)
        elif entry.is_dir():
            yield from scandir_search(entry.path, search_term)
        else:
            pass

@return_list
def walk_search(base_dir, search_term):
    for root, directories, filenames in os.walk(base_dir):
        if any([search_term in filename for filename in filenames]):
            for filename in filenames:
                if search_term in filename:
                    yield os.path.join(root, filename)

########################
### DOS+ dir command ###
########################

@return_list
def dir_custom_search(base_dir, search_term):
    os.system('dir /b/s "{location}*{search_term}" > files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f.read().splitlines(): # have to use read & splitlines: otherwise "\n" appended to the end of each line
            yield line

@return_list
def dir_custom_altsplit_search(base_dir, search_term):
    os.system('dir /b/s "{location}*{search_term}" > files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f: # alternative splitlines, strip the \n instead of reading it with splitlines()
            yield line[:-1]

@return_list
def dir_custom_rstrip_search(base_dir, search_term):
    os.system('dir /b/s "{location}*{search_term}" > files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f: # alternative to splitlines using rstrip instead
            yield line.rstrip()

@return_list
def dir_custom_tkpre_search(base_dir, search_term): # Use clipboard + tkinter prebuilt
    os.system('dir /b/s "{location}*{search_term}" | clip'.format(location=base_dir, search_term=search_term))
    for line in copy_pasta.clipboard_get().splitlines():
        yield line

@return_list
def dir_custom_tkon_search(base_dir, search_term): # Use clipboard + tkinter built on run
    os.system('dir /b/s "{location}*{search_term}" | clip'.format(location=base_dir, search_term=search_term))
    for line in tk.Tk().clipboard_get().splitlines():
        yield line

@return_list
def dir_custom_win32_search(base_dir, search_term): # Use clipboard + pywin32
    os.system('dir /b/s "{location}*{search_term}" | clip'.format(location=base_dir, search_term=search_term))
    win32clipboard.OpenClipboard()
    for line in win32clipboard.GetClipboardData().splitlines()[:-1]: # [:-1 because the last line of the clipboard reads "\x00\x00\x00\x00\x00"]
        yield line
    win32clipboard.CloseClipboard()


################################
### Windows 7+ where command ###
################################

@return_list
def where_custom_search(base_dir, search_term):
    os.system('where /r "{location}" *{search_term}* > files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f.read().splitlines(): # have to use read & splitlines: otherwise "\n" appended to the end of each line
            yield line

@return_list
def where_custom_altsplit_search(base_dir, search_term):
    os.system('where /r "{location}" *{search_term}* > files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f: # alternative splitlines, strip the \n instead of reading it with splitlines()
            yield line[:-1]

@return_list
def where_custom_rstrip_search(base_dir, search_term):
    os.system('where /r "{location}" *{search_term}* > files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f: # alternative to splitlines using rstrip instead
            yield line.rstrip()

@return_list
def where_custom_tkpre_search(base_dir, search_term): # Use clipboard + tkinter prebuilt
    os.system('where /r "{location}" *{search_term}* | clip'.format(location=base_dir, search_term=search_term))
    for line in copy_pasta.clipboard_get().splitlines():
        yield line

@return_list
def where_custom_tkon_search(base_dir, search_term): # Use clipboard + tkinter built on run
    os.system('where /r "{location}" *{search_term}* | clip'.format(location=base_dir, search_term=search_term))
    for line in tk.Tk().clipboard_get().splitlines():
        yield line

@return_list
def where_custom_win32_search(base_dir, search_term): # Use clipboard + pywin32
    os.system('where /r "{location}" *{search_term}* | clip'.format(location=base_dir, search_term=search_term))
    win32clipboard.OpenClipboard()
    for line in win32clipboard.GetClipboardData().splitlines()[:-1]: # [:-1 because the last line of the clipboard reads "\x00\x00\x00\x00\x00"]
        yield line
    win32clipboard.CloseClipboard()

##################
### SCANDIR_RS ###
##################
@return_list
def scandir_rs_search(base_dir, search_term):
    for root, directories, filenames in scandir_rs.walk.Walk(base_dir):
        if any([search_term in filename for filename in filenames]):
            for filename in filenames:
                if search_term in filename:
                    yield os.path.join(root, filename)

if __name__ == "__main__":
    
    test_location = "D:\\SteamLibrary"
    dir_test_directory = "D:\\SteamLibrary\\\\"
    
    # BUILT-IN
    glob_search(test_location, ".exe")
    scandir_search(test_location, ".exe")
    walk_search(test_location, ".exe")
    # DIR
    dir_custom_search(dir_test_directory, ".exe")
    dir_custom_altsplit_search(dir_test_directory, ".exe")
    dir_custom_rstrip_search(dir_test_directory, ".exe")
    dir_custom_tkpre_search(dir_test_directory, ".exe")
    dir_custom_tkon_search(dir_test_directory, ".exe")
    dir_custom_win32_search(dir_test_directory, ".exe")
    # WHERE
    where_custom_search(test_location, ".exe")
    where_custom_altsplit_search(test_location, ".exe")
    where_custom_rstrip_search(test_location, ".exe")
    where_custom_tkpre_search(test_location, ".exe")
    where_custom_tkon_search(test_location, ".exe")
    where_custom_win32_search(test_location, ".exe")

    scandir_rs_search(test_location, ".exe")

