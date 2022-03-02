my_list = [1, 3, 5, 7, 9, 12, 34 ,55, 678, 12345]

def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None 
    
print(binary_search(my_list, 3))

names = ['mark', 'john', 'fred', 'simon', 'lisa', 'bart']
names.sort()
print(binary_search(names, 'fred'))
        