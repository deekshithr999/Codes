1. ### Coin Change Problem

> [[Leet Code 322. Coin Change](https://leetcode.com/problems/coin-change/) | DP ] 
> 
> **Approach:**  
>     Given Amount=11, coins = [1,2,5]. Calculate min denominations
>     Each amount can be written as coin+dp[remaining_amount]

---

2. ### Maximum Product SubArray
   
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
