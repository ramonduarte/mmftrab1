import random
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt
import numpy as np
from binomial import alg2, alg3
from math import sqrt

from sys import argv
reps = int(argv[1])
assert type(reps) == int

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
# flier_high = np.random.rand(10) * 100 + 100
# flier_low = np.random.rand(10) * -100
# data = np.concatenate((alg1(100, 20, 0.5, 1.024 , 0.9765625, 0.5, 95), range(95)))
data = [
    alg2(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps),
    alg2(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps*2),
    alg2(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps*4),
    alg2(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps*8),
]
# data = np.concatenate((alg1(100, 20, 0.5, 1.024 , 0.9765625, 0.5, 95), range(95), flier_high, flier_low))


red_square = dict(markerfacecolor='r', marker='s')
fig5, ax5 = plt.subplots()
ax5.set_title('Stock Price Distribution (prices in dollars)')
ax5.boxplot(data, vert=False, flierprops=red_square)
ax5.set_yticklabels([reps, reps*2, reps*4, reps*8])
# fig5.show()

# Save the figure
fig5.savefig('fig5_' + str(reps) + '.png', bbox_inches='tight')
