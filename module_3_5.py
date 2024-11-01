def get_multiplied_digits(number): #n!=1*2*3*...*n
    str_number = str(number)
    first = int(str_number[0])
    if int(len(str(number))) != 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


#get_multiplied_digits(40203) -> 4*get_multiplied_digits(203) -> 4*2*get_multiplied_digits(3) -> 4*2*3
#get_multiplied_digits(40203)

result = get_multiplied_digits(40203)
print(result)
