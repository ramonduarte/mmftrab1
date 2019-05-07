import random
import matplotlib.pyplot as plt
import numpy as np
import itertools


def alg1(s0, T, dt, u, d, p, reps=1):
    # markers = [".", "o", "v", "^", "<", ">", "s", "P", "*", "+", "D", "d", "--"]
    markers = [".-", "--", "d-", "o-", "*-", "+-", "P-", "s-", "D-", "v-", "<-", "v-", "-", ">-"]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', "lime", "fuchsia", "gold", "teal", "navy"]
    available_markers = list(itertools.product(markers, colors))
    random.shuffle(available_markers)
    final_values = []
    for i in range(reps):
        x = np.arange(0, T + dt, dt)   # time
        y = [s0]  # stock price
        s = s0
        t = 0
        # print("rep #", i+1)
        while t < T:
            t += dt
            if random.random() < p:
                s *= u
            else:
                s *= d
            y.append(s)
            # print("S({}) = {}".format(t, s))
        # m = str(random.choice(colors) + random.choice(markers))
        # while m in used_markers:
        #     m = str(random.choice(colors) + random.choice(markers))
        # used_markers.append(used_markers)
        plt.plot(x, y, "".join(available_markers.pop()), label="stock " + str(i+1))
        final_values.append(y.pop())
    plt.ylabel("Stock Price (S), in dollars")
    plt.xlabel("Time elapsed (t), in days")
    plt.legend(bbox_to_anchor=(1., 1), loc=2, borderaxespad=0.)
    plt.show()

    return final_values



if __name__ == "__main__":
    alg1(100, 20, 0.5, 1.024 , 0.9765625, 0.5, 20)
