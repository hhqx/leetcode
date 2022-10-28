import time


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

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    # def __str__(self):
    #     return "A trie object."

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
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

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
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def query_all(self, x):
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        node = self.root

        results = []
        # Check if the prefix is in the trie
        for i, char in enumerate(x):
            self.output = []
            if char in node.children:
                child = node.children[char]
                self.dfs(child, x[:i])
                results.append(self.output)
                node = child
            else:
                # cannot found the prefix, return empty list
                for i in range((len(x)-i)):
                    results.append([])
                return results

        # Traverse the trie to get all candidates
        # self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return results

    def query_from_start_to_end(self, x):

        results = []
        true_root = self.root
        query_trie = self

        for i in range(len(x)):
            if x[i] in query_trie.root.children:
                res = [x[:i] + prefix for prefix, cnt in query_trie.query(x[i])]
                results.append(res)
                query_trie.root = query_trie.root.children[x[i]]
            else:
                for i in range((len(x) - i)):
                    results.append([])

        self.root = true_root
        return results


import time
if __name__ == "__main__":
    t = Trie()
    t.insert('was')
    t.insert('word')
    t.insert('war')
    t.insert('war')
    t.insert('what')
    t.insert('where')
    t.insert('wh')
    t.insert('apple')
    result = t.query('wh')
    print(result)

    start = time.time()
    print(t.query_all('whatsdf1'))
    print(f'执行时间: {time.time() - start}')

    start = time.time()
    print(t.query_from_start_to_end('what1'))
    print(f'执行时间: {time.time()-start}')
