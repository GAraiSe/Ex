list2 = [2,4,5,5,7,9]

def check(*nums):
    x = []
    for num in nums:
        if num in x:
            return False 
        else: 
            x.append(num)
    return True
print(check(*list2))