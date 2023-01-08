import numpy as np

prefix_file = "./images/car_"
suffix_file = ".npy"
images = []
for i in range(9):
    image = np.load(prefix_file+str(i)+suffix_file)
    images.append(image)


images= np.stack(images)

images.shape

np.sum(images)

np.sum(images,axis=(1,2))

np.argmax(np.sum(images,axis=(1,2)))

mean_image = np.mean(images,axis=0)

mean_image.shape