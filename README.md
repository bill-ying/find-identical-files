# find-identical-files

This program takes a folder as input and displays the names of identical files (files with the same content) in the folder.  It optimizes the process by first grouping files by their size and then calculating hashes only for files  with the same size.  Additionally, it provides an option to automatically delete duplicate files.

## Features:

- Effectively finds identical files by groouping files by size before hashing.
- Uses MD5 hashing to compare file contents.
- Handles errors gracefully and prints error messages to the console.
- Optionally deletes duplicate files automatically.

## Usage:

Run the script with the folder path as an argument:
- python find_identical_files /path/to/folder

To automatically delete duplicate files, use the -d or --delete option:
- python find_identical_files /path/to/folder -d

The script will display the names of identical files in the specified folder and print any error encountered.  If -d or --delete option is specified, duplicate files will be deleted automatically.

## Example:

- python find_identical_files /path/to/folder
- python find_identical_files /path/to/folder -d


## Error Handing:

- Error accessing file /path/to/folder/file.txt: [Errno 13] Permission denied: '/path/to/folder/file.txt'
- Error hashing file /path/to/folder/file.txt: [Errno 2] No such filee or directory: '/path/to/folder/file.txt'
- Error deleting file /path/to/folder/file.txt: [Errno 13] Permission denied: '/path/to/folder/file.txt'