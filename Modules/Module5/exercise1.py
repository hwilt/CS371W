def get_change_coins(optimal, chosen_coins, amt, all_ways):
    """
    Recursively backtrace through optimal coin choices to see
    all of the ways of making changes
    Parameters
    ----------
    optimal: list of list
        A list of optimal coin choices, indexed by amount
    chosen_coins: list
        All of the coins considered so far
    amt: int
        The current amount that's being turned into change
    all_ways: set
        A set of strings describing all unique ways to make change.
        Returned by reference
    """
    if len(optimal[amt]) == 0:
        # Stopping condition: No more coins left to look at
        # Make a dictionary of amount:count for all chosen coins
        counts = {amt:1} # We know that this amount is one of the coins
        for coin in chosen_coins:
            if not coin in counts:
                counts[coin] = 0
            counts[coin] += 1
        # Format this nicely in a string sorted in increasing
        # order of coin value
        way = ""
        for i, coin in enumerate(sorted(counts.keys())):
            way += "{}x{}".format(coin, counts[coin])
            if i < len(counts)-1:
                way += ","
        all_ways.add(way)
    else:
        for c in optimal[amt]:
            ## TODO: Fill this in
            ## 1. Put this coin on the back of the list of chosen coins
            ## 2. Make a recursive call 
            ## 3. Pop this coin off of the back of the list of chosen coins
            chosen_coins.append(c)
            get_change_coins(optimal, chosen_coins, amt-c, all_ways)
            chosen_coins.pop()

def min_coins_needed_dyn(coins, amt):
    """
    Parameters
    ----------
    coins: list
        List of all possible coin values (including 1 cent)
    amt: int
        The change I'm trying to make
    
    Returns
    -------
    int: The minimum number of coins needed to make change,
    set: A set describing all of the ways to make that change
    """
    mem = [0]*(amt+1) # Ex) mem[10] is minimum # needed to make 10c
    optimal = [[] for i in range(amt+1)]
    for amti in range(1, amt+1):
        if amti in coins:
            mem[amti] = 1
        else:
            min_coins = amti
            for c in coins:
                sm_amt = amti - c
                if sm_amt > 0:
                    min_c = 1 + mem[sm_amt]
                    min_coins = min(min_coins, min_c)
            for c in coins:
                sm_amt = amti - c
                if sm_amt > 0:
                    min_c = 1 + mem[sm_amt]
                    if min_c == min_coins:
                        optimal[amti].append(c)
            mem[amti] = min_coins
    chosen_coins = []
    all_ways = set([])
    get_change_coins(optimal, chosen_coins, amt, all_ways)
    return mem[-1], all_ways

coins = [1, 3, 5, 10, 25]
for amt in [6, 41, 94]:
    cost, ways = min_coins_needed_dyn(coins, amt)
    print("{}:{}".format(amt, ways), end='.')