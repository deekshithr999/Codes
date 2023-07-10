
class Panagram(object):

    def __init__(self):
        pass

    def panagram(self, st1):
        
        st1 = st1.lower()
        if (len(st1)==0):
            return 0
        
        lst =[0]*26

        for i in range(len(st1)):

            l1 = ord('a')
            h1 = ord('z')
            ch = (st1[i])
            num = ord(ch)
            if num >=l1 and num <=h1:
                lst[num-l1] = 1

        cnt = 0
        for i in range(26):
            cnt+= lst[i]
        
        if cnt == 26:
            return 1
        else :
            return 0



if __name__ == "__main__":
    pang = Panagram()

    print(" yes ", pang.panagram(input()))
