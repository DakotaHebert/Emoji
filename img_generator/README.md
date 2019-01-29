Generate Photos From a Sample
===============================

You can use this to create however many photos you want
from a directory of input images. It crops, rotates, and flips the image
randomly. This is so we do not have to manually download all of
the images that will be used for training. However, we still 
need to collect a few highly disparate images that will belong
to the same class, and use them as base images for generation.

To run this:

	./img_gen.py N input_directory/ output_directory/ 

(N is how many images you want to create) 
