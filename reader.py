import numpy as np
import matplotlib.pyplot as plt
import cv2


image = cv2.imread('license_plate_skew.jpg')
image = cv2.resize(image,(512,341))
# Convert to RGB (from BGR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# ---------------------------------------------------------- #

## TODO: Define the geometric tranform function
## This function take in an image and returns a 
## geometrically transformed image
def geo_tx(image):
    image_size = (image.shape[1], image.shape[0])
    
    ## TODO: Define the four source coordinates
    source_pts = np.float32(
        [[35, 119],
          [340, 146],
         [33, 253],
         [385, 324]
        
         ])
    
    ## TODO: Define the four destination coordinates    
    ## Tip: These points should define a 400x200px rectangle
    warped_pts = np.float32([[0,0],[image.shape[1],0],[0,image.shape[0]],[image.shape[1],image.shape[0]]])
    
    ## TODO: Compute the perspective transform, M
    M = cv2.getPerspectiveTransform(source_pts,warped_pts)
    
    ## TODO: Using M, create a warped image named `warped`
    warped =  cv2.warpPerspective(image,M,(image.shape[1], image.shape[0]))

    return warped
    
    
# ---------------------------------------------------------- #
# Make a copy of the original image and warp it
warped_image = np.copy(image)
warped_image = geo_tx(warped_image)

if(warped_image is not None):
    # Visualize
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
    ax1.set_title('Source image')
    ax1.imshow(image)
    ax2.set_title('Warped image')
    ax2.imshow(warped_image)
else:
    print('No warped image was returned by your function.')
