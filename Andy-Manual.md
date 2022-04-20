# Dense Captioning Front-End Manual

### Introduction

The Front-End for Dense Captioning is meant to act as an easy to use user interface to run a machine learning algorithm on images submitted by the user. This algorithm can take an inputed image and return a large JSON file of data that contains the analysis of the algorithm. 

This output contains:

- The image name
- The captions for each image. This is what the algorithm has identified in the image
- The "score" for each caption. This is the confidence the algorithm has assigned to that specific caption
- The bounding box coordinates for each caption. This defines where in the original image the caption is refering to

The front-end is meant to be an easy to use user interface to abstract away all the intricate processess associated with running this algorithm, whilst also providing a more digestible format for the results of the algorithm.

### How does it work?

The Front-End is based on a React.js framework and Material UI is used for the styling of components. The front end allows for the user to submit an image file, which then is sent to an Azure cloud storage and retrived by the algorithm in the backend. The algorithm runs and uploads the output of the algorithm into the back-end database where all the information will be stored. The data is then retrived by the front-end from the database and displays 4 captions from the image that have the highest scores. Each caption will be displayed along with its score, and the coordinates of the bounding box. 

The information on how the backend and the algorithm works can be found on their own manual pages.

### Setup

- Download Docker and follow the setup guide found in the UMass-Rescue/596-S22-Backend repository ReadMe file
- Download/install node, and install yarn through node
- In the dense_frontend subdirectory of the aforementioned repository, run "yarn start" in the terminal
- The web app will display on localhost:3000

## What is Implemented vs "In-Production"

### Currently Implemented

- Image submission to front-end
- Image submission to azure and obtaining image from azure to do analysis (seperate from front-end)
- Front-End obtaining results from database
- Results tab that displays all the output information
- back-end route for obtaining results for an inputed image name

### In-Production

- Linking the front-end to the azure functionality
- Containerizing algorithm so that everything works within the same directory
- Adding a search image function so the user can type in any image name of any image stored in the database
    and the results will be displayed.

## Future Plans

A potentail feature that can be implemented would be to display the given image, but cropped at the bounding boxes for each caption. This would be more user friendly and easier to use instead of just having the bounding box coordinates displayed for each caption. Another potential feature to add is dynamically adding and subtracting the number of captions displayed per the user's preference. Currently it only displays 4 captions and if one wanted more or less they would have to add them or subtract them manually.
