from array import *

arr = array('i', [2,6,8,9,3,8])

def list_opr():
    print("Special Note :- Array only contain eithera a integer or a float value")
    print("The number of operation in array")
    fun = ['append()', 'count()', 'extend()', 'index()', 'insert()', 'pop()', 'remove()','reverse()',]

    for i in range(0,8):
       print("[{}] = {}".format(i, fun[i]))
    
    operation = int(input("Enter Which No. Of Operation Your Want To Call (Note:-Select one function at a time) :"))
    if operation > 12:
        print("Please Select The Correct Number Of Operation")
    else:
        print("Your Select the {} Function".format(fun[operation]))

    if operation == 0:
        value = int(input("Write what you want to {}: ".format(fun[operation])))
        print("The old array is {}".format(arr))
        arr.append(value)
        print("After appending value your array will be {}".format(arr))
    
    elif operation == 1:
        print(arr)
        value = int(input("Enter which value you want to count in your array: "))
        print("{} is {} times in your array".format(value, arr.count(value)))
    
    elif operation == 2:
        list = []
        value = input("Enter The Values of list Your Want To Extend(Note:- Make Sure to enter ',' between two values): ")
        for i in value.split(","):
            list.append(int(i))
        arr.extend(list)
        print("After extending value {}".format(arr))
    
    elif operation == 3:
        print(arr)
        value = int(input("Enter the value to know the index number: "))
        print("The index number of {} is {}".format(value,arr.index(value)))
    
    elif operation == 4:
        index = int(input("Enter The Index Number: "))
        value = int(input("Enter Which Value You Want To Insert:"))
        arr.insert(index, value)
        print( "After inserting the {} value, your array becomes = ".format(value), arr )

    elif operation == 5:
        print(arr)
        index = int(input("Enter the index number of which value you want to pop up: "))
        arr.pop(index)
        print("{} is pop up from your {}".format(arr[index], arr))

    elif operation == 6:
        print(arr)
        value = int(input("Select the value to romove from array: "))
        arr.remove(value)
        print("{} is remove from {}".format(value, arr))

    elif operation == 7:
        print(arr)
        arr.reverse()
        print("After reverse operatio {}".format(arr))

true_value = "YES"
while true_value == "YES":

    list_opr()
    value = input("If You still want to make changes in your array type 'Yes' else any key to exit: ")
    true_value = value.upper()

print("Your Exit The Operation Room")
