

from byuimage import Image
import sys


def validate_commands(command_list):
   
   operation = command_list[1]

   if operation == '-k' and len(command_list) >= 4:  #changed -d to -k and 2 to 3
         percent = float(command_list[4])
         filename = command_list[2]
         darken(filename, percent)
      
   if operation == '-d' and len(command_list) >= 2:
      filename = command_list[2]
      displayimage(filename)

   if operation == '-s' and len(command_list) >=2:
      filename = command_list[2]
      sepia(filename)
      
   if operation == '-g' and len(command_list) >=2:
      filename = command_list[2]
      grayscale(filename)

#def make_borders(filename, thickness, red, green, blue):


   if operation == '-b' and len(command_list) >=6:
      filename = command_list[2]
      make_borders(filename, command_list[4], command_list[5], command_list[6], command_list[7])

   if operation == '-f' and len(command_list) >=2:
      filename = command_list[2]
      flipped(filename)

   if operation == '-m' and len(command_list) >=2:
      filename = command_list[2]
      output = command_list[3]
      mirror(filename, output)

   if operation == '-c' and len(command_list) >=7:
      collage(command_list[2], command_list[3], command_list[4], command_list[5], command_list[6], command_list[7])

#def greenscreen(frontImage, backImage, outputfile, threshold, factor):

   if operation == '-y' and len(command_list) >=6:
      filename = command_list[2]
      greenscreen(filename, command_list[3], command_list[4], command_list[5], command_list[6])
   
   

      return False 




def collage(filename1, filename2, filename3, filename4, outputfile, thickness):
   image1 = Image(filename1)
   image2 = Image(filename2)
   image3 = Image(filename3)
   image4 = Image(filename4)
   thickness = int(thickness)
   c_image = Image.blank(2 * image1.width + 3 * thickness, 2 * image1.height + 3 * thickness)
   for pixel in c_image:
       pixel.red = 0 
       pixel.green = 0
       pixel.blue = 0 
   for y in range(image1.height):
       for x in range(image1.width):
         image1_pixel = image1.get_pixel(x,y)
         c_image_pixel = c_image.get_pixel(x + thickness, y + thickness)
         c_image_pixel.red = image1_pixel.red
         c_image_pixel.green = image1_pixel.green
         c_image_pixel.blue = image1_pixel.blue

         image2_pixel = image2.get_pixel(x,y)
         c_image_pixel = c_image.get_pixel(x + 2 * thickness + image1.width, y + thickness)
         c_image_pixel.red = image2_pixel.red
         c_image_pixel.green = image2_pixel.green
         c_image_pixel.blue = image2_pixel.blue

         image3_pixel = image3.get_pixel(x,y)
         c_image_pixel = c_image.get_pixel(x + thickness, y + 2 * thickness + image1.height)
         c_image_pixel.red = image3_pixel.red
         c_image_pixel.green = image3_pixel.green
         c_image_pixel.blue = image3_pixel.blue

         image4_pixel = image4.get_pixel(x,y)
         c_image_pixel = c_image.get_pixel(x + 2 * thickness + image1.width, y + 2 * thickness + image1.height)
         c_image_pixel.red = image4_pixel.red
         c_image_pixel.green = image4_pixel.green
         c_image_pixel.blue = image4_pixel.blue
   c_image.save(outputfile)


def greenscreen(frontImage, backImage, outputfile, threshold, factor):
   image = Image(frontImage)
   backImage = Image(backImage)
   threshold = int(threshold)
   factor = float(factor)
   
   for y in range(backImage.height):
         for x in range(backImage.width):
            pixel = image.get_pixel(x,y)
            pixelBack = backImage.get_pixel(x,y)
            avg = (pixel.red + pixel.green + pixel.blue)/3
            if pixel.green >= factor * avg and pixel.green > threshold:
               pixel.red = pixelBack.red
               pixel.green = pixelBack.green
               pixel.blue = pixelBack.blue
   return image.save(outputfile)



def displayimage(filename):
   image = Image(filename)
   image.show()


def mirror(filename, output):
   image = Image(filename)
   mirrored_image = Image.blank(image.width, image.height)
    
   for y in range(image.height):
      for x in range(image.width):
            pixel = image.get_pixel(image.width-x-1, y)
            mirrored_image_pixel = mirrored_image.get_pixel(x, y)
      
            mirrored_image_pixel.red = pixel.red
            mirrored_image_pixel.green = pixel.green
            mirrored_image_pixel.blue = pixel.blue

   mirrored_image.save(output)



def flipped(filename):
    image = Image(filename)
    flipped_image = Image.blank(image.width, image.height)

    for y in range(image.height):
        for x in range(image.width):
            pixel  = image.get_pixel(x,(image.height- 1-y))
            
            new_pixel  = flipped_image.get_pixel(x,y)

            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue
    flipped_image.save(sys.argv[3])





def darken(filename, percent):

   #open the input image 
   image = Image(filename)
   percent = float(percent)
   factor = 1 - percent #convert the percent to a factor for darkening 
   
   
   for pixel in image:
      pixel.red *= factor
      pixel.green *= factor
      pixel.blue *= factor

   image.save(sys.argv[3])

def sepia(filename):
   image = Image(filename)

   for pixel in image:
      true_red = min(255, 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue)
      true_green = min(255, 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue)
      true_blue = min(255, 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue)

      pixel.red = true_red
      pixel.blue = true_blue
      pixel.green = true_green
   image.save(sys.argv[3])
   



def grayscale(filename):
    
    image = Image(filename)
    for pixel in image:
         average = (pixel.red + pixel.green + pixel.blue) / 3
         pixel.red = average 
         pixel.blue = average
         pixel.green = average
    image.save(sys.argv[3]) 



def make_borders(filename, thickness, red, green, blue):
    image = Image(filename)
    width, height = image.width, image.height 
    thickness = int(thickness)
    new_width = width + (2 * thickness)
    new_height = height + (2 * thickness)

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
    image_border.save(sys.argv[3])





def main():
   args = sys.argv
   if validate_commands(args):
      print("valid")

      operation = args[1]
      input_file = args[2]
      output_file = args[3]
      percent = float(args[4])



      if operation == "-k":
         image123 = Image(args[2])
         image123.show()



if __name__ == "__main__":
   main()