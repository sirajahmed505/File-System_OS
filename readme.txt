File System User Manual

Supported File Types
This system is a python based file system, that maintains directories and files(text files only).

Pathing
Some important instructions to know before using this system include the file and directory pathing.
There is a root directory named '/', which is the home directory, is the parent of all the content in the 
file system(files and directories). If a file 'file.txt' is created just by specifying the name, 
then is absolute path is '/file.txt'. For a directory 'dir1' in root, containing a file 'text.txt', 
then the path for 'text.txt' is specified as '/dir1/text.txt'. And hence, all the file paths can be 
managed in an orderly manner.

Operations in the File System
1. Create a file, takes file name/path as parameter.
2. Delete a file, takes file name/path as parameter.
3. Make a directory, takes directory name/path as parameter.
4. Move a directory or file, takes file/directory name/path and destination 
directory path as parameter,
5. Open a file, it takes two parameters, file name/path to open, and mode in which to open.
This file system supports two modes, write 'w' and append 'a'.
6. Close a file, takes file name/path as parameter.
7. Writing to a file, there are two ways to write in a file, implemented by file system.
	a. Default write, it will overwrite the given string, or append it. Depending on the 
	open mode. It takes one parameter, the string to write.
	b. Write at a location, it overwrites or appends at a specified location. It takes two 
	parameters, the content to write and location to write at. 
8. Reading from a file, there are two ways to read from a file, implemented by file system.
	a. Default read, reads all the content in a file. 
	b. Read at location, it reads the certain specified content of a file. It takes two 
	parameters start location, and the size to read.
9. Moving within a file, this functionality, moves certain content in the file to another
location in the same file. It takes three parameters, start location, size to read, and the target 
location.
10. Truncate file operation truncates the content in a file.
11. You can view the directory and file structure of the file system by the option to view
memory map.

Note:
 - The file related operations can only be perform on a file at time and only afer it has been
   opened by the functionality of open file.
 - All locations and sizes are integers, and the count is based on number of characters. The first
   index is zero. For instance, in string "hello" the charater count starts on 0 and ends on 4.
 - To perform edits in another file, you must close the current file first.
 - Additionally, when you are done with the file system, you can exit the system, it will create
   a .dat file for your file system, so next time you execute the file it will start from where
   you left off on the system.

Interface 
The file system is very easy to use since whenever you wish to perform anything, there are
text prompts to tell you what parameter to end. So, you don't have to remember the parameters.
You can also view the directory structure as you require, in case you forgot any paths.


	

