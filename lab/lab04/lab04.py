from byuimage import Image

cougar_image = Image("test_files/cougar.png")
#                      ^ path to `cougar.png` file
for pixel in cougar_image:
    pixel.green = 0
    pixel.red = 0
cougar_image.show()

def iron_puzzle(filename):
    """takes in an image, retunrs same image but with altered pixel values 
    
    function multiplies Blues values by 10 
    function sets Red and Green values to 0"""

    image = Image(filename)
    for pixel in image:
        pixel.green = 0
        pixel.red = 0
        pixel.blue *= 10
    return image




def west_puzzle(filename):
    """Write your code here"""
    image = Image(filename)
    width, height = image.size

    #for x in range(width):
        #for y in range(height):
            #pixel = image.getpixel((x, y))
            #red, green, blue = pixel[0], pixel[1], pixel[2]

    for pixel in image:
        pixel.green = 0 
        pixel.red = 0     
        if blue < 16:
            blue *= 16
        else:
            blue = 0



    return image 
solution_image = iron_puzzle("test_files/west.png")
solution_image.show()

def darken(filename, percent):
    # Open the image using Pillow
    image = Image.open(filename)
    
    # Convert the percent to a factor for darkening
    factor = 1 - percent
    
    # Apply the darkening effect to each pixel
    pixels = image.load()
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (int(r * factor), int(g * factor), int(b * factor))
    
    # Return the modified image
    return image



def grayscale(filename):
    
    image = Image.open(filename)
    width, height = image.size
    grayscale_image = Image.new("L", (width, height))
    
   
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            gray_value = int((pixel[0] + pixel[1] + pixel[2]) / 3)
            grayscale_image.putpixel((x, y), gray_value)
    
    
if __name__ == "__main__":
    gray = grayscale("myImage.jpeg")
    gray.show()

    



def sepia(filename):
    def apply_sepia(pixel):
        true_red = min(255, 0.393 * pixel[0] + 0.769 * pixel[1] + 0.189 * pixel[2])
        true_green = min(255, 0.349 * pixel[0] + 0.686 * pixel[1] + 0.168 * pixel[2])
        true_blue = min(255, 0.272 * pixel[0] + 0.534 * pixel[1] + 0.131 * pixel[2])
        return (int(true_red), int(true_green), int(true_blue))

    image = Image(filename)  
    image = image.convert("RGB")
    sepia_image = Image.new("RGB", image.size)
    

    for x in range(image.width):
        for y in range(image.height):    
            pixel = image.getpixel((x, y))
            new_pixel = apply_sepia(pixel)
            sepia_image.putpixel((x, y), new_pixel)



def create_left_border(filename, weight):
    """Write your code here"""


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    """Write your code here"""


def copper_puzzle(filename):
    """Write your code here"""
