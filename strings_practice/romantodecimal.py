


class RomToDecimal :
    
    def __init__(self):
        pass
    def conv(self, letter:str):
            if letter == 'I':
                return 1
            elif letter == 'V':
                return 5
            elif letter == 'X':
                return 10
            elif letter == 'L':
                return 50
            elif letter == 'C':
                return 100
            elif letter == 'D':
                return 500
            elif letter == 'M':
                return 1000
            

    def rom_to_dec(self, rom_str:str):

        prev = 10000
        curr = 0
        tot = 0

        for letter in rom_str:
            curr = self.conv(letter)
            tot += curr
            if prev < curr:
                tot -= 2*prev
            
            prev = curr
        return tot


    def rom_to_dec2(self, rom_str:str):
        tot = 0
        for i in range(len(rom_str)):
            if i==0:
                tot = tot + self.conv(rom_str[i])
            else:
                if self.conv(rom_str[i-1]) < self.conv(rom_str[i]):
                    tot = tot +self.conv(rom_str[i]) -2*self.conv(rom_str[i-1])
                else:
                    tot += self.conv(rom_str[i])
        return tot
    
    def rom_to_dec3(self, rom_str:str):

        tot = 0
        i = 0
        while i < len(rom_str):
            if i == len(rom_str)-1:
                tot += self.conv(rom_str[i])
                break
            if self.conv(rom_str[i]) < self.conv(rom_str[i+1]):
                tot += (self.conv(rom_str[i+1]) - self.conv(rom_str[i]))
                i+=1
            else :
                tot += self.conv(rom_str[i])
            i+=1
        return tot




            
if __name__ == "__main__":

    rom = input()
    rtod = RomToDecimal()
    print(rom, " : ", rtod.rom_to_dec(rom))
    print(rom, " : ", rtod.rom_to_dec2(rom))
    print(rom, " : ", rtod.rom_to_dec3(rom))


               



