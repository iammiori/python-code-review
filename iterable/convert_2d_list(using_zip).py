import sys

def solution(mylist):
    new_list = list(map(list, zip(*mylist)))
    #print(list(zip(*mylist)))
    return new_list

input = [[1,2,3],[4,5,6],[7,8,9]]
output = solution(input)
print(output)