class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def segment_longest_words(input_string, trie):
    words = []
    s = 0
    n = len(input_string)

    while s < n:
        found_word = False
        for e in range(n, s, -1):
            if trie.search(input_string[s:e]):
                words.append(input_string[s:e])
                s = e
                found_word = True
                break
        if not found_word:
            words.append(input_string[s])
            s += 1
    return " ".join(words)

# Từ điển
dictionary = [
    "thời", "khóa", "biểu", "đang", "được", "cập", "nhật",
    "môn", "học", "xử", "lý", "ngôn", "ngữ", "tự", "nhiên",
    "con", "ngựa", "đá",
    "học", "sinh", "sinh học",
]


trie = Trie()
for word in dictionary:
    trie.insert(word)


samples = [
    "thờikhóabiểulàđượccậpnhật",
    "mônhọcxửlýngônngữtựnhiên",
    "conngựđácôngựađá",
    "họcsinhhọcsinhhọc"
]

for sample in samples:
    print(segment_longest_words(sample, trie))
