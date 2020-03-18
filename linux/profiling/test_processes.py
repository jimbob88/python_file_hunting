import glob
import os
import subprocess
import scandir_rs

def return_list(func):
    def to_list(*args, **kwargs):
        return list(func(*args, **kwargs))
    return to_list

@return_list
def glob_search(base_dir, search_term):
    return glob.iglob(f"{base_dir}/**/*{search_term}*", recursive=True)

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

@return_list
def find_custom_search(base_dir, search_term):
    os.system('find {location} -name "*{search_term}*" > ./files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f:
            yield line

@return_list
def find_custom_mem_search(base_dir, search_term):
    os.system('find {location} -name "*{search_term}*" > /dev/shm/files.txt'.format(location=base_dir, search_term=search_term))
    with open('/dev/shm/files.txt', 'r') as f:
        for line in f:
            yield line            

@return_list
def find_custom_mem_qread_search(base_dir, search_term):
    result = subprocess.check_output('find {location} -name "*{search_term}*"'.format(location=base_dir, search_term=search_term), shell=True).decode()   
    for line in result.splitlines():
        yield line

@return_list
def mlocate_custom_search(base_dir, search_term):
    os.system('mlocate {location} {search_term} > ./files.txt'.format(location=base_dir, search_term=search_term))
    with open('files.txt', 'r') as f:
        for line in f:
            yield line

@return_list
def mlocate_custom_mem_search(base_dir, search_term):
    os.system('mlocate {location} {search_term} > /dev/shm/files.txt'.format(location=base_dir, search_term=search_term))
    with open('/dev/shm/files.txt', 'r') as f:
        for line in f:
            yield line            

@return_list
def mlocate_custom_mem_qread_search(base_dir, search_term):
    result = subprocess.check_output('mlocate {location} {search_term}'.format(location=base_dir, search_term=search_term), shell=True).decode()   
    for line in result.splitlines():
        yield line

@return_list
def scandir_rs_search(base_dir, search_term):
    for root, directories, filenames in scandir_rs.walk.Walk(base_dir):
        if any([search_term in filename for filename in filenames]):
            for filename in filenames:
                if search_term in filename:
                    yield os.path.join(root, filename)

if __name__ == "__main__":
    glob_search("/media/james/Development/Programming", 'py')
    scandir_search("/media/james/Development/Programming", 'py')
    walk_search("/media/james/Development/Programming", 'py')
    find_custom_search("/media/james/Development/Programming", 'py')
    find_custom_mem_search("/media/james/Development/Programming", 'py')
    find_custom_mem_qread_search("/media/james/Development/Programming", 'py')
    mlocate_custom_search("/media/james/Development/Programming", 'py')
    mlocate_custom_mem_search("/media/james/Development/Programming", 'py')
    mlocate_custom_mem_qread_search("/media/james/Development/Programming", 'py')
    scandir_rs_search("/media/james/Development/Programming", 'py')