# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd). (problem here per DK???????)
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).


"""

"cant use .count per dk ???????????" ------ only works for one number!!!!!!!!

def solution(my_list):

    for num in my_list:

        if my_list.count(num) % 2 == 1:
            return num

      

print(solution([1,2,2,3,3,3,4,3,3,3,2,2,1]))

"""


def solution(my_list):
    my_dict = {}

    for num in my_list:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += 1

    for num in my_dict:
        if my_dict[num] % 2 == 1:
            return num

my_list = [0,1,0,1,0]


print(solution(my_list))
