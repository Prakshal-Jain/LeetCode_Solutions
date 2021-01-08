import shutil
import os

source_dir = '.'
target_dir = 'LeetCode Linked List'

file_names = os.listdir(source_dir)

def moveFile(file):
    for file_name in file_names:
        if(file_name.find(file) != -1):
            shutil.move(os.path.join(source_dir, file_name), target_dir)
moveFile("LeetCode Linked List")