from typing import List


def bestChange(coins:List[int], value:int)->List[int]:
    iterations:int = 0
    change:List[int] = []
    coins.sort(reverse=True) # Ordena as moedas em ordem decrescente

    if value % 2 != 0:
        value = value*100
    
    try:
        while value > 0:
            for i in range(len(coins)):
                if value >= coins[i]:
                    change.append(coins[i])
                    value -= coins[i]
                    break
                elif value < coins[len(coins)-1]:
                    raise ValueError   
            iterations += 1
        print(f"Number of iterations: {iterations}")
        return change
    except ValueError:
        print("No change available")

value:float = 2.89
print(f"The best change for {value} é {bestChange([1, 5, 10, 25, 100], value)}")

print(f"The best change for {bestChange([3, 6, 15, 50, 100], value)}")

print(f"The best change for {bestChange([5, 10, 20, 50, 100], value)}")
