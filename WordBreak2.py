'''
link : https://www.codingninjas.com/codestudio/problems/983635
Word Break II
Difficulty: HARD
Level 1
Avg. time to solve
15 min
Success Rate
85%
Problem Statement
You are given a non-empty string S containing no spaces’ and a dictionary of non-empty strings (say the list of words). You are supposed to construct and return all possible sentences after adding spaces in the originally given string ‘S’, such that each word in a sentence exists in the given dictionary.
Note :
The same word in the dictionary can be used multiple times to make sentences.
Assume that the dictionary does not contain duplicate words.
Input format :
The first line contains an integer ‘T’ denoting the number of test cases. 

Then the 'T' test cases follow.

The first line contains an integer value ‘K’ which denotes the size of the dictionary.

The second line contains ‘K’ non-empty, space separated strings denoting the words of the dictionary.

The third line contains a non-empty string ‘S’.
Output format :
For each test case, print each possible sentence after adding spaces, in different lines.

The output of each test case is printed in a separate line. 
Note :
1. You do not need to print anything, it has already been taken care of. Just implement the given function.
2. The order in which the output sentences are returned does not matter.
Constraints :
1 <= T <= 10
1 <= K <= 100
1 <= | word | <= 16
1 <= | S | <= 13

where |word| is the length of each word in the dictionary and |S| is the length of the string S.

Time Limit: 1 sec
Sample Input 1:
1
6
god is now no where here
godisnowherenowhere
Sample Output 1:
god is no where no where
god is no where now here
god is now here no where
god is now here now here
Explanation To Sample Input 1:
One way to make sentences is to take “god” and append a space, then take “is”  and append space, take “now” from the dictionary and take “here” as well. 
Similarly, for other sentences also, we can add space to get other possible sentences. Note that we can reuse dictionary words as “no” and “now” are used two times in the same sentence.
Sample Input 2:
1
4
god is no here
godisnowhere
Sample Output 2:
No output to be printed
Explanation To Sample Input 2:
We can not make any sentence because after making “god is no” we will be stuck with “where”. There is no way to break “where” further such that we can get any word from the dictionary.

'''

############################################
'''
TC : O(n!) . #check this again
SC : O(n!) auxillary

'''

def wordBreak(s, dictionary):

    # Write your code here
    st=set(dictionary)
    #print(dictionary)
    res_sen=[]
    start=0
    sen=""
    sentenceForm(s,st,start,res_sen,sen)
    for i in range(len(res_sen)):
        #if i !=None:
        #print(res_sen[i])
        res_sen[i]=res_sen[i].strip()
        #print(res_sen[i])
        #print("=====")
            
    return res_sen
    

def sentenceForm(s,word_set,start, sen_lst,curr_sen):
    
    if start==len(s) and len(curr_sen)!=0:
        sen_lst.append(curr_sen)
        #print("cur sen ", curr_sen)
        return
    
    for i in range(start,len(s)):
        if s[start:i+1] in word_set:
            sentenceForm(s,word_set,i+1,sen_lst,curr_sen+" "+s[start:i+1])