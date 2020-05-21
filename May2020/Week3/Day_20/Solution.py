# DFS Approach
# Finding inorder traversal of given BST tree and than return the Kth element in the list

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        traversal = []
        def inorder(root):
            if(not root):
                return True
            inorder(root.left)
            traversal.append(root.val)
            inorder(root.right)
            return traversal
        return inorder(root)[k-1]
        
Time Complexity : O(N) , N = no.of nodes in tree

Space Complexity : O(N)


# Method - 2
# return the value when you find the the Kth number instead of visiting all nodes

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [] 
        # que.append(root)
        n = 0
        while True:
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if(k == 0):
                return root.val
            root = root.right
            
Time Complexity : O(H+K) , H = hight of the tree and K= kth node

Space Complexity : O(H+k)


