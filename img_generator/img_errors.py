from PIL import Image
import sys, glob

total_broken = 0
for img in glob.glob(sys.argv[1] + '*'):
	try:
		p = Image.open(img)
	except:
		total_broken += 1
		print(img)

if total_broken == 0:
	print("Could open all images")
else:
	print('Total broken imgs ', total_broken)
