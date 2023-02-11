import random

decksize = 0
millamount = 0
iterations = []
dataset = []
dataset2 = []


def repeat_fun(times, f, args):
    for i in range(times):
        f(args)
    average = sum(dataset) / len(dataset)
    print(average)
    dataset2.append(average)
    dataset.clear()



def mirrormad(x):
    x = x + 1
    decksize = x
    millamount = random.randint(1, x)
    x = x - millamount
    decksize = decksize - millamount
    iterations.append(1)
    #print("you milled " + str(millamount) + (" cards"))
    #print("decksize is now " + str(decksize))

    if decksize > 0:
        mirrormad(decksize)
    else:
        dataset.append(len(iterations))
        #print(len(iterations))
        #print(dataset)
        iterations.clear()


for a in range(99):
    repeat_fun(50000, mirrormad, a)

print(dataset2)


