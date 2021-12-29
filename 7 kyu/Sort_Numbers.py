"""
7 kyu
Sort Numbers
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or
null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []

Fundamentals
"""

"""
def solution(nums):
    if nums is None:
        return []
    elif len(nums) > 0:
        return sorted(nums)
    else:
        return []
"""


# How this works
def main():
    print(solution([1, 2, 3, 10, 5]))
    print(solution(None))
    print(solution([]))


def solution(nums):
    if nums is None:
        return None
    elif len(nums) > 0:
        return sorted(nums)
    else:
        return []


if __name__ == "__main__":
    main()
