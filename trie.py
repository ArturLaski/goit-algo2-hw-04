from typing import Dict, List, Optional, Callable
import functools

class TrieNode:
    """
    Węzeł dla drzewa prefiksowego (Trie).
    """
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.value: Optional[str] = None
        self.is_end_of_word: bool = False


def validate_key(func: Callable) -> Callable:
    """
    Dekorator do sprawdzania poprawności wprowadzonego klucza.
    """
    @functools.wraps(func)
    def wrapper(self, key: str, *args, **kwargs):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument: key = {key} musi być niepustym łańcuchem znaków")
        return func(self, key, *args, **kwargs)
    return wrapper


class Trie:
    """
    Implementacja drzewa prefiksowego (Trie).
    """
    def __init__(self):
        self.root: TrieNode = TrieNode()
        self.size: int = 0

    @validate_key
    def put(self, key: str, value: Optional[str] = None) -> None:
        """
        Dodaje parę klucz-wartość do Trie.
        """
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    @validate_key
    def get(self, key: str) -> Optional[str]:
        """
        Zwraca wartość dla danego klucza lub None, jeśli klucz nie istnieje w Trie.
        """
        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    @validate_key
    def delete(self, key: str) -> bool:
        """
        Usuwa klucz z Trie. Zwraca True, jeśli klucz został usunięty, lub False, jeśli nie istnieje.
        """
        def _delete(node: TrieNode, key: str, depth: int) -> bool:
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -= 1
                    return len(node.children) == 0
                return False

            char = key[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], key, depth + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0 and node.value is None
            return False

        return _delete(self.root, key, 0)

    def is_empty(self) -> bool:
        """
        Sprawdza, czy Trie jest puste.
        """
        return self.size == 0

    @validate_key
    def longest_prefix_of(self, s: str) -> str:
        """
        Znajduje najdłuższy prefiks spośród kluczy w Trie, który pasuje do podanego ciągu.
        """
        current = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in s:
            if char in current.children:
                current = current.children[char]
                current_prefix += char
                if current.value is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix

    @validate_key
    def keys_with_prefix(self, prefix: str) -> List[str]:
        """
        Zwraca listę wszystkich kluczy rozpoczynających się od zadanego prefiksu.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result: List[str] = []
        self._collect(current, list(prefix), result)
        return result

    def _collect(self, node: TrieNode, path: List[str], result: List[str]) -> None:
        """
        Rekurencyjnie zbiera wszystkie klucze z Trie.
        """
        if node.value is not None:
            result.append("".join(path))
        for char, next_node in node.children.items():
            path.append(char)
            self._collect(next_node, path, result)
            path.pop()

    def keys(self) -> List[str]:
        """
        Zwraca listę wszystkich kluczy w Trie.
        """
        result: List[str] = []
        self._collect(self.root, [], result)
        return result

    @validate_key
    def insert(self, word: str) -> None:
        """
        Wstawia słowo do Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
