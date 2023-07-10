
'''
https://www.geeksforgeeks.org/find-the-minimum-distance-between-the-given-two-words/

https://practice.geeksforgeeks.org/problems/closest-strings0611/1

'''

'''
TC: O(n^2) #exc str comparision
SC : O(n+m)
'''
class DBwTwoWords(object):

    def __init__(self):
        pass

    def dist_bw_two_words (self, lst: list, word_lst: list):

        word1_pos = []
        word2_pos = []

        for i in range(len(lst)):
            if word_lst[0] == lst[i]:
                word1_pos.append(i)
        
        for i in range(len(lst)):
            if word_lst[1] == lst[i]:
                word2_pos.append(i)

        return self.min_sub_bw_nums(word1_pos, word2_pos)    


    def min_sub_bw_nums (self, num1_lst: list, num2_lst: list):
        if len(num1_lst)==0 or len(num2_lst)==0:
            return 0
        mini = abs(num1_lst[0]-num2_lst[0])
        for num1 in num1_lst:
            for num2 in num2_lst:
                mini = min(mini, abs(num1-num2))        
        return mini

'''
TC : O(N)
SC : O(1)
'''

def distbw2words(lst: list[str], word_lst: list[str]):
    import sys
    mini = sys.maxsize
    w1idx =-1
    w2idx = -1

    for i in range(len(lst)):
        if lst[i] == word_lst[0]:
            w1idx = i
        elif lst[i] == word_lst[1]:
            w2idx = i
        
        if w1idx != -1 and w2idx != -1:
            mini = min(mini, abs(w1idx-w2idx))
    
    return mini

def distbw2words2(lst, target_lst):
    if target_lst [0] ==target_lst[1]:
        return 0
    mini_dist = len(lst)
    prev_pos = -1
    for i in range(len(lst)):
        if prev_pos == -1:
            if (lst[i]== target_lst[0]) | (lst[i] == target_lst[1]):
                prev_pos = i
        
        if lst[i] == target_lst[0] or lst[i] == target_lst[1]:
            if lst[prev_pos] !=lst[i]:
                mini_dist = min(mini_dist, i-prev_pos)
            prev_pos = i
    return mini_dist



if __name__ == "__main__":

    word_lst = input().split()
    words = input().split()
    
    db2words =DBwTwoWords()
    print("result : ", db2words.dist_bw_two_words(word_lst, words))
    print("result : ", distbw2words(word_lst, words))
    print("result : ", distbw2words2(word_lst, words))