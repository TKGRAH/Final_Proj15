print ("Please input sim(A, D, Number of Rolls) Attacking number and defending number, in that order.")
from random import randint
def sim(x, y, rolls):
    attacking = x - 1
    defending = y - 1
    attackerloss = 0
    defenderloss = 0
    for roll in range(rolls):
        attRolls = []
        for die in range(attacking):
            attRolls.append(randint(1, 6))
        defRolls = []
        for die in range(defending):
            defRolls.append(randint(1, 6))

            if max(attRolls) > max(defRolls) and min(attRolls) > min(defRolls):
                print ("Attacker Wins Both")
                defenderloss += 2
            if max(attRolls) > max(defRolls) and min(attRolls) <= min(defRolls):
                print ("Both Lose 1")
                attackerloss += 1
                defenderloss += 1
            if max(attRolls) <= max(defRolls) and min(attRolls) > min(defRolls):
                print ("Both Lose 1")
                attackerloss += 1
                defenderloss += 1
            if max(attRolls) <= max(defRolls) and min(attRolls) <= min(defRolls):
                print ("Defender Wins Both")
                attackerloss += 2

    print ("Attacker Lost:", attackerloss)
    print ("Defender Lost:", defenderloss)
