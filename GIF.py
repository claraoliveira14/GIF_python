#Creating a GIF with Python!
import imageio.v3 as iio # A python library that provides an easy interface to read and write a wide range of image data.

filenames = ['GIFimagem1.jpeg', 'GIFimagem2.jpeg'] #list of files used for the GIF
images = [ ] #empty list used to store the actual image data

for filename in filenames:                  #using for to comb thru the data
    images.append(iio.imread(filename))     #using .imread (imageio function) to read the data

iio.imwrite('cat.gif', images, duration = 200, loop = 0) #using the function .imwrite to make the gif
                                                         #the duration is how long each image should appear (in milliseconds)