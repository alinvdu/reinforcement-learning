def printValues(values, g):
    # values are a dictionary of tuples with the value being the probability
    # g is the gridWorld
    for i in range(g.rows):
        print("-------------------------")
        for j in range(g.cols):
            v = values.get((i, j), 0)
            if v >= 0:
                print(" %.2f|" % v, end="")
            else:
                print("%.2f|" % v, end="")
        print("")
    

def printPolicy(policy, g):
    for i in range(g.rows):
        print("-------------------------")
        for j in range(g.cols):
            p = policy.get((i, j), ' ')
            print(" %s |" % p, end="")
        print("")
