from byuimage import Image 

def flipped(filename):
    image = Image(filename)
    flipped_image = Image.blank(image.width, image.height)

    for y in range(image.height):
        for x in range(image.width):
            pixel  = image.get_pixel(x,(image.height- 1-y))
            
            
            
            new_pixel  = flipped_image.get_pixel(x,y)


            new_pixel.green = pixel.green
            new_pixel.red = pixel.red
            new_pixel.blue = pixel.blue
    return flipped_image

def make_borders(filename, thickness, red, green, blue):
    image = Image(filename)
    width, height = image.width, image.height 
    new_width = width + 2 *thickness
    new_height = height + 2 *thickness 

    image_border = Image.blank(new_width, new_height)
    

    for y in range(image_border.height):
        for x in range(image_border.width):
            border_pixel = image_border.get_pixel(x, y) 
            image_border.get_pixel(x + thickness, y + thickness)

            border_pixel.red = red 
            border_pixel.green = green 
            border_pixel.blue = blue 

    for y in range(image.height):
        for x in range(image.width):
            pixel  = image.get_pixel(x,y)
            border_pixel = image_border.get_pixel(x + thickness, y + thickness) 

            border_pixel.green = pixel.green
            border_pixel.red = pixel.red
            border_pixel.blue = pixel.blue


    return image_border

if __name__ == "__main__":
    #image_path = "flamingo-float.png"
    thickness = 10 
    border_color = (255, 0, 0) #red (RGB)
    bordered_image = make_borders(thickness, *border_color)
    bordered_image.show()
    pass