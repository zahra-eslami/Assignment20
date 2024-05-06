def is_symmetric(array):
    length = len(array)
    mid = length // 2
    if length % 2 == 1:  # if array's len is odd
        for i in range(mid):
            if array[i] != array[length - i - 1]:
                return False
    else:  # if array's len is even
        for i in range(mid):
            if array[i] != array[length - i - 1]:
                return False
    return True

odd_arr = [1, 4, 3, 4, 1]
even_arr=[1,2,3,4,4,3,2,1]

if is_symmetric(even_arr):
    print("this array is symmetric.")
else:
    print("this array isn't symmetric.")
