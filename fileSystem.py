import json
import pickle

#file object
class File:
    def __init__(self, data : str = "") -> None:
        self.data = data
        self.mode = ""
        self.open = False

    def write(self, text : str):
        assert(self.open)
        if self.mode == 'w':
            self.data = text
        elif self.mode == 'a':
            self.data = self.data + text
      
    def read_from_file(self):
        assert(self.open)
        print(self.data)

    def read_certain_content(self, start, size):
        assert(self.open)
        print(self.data[start:(start+size)])

    def write_at_location(self, location, text : str):
        assert(self.open)
        self.data = self.data[0:location] + text
    
    def truncate(self, location):
        assert(self.open)
        self.data = self.data[0 : location]
        
    def close(self):
        assert(self.open)
        self.open = False

    def move_within_file(self, start, size, target):
        assert(self.open)
        move_chars = self.data[start, start + size]
        self.data = self.data[0:start]+self.data[(size+start):target]+move_chars+self.data[target:len(self.data)]

def get(dictionary : dict,list : list) -> dict:
    if len(list) == 1:
        return dictionary[list[0]]
    else:
        return get(dictionary[list[0]],list[1:])

# will filter out all the empty strings after splitting
def get_keys_list(text : str):
    return filter(None, text.split('/')) 

class FileSystem:
    def __init__(self) -> None:
        self.catalogue = {'/' : {}} # '/' is the root folder

    #Creates a file in the directory specified with '/' delimiter. Example create('Hello/Meow/mahad.txt') will create 'mahad.txt' in Hello/Meow nested directory
    #All paths must be relative to root
    def create(self, name : str) -> None:
        keys_list = [ '/', *get_keys_list(name)] # => [ "/", "dir1", "whattaburger"]
        get(self.catalogue, keys_list[:-1]).update({keys_list[-1] : File()})

    #Creates a directory in the specified path. Each directory node is a python dictionary to accomodate its files
    def mkdir(self, name : str) -> None:
        keys_list = [ '/', *get_keys_list(name)]
        get(self.catalogue, keys_list[:-1]).update({keys_list[-1] : {}})

    #delete both file or directory
    def delete(self, name : str) -> None:
        keys_list = [ '/', *get_keys_list(name)]
        get(self.catalogue, keys_list[:-1]).pop(keys_list[-1])

    def move(self, name : str, target_directory):
        source_keys_list = [ '/', *get_keys_list(name)]
        target_keys_list = [ '/', *get_keys_list(target_directory)]
        #updating the catalogue
        target = get(self.catalogue, source_keys_list[:-1]).pop(source_keys_list[-1])
        get(self.catalogue, target_keys_list).update({source_keys_list[-1] : target})

    def open(self, name : str, mode : str) -> File:
        source_keys_list = [ '/', *get_keys_list(name)]
        f = get(self.catalogue, source_keys_list)
        f.mode = mode
        f.open = True
        return f

    def close(self, name : str):
        source_keys_list = [ '/', *get_keys_list(name)]
        f = get(self.catalogue, source_keys_list)
        f.open = False

#displays memory map
def show_memory_map():
    with open(b"fs.dat", "wb") as f:
        pickle.dump(fs, f)
    with open("fs.dat", "rb") as f:
        FS  = pickle.load(f)
        print(json.dumps(FS.catalogue, indent=4, sort_keys=True, default=str))

#generates the object .dat file
def create_dat_file():
    with open(b"fs.dat", "wb") as f:
        pickle.dump(fs, f)

#displays the operations availible in file system
def display_command_menu():
    print("This file system supports the following commands.")
    print("Enter the number associated with each command and the parameters it takes.")
    print("\t 1. Create a file\n \
    2. Delete a file\n \
    3. Create a directory\n \
    4. Change the directory of a file or directory\n \
    5. Move a file\n \
    6. Open a file\n \
    7. Close a file\n \
    8. Write to a file\n \
    9. Read from a file\n \
    10. Move within a file\n \
    11. Truncate a file\n \
    12. Show memory Map.\n \
    13. Exit the file system.\n \
    Enter your choice: ",end = '')

#handles the menu choices
def handle_menu(choice):
    if (choice == 1):
        print("Enter the file path with new name: ",end='')
        file_name = input()
        fs.create(file_name)
        
    elif (choice == 2):
        print("Enter the file path to delete: ",end='')
        file_name = input()
        fs.delete(file_name)
        
    elif (choice == 3):
        print("Enter the new directory path with new name: ",end='')
        dir_name = input()
        fs.mkdir(dir_name)
        
    elif (choice == 4):
        #this command is redundant in this file system
        pass
    
    elif (choice == 5):
        print("Enter the path of file or dir to move: ",end='')
        file_name = input()
        print("Enter the destination path: ", end='')
        dest_path = input()
        fs.move(file_name, dest_path)

    elif (choice == 6):
        print("Enter the path of file to open: ",end='')
        file_name = input()
        print("Open the mode you want to open the file in. You can type 'w' or 'a': ",end='')
        mode = input()
        global File
        File= fs.open(file_name,mode)

    elif (choice == 7):
        print("Enter the path of file to close: ",end='')
        File.close()

    elif (choice == 8):
        print("Do you want to write in default mode or specific location? Enter 1 or default, 2 for a location: ",end='')
        write_method = int(input())
        print("Enter the content you wish to write: ", end='')
        write_string = input()
        if (write_method == 1):
            File.write(write_string)
        else:
            print("Enter the start location: ",end='')
            location = int(input())
            File.write(location, write_string)

    elif (choice == 9):
        print("Do you want to read in default mode or specific location? Enter 1 or default, 2 for a location: ",end='')
        write_method = int(input())
        if (write_method == 1):
            File.read()
        else:
            print("Enter the start location: ",end='')
            location = int(input())
            print("Enter the size you wish to read:",end='')
            size = int(input())
            File.read_certain_content(location, size)

    elif (choice == 10):
        print("Enter start location: ",end='')
        start = int(input())
        print("Enter the size to move: ",end='')
        size = int(input())
        print("Enter the target location: ",end='')
        target = int(input())
        File.move_within_file(start,size,target)

    elif (choice == 11):
        File.truncate()
        print("File successfully truncated.")

    elif (choice == 12):
        print("Displaying memory map...")
        show_memory_map()

    elif (choice == 13):
        with open(b"fs.dat", "wb") as f:
            pickle.dump(fs, f)
        global loop_var
        loop_var = False

#a sample file system creation with some operations     
def sampleFileSystem():
    fs = FileSystem()
    fs.create("Siraj.txt")
    fs.create("Hello.txt")
    fs.mkdir("dir1")
    fs.create("dir1/shahab.txt")
    fs.mkdir("dir1/meow")
    fs.create("dir1/meow/hello.txt")
    fs.delete("dir1/meow")
    file = fs.open("Siraj.txt","w")
    file.write("hello world")
    file.read_from_file()
    with open(b"fs.dat", "wb") as f:
        pickle.dump(fs, f)
    with open("fs.dat", "rb") as f:
        FS  = pickle.load(f)
        print(json.dumps(FS.catalogue, indent=4, sort_keys=True, default=str))

    

#sampleFileSystem()    
main execution menu
fs = FileSystem()
loop_var = True
while (loop_var):
    display_command_menu()
    choice = int(input())
    handle_menu(choice)
print("File System Successfully exited.")

