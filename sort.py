import os
import shutil
from  tkinter import Tk, filedialog

Tk().withdraw()
path0 = filedialog.askdirectory(title="Slect your folder")

if not os.path.exists(path0):
		print (item, "is worng path !!!")
		
for item in os.listdir(path0):
	full_path = os.path.join(path0 , item)
	
	if os.path.isfile(full_path):
		name, ext = os.path.splitext(item)
		ext = ext[1:].lower()
		
		if ext == "":
			print ("NoN Format !!!")

	dest_file = os.path.join(path0, ext)
	os.makedirs(dest_file, exist_ok = True)
	
	dest_path = os.path.join(dest_file, item)
	
	
	shutil.move(full_path, dest_path)
	
	print (f"{item} --> {ext} ")
	print (f"Sort Succsusfull !!! ")
