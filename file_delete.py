import os

try:
    os.remove('./file_to_be_deleted.txt')
except FileNotFoundError:
    print('File already deleted!')



# -----WITH function exists checking if file is existing and then remove-----
# from os import remove
# from os.path import exists
#
# file_path = './file_to_be_deleted.txt'
#
# if exists(file_path):
#     remove(file_path)
#     print("File Deleted")
# else:
#     print('File already deleted')