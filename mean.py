import random
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt
import numpy as np
from binomial import alg3
from math import sqrt

from sys import argv
reps = int(argv[1])
assert type(reps) == int

data = [
    alg3(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps),
    alg3(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps*2),
    alg3(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps*4),
    alg3(100, 20, 0.25, sqrt(1.024) , sqrt(0.9765625), 0.5, reps*8),
]


fig5, ax5 = plt.subplots()
ax5.set_title('Mean Squared Deviation')
# ax5.scatter(x=data[0], y=[[reps], [reps*2], [reps*4], [reps*8]])
ax5.plot([data[0]], reps, 'g.-', [data[1]], reps*2, 'g.-', [data[2]], reps*4, 'g.-', [data[3]], reps*8, 'g.-')
# ax5.plot(x=data[2], y=reps*4)
# ax5.plot(x=data[3], y=reps*8)
# ax5.set_yticklabels([reps, reps*2, reps*4, reps*8])
# fig5.show()

# Save the figure
fig5.savefig('fig7_' + str(reps) + '.png', bbox_inches='tight')
