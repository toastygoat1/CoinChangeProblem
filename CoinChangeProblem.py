def coinChange(x, arr):

    arr.sort(reverse=True)    

    result = []
    
    for coin in arr:
        while x >= coin:
            x -= coin
            result.append(coin)
    
    return result

arr = [10, 5, 2, 1]
x = int(input("Masukkan jumlah uang: "))
coins_used = coinChange(x, arr)  
print(f"Koin yang digunakan: {coins_used}")
print(f"Jumlah koin yang dibutuhkan: {len(coins_used)}")
