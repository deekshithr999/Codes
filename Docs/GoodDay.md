1. #### Coin Change Problem
   
   > [[Leet Code 322. Coin Change](https://leetcode.com/problems/coin-change/) | DP | NC-75 ] 
   > 
   > **Approach:**  
   >     Given Amount=11, coins = [1,2,5]. Calculate min denominations
   >     Each amount can be written as coin+dp[remaining_amount]

---

2. #### Coin Change II
   
   > [[518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) | DP| NC-150]
   > 
   > **Approach 1:**
   > Using Memoization techinque.
   > Also, the way coins are included also matters here, 1+1+2 = 2+1+1
   > 
   > **Approach 2:**
   > Using DP.
   > Think of the problem as unbounded knapsack

---

3. #### Maximum Product SubArray
   
   > [[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | DP ]
   > 
   > **Approach 1: Uing 2 ptr Approach (l, r)**
   > 
   > There are 3 number types `(+ve, -ve, 0)`. whenever a `0` is encountered, the max_product will be `0` or +ve. 
   > If a -ve is encountered there can be -ve number towards the right so Keep Adding. *Brief:* i) right++ does calculate max_prod (1,2,3,-4,7). Here (1,2,3) is calculated.
   >           ii) left++ does 7. **Approach 2:** Using Max_prod & Min_Prod Approach   
   > 
   > **Approach 2: Using Max_prod & Min_prod Approach**
   > 
   > The Max_prod stores the max & Min_prod stores the min_prod

---

3. ### Lowest Common Ancestor of a Binary Tree
   
   > [[235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Trees ]
   > 
   > **Approach 1: (Most Efficient)**
   > TC: O(n), SC: O(1)
   > If either nodes is encountered return the node.
   > If both the nodes are encountered, then return the node.
   > 
   > **Approach 2:**
   > TC: O(n)
   > SC: O(n)
   > Store the paths of the nodes.

---

4. ### Lowest Common Ancestor of a Binary <u>Search</u> Tree
   
   > [ [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Trees ]
   > 
   > **Approach 1 :** If both nodes gt than root explore right, elif less than explore left, /\ if there is division return the node.
   > 
   > ```python
   >     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
   >         if p.val < root.val and q.val < root.val:
   >             return self.lowestCommonAncestor(root.left, p, q)
   >         elif p.val > root.val and q.val > root.val:
   >             return self.lowestCommonAncestor(root.right,p,q)
   >         else:
   >             return root
   > ```

---

5. ### Validate Binary Search Tree
   
   > [ [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Tree ]
   > 
   > **Approach 1:** Using top to bottom Approach
   > TC: O(n)
   > SC: O(1)
   > Idea: start with -inf < val < inf (left < val< right)
   > exploring left -> replace right with node.val ->  gng left child < curr_val
   > exploring right -> replace right -> right_child > node.val
   > 
   > ```python
   > class Solution:
   >     def isValidBST(self, root: Optional[TreeNode]) -> bool:
   > 
   >         def trav(node, left, right):
   >             if node is None:
   >                 return True
   >             if not (node.val <right and node.val > left) :
   >                 return False
   >             return trav(node.left, left, node.val) and trav(node.right, node.val, right)
   >         return trav(root, float('-inf'), float('inf'))
   > ```
   > 
   > ---
   > 
   > **Approach 2:** Using bottom to top approach
   > TC: O(n)
   > SC: O(1)
   >  Idea:
   >     1. Min in the right subTree is always greater than parent.
   >     2. Max in left subTree is always less than parent.
   > 
   > ---
   > 
   > **Approach 3:** Use ***Inorder*** Traversal
   >     TC : O(n)
   >     SC: O(n)
   >     Inorder traversal gives the sorted Tree.
   
   ---

6. ### Implement Queue Using Stacks
   
   > [ [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Stacks, Queues ]
   > 
   > **Approach 1:** Use 2 stacks
   > Push into Stack1, pop from Stack2
   > while popping see if Stack2 is empty, then copy all contents from stack 1 -> stack2
   > 
   > class MyQueue:
   > 
   > ```python
   > def __init__(self):
   >     self.stack1 = []
   >     self.stack2 = []
   > 
   > 
   > def push(self, x: int) -> None:
   >     if not self.stack2:
   >         self.stack2.append(x)
   >     else:
   >         self.stack1.append(x)
   > 
   > def pop(self) -> int:
   >     ele = self.stack2.pop()
   >     if not self.stack2:
   >         while self.stack1:
   >             top = self.stack1.pop()
   >             self.stack2.append(top)
   >     return ele
   > 
   > 
   > def peek(self) -> int:
   >     return self.stack2[-1]        
   > 
   > def empty(self) -> bool:
   >     if not self.stack2:
   >         return True
   > ```

---

7. ### Inorder Traversal - Iterative
   
   > [ [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Trees ]
   > 
   > **Approach 1:**
   > take curr = root and stack
   > while pushing into stack -> Traverse left
   > while popping from stack -> Traverse right
   > 
   > ```
   > ```python
   > # Definition for a binary tree node.
   > # class TreeNode:
   > #     def __init__(self, val=0, left=None, right=None):
   > #         self.val = val
   > #         self.left = left
   > #         self.right = right
   > class Solution:
   >     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
   >         curr = root
   >         res, stack = [], []
   > 
   >         while curr or stack :
   >             while curr :
   >                 stack.append(curr)
   >                 curr = curr.left
   >             curr = stack.pop()
   >             res.append(curr.val)
   >             curr = curr.right
   >         return res
   > ```

---

8. ### Daily Temperatures
   
   > [ [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Stacks ]
   > **Approach 1:**
   > 
   > TC: O(n)
   > SC: O(n)
   > Insert temperatures into stack. => monotonically descending
   > when a temp higher than top[-1] ele is encountered pop the top
   > 
   > **Approach 2:** " lookout for the numbers constraint "
   > Start from left and store the visited indices in array. This becomes O(n) -> O(30) for each temperature.
   
   ---

9. #### Path Sum III
   
   > [[437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Trees, DP]
   > **Approach 1:**
   > TC: O(n)
   > SC: O(n)
   > 
   > we'll store the running sum in dictionary. when runningSum - target is present in a *dict*, which means we've encountered a target in the middle.
   > *Notes to think:* How does dt[runningSum]=2, In a given Path we've countered the runningSum 2 times, how? which means the first runningSum is compensated. 

---

10. #### Linked List Cycle
    
    > [ [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Linked List ]
    > Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
    > 
    > ```python
    > # Definition for singly-linked list.
    > # class ListNode:
    > #     def __init__(self, x):
    > #         self.val = x
    > #         self.next = None
    > 
    > class Solution:
    >     def hasCycle(self, head: Optional[ListNode]) -> bool:
    > 
    >         slow, fast = head, head
    >         while fast and fast.next: #base case covered here, head is null
    >             fast = fast.next.next
    >             slow = slow.next
    >             if fast == slow:
    >                 return True
    >         return False
    > ```

---

11. #### Best Time to Buy and Sell Stock with Cooldown
    
    > [ [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | DP | NC-150 ]
    > 
    > **Approach 1:**
    > TC: O(n)
    > SC: O(n)
    > Draw a state-space tree. In that sub elements overlap. 
    > sale, nothing includes as sale, & same with buy
    > ![state space image](C:\Users\reddy\Downloads\stocks_buy.jpg)
    > 
    > **Approach 2:**
    > TC: O(n^2)
    > SC: O(n)
    > Idea is to start from the last. Compute maxProfit from last. so 
    > ithday_profit is buying it on ith day and maximizing profit any day after that buy selling, following by buy&sell..s

---

12. #### Bounded KnapSack / 0-1 KnapSack Problem
    
    > [[9. 0 - 1 Knapsack Problem | Practice | GeeksforGeeks](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article) | DP | Standard]
    > 
    > ```python
    > class Solution:
    > 
    >     #Function to return max value that can be put in knapsack of capacity W.
    >     def knapSack(self,W, wt, val, n):
    >         wVal = []
    >         for i in range(n):
    >             wVal.append((wt[i], val[i]))
    >         wVal.sort()
    > 
    >         mat = [[0]*(W+1) for _ in range(n+1)]
    >         for r in range(1, n+1):
    >             for c in range(1, W+1):
    >                 if c - wVal[r-1][0] >= 0 :
    >                     mat[r][c] = max(mat[r-1][c], wVal[r-1][1] + mat[r-1][c - wVal[r-1][0]])
    >                 else:
    >                     mat[r][c] = mat[r-1][c]
    >         return mat[n][W]
    > ```

---

12. #### Knapsack with Duplicate Items / UnBounded KnapSack
    
    > [[-. Knapsack with Duplicate Items | Practice | GeeksforGeeks](https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article) | DP | Standard ]
    > The approach remains same, except in considering top row (i.e row-1) while including the current item, consider the curr row.
    > 
    > ```python
    > #User function Template for python3
    > 
    > class Solution:
    >     def knapSack(self, N, W, val, wt):
    >         wVal = []
    >         for i in range(N):
    >             wVal.append((wt[i], val[i]))
    >         wVal.sort()
    >         mat = [[0]*(W+1) for i in range(N+1)]
    > 
    >         for i in range(1, N+1):
    >             for j in range(1, W+1):
    >                 if j-wVal[i-1][0] >= 0:
    >                     mat[i][j]= max(mat[i-1][j], wVal[i-1][1] + mat[i][j-wVal[i-1][0]])
    >                 else:
    >                     mat[i][j] = mat[i-1][j]
    >         return mat[N][W]
    > #{ 
    >  # Driver Code Starts
    > #Initial Template for Python 3
    > 
    > if __name__ == '__main__':
    >     t = int(input())
    >     for _ in range(t):
    >         N, W = [int(x) for x in input().split()]
    >         val = input().split()
    >         for itr in range(N):
    >             val[itr] = int(val[itr])
    >         wt = input().split()
    >         for it in range(N):
    >             wt[it] = int(wt[it])
    > 
    >         ob = Solution()
    >         print(ob.knapSack(N, W, val, wt))
    > # } Driver Code Ends
    > ```

---

13. #### Top K Frequent Elements
    
    > [ [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Arrays & Hashing| NC-75 ]
    > *For k frequentss, use heaps of size k *
    > 
    > **Approach 1:**
    > Most Efficient 
    > TC:O(N)
    > SC: O(N)
    > *Idea:* The maximum frequent is len(array). create a frequency array which stores list of elements of that frequency. 
    > 
    > **Approach 2:**
    > Using minHeaps of size k. Every least freq ele in minHeap is kicked out by new ele with greater Freq.

---

14. #### Interleaving String
    
    > [ [97. Interleaving String](https://leetcode.com/problems/interleaving-string/) | DP | NC-150 ]
    > 
    > **Approach 1:** Using a 2D matrix
    > TC: O(n\*m)
    > SC: O(n\*m)
    > Idea: Look at the code for clarity
    > Value in a given cell is determined by, if a char at that postion matches with any string, then look for the match before.... blahh blahh..
    > 
    > **Approach 2:** Using Memoization
    > 
    > 
