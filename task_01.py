from trie import Trie
from typing import List


class Homework(Trie):
    """
    Rozszerzona klasa Trie, która dodaje metody wyszukiwania sufiksów oraz sprawdzania prefiksów.
    """
    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Zlicza liczbę słów, które kończą się na podany sufiks.
        """
        if not isinstance(pattern, str):
            raise ValueError("Wzorzec musi być łańcuchem znaków.")
        
        return sum(1 for key in self.keys() if key.endswith(pattern))

    def has_prefix(self, prefix: str) -> bool:
        """
        Sprawdza, czy w Trie jest co najmniej jedno słowo z podanym prefiksem.
        """
        if not isinstance(prefix, str):
            raise ValueError("Prefiks musi być łańcuchem znaków.")
        
        return bool(self.keys_with_prefix(prefix))


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    try:
        # Sprawdzenie liczby słów kończących się na dany sufiks
        assert trie.count_words_with_suffix("e") == 1   # apple
        assert trie.count_words_with_suffix("ion") == 1  # application
        assert trie.count_words_with_suffix("a") == 1   # banana
        assert trie.count_words_with_suffix("at") == 1  # cat

        # Sprawdzenie obecności prefiksu
        assert trie.has_prefix("app") is True   # apple, application
        assert trie.has_prefix("bat") is False
        assert trie.has_prefix("ban") is True   # banana
        assert trie.has_prefix("ca") is True    # cat
        
        print("Wszystkie testy zakończone sukcesem")
        
    except AssertionError:
        print("Niektóre testy nie powiodły się!")
