import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#what are the attributes for each person:
# [0] - X position - double
# [1] - Y position - double
# [2] - Z position - double
# [3] - does the person have Covid - bool
# [4] - if they have covid - probability they will spread it (0 otherwise) - double
# [5] - infection radius (how far does someone have to be to get covid?)
# [6] - home radius - the radius of their home
# [7] - home point X position - centre of their home
# [8] - home point Y position - centre of their home
# [9] - home point Z position - centre of their home


def array_create(N, domain_shape, home_radius_multiplier): # creates an array for N people, with randomised points on a square or sphere
    
    People = np.zeros((10, N))

    if domain_shape == "square":

        for i in range(N):

            People[0][i] = np.random.rand()
            People[7][i] = People[0][i]

            People[1][i] = np.random.rand()
            People[8][i] = People[1][i]

            People[3][i] = False

            People[6][i] = np.random.random() * home_radius_multiplier
        
        return People
        
    elif domain_shape == "sphere": #not quite a uniform distrubtion - corners of cube have higher density, but should suffice for usecase

        for i in range(N):

            cube_point = 2 * (np.random.rand(3) - .5)

            People[0][i] = cube_point[0] / np.linalg.norm(cube_point)
            People[7][i] = People[0][i]

            People[1][i] = cube_point[1] / np.linalg.norm(cube_point)
            People[8][i] = People[1][i]

            People[2][i] = cube_point[2] / np.linalg.norm(cube_point)
            People[9][i] = People[2][i]

            People[3][i] = False

            People[6][i] = np.random.random() * 0.1

        
        return People

def initialisation(People, percentage_infected, mean_covid_probability, infection_radius_multiplier): #to initialise the People - infecting a random percentage of the population


    num_infected = int(np.round(len(People[0]) * percentage_infected))

    for i in range(num_infected):

        People[3][i] = True #fine since order of people doesn't matter
        People[4][i] = mean_covid_probability * np.random.random()
        People[5][i] = np.random.random() * infection_radius_multiplier
    
    return People

def movement(People, within_radius): #to shuffle the points, either completely randomly or within a radius

    if within_radius:
        
        if People[2][0] == 0:
            
            print()
            #code for shuffling points in square within radius

        else:

            print()
            #code for shuffling points in circle within radius

    else:

        if People[2][0] == 0:
            
            print()
            #code for shuffling within square, completely randomly

        else:

            print()
            #code for shuffling within sphere, completely randomly

    return People








X = array_create(600,"sphere", 0.1)
X = initialisation(X, 0.1, 0.2, 0.05)


count = 0

for i in range(len(X[0])):
    if X[3][i]:
        count += 1
print(count)



plt.plot(X[0], X[1], ',')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X[0], X[1], X[2])
plt.show()





