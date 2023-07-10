

def divby7(num_st):

    rem = 0
    for letter in num_st:
        num = rem*10+int(letter)
        rem = num%7
    return int(rem==0)

        


if __name__ == "__main__":

    num_st = input()
    #divby7(num_st)
    print("res : ", divby7(num_st))