import random
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt
import numpy as np
from binomial import alg1

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
# flier_high = np.random.rand(10) * 100 + 100
# flier_low = np.random.rand(10) * -100
# data = np.concatenate((alg1(100, 20, 0.5, 1.024 , 0.9765625, 0.5, 95), range(95)))
data = alg1(100, 20, 0.5, 1.024 , 0.9765625, 0.5, 95)
# data = np.concatenate((alg1(100, 20, 0.5, 1.024 , 0.9765625, 0.5, 95), range(95), flier_high, flier_low))


red_square = dict(markerfacecolor='r', marker='s')
fig5, ax5 = plt.subplots()
ax5.set_title('Horizontal Boxes')
ax5.boxplot(data, vert=False, flierprops=red_square)
# fig5.show()

# Save the figure
fig5.savefig('fig1.png', bbox_inches='tight')