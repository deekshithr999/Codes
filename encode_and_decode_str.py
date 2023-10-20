

class Solution:

    def encode(self, l_sts): # takes list of strings, returns encoded strings and encoded chars

        res_str = ""
        encod_str = "#"

        for st in l_sts:
            for i in range(len(st)):
                if st[i] == encod_str:
                    res_str = res_str+ "\\" 
                res_str = res_str + st[i]
            res_str += "#"
        
        return res_str, encod_str
    
    def decode(self, encd_st, encd_chr):
        dec_strs = []
        tmp_str = ""
        for i in range(len(encd_st)):
            # \#
            if encd_st[i] == "\\":
                if i +1 < len(encd_st) and encd_st[i+1]== encd_chr:
                    continue
            if encd_st[i]== encd_chr:
                if  encd_st[i-1]=='\\':
                    tmp_str += encd_st[i]
                    continue
                else:
                    dec_strs.append(tmp_str)
                    tmp_str = ""
                    continue
            tmp_str += encd_st[i]
        if len(tmp_str)!= 0:
            dec_strs.append(tmp_str)
        return dec_strs
            


if __name__ == "__main__":

    l_sts = input().split()
    sol = Solution()

    encod_str, encod_char = sol.encode(l_sts)
    print("encode str ", encod_str, "encod_char  ", encod_char)
    print("decoded vals : ", sol.decode(encod_str, encod_char))



