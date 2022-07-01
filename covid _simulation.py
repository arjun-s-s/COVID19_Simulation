import numpy as np
import matplotlib.pyplot as plt
from regex import P


#what are the attributes for each person:
# [0] - X position - double
# [1] - Y position - double
# [2] - Z position - double
# [0] - does the person have Covid - bool
# [0] - if they have covid - probability they will spread it (0 otherwise) - double
# [0] - X position

N = 100 #No. of people in the simulation
People = np.zeros((N, 6))
print(People[0])
