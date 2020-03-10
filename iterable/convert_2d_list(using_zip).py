import sys

def solution(mylist):
    new_list = list(map(list, zip(*mylist)))
    #print(list(zip(*mylist)))
    return new_list

input = [[1,2,3],[4,5,6],[7,8,9]]
output = solution(input)
print(output)

# zip을 쓰지 않았다면 이중for문으로 값을 받아왔을것 같다.
# 흔히 tranpose할때 유용할것 같다

#---추가---
# list comprehension과 map 함수를 비교해 봐야 겠다
