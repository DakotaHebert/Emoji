#!/usr/bin/env python3
from predict import *
import glob

correct = 0
total = 0
for pic in glob.glob(sys.argv[1] + "*"):
	print('Result ' + main(pic))
	if main(pic) == str(sys.argv[1].strip("/")):
		correct += 1
	total += 1
	print('Correct ', correct)
	print('Total ', total)
	print('')
print(correct/total)
