list1 = [1,5,7,9]

def check(*nums):
    for num in nums:
        if num < 2:
            return False   
        for i in range(2,int(num**0.5)+1):
            if num %1 == 0:
                return False
        else:
            return True

print(check(*list1))
