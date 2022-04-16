##################################

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))    # answer    <class 'numpy.ndarray'>

##################################

# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_inprint(height_in)
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254      # se multiplica cada valor del array

# Print np_height_m
print(np_height_m)
