def strategy(n):

    #Description
    #n :Number of iterations.It can be set according to user's choice while invoking the strategy() function

    """
    For each iteration the function will be invoked repeatedly until either of the player's score becomes 5.
    The function calculates the modulo with 2 of each iteration call value
    and returns the number to be compared against the other player's number.
    Considering the opponent chooses numbers between 1-9
    """
    #Please plug-in the below code in the actual function.

    import random
    magic_number = n % 2
    if (magic_number == 0):
        return random.randrange(1, 5)
    elif (magic_number == 1):
        return 2