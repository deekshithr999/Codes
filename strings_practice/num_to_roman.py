class Conv2(object):

    def __init__(self):
        self.numtorommap = {1:'I', 4:'IV', 5: 'V', 9: 'IX',
                        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
                        1000: 'M'}
        
        self.num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
    def numtorom(self,num):

        tnum = num
        rom_str = ""

        # while tnum!=0:
        #     for n in self.num:
        #         if tnum//n != 0:
        #             rom_str += self.numtorommap[n]*(tnum//n)
        #             tnum %= n

        for n in self.num:
            if tnum == 0:
                break

            if tnum//n !=0:
                rom_str += self.numtorommap[n]*(tnum//n)
                tnum%=n
        return rom_str





class Conv (object):

    def __init__(self):
        pass

    def get_roman(self, num):

        if num == 1:
            return 'I'
        elif num == 5:
            return 'V'
        elif num == 10:
            return 'X'
        elif num == 50:
            return 'L'
        elif num == 100:
            return 'C'
        elif num == 500:
            return 'D'
        elif num == 1000:
            return 'M'


    def conv_num_to_rom(self, num):

        tnum = num
        rom_str = ""
        while tnum != 0:
            if (tnum//1000 !=0):
                rom_str += self.get_roman(1000)*(tnum//1000)
                tnum =tnum%1000
            
            elif (tnum//900 != 0):
                rom_str += self.get_roman(100)
                rom_str += self.get_roman(1000)
                tnum = tnum%900
            
            elif (tnum//500 != 0):
                rom_str += self.get_roman(500)* (tnum//500)
                tnum = tnum%500
            
            elif (tnum//400!=0):
                rom_str += self.get_roman(100)
                rom_str += self.get_roman(500)
                tnum = tnum%400
            
            elif (tnum//100 != 0):
                rom_str += self.get_roman(100) * (tnum//100)
                tnum = tnum%100
            
            elif (tnum//90 != 0):
                rom_str += self.get_roman(10)
                rom_str += self.get_roman(100)
                tnum = tnum%90
            
            elif (tnum//50 != 0):
                rom_str += self.get_roman(50) * (tnum//50)
                tnum = tnum%50
            
            elif (tnum//40 != 0):
                rom_str += self.get_roman(10)
                rom_str += self.get_roman(50)
                tnum = tnum%40
            
            elif (tnum//10 != 0):
                rom_str += self.get_roman(10) * (tnum//10)
                tnum = tnum%10
            
            elif (tnum//9 != 0):
                rom_str += self.get_roman(1)
                rom_str += self.get_roman(10)
                tnum = tnum%9
            
            elif (tnum//5 != 0):
                rom_str += self.get_roman(5) * (tnum//5)
                tnum = tnum%5
            
            elif (tnum//4 != 0):
                rom_str += self.get_roman(1)
                rom_str += self.get_roman(5)
                tnum = tnum%4
            
            elif (tnum//1 != 0):
                rom_str += self.get_roman(1)*(tnum)
                tnum = tnum%1
        return rom_str


if __name__ == "__main__":

    conv = Conv()
    conv2 = Conv2()
    num = int(input("Enter num : "))
    print(num," : ",conv.conv_num_to_rom(num))
    print (num, " : ", conv2.numtorom(num))