# 10989_수 정렬하기 3

# 문제 핵심
# 입력되는 수의 개수 N이 매우 큼 최대 10,000,000
# 숫자를 전부 리스트에 저장하면 메모리 초과 가능성이 높음
# 파이썬에서 int는 객체라서 1개당 메모리 사용량이 큼
# arr.apend() + arr.sort() 방식은 메모리 초과가 나타남

# 값을 저장하는 것이 아닌, 각 숫자가 몇 번 나왔는지에 대한 빈도를 저장함.
# count[x]는 x가 나온 횟수임
# 이후 1부터 10000까지 순서대로 count만큼 출력하면 자동으로 정렬된 결과가 된다.

import sys

input = sys.stdin.readline # input 함수를 sys.stdin.readline으로 변경하여 사용

N = int(input()) # 숫자의 개수를 입력받을 N
count = [0] * 10001 # count[i] = i라는 숫자가 등장한 횟수임

for _ in range(N): # 숫자를 저장하지 않고 등장횟수만 누적시킴.
    num = int(input())
    count[num] += 1

for i in range(10001): # 1부터 10000까지, 등장 횟수만큼 출력하면 오름차순 정렬과 동일함.
    for _ in range(count[i]):
        print(i) # 출력