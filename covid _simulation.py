import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#This is the class version!!!!
#sadfasdsadaswdasd

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

            People[6][i] = np.random.random() * home_radius_multiplier

        
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
            
            for i in range(len(People[0])):

                random_angle = np.random.random() * 2 * np.pi

                People[0][i] = (People[7][i] + (np.random.random() * People[6][i] * np.cos(random_angle))) % 1
                People[1][i] = (People[8][i] + (np.random.random() * People[6][i] * np.sin(random_angle))) % 1

        else:

            for i in range(len(People[0])):

                random_angle1 = np.random.random() * 2 * np.pi
                random_angle2 = np.random.random() * 2 * np.pi

                People[0][i] = People[7][i] + (People[6][i] * np.cos(random_angle1) * np.sin(random_angle2))
                People[1][i] = People[8][i] + (People[6][i] * np.sin(random_angle1) * np.sin(random_angle2))
                People[2][i] = People[9][i] + (People[6][i] * np.cos(random_angle2))

                magnitude = np.linalg.norm([People[0][i], People[1][i], People[2][i]])

                People[0][i] = People[0][i] / magnitude
                People[1][i] = People[1][i] / magnitude
                People[2][i] = People[2][i] / magnitude

    else:

        if People[2][0] == 0:

            for i in range(len(People[0])):
                
                People[0][i] = np.random.rand()
                People[1][i] = np.random.rand()

        else:

            for i in range(len(People[0])):
                
                cube_point = 2 * (np.random.rand(3) - .5)
                
                People[0][i] = cube_point[0] / np.linalg.norm(cube_point)
                People[1][i] = cube_point[1] / np.linalg.norm(cube_point)
                People[2][i] = cube_point[2] / np.linalg.norm(cube_point)

    return People

def spreading(People):

    People_temp = People

    if People[2][0] == 0:

        for i in range(len(People[0])):

            for j in range(len(People[0])):

                vector = np.array([People[0][i], People[1][i]]) - np.array([People[0][j], People[1][j]])

                if np.linalg.norm(vector) < People[5][i] and np.random.binomial(1,People[4][i]) == 1:

                    People_temp[3][j] = True
                    People_temp[4][j] = People_temp[4][i]
    
    else:
        
        for i in range(len(People[0])):

            for j in range(len(People[0])):

                vector = np.array([People[0][i], People[1][i], People[2][i]]) - np.array([People[0][j], People[1][j], People[2][j]])

                if np.linalg.norm(vector) < People[5][i] and np.random.binomial(1,People[4][i]) == 1:

                    People_temp[3][j] = True
                    People_temp[4][j] = People_temp[4][i]
    
    return People_temp


def simulation(People, num_days, within_radius):

    infection_count = []

    for i in range(num_days):

        count = 0

        for i in range(len(People[3])):

            if People[3][i]:

                count += 1

        infection_count.append(count)

        People = movement(People, within_radius)
        People = spreading(People)
    
    return infection_count




X = array_create(60000,"square", 0.1)
X = initialisation(X, 0.1, 0.2, 0.05)
infection_count = simulation(X, 50, True)

plt.plot(infection_count)
plt.show()


'''
for i in range(365):
    X = movement(X, True)
'''
plt.plot(X[0], X[1], ',')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X[0], X[1], X[2])
plt.show()





