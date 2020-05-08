# Travel the throughout the tree if you find the node, then set the parent and the level using the pair class
# Return the object of pair class
# finally check the condition

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        class Pair:
            def __init__(self,level,parent):
                self.parent = parent
                self.level = level
        
        def levelAndParent(root,key,level,parent):
            if(root is None):
                return None
            if(root.val == key):
                return Pair(level,parent)
            return levelAndParent(root.left,key,level+1,root.val) or levelAndParent(root.right,key,level+1,root.val)
        
        first = levelAndParent(root,x,0,None)
        second = levelAndParent(root,y,0,None)
        if(first.level == second.level and first.parent != second.parent):
            return True
        return False
        
Time Complexity : O(N)
Space Complexity : O(1)

