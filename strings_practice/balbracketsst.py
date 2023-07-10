

class Balance(object):

    def __init__(self):
        pass

    def balanced_pos(self, bra_str:str):

        left = 0
        right = len(bra_str)-1

        while left < right:

            if bra_str[left] == ')':
                left +=1
            elif bra_str[right] == '(':
                right -=1
            elif bra_str[left] == '(' and bra_str[right] == ')':
                left += 1
                right -= 1
        print("left ",left, "right ", right)
        if left == 0:
            return -1
        elif right == len(bra_str)-1:
            return len(bra_str)
        else:
            return right+1
    
    def balanced_pos2(self, brstr):
        if len(brstr)==1:
            if brstr[0]=='(':
                return 0
            else:
                return 1
        opbr = [0]*len(brstr)
        clbr = [0]*len(brstr)

        for i in range(1,len(brstr)):
                if brstr[i-1]=='(':
                    opbr[i] = opbr[i-1]+1
                else:
                    opbr[i]=opbr[i-1]
        
        for j in range(len(brstr)-1,-1,-1):
            if j == len(brstr)-1 :
                if brstr[j]==')':
                    clbr[j]=1
            else:
                if brstr[j]==')':
                    clbr[j] = clbr[j+1]+1
                else:
                    clbr[j]=clbr[j+1]
        
        if sum(opbr) ==0:
            return len(brstr)
        elif sum(clbr)==0:
            return -1
        else:
            for j in range(len(brstr)-1,-1,-1):
                if opbr[j] == clbr[j]:
                    return j

         
            

if __name__ =="__main__":

    bal = Balance()
    print("pos : ", bal.balanced_pos2(input()))

