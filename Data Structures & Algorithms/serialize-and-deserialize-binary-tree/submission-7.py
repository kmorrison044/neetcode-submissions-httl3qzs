# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(",".join(res))
        return ",".join(res)

    def deserialize(self, data):
        data = data.split(",")
        idx = 0

        def dfs():
            nonlocal idx
            if data[idx] == "N":
                idx += 1
                return
            
            root = TreeNode(int(data[idx]))
            idx += 1
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()