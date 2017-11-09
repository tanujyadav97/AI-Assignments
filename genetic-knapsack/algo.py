from random import *

p = [6, 5, 8, 9, 6, 7, 3, 7, 4, 2, 5, 8, 3, 1, 5, 2, 8]  # profit array
w = [2, 3, 6, 7, 5, 9, 4, 5, 2, 3, 4, 1, 7, 8, 4, 5, 3]  # weight array
mw = 29                                                  # capacity of knapsack
n = 17                                                   # number of items
pm = 0.3                                                 # probability of mutation
pc = .8                                                  # probability of crossover
pool_size = 500                                          # pool size
stopc = 5000                                              # stop the evolution if maximum doesnt change for 'stopc' evolutions

pool = []
c1 = []                                                  # first child
c2 = []                                                  # second child

sumw = 0                                                 # sum of weights
maxc = -10000                                            # maximum profit
maxci = []                                               # maximum profit combination

for i in range(0, n):
    sumw += w[i]


def crossover(a, b):
    l = randint(1, n)
    global c1, c2
    c1 = []
    c2 = []
    for i in range(0, l):
        c1.append(a[i])
        c2.append(b[i])
    for i in range(l, n):
        c2.append(a[i])
        c1.append(b[i])


def mutation(a):
    l = randint(1, n)
    a[l - 1] ^= 1
    return a


def fitness(a):                                                      # function to calculate fitness of a genome
    f = 0
    sumxw = 0
    for i in range(0, n):
        f += a[i] * p[i]
    for i in range(0, n):
        sumxw += a[i] * w[i]

    penalty = sumw * abs(sumxw - mw)
    return f - penalty


def get_genome():
    genome = []
    for i in range(0, n):
        genome.append(randint(1, 100) & 1)

    return genome


def get_pool():
    global pool
    for i in range(0, pool_size):
        pool.append(get_genome())


def kill_weakest():                                                 # kills the 2 weakest genomes, to maintain the size of the pool
    global pool, maxc, maxci
    min1 = 0
    min2 = 0
    min1i = 0
    min2i = 0
    a = fitness(pool[0])
    b = fitness(pool[1])
    if a < b:
        min1 = a
        min1i = 0
        min2 = b
        min2i = 1
    else:
        min1 = b
        min1i = 1
        min2 = a
        min2i = 0
    for i in range(2, n):
        a = fitness(pool[i])
        if (a <= min1):
            min2 = min1
            min2i = min1i
            min1 = a
            min1i = i
        elif (a <= min2):
            min2 = a
            min2i = i

    pool[min1i] = pool[len(pool) - 1]
    pool[min2i] = pool[len(pool) - 2]


def fittest():
    global maxc, maxci
    for i in range(0, len(pool) - 2):
        a = fitness(pool[i])
        if a > maxc:
            maxc = a
            maxci = pool[i]*1


def evolve():
    global pool
    get_pool()
    pool.append(get_genome())
    pool.append(get_genome())
    fittest()
    c = 0

    while (c < stopc):

        if (randint(1, 10) <= pc * 10):
            a = randint(0, len(pool) - 1)
            b = randint(0, len(pool) - 1)
            while (b == a):
                b = randint(0, len(pool) - 1)
            crossover(pool[a], pool[b])
            pool[len(pool) - 2] = c1
            pool[len(pool) - 1] = c2

            kill_weakest()

        if (randint(1, 10) <= pm * 10):
            a = randint(0, len(pool) - 1)
            pool[i] = mutation(pool[i])

        maxo = maxc
        fittest()
        if (maxo == maxc):
            c += 1
        else:
            c = 0


evolve()
print(maxci)
print('maximum possible profit is: '+str(maxc))
