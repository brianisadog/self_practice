class TrieNode(object):
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_complete = False


class AutoComplete(object):
    def __init__(self, head):
        self.trie = head

    def auto_complete(self, term):
        results = []

        head = self.trie
        i = 0
        while i < len(term):
            if term[i] in head.children:
                head = head.children[term[i]]
                i += 1
            else:
                break

        if i > 0 and i == len(term):
            self.dfs(head, results, term[:-1])

        return results

    def dfs(self, head, results, current):
        current += head.val
        if head.is_complete:
            results.append(current)

        for node in head.children.values():
            self.dfs(node, results, current)


def build(head, term):
    for char in term:
        if char in head.children:
            head = head.children[char]
        else:
            node = TrieNode(char)
            head.children[char] = node
            head = node

    head.is_complete = True


words = ['he', 'help', 'hee', 'her', 'heap', 'hello', 'hero', 'happy', 'hi', 'apple']
trie = TrieNode()

for word in words:
    build(trie, word)

ac = AutoComplete(trie)
print(ac.auto_complete('he'))
print(ac.auto_complete('ha'))
print(ac.auto_complete('a'))
print(ac.auto_complete(''))
print(ac.auto_complete('hc'))
