import os
import hashlib
from collections import defaultdict
import argparse
from unittest.mock import file_spec


def __hash_file(file_path):
        hasher = hashlib.md5()

        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)

        return hasher.hexdigest()

def __find_identical_files(folder_path, delete_duplicate=False):
    size_to_files = defaultdict(list)

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_size = os.path.getsize(file_path)
                size_to_files[file_size].append(file_path)
            except OSError as e:
                print(f'Error accessing file {file_path}: {e}')

    file_hashes = defaultdict(list)

    for file_list in size_to_files.values():
        if len(file_list) > 1:
            for file_path in file_list:
                try:
                    file_hash = __hash_file(file_path)
                    file_hashes[file_hash].append(file_path)
                except OSError as e:
                    print(f'Error hashing file {file_path}: {e}')


    identical_files = [files for files in file_hashes.values() if len(files) > 1]

    if identical_files:
        print('Identical files')
        print()

        for files in identical_files:
            for file in files:
                print(file)
            if delete_duplicate:
                for file in files[1:]:
                    try:
                        os.remove(file)
                        print(f'Deleted: {file}')
                    except OSError as e:
                        print(f'Error deleting file {file}: {e}')
            print()
    else:
        print('No identical files found.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Find identical files in a folder')
    parser.add_argument('folder_path', type=str, help='Path to the folder to search for identify files')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete duplicate files automatically.')
    args = parser.parse_args()

    if os.path.isdir(args.folder_path):
        __find_identical_files(args.folder_path, args.delete)
    else:
        print('Invalid folder path.')