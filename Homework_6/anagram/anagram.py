def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if candidate.lower() != word.lower() and sorted(candidate.lower()) == sorted(word.lower()):
            anagrams.append(candidate)
    return anagrams


def test_find_anagrams():
    # Normal
    assert find_anagrams("education", ["auctioned", "cautioned", "educati"]) == ["auctioned", "cautioned"]
    assert find_anagrams("aeprs", ["apers", "apres", "asper", "pares", "parse", "pears", "prase", "presa", "reaps", "spare", "spear"]) == ["apers", "apres", "asper", "pares", "parse", "pears", "prase", "presa", "reaps", "spare", "spear"]

    # Bad (no candidates given, no word given)
    assert find_anagrams("dsafgasdgf", []) == []
    assert find_anagrams("", ["am i", "a valid", "option?"]) == []

    # Edge Cases (spaces, no possible anagrams, only option is the exact word)
    assert find_anagrams("the eyes", ["they see", "hello", "lol", "not this one"]) == ["they see"]
    assert find_anagrams("test", ["maybe this?", "lol", "not this one"]) == []
    assert find_anagrams("am i", ["am i", "a valid", "option?"]) == []


if __name__ == '__main__':
    test_find_anagrams()