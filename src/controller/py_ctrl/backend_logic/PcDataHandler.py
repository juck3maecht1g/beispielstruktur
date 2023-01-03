#Todo sauberes Error handling

from .root_dir import root_path

root = root_path


import shutil
import os
os.chdir(root)


def navigate_to_parent():
    if not (os.getcwd() == root):
        new_path = os.path.dirname(os.getcwd())
        os.chdir(new_path)

def navigate_to_child(name):
    if(name in list_children()):
        new_path = os.path.join(os.getcwd(), name)
        os.chdir(new_path)
    
def list_children():
    return os.listdir()


def change_directory(path):
    os.chdir(path)

def change_directory_to_root():
    os.chdir(root)

def get_cwd():
    return os.getcwd()

def cwd_contains(name):
    return name in list_children()

def is_root():
    return root == os.getcwd()

def is_child_from_root():
    return root == os.path.dirname(os.getcwd())

def copy_file_from_parent(name):
    if not (name in list_children()):
            target = os.path.join(os.getcwd(), name)
            parent = os.path.dirname(os.getcwd())
            file_in_parent = os.path.join(parent, name)
            shutil.copyfile(file_in_parent, target)

def createDirectory(name):
    if not (name in list_children()):
        os.mkdir(name)

def deleteFile(name):
    remove_path = os.path.join(os.getcwd(), name)
    os.remove(remove_path)

def deleteDirectory(name):
    remove_path = os.path.join(os.getcwd(), name)
    shutil.rmtree(remove_path)
    
