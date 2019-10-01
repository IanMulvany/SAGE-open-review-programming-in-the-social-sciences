import os
import glob 

ROOTDIR = os.sep.join(os.getcwd().split(os.sep)[:-1])
os.chdir(ROOTDIR +os.sep)

OUTPUTDIR = "Word_version"
TEMPDIR = ROOTDIR + os.sep + "temp"

for directory in glob.glob("Ch*"):
	CHAPTER = directory.split(os.sep)[-1][:5]
	print(CHAPTER)
	if  len(glob.glob(directory + os.sep + "*.ipynb")):
		os.system("jupyter nbconvert %s%s*.ipynb --to markdown --output-dir=\"%s\" >/dev/null" % (directory, os.sep,TEMPDIR))
		os.system("pandoc temp%s*.md -s -o %s%s%s.docx" % (os.sep, OUTPUTDIR, os.sep, CHAPTER))
		os.system("rm temp/*.md")
	
