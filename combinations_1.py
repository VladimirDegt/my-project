from itertools import combinations
def est_subsets(arr):
    set_ = set(arr)
    res = []
    for i in range(1, len(set_)+1):
        result = list(combinations(set_, i))
        res.extend(result)
    return len(res)

'''
test.describe("Example Tests")
test.assert_equals(est_subsets([1, 2, 3, 4]), 15)
test.assert_equals(est_subsets(['a', 'b', 'c', 'd', 'd']), 15)

arr = [2, 3, 4, 5, 5, 6, 6, 7, 8, 8]
test.assert_equals(est_subsets(arr), 127)

arr = ['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b', 
'd', 'j', 'j', 'n', 'm', 'm']
test.assert_equals(est_subsets(arr), 511)
'''
'''
Given a set of elements (integers or string characters, characters only in RISC-V) that may occur more than once, we need to know the amount of subsets that none of their values have repetitions.

Let's see with an example:

set numbers = {1, 2, 3, 4}

The subsets are:

{{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4},{3,4}, {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}, {1,2,3,4}} (15 subsets, as you can see the empty set, {}, is not counted)
'''
