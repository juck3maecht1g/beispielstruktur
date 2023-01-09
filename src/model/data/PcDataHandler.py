# Todo sauberes Error handling


import yaml
import os
import shutil

class PcDataHandler:
    def __init__(self, root_path) -> None:
         self.root = root_path
         self.path = root_path

    def navigate_to_parent(self):
        if not (self.path == self.root):
            self.path = os.path.dirname(self.path)
            

    def navigate_to_child(self, name):
        if (name in self.list_children()):
            self.path = os.path.join(self.path, name)
            

    def list_children(self):
        return os.listdir(self.path)


    def get_path(self):
        return self.path

    def set_path(self, new_path):
        self.path = new_path


    def path_contains(self, name):
        return name in self.list_children()


    def is_root(self):
        return self.root == self.path


    def is_child_from_root(self):
        return self.root == os.path.dirname(self.path)

    def write_experiment_yaml(self, data, file):
        write_path = os.path.join(self.path, file)
        with open(write_path, "w") as outfile:
            yaml.dump(data, outfile)

    def write_global_yaml(self, data, file):
        write_path = os.path.join(self.root, file)
        with open(write_path, "w") as outfile:
            yaml.dump(data, outfile)

    def read_experiment_config(self, file):
        read_path = os.path.join(self.path, file)
        with open(read_path, 'r') as infile:
            return yaml.safe_load(infile)

    def read_global_config(self, file):
        read_path = os.path.join(self.root, file)
        with open(read_path, 'r') as infile:
            return yaml.safe_load(infile)


    def copy_file_from_parent(self, name):
        if not (name in self.list_children()):
            target = os.path.join(self.path, name)
            parent = os.path.dirname(self.path)
            file_in_parent = os.path.join(parent, name)
            shutil.copyfile(file_in_parent, target)


    def createDirectory(self, name):
        if not (name in self.list_children()):
            new_dir = os.path.join(self.path, name)
            os.mkdir(new_dir)

    def deleteDirectory(self, name):
        remove_path = os.path.join(self.path, name)
        shutil.rmtree(remove_path)

    def deleteFile(self, name):
        remove_path = os.path.join(self.path, name)
        os.remove(remove_path)


    

