# you have 1 cent, 3 cent, 4 cent, 7 cent, and 10 cent coins
# objective to find the minimum amount of coins to find a certain cents

def make_change(coins, value, mem = {}):
    """
    Ex) make_change([1,3,4,7,10], 32)

    Parameters
    ----------
    coins: list of int
        The coins I have available to me
    value: int
        The value I'm trying to make

    Return
    ------
    *First Version: Return min # of coins
        return 5

    *Later Version: Return coins and how many times they're used
        return [{10,3, 1:2}, {7:4,4:1}, {4:3, 10:2}, {10:2, 7:1, 4:1, 1:1}]
    """
    minCoins = value
    for c in coins:
        if not value-c in mem:
            sol = 1 + make_change(coins, value-c, mem)
            mem[value-c] = sol
        sol = mem[value-c]
        if sol < minCoins:
            minCoins = sol
    return minCoins

def main():
    coins = [1,3,4,7,10]
    amount = 32
    print(make_change(coins, amount))

if __name__ == "__main__":
    main()
