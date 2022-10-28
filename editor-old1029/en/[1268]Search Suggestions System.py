import time

question_content = """
You are given an array of strings products and a string searchWord. 

 Design a system that suggests at most three product names from products after 
each character of searchWord is typed. Suggested products should have common 
prefix with searchWord. If there are more than three products with a common prefix 
return the three lexicographically minimums products. 

 Return a list of lists of the suggested products after each character of 
searchWord is typed. 

 
 Example 1: 

 
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor",
"mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot",
"monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
 

 Example 2: 

 
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
 

 Example 3: 

 
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"]
,["baggage","bags","banner"]
,["baggage","bags"],["bags"]
]
 

Input: products = ["havana"], searchWord = "asdfg"
Output: [[],[],[],[],[],]
 
 Constraints: 

 
 1 <= products.length <= 1000 
 1 <= products[i].length <= 3000 
 1 <= sum(products[i].length) <= 2 * 10⁴ 
 All the strings of products are unique. 
 products[i] consists of lowercase English letters. 
 1 <= searchWord.length <= 1000 
 searchWord consists of lowercase English letters. 
 
 Related Topics Array String Trie 👍 2869 👎 148

"""

from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self, words):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.query_cnt = 0
        self.root = TrieNode("")
        for word in sorted(words):
            self.insert(word)


    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if self.query_num <= 0:
            return

        if node.is_end:
            self.output.append(prefix + node.char)
            self.query_num -= 1

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x, query_num=100):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root
        self.query_num = query_num

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        # return sorted(self.output)
        return self.output

    def query_all(self, x):
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        node = self.root

        results = []
        # Check if the prefix is in the trie
        for i, char in enumerate(x):
            self.output = []
            self.query_num = 3
            if char in node.children:
                child = node.children[char]
                self.dfs(child, x[:i])
                # results.append(sorted(self.output))
                results.append(self.output)
                node = child
            else:
                # cannot found the prefix, return empty list
                for i in range((len(x) - i)):
                    results.append([])
                return results

        # Sort the results in reverse order and return
        return results

    def query_from_start_to_end(self, x):

        results = []
        true_root = self.root
        query_trie = self

        for i in range(len(x)):
            if x[i] in query_trie.root.children:
                res = [x[:i] + prefix for prefix in query_trie.query(x[i], query_num=3)]
                results.append(res)
                query_trie.root = query_trie.root.children[x[i]]
            else:
                results.append([] * (len(x)-i))

        self.root = true_root
        return results


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie(products)

        out = t.query_all(searchWord)

        # out = t.query_from_start_to_end(searchWord)

        return out
# leetcode submit region end(Prohibit modification and deletion)
 

from RunLeetCodeInPycharm import StartTest

if __name__ == "__main__":

    TestObj = StartTest(question_content, Solution)
    TestObj.run_test()
