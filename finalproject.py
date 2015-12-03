import random
from random import randint
print("Type Run(Number Attacking, Number Defending)")
print("Must be 3 or less attackers and 2 or less defenders")


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

def do_battle(attackers, defenders):
    """DOCSTRING HERE.

    >>> random.seed(0)
    >>> do_battle()

    """

    if 0 <= attackers > 3 or 0 <= defenders > 2:
        return None
        print("Must be between 0 and 3 attackers. Must be between 0 and 2 defenders.")
    
    attRolls = get_rolls(attackers)
    defRolls = get_rolls(defenders)

    attRolls.sort(reverse=True)
    defRolls.sort(reverse=True)
    print (attRolls)
    print (defRolls)

    rollA = 0
    rollD = 0

    while rollA is not None and rollD is not None:
        try:
            rollA = attRolls.pop(0)
            rollD = defRolls.pop(0)
        except IndexError:
            return attackers, defenders        
        if rollA > rollD:
            attackers -= 1
            print ("Attack Loses 1")
        else:
            defenders -= 1
            print ("Defense Loses 1")
    return attackers, defenders

def roll_again():
    print "Input format is: 'Yes, 1:2' or 'Yes, 2:1' or 'No'"
    answer = raw_input("Attack Again? ")
    if answer == "Yes, 2:1":
        do_battle(2, 1)
    if answer == "Yes, 1:2":
        do_battle(1, 2)
    else:
        print "Battle Over"
            
    
def Risk():
    ## Risk_Map = {'Alaska' : raw_input("Player? "), 'Alberta' : raw_input("Player? "), 'Central America' : raw_input("Player? "), 'Eastern United States' : raw_input("Player? "), 'Greenland' : raw_input("Player? "), 'Northwest Territory' : raw_input("Player? "), 'Ontario' : raw_input("Player? "), 'Quebec' : raw_input("Player? "), 'Western United States' : raw_input("Player? "), 'Argentina' : raw_input("Player? "), 'Brazil' : raw_input("Player? "), 'Peru' : raw_input("Player? "), 'Venezuela' : raw_input("Player? "), 'Great Britain' : raw_input("Player? "), 'Iceland' : raw_input("Player? "), 'Northern Europe' : raw_input("Player? "), 'Scandinavia' : raw_input("Player? "), 'Southern Europe' : raw_input("Player? "), 'Ukraine' : raw_input("Player? "), 'Western Europe' : raw_input("Player? "), 'Congo' : raw_input("Player? "), 'East Africa' : raw_input("Player? "), 'Egypt' : raw_input("Player? "), 'Madagascar' : raw_input("Player? "), 'North Africa' : raw_input("Player? "), 'South Africa' : raw_input("Player? "), 'Afghanistan' : raw_input("Player? "), 'China' : raw_input("Player? "), 'India' : raw_input("Player? "), 'Irkutsk' : raw_input("Player? "), 'Japan' : raw_input("Player? "), 'Kamchatka' : raw_input("Player? "), 'Middle East' : raw_input("Player? "), 'Mongolia' : raw_input("Player? "), 'Siam' : raw_input("Player? "), 'Siberia' : raw_input("Player? "), 'Ural' : raw_input("Player? "), 'Yakutsk' : raw_input("Player? "), 'Eastern Australia' : raw_input("Player? "), 'Indonesia' : raw_input("Player? "), 'New Guinea' : raw_input("Player? "), 'Western Australia' : raw_input("Player? ")}

    print("Both Players start with 40 armies split among 14 provinces")
    print("Player 1 Starts.")

    no_count = 0
    
    valid_result1 = (0, 2)
    valid_result2 = (3, 0)
    
    Player1_Army = 40
    Player2_Army = 40

    while Player1_Army != 0 and Player2_Army != 0 and no_count < 5:
        player1_attack = raw_input("Does player 1 want to attack? ")
        if player1_attack == "Yes":
            player1_number_att = raw_input("How many attacking? ")
            player1_number_att = int(player1_number_att)
            player2_number_def = raw_input("How many defending? ")
            player2_number_def = int(player2_number_def)
            return do_battle(player1_number_att, player2_number_def)
        if player1_attack == "No":
            no_count += 1
        player2_attack = raw_input("Does player 2 want to attack? ")
        if player2_attack == "Yes":
            player2_number_att = raw_input("How many attacking? ")
            player2_number_att = int(player2_number_att)
            player1_number_def = raw_input("How many defending? ")
            player1_number_def = int(player1_number_def)
            return do_battle(player2_number_att, player1_number_def)
        if player2_attack == "No":
            no_count += 1
        if no_count > 5:
            print("No contest")
                
            
    


### MAIN
if __name__ == '__main__':
    import doctest
    doctest.testmod()

provinceA = 7
provinceB = 5
## print("Player A has {} armies, Player B has {} armies.".format(ProvinceA, ProvinceB))
## print("Its playerA's turn.")
## Repeat until someone wins or both players pass three times
    ## Repeat until armies depleted or player passes
        ## Ask if they want to attack.
        ## Ask how many to attack with.
        ## Do Battle
        ## Adjust Province Pop
        ## Ask to battle again 
## End Game


##print ("Please input sim(A, D, Number of Rolls) Attacking number and defending number, in that order.")
