import random
from random import randint

def get_rolls(rolls):
    """DOCSTRING HERE.

    >>> random.seed(0)
    >>> get_rolls(1)
    [6]
    >>> get_rolls(3)
    [5, 3, 2]
    
    """
    results = []
    for die in range(rolls):
        results.append(randint(1, 6))
    return results

def do_battle_large():
    """DOCSTRING HERE.

    >>> random.seed(0)
    >>> do_battle_large()

    """
    attRolls = get_rolls(3)
    defRolls = get_rolls(2)

    if max(attRolls) > max(defRolls) and min(attRolls) > min(defRolls):
        return ("Attacker Wins Both")
        print ("Attacker Wins Both")
    if max(attRolls) > max(defRolls) and min(attRolls) <= min(defRolls):
        return ("Both Lose 1")
        print ("Both Lose 1")
    if max(attRolls) <= max(defRolls) and min(attRolls) > min(defRolls):
        return ("Both Lose 1")
        print ("Both Lose 1")
    if max(attRolls) <= max(defRolls) and min(attRolls) <= min(defRolls):
        return ("Defender Wins Both")
        print ("Defender Wins Both")
        

def sim(Attack_Number, Defense_Number):
    Attack_Units = Attack_Number
    Defense_Units = Defense_Number

    while Attack_Units != 0 and Defense_Units != 0:
        if do_battle_large() == "Attacker Wins Both":
            Defense_Units -= 2
        if do_battle_large() == "Both Lose 1":
            Attack_Units -= 1
            Defense_Units -= 1
        if do_battle_large() == "Defender Wins Both":
            Attack_Units -= 2

    if Attack_Units == 0:
        print ("Attacker Loses")
    if Defense_Units == 0:
        print ("Defender Loses")
    

    


### MAIN
if __name__ == '__main__':
    import doctest
    doctest.testmod()


##print ("Please input sim(A, D, Number of Rolls) Attacking number and defending number, in that order.")
