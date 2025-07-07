# File Organizer by Exension 
a sample and bedinner-friendly Python script to organaze files in a slected folder based on their entension .
This is my first personal Python  project ,  built to help me learn scripting, file handling, and GUI interactions in Python .

------------

## Fatures 

	- GUI folder selection (no needto type the path)
	- Atuomatically creates folder for each file exetension
	- Moves each file into the corresponding
	- Handle files without extension to (places them in a "no_extension" folder)
	
------------

## How It Works 
	
	1. Run the script.
	2. A dialog opens for you to choose a folder .
	3. All file inside the selected folder are scanned.
	4. Files are moved into subfolders based on their extension:
		- image.jpeg --> jpeg
		- song.mp3 --> mp3
		- README --> no_extension
		
--------------

## How It Run 
	Make share Python is installed on your system, then run :
	
'''bash
	python sort.py
