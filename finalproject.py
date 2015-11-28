print ("Please input Attacking number and defending number, in that order.")
def numdiceroll(x, y):
    import random
    sides = 6
    attacking = x
    defending = y
    if attacking >= 3 and defending >= 2:
        dicea = random.sample(range(1, sides + 1), 3)
        print (dicea)
        diced = random.sample(range(1, sides +1), 2)
        print (diced)
        if max(dicea) > max(diced) and min(dicea) > (diced):
            print ("Attacker Wins Both")
        if max(dicea) > max(diced) and min(dicea) < (diced):
            print ("Both Lose 1")
        if max(dicea) < max(diced) and min(dicea) > (diced):
            print ("Both Lose 1")
        if max(dicea) < max(diced) and min(dicea) < (diced):
            print ("Defender Wins Both")
            
