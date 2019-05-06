import random



def alg1(s0, T, dt, u, d, p, reps=1):
    for i in range(reps):
        s = s0
        t = 0
        print("rep #", i+1)
        while t < T:
            t += dt
            if random.random() < p:
                s *= u
            else:
                s *= d
            print("S({}) = {}".format(t, s))


if __name__ == "__main__":
    alg1(100, 20, 0.5, 2, 0.5, 0.5, 20)
5