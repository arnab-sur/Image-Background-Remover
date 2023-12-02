#Background remover program

from rembg import remove
from PIL import Image

#Enter image path
input_image = "hi.jpeg"
result_image = "Enter_output_image_name.png"

Input = Image.open(input_image)
Output = remove(Input)

#Save the image
Output.save(result_image)