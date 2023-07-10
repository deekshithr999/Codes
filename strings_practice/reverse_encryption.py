
class DecToHex(object):


    def __init__(self):
        pass

    def dec_to_bin(self,num):
        if num == 0:
            return "0"
        bin_str = ""
        rem = 0
        while num!=0:
            rem = num%2
            bin_str = str(rem)+bin_str
            num //= 2
        #print("bin_str ", bin_str)
        return bin_str
    
    def bin_to_hex(self,bin_num :str):
        hex_map = {10: 'a', 11: 'b', 12: 'c', 13:'d', 14:'e', 15:'f'}
        hex_str = ""
        tnum = bin_num
        if len(bin_num)%4 != 0:
            tnum = "0"*(4-len(bin_num)%4) + bin_num

        tval = 0
        mul = 1
        for i in range(len(tnum)-1,-1,-1):
            tval = tval + int(tnum[i])*mul
            mul = mul*2
            if i%4 == 0:
                if tval <10:
                    hex_str = str(tval)+hex_str
                else:
                    hex_str = hex_map[tval]+hex_str
                mul = 1
                tval = 0
        return hex_str
    
    def dec_to_hex(self, num):
        bin_str = self.dec_to_bin(num)
        hex_str = self.bin_to_hex(bin_str)
        return hex_str
    
    def encryptword(self, word):

        res_str = ""

        prev_letter = word[0]
        cnt = 0

        for i in range(len(word)):
            if prev_letter == word[i]:
                cnt +=1
            else:
                res_str =  self.dec_to_hex(cnt) + prev_letter + res_str
                cnt =1
                prev_letter = word[i]
        res_str = self.dec_to_hex(cnt) + prev_letter + res_str
        #rev_res_str = res_str[::-1]
        #print(rev_res_str)
        return res_str


word = input()
dectohex = DecToHex()
print("encrypted : ", dectohex.encryptword(word) )
