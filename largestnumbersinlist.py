def largestnumber(numbers):

    biggest_num=numbers[0]

    for num in numbers:
        if num>biggest_num:
            biggest_num=num


    return biggest_num

print(largestnumber([1,23,3334,456,7777]))