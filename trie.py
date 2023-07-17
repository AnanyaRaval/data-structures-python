from typing import List

class TrieNode(object):
    """Node for Trie data structure"""

    def __init__(self, char:str):
        #Character stored in this node
        self.char = char

        #dictionary of child nodes
        self.children = {}

        #Whether this character is the end of the word
        self.isEnd = False

class Trie:
    """Trie data structure"""

    def __init__(self):
        """Root node of Trie contains an empty character"""
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        """Insert a word into the Trie"""

        node = self.root
        for ch in word:
            if ch not in node.children:
                #Create node if not already existent
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        
        #Mark the end of this word
        node.isEnd = True

    def search(self, word: str) -> bool:
        """Search if word exists in the Trie"""

        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]           
        return node.isEnd
        
    def starts_with(self, prefix: str) -> bool:
        """Search if prefix exists is in the Trie"""

        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def _dfs(self, node, word=[]) -> None: 
        """Helper function to run DFS on Trie"""
       
        if node.isEnd:
            curr_word = word + [node.char]
            self.output.append(curr_word[:])
        
        for child in node.children.values():
            self.dfs(child, word + [node.char])

    def find_words_with_prefix(self, prefix) -> List[str]:
        """Find all words with prefix"""

        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]

        self.output = []
        self._dfs(curr)
        return [''.join(list(prefix[:-1]) + word) for word in self.output]
    
    def _delete(self, node:TrieNode, word:str, index:str):
        if index == len(word):
            if not node.isEnd:
                return False
            
            #Un-mark the end of word
            node.isEnd = False
            return len(node.children) == 0
        
        char = word[index]
        if char not in node.children:
            return False

        #Delete the node if it has no children and is not an end to another node.
        should_delete = self._delete(node.children[char], word, index+1) and not node.isEnd
        if should_delete:
            del node.children[char]
            return len(node.children) == 0

        return False

    def delete(self, word:str):
        """Delete word from Trie"""

        return self._delete(self.root, word, 0)

if __name__ == "__main__":
    trie = Trie()
    for word in ["dog", "dogs", "cat", "cats", "catsanddog", "and"]:
        trie.insert(word)

    print("Does trie contain the word dog: ", trie.search("dog"))
    print("Does trie contain the word cats: ", trie.search("dog"))
    print("Does trie contain the word catsanddog: ", trie.search("catsanddog"))

    print("Does trie contain the prefix b: ", trie.starts_with('b'))
    print("Does trie contain the prefix cat: ", trie.starts_with('cat'))

    print("All words in trie which start with 'ca':", trie.find_words_with_prefix("ca"))
    print("All words in trie which start with 'd' :", trie.find_words_with_prefix("d"))

    print("All words in trie: ", trie.find_words_with_prefix(""))

    for word in ["dogs", "catsanddog", "and"]:
        trie.delete(word)
        print("Deleted {} from Trie:".format(word))
    
    print("All words in trie after deletion: ", trie.find_words_with_prefix(""))
