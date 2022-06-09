import io

file_path = 'text2.txt'

try:
    io.open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')