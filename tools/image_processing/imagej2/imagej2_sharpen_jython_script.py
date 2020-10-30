import sys

from ij import IJ

# Fiji Jython interpreter implements Python 2.5 which does not
# provide support for argparse.
error_log = sys.argv[-4]
input_file = sys.argv[-3]
tmp_output_path = sys.argv[-2]
output_datatype = sys.argv[-1]

# Open the input image file.
input_image_plus = IJ.openImage(input_file)

# Create a copy of the image.
input_image_plus_copy = input_image_plus.duplicate()
image_processor_copy = input_image_plus_copy.getProcessor()

# Run the command.
IJ.run(input_image_plus_copy, "Sharpen", "")
# Save the ImagePlus object as a new image.
IJ.saveAs(input_image_plus_copy, output_datatype, tmp_output_path)
