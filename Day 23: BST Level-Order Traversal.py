Link : https://www.hackerrank.com/challenges/30-binary-trees/problem?isFullScreen=true

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        l = []
        if (root.data is not None):
            l.append(root)
        answer = ""
        while (l):
            current = l[0]
            answer = answer + str(current.data) + " "
            if current.left is not None:
                l.append(current.left)
            if current.right is not None:
                l.append(current.right)
            l.pop(0)
        print(answer)
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
