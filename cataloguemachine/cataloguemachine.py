# PZI FINAL CATALOGUE 2008

from scribus import *
import glob, random, sys, datetime
# f = random.choice(files)
import os.path

# lettrist
def lettrist():
    theSizes = [20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25]

    for letter in range(159):
        selectText(letter, 1, 'name_box')
        setFontSize(random.choice(theSizes), 'name_box')

catpath = fileDialog("Pick Catalogue Folder", isdir=True)
matpath = os.path.join(catpath, "material")

# HOW MANY DIALOG
howmany = valueDialog("how many", "make how many catalogues? (0 for all)", "2")
howmany = int(howmany)

# exception class to "jump" out of the script
class MyStop(Exception):
	pass

def check(things, howmany, msg = "things"):	
	if len(things) < howmany:
		messageBox("uhoh", "not enough %s, there are %d, you want %d" % (msg, len(things), howmany))
		raise MyStop()

try:

	########################
	# GET THE MATERIALS
	########################
	
	# TITLE
	f = open(os.path.join(matpath, "ourCode.txt"))
	texts_title = f.readlines()
	f.close()
	if howmany == 0:
		howmany = len(texts_title)
	check(texts_title, howmany, "texts_title")
		
	# DANJA
	f = open(os.path.join(matpath, "danja/ip.txt"))
	texts_danja = f.readlines()
	f.close()
	if howmany == 0: # "all" actually means as many ip addresses as there are (500)
		howmany = len(texts_danja)
	check(texts_danja, howmany, "texts_danja")
	
	# ANNEMIEKE
	f = open(os.path.join(matpath, "annemieke/epicpedia.txt"))
	texts_annemieke = f.readlines()
	f.close()
	if howmany == 0:
		howmany = len(texts_annemieke)
	check(texts_annemieke, howmany, "texts_annemieke")
	
	# GORDO
	images_gordo = glob.glob(os.path.join(matpath, "gordo/*"))
	images_gordo.sort()
	check(images_gordo, howmany, "images_gordo")
	
	# RICARDO
	images_ricardo = glob.glob(os.path.join(matpath, "ricardo/ricardo_tiff/*"))
	images_ricardo.sort()
	check(images_ricardo, howmany, "images_ricardo")
	
	# LINDA
	images_linda = glob.glob(os.path.join(matpath, "linda/*"))
	images_linda.sort()
	check(images_linda, howmany, "images_linda")
	
	# MARIA
	images_maria = glob.glob(os.path.join(matpath, "maria/*"))
	images_maria.sort()
	check(images_maria, howmany, "images_maria")

	########################
	# MAKE THE DOCUMENTS
	########################

	pdf = PDFfile()
	# set pdf attributes common to all documents
	pdf.outdst = 1 # printer
		
	for count in range(howmany):
		
		#######
		# MAKE THE ACTUAL PAGE/OBJECT SUBSTITUTIONS WITH SCRIBUS COMMANDS
		#######
		
		defineColor("color_light",random.randrange(0,150),random.randrange(0,150),random.randrange(0,150),0)
                defineColor("color_medium",random.randrange(40,150),random.randrange(40,150),random.randrange(40,150),0)
		defineColor("color_dark",random.randrange(70,255),random.randrange(70,255),random.randrange(70,255),0)
		
                setFillColor("color_dark","background")
		setFillColor("color_light","spine_box")
		setTextColor("color_medium","name_box")
		
		rotateObject(random.randrange(0,360), "Polygon1")
		rotateObject(random.randrange(0,360), "Polygon2")
		rotateObject(random.randrange(0,360), "Polygon3")
		rotateObject(random.randrange(0,360), "Polygon4")
		rotateObject(random.randrange(0,360), "Polygon5")
		rotateObject(random.randrange(0,360), "Polygon6")
		rotateObject(random.randrange(0,360), "Polygon7")
		rotateObject(random.randrange(0,360), "Polygon8")
		rotateObject(random.randrange(0,360), "Polygon9")
		
		rotateObject(random.randrange(0,360), "PolygonA")
		rotateObject(random.randrange(0,360), "PolygonB")
		rotateObject(random.randrange(0,360), "PolygonC")
		
		rotateObject(random.randrange(0,360), "Line1")
		rotateObject(random.randrange(0,360), "Line2")
		rotateObject(random.randrange(0,360), "Line3")
		rotateObject(random.randrange(0,360), "Line4")
		rotateObject(random.randrange(0,360), "Line5")
		rotateObject(random.randrange(0,360), "Line6")
		rotateObject(random.randrange(0,360), "Line7")
		rotateObject(random.randrange(0,360), "Line8")
		rotateObject(random.randrange(0,360), "Line9")
		
		setText(texts_title[count], "text_title")
		setTextAlignment(0, "text_title")

		setText(texts_danja[count], "text_danja")
		
		setText(texts_annemieke[count], "text_annemieke")
		setTextAlignment(1, "text_annemieke")
		
		loadImage(images_gordo[count], "image_gordo")
		
		loadImage(images_linda[count], "image_linda")
		
		loadImage(images_ricardo[count], "image_ricardo")
		
		loadImage(images_maria[count], "image_maria")
				
		#######ivan
        	lettrist()
		#######
		
		now = datetime.datetime.now()
		setText(now.strftime("%Y-%m-%d %H:%M:%S"),"date_box")
		setTextAlignment(1, "date_box")

		#######
		# NAME & EXPORT THE PDF
		#######
		
		pdf.file = os.path.join(catpath, "pzimdma2008_cover_%04d.pdf" % (count+1))
		# supposedly "info" is required for some PDF compliance
		pdf.info = "pzimdma2008_cover_%04d" % (count+1)
		pdf.save()
		
except MyStop:
	pass