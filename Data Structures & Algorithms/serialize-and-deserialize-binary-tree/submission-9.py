# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # BFS version of the problem. Append "N" to res list anytime
    # node is None, else append the string of it's value
    # join the list to a string with ",". To deserialize, split
    # the data by comma and if the first value is "N", return None
    # else create a node with the first value, through it into a deque
    # set idx to 1, and create nodes from the vals in the data list and
    # append to q, until there is nothing in the q
    def serialize(self, root):
        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(res)


    def deserialize(self, data):
        data = data.split(",")
        if data[0] == "N":
            return None
        
        root = TreeNode(int(data[0]))
        q = deque([root])
        idx = 1

        while q:
            node = q.popleft()
            if data[idx] != "N":
                node.left = TreeNode(int(data[idx]))
                q.append(node.left)
            idx += 1

            if data[idx] != "N":
                node.right = TreeNode(int(data[idx]))
                q.append(node.right)
            idx += 1
        
        return root
