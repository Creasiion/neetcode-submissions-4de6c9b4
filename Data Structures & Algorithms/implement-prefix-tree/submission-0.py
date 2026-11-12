class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            # Go to the last char in that word (to make it more nested)
            # i.e. for dog it'd be {{d:{o:{g:{.}}}}
            trie = trie[char]
        # Mark that you have the particular word
        trie['.']='.'

    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        return '.' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True
        