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

---

15. #### Increasing Triplet SubSequence
    
    > [ [334.Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | | LC-75]
    > 
    > **Approach 1:** Take minArr from left, maxArr from right.
    > TC: O(n)
    > SC: O(n)
    > 
    > **Approach 2:** Using 2 Vars
    > TC: O(n)
    > SC: O(1)
    > 
    > *idea:* `first` var stores the lowest, `second` var stores the second lowest, edge case: `if(curr > second) ` which return `true`. Imaginee... . thinked how store previous small vals, thats where 2nd var comes into playy..

---

16. #### Construct Binary Tree from Preorder and Inorder Traversal
    
    > [ [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Trees | NC-75 ]
    > Approach:
    > Preorder - *par* left right
    > inorder - left *par* right
    > 
    > => preorder gives idea which is a par node, based on it, split the tree in **inorder**.
    >                 par
    >                 / \
    >              left  right
    > Note: To track the preorder, the #left_tree_inorder_elems = #left_tree_preorder_elems. split preorders' array accordingly.

---

17. #### Find Minimum in Rotated Sorted Array
    
    > [ [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)| Binary Search | NC-75 ]
    > Approach:
    > TC: O(logn)
    > 
    > there  is always a sorted array & unsorted array<img title="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAApgAAAGACAYAAAAJXBKiAAAAAXNSR0IArs4c6QAAA3R0RVh0bXhmaWxlACUzQ214R3JhcGhNb2RlbCUyMGR4JTNEJTIyOTQ2JTIyJTIwZHklM0QlMjI2NTIlMjIlMjBncmlkJTNEJTIyMSUyMiUyMGdyaWRTaXplJTNEJTIyMTAlMjIlMjBndWlkZXMlM0QlMjIxJTIyJTIwdG9vbHRpcHMlM0QlMjIxJTIyJTIwY29ubmVjdCUzRCUyMjElMjIlMjBhcnJvd3MlM0QlMjIxJTIyJTIwZm9sZCUzRCUyMjElMjIlMjBwYWdlJTNEJTIyMSUyMiUyMHBhZ2VTY2FsZSUzRCUyMjElMjIlMjBwYWdlV2lkdGglM0QlMjI4MjclMjIlMjBwYWdlSGVpZ2h0JTNEJTIyMTE2OSUyMiUyMG1hdGglM0QlMjIwJTIyJTIwc2hhZG93JTNEJTIyMCUyMiUzRSUzQ3Jvb3QlM0UlM0NteENlbGwlMjBpZCUzRCUyMjAlMjIlMkYlM0UlM0NteENlbGwlMjBpZCUzRCUyMjElMjIlMjBwYXJlbnQlM0QlMjIwJTIyJTJGJTNFJTNDbXhDZWxsJTIwaWQlM0QlMjJYdlNISTZlT2dQb1ViNkpiSTJ0Ti0yJTIyJTIwdmFsdWUlM0QlMjIlMjIlMjBzdHlsZSUzRCUyMmVuZEFycm93JTNEY2xhc3NpYyUzQmh0bWwlM0QxJTNCcm91bmRlZCUzRDAlM0IlMjIlMjBlZGdlJTNEJTIyMSUyMiUyMHBhcmVudCUzRCUyMjElMjIlM0UlM0NteEdlb21ldHJ5JTIwd2lkdGglM0QlMjI1MCUyMiUyMGhlaWdodCUzRCUyMjUwJTIyJTIwcmVsYXRpdmUlM0QlMjIxJTIyJTIwYXMlM0QlMjJnZW9tZXRyeSUyMiUzRSUzQ214UG9pbnQlMjB4JTNEJTIyMzgwJTIyJTIweSUzRCUyMjM0MCUyMiUyMGFzJTNEJTIyc291cmNlUG9pbnQlMjIlMkYlM0UlM0NteFBvaW50JTIweCUzRCUyMjUxMCUyMiUyMHklM0QlMjIyODAlMjIlMjBhcyUzRCUyMnRhcmdldFBvaW50JTIyJTJGJTNFJTNDJTJGbXhHZW9tZXRyeSUzRSUzQyUyRm14Q2VsbCUzRSUzQyUyRnJvb3QlM0UlM0MlMkZteEdyYXBoTW9kZWwlM0W178ynAAAgAElEQVR4Xu3dS6hu51kH8KexIg6c2OhAHGp1IESltDXibSJtFcELKq1WQZycE6+gguJE0IF4Qzi7IIKJII1g1aQKJlInTSdtdCCmpWDroGhThLZe0CSl4lnJd5Kdc/b+vmet711rvZffgTNI8q738nvelj/f3s+3XhP+ECBAgAABAgQIECgo8JqCc5mKAAECBAgQIECAQAiYLgEBAgQIECBAgEBRAQGzKKfJCBAgQIAAAQIEBEx3gAABAgQIECBAoKiAgFmU02QECBAgQIAAAQICpjtAgAABAgQIECBQVEDALMppMgIECBAgQIAAAQHTHSBAgAABAgQIECgqIGAW5TQZAQIECBAgQICAgOkOECBAgAABAgQIFBUQMItymowAAQIECBAgQEDAdAcIECBAgAABAgSKCgiYRTlNRoAAAQIECBAgIGC6AwQIECBAgAABAkUFBMyinCYjQIAAAQIECBAQMN0BAgQIECBAgACBogICZlFOkxEgQIAAAQIECAiY7gABAgQIECBAgEBRAQGzKKfJCBAgQIAAAQIEBEx3gAABAgQIECBAoKiAgFmU02QECBAgQIAAAQICpjtAgAABAgQIECBQVEDALMppMgIECBAgQIAAAQHTHSBAgAABAgQIECgqIGAW5TQZAQIECBAgQICAgOkOECBAgAABAgQIFBUQMItymowAAQIECBAgQEDAdAcIECBAgAABAgSKCgiYRTlNRoAAAQIECBAgIGC6AwQIECBAgAABAkUFBMyinCYjQIAAAQIECBAQMN0BAgQIECBAgACBogICZlFOkxEgQIAAAQIECAiY7gABAgQIECBAgEBRAQGzKKfJCBAgQIAAAQIEBEx3gAABAgQIECBAoKiAgFmU02QECBAgQIAAAQICpjtAgAABAgQIECBQVEDALMppMgIECBAgQIAAAQHTHSBAgAABAgQIECgqIGAW5TQZAQIECBAgQICAgOkOECBAgAABAgQIFBUQMItymowAAQIECBAgQEDAdAcIECBAgAABAgSKCgiYRTlNRoAAAQIECBAgIGC6AwQIECBAgAABAkUFBMyinCYjQIAAAQIECBAQMN0BAgQIECBAgACBogICZlFOkxEgQIAAAQIECAiY7gABAgQIECBA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Bw7B8lMuEgECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUENDlsJ8AAAB0SURBVDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE5AwMw5GUWAAAECBAgQIJAUEDCTUIYRIECAAAECBAjkBATMnJNRBAgQIECAAAECSQEBMwllGAECBAgQIECAQE7g/wEMiXCu3MdmrwAAAABJRU5ErkJggg==" alt="" width="87" data-align="left">if mid to right is increasing, then smallest will be either the mid or to the left of it. nums[mid]<nums[right], else it would be on the side side. 

---

18. #### Search in Rotated Sorted Array
    
    > [ [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Binary Search | NC-75 ]
    > 
    > TC: O(logn)
    > SC: O(1)
    > 
    > In a rotated sorted array, the array will be either left sorted/ right sorted.
    >    2 3 4 ***5*** 6 1 - left sorted array
    >    5 6 1 ***2*** 3 4 - right sorted array

---

19. #### SubSet Generation
    
    > [ [78. Subsets](https://leetcode.com/problems/subsets/) | Sub Sets| ]
    > 
    > For each element, we have choice of including/ excluding the element.
    > 
    > ```python
    > class Solution:
    >     def subsets(self, nums: List[int]) -> List[List[int]]:
    >         res = []
    > 
    >         def genSubSet(idx, sset):
    >             if idx == len(nums):
    >                 res.append(sset[:])
    >                 return
    >             genSubSet(idx+1, sset)
    >             sset.append(nums[idx])
    >             genSubSet(idx+1, sset)
    >             sset.pop()
    >         genSubSet(0, [])
    >         return res 
    > ```
    
    ---
    
    20. #### Topological Sorting
        
        > [ [GFG Topological Sorting ]([Topological sort | Practice | GeeksforGeeks](https://www.geeksforgeeks.org/problems/topological-sort/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)) | Topological Sorting | ]
        > DFS Method
        > Stack to store the traverse order
        > After each traversal of vertex, push to stack, return pop of stack for the topological order.
        > Imagine in dfs, all childs are traversed, before pushing to the stack.
        > 
