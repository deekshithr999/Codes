class Solution:
    '''
    TC: O(n)
    SC: O(n)
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        opers = '+*/-'
        st = list()
        
        def oper(a,b, ele):
            if ele == "*":
                return a*b
            elif ele == "/":
                return a/b
            elif ele == '+':
                return a+b
            elif ele == '-':
                return a - b
        
        for ele in tokens:
            if ele in opers:
                b,a = st.pop(), st.pop()
                tres = oper(a,b, ele)
                st.append(int(tres))
            else:
                st.append(int(ele))
        return st.pop()