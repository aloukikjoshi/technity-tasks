1) A relative path is a way to specify the location of a file or directory in a file system relative to a current working directory or another reference point. It is not an absolute path that starts from the root of the file system but rather describes how to navigate from one location to another within the file system structure. It is more securer than the absolute path.

2) An absolute path is a complete and unambiguous reference to a file or directory in a file system, and it always starts with the root directory of the file system.

3) Path('C:/Users') / 'Al' evaluates to C:\Users\Al when using the pathlib module.

4) "/" is used as the path separater in Python. I don't know about the others but on windows 'C:/Users' / 'Al' will evaluate to C:/Users/Al.

5) Both the functions are part of "os" module. 'os.getcwd()' returns the current working directory as a string. 'os.chdir(path)' changes the current working directory to the specified path.

6) The '.' folder represents the current directory and the '..' folder represents the parent directory of the current directory.

7) 'C:\bacon\eggs' is the directory name and the base name is the actual name of the file which is 'spam.txt'.

8) Read(r), Write(w) and Append(a).

9) If the file already exists, and is opened in the write mode, then the file will get overwrited on the existing file.

10) 'read()' Method: Reads the entire file content as a single string (in text mode) or as bytes (in binary mode).
    'readlines()' Method: Reads all lines of a text file and returns them as a list of strings.
