from __future__ import annotations
from typing import List

class Trie:
    def __init__(self) -> None:
        self.ch_arr: List[Trie | None] = [None] * 26
        self.end = False
    
    def add_word(self, word: str) -> None:
        p = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if p.ch_arr[idx] is None:
                p.ch_arr[idx] = Trie()
            p = p.ch_arr[idx]
        p.end = True
    
    def search_prefix(self, prefix: str) -> Trie | None:
        p = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if p.ch_arr[idx] is None:
                return None
            p = p.ch_arr[idx]
        
        return p
    
    def is_word(self, word: str) -> bool:
        
        return (p := self.search_prefix(word)) is not None and p.end
        


if __name__ == '__main__':
    import json
    
    trie = Trie()
    with open('../word_list/possible_guesses.json', 'r') as f:
        words = json.load(f)
        for w in words:
            trie.add_word(w)
    
    while True:
        s = input('Input one word:')
        print(trie.is_word(s))