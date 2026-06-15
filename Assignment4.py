#Q5

def evenNumbers(array):
    for number in array:
        if number % 2 == 0:
            print(number)

myArray = [3, 8, 12, 5, 7, 14]
evenNumbers(myArray)

print('---------------------------')


#Q6

def linearSearch(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return index
        
    return -1
        
test_array = [12, 4, 40, 20, 78]
print(linearSearch(test_array, 20))
print(linearSearch(test_array, 78))

