from typing import List
from collections import Counter

# Time : Beats 88.89 %
# Memo : Beats 94.44 %
class Solution:
    class TrieNode:
        serial = ""
        def __init__(self):
            self.children = {}

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        '''
        1. construct trie to reduce iteration
            - node.children = {name:node, ..}
            - node.serial = 'node1(node11(node111()))node2()'
        2. serialize child nodes to compare structure with counter
            - post-order dfs
            - seiralize children 
            - sort serialized children
            - store to node
        3. count valid path
        '''

        # construct trie
        root = self.TrieNode()
        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = self.TrieNode()
                curr = curr.children[folder]
        

        # serialize node : post-oder dfs
        freq = Counter()
        def serialize(node):
            if not node.children:
                return
            s = []
            for folder,child_node in node.children.items():
                serialize(child_node)
                s.append(f'{folder}({child_node.serial})')
            s.sort()
            node.serial = "".join(s)
            freq[node.serial] += 1
        serialize(root)
        
        # count valid path : pre-order dfs
        ret = []
        curr_path = []
        def count_valid(node):
            # end iteration 
            if freq[node.serial] > 1:
                return
            # add curr path to ret
            if curr_path:
                ret.append(curr_path[:])
            # process children
            for folder,child_node in node.children.items():
                curr_path.append(folder)
                count_valid(child_node)
                curr_path.pop()
        count_valid(root)
        return ret
            

