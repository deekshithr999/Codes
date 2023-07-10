
'''
TC: O(N)
SC: O(N)
'''

class IsoMorphic2(object):
    def __init__(self):
        pass

    def is_isomorphic(self, st1, st2):
        if len(st1)!= len(st2):
            return 0
        
        for i in range(len(st1)):
            for j in range(i,len(st1)):
                if st1[i] == st1[j]:
                    if st2[i] == st2[j]:
                        continue
                    else:
                        return 0
        
        return 1

class IsoMorphic(object):
    def __init__(self):
        pass
    
    def is_isomorphic(self, st1, st2):

        if len(st1)!= len(st2):
            return 0
        dt = {}

        for i in range(len(st1)):
            if st1[i] not in dt:
                dt[st1[i]]=set()
            dt[st1[i]].add(st2[i])
            if len(dt[st1[i]])>1:
                return 0
        
        return 1


if __name__ == "__main__":

    st1 = input()
    st2 = input()
    isomorphic = IsoMorphic2()
    print("is isomorhic : ", isomorphic.is_isomorphic(st1,st2)&isomorphic.is_isomorphic(st2,st1))

