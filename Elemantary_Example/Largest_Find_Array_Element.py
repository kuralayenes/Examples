my_array = [1,2,3,4,5,22,11,32,322,123321]

def largest_element():
    max1 = my_array[1]
    for i in range(len(my_array)):

        if my_array[i] > max1 :
            max1 = my_array[i]

    return max1

print("Largest in given array is ", largest_element())

