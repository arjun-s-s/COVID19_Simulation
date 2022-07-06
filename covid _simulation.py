import numpy as np
import matplotlib.pyplot as plt
from regex import P
import matplotlib

#what are the attributes for each person:
# [0] - X position - double
# [1] - Y position - double
# [2] - Z position - double
# [0] - does the person have Covid - bool
# [0] - if they have covid - probability they will spread it (0 otherwise) - double
# [0] - 

def array_create(N, domain_shape):
    
    People = np.zeros((N, 7))

    if domain_shape == "square":

        for i in range(N - 1):

            People[i][0] = np.random.rand()

            People[i][1] = np.random.rand()
        
        return People
        
    elif domain_shape == "sphere":

        for i in range(N):

            cube_point = 2 * (np.random.rand(3) - .5)

            People[i][0] = cube_point[0] / np.linalg.norm(cube_point)
            People[i][1] = cube_point[1] / np.linalg.norm(cube_point)
            People[i][2] = cube_point[2] / np.linalg.norm(cube_point)

        
        return People


'''
X = array_create(60,"sphere")

plt.plot(np.transpose(X)[0], np.transpose(X)[1], ',')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(np.transpose(X)[0], np.transpose(X)[1], np.transpose(X)[2])
plt.show()
'''




