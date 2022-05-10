
'''
Link : https://www.codingninjas.com/codestudio/problems/975286?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

Problem Statement
You have been given weights and values of ‘N’ items. You are also given a knapsack of size ‘W’.
Your task is to put the items in the knapsack such that the total value of items in the knapsack is maximum.
Note:
You are allowed to break the items.
Example:
If 'N = 4' and 'W = 10'. The weights and values of items are weights = [6, 1, 5, 3] and values = [3, 6, 1, 4]. 
Then the best way to fill the knapsack is to choose items with weight 6, 1 and  3. The total value of knapsack = 3 + 6 + 4 = 13.00   
Input Format:
The first line contains an integer ‘T’ denoting the number of test cases. Then each test case follows.

The first line of each test case contains two single space-separated integers ‘N’ and ‘W’, respectively.

The second line of each test case contains ‘N’ single space-separated integers representing the weight of the i-th item.

The third line of each test case contains ‘N’ single space-separated integers representing the value of the i-th item.
Output Format:
For each test case, the only line of output will print the maximum total value of items in the knapsack.  

The output must be rounded correctly up to two decimal places.

Print the output of each test case in a separate line.
Note:
You are not required to print the expected output; it has already been taken care of. Just implement the function.
Constraints:
1 <= T <= 100
1 <= N <= 5000
1 <= W <= 10^5
1 <= weights[i] <= 10^5
1 <= values[i] <= 10^5

Time limit: 1 sec
Sample Input 1:
1
6 200
50 40 90 120 10 200 
40 50 25 100 30 45
Sample Output 1:
204.00
Explanation Of Sample Output 1:
The most optimal way to fill the knapsack is to choose full items with weight 10 and value 30, weight 40 and value 50, weight 120 and value 100. Then take weight 30 from the item with weight 50 and value 40.

The total value =  30 + 50 + 100 + (30/50)*(40) = 204.00
Sample Input 2:
1
5 100
20 24 36 40 42
12 35 41 25 32
Sample Output 2:
106.48

'''

################################################################
'''
Idea Greedy approach. 
Since the items are selected based on max val/weight basis.

TC : O(nlogn)+O(n)
SC : O(n)

'''
def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
	lst=[]
	maxval = 0
	for i in range(len(items)):
		val = items[i][1]/items[i][0]
		lst.append((val,i))
	
	lst.sort(reverse=True)
	#print (lst)
	
	for vpw,i in lst:
		if n == 0 :
			break
		m =min(items[i][0],w)
		maxval+= m*items[i][1]/items[i][0]
		w-=m
	
	return maxval
