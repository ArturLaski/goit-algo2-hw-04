from trie import Trie
from typing import List


class LongestCommonWord(Trie):
    """
    Klasa do znajdowania najdłuższego wspólnego prefiksu w zbiorze słów.
    """
    def find_longest_common_word(self, strings: List[str]) -> str:
        """
        Znajduje najdłuższy wspólny prefiks spośród wszystkich słów na liście.
        """
        if not strings:
            return ""

        for word in strings:
            self.insert(word)

        prefix = ""
        node = self.root
        while node:
            # Jeśli węzeł ma dokładnie jednego potomka i nie jest końcem słowa, kontynuujemy budowanie prefiksu
            if len(node.children) == 1 and not node.is_end_of_word:
                char = next(iter(node.children))  # Pobieramy jedynego potomka
                prefix += char
                node = node.children[char]
            else:
                break

        return prefix


if __name__ == "__main__":
    # Testy
    try:
        trie = LongestCommonWord()
        strings = ["flower", "flow", "flight"]
        assert trie.find_longest_common_word(strings) == "fl"

        trie = LongestCommonWord()
        strings = ["interspecies", "interstellar", "interstate"]
        assert trie.find_longest_common_word(strings) == "inters"

        trie = LongestCommonWord()
        strings = ["dog", "racecar", "car"]
        assert trie.find_longest_common_word(strings) == ""

        print("Wszystkie testy zakończone sukcesem")
        
    except AssertionError:
        print("Niektóre testy nie powiodły się!")
