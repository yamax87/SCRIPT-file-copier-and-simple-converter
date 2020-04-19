import shutil
import os

folder_origin = r'C:\Users\donenmax\Desktop\test folder\test files2'

holding_folder = r'C:\Users\donenmax\Desktop\test folder\copied files'

destination_folder = r'C:\Users\donenmax\Desktop\test folder\destination'



for folder_location, child_folders, files in os.walk(folder_origin):
	for file_name in files: 
		directory = os.path.join(folder_location, file_name)
		shutil.copy(directory, holding_folder)



for folder_location, child_folders, files in os.walk(holding_folder):
	for file_name in files:
		full_path = os.path.join(folder_location, file_name)
		primed_path = os.path.splitext(full_path)[0]
		full_path = os.rename(full_path, primed_path + '.txt')


for item in os.listdir(holding_folder):
	print(item)
	full_path = os.path.join(holding_folder, item)
	shutil.move(full_path,folder_origin)
	

		

