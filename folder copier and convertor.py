import shutil
import os
import sys

while True:
	folder_origin = input('Enter the folder location whose files you wish to back up.\n')
	try:
		os.listdir(folder_origin)
		break
	except FileNotFoundError:
		print('Sorry, this folder does not appear to exist, or is not valid.\n')
		

while True:
	convert_to_txt = input('\nConvert files to .txt? (y/n)')
	convert_to_txt = convert_to_txt.lower()
	if (convert_to_txt == 'y') or (convert_to_txt == 'n'):
		break
	else:
		print('Sorry, that input is not valid.\n')
 

backup_folder_name = 'NEW FILES'

backup_folder_nameIteration = 1

total_child_folders = 0
total_files = 0

if convert_to_txt == 'n':

	while backup_folder_name + '_' + str(backup_folder_nameIteration) in os.listdir(folder_origin):
		backup_folder_nameIteration += 1

	backup_folder_name += '_' + str(backup_folder_nameIteration)
	backup_folder = os.path.join(folder_origin, backup_folder_name)

	shutil.copytree(folder_origin, backup_folder)
	

if convert_to_txt == 'y':
	
	while backup_folder_name + '_' + str(backup_folder_nameIteration) + '_TxtFiles' in os.listdir(folder_origin):
		backup_folder_nameIteration += 1

	backup_folder_name += '_' + str(backup_folder_nameIteration) + '_TxtFiles'
	backup_folder = os.path.join(folder_origin, backup_folder_name)

	shutil.copytree(folder_origin, backup_folder)

	for folder_location, child_folders, files in os.walk(backup_folder):
		for file_name in files:
			full_path = os.path.join(folder_location, file_name)
			primed_path = os.path.splitext(full_path)[0]
			full_path = os.rename(full_path, primed_path + '.txt')
	shutil.move(backup_folder, backup_folder)
	
	
for folder_name, child_folders, files in os.walk(backup_folder):
		for child_folder in child_folders:
			total_child_folders += 1
		for each_file in files:
			total_files += 1

print('-'*50+'\n')

print(str(total_child_folders) + ' folders found.')
print(str(total_files) + ' files found.')

print('\nAll files and folders successfully relocated.\n')

if convert_to_txt == 'y':
	print('All files successfully converted.\n')

print('-'*50)

input('\n\nPress Enter to exit.')







		

