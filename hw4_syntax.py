# contains_duplicate() function was copied over from a google doc.

# Answering this interview question:
#     Given a list of n numbers, determine if it contains any duplicate numbers.


def contains_duplicate(num_list):
    # Sort the given list
    dups = []
    num_list.sort()
    # Check each list item
    for i in range(1, len(num_list)):
        # Compare it against the previous list item to find any dups
        if num_list[i] == num_list[i-1]:
            # Any duplicates are added to a list
            dups.append(num_list[i-1])
    if len(dups) > 0:
        return dups
    return None


# Tests
if __name__ == '__main__':
    # No dups
    l1 = [3, 8, 6, 4, 1]
    print(f"contains_duplicate({l1}) => {contains_duplicate(l1)}")
    assert contains_duplicate(l1) == None

    # duplicates
    l2 = [3, 8, 6, 4, 1, 3, 6, 5, 2]
    print(f"contains_duplicate({l2}) => {contains_duplicate(l2)}")
    assert contains_duplicate(l2) == [3, 6]

    # Empty List
    l3 = []
    print(f"contains_duplicate({l3}) => {contains_duplicate(l3)}")
    assert contains_duplicate(l3) == None
