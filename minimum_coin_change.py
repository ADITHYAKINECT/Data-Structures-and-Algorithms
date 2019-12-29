coins = [9,5,6,1]
total = 16
min_of_coins= float("inf")

def __minimum_coins(coin_value,min_of_coins):
    if coin_value == 0:
        return 0
    else:
        for coin in coins:
            if coin_value >= coin:
                min_of_coins= min(min_of_coins, __minimum_coins(coin_value-coin,min_of_coins)+1)
        return min_of_coins

def minimum_coins(total):
    print(__minimum_coins(total,min_of_coins))


minimum_coins(total)