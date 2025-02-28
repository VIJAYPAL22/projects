# to get file with its extention
import os
file = input("Enter file with extention")
file_name,file_extention =os.path.splitext(file)
print("File name is "+file_name)
print("File extention name is "+file_extention)
