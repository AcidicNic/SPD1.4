import string


def is_pangram(sentence):
    sentence = sentence.lower()
    for char in string.ascii_lowercase:
        if char not in sentence:
            return False
    return True


def test_is_pangram():
    # Normal
    assert is_pangram("Pack my box with five dozen liquor jugs")
    assert is_pangram("A wizard's job is to vex chumps quickly in fog")
    assert not is_pangram("Oh, no! This isn't a pangram! :'( How sad.")

    # Bad (empty, no letters)
    assert not is_pangram("")
    assert not is_pangram("*#&$^)@&^)$&*!$*&%#!@)$#!&*")

    # Edge Cases (alternating case, screaming, no spaces/lowercase)
    assert is_pangram("tHe qUiCk bRoWn fOx jUmPs oVeR A LaZy dOg")
    assert is_pangram("THE QUICK BROWN FOX JUMPS OVER A LAZY DOG")
    assert is_pangram("abcdefghijklmnopqrstuvwxyz")


if __name__ == '__main__':
    test_is_pangram()
