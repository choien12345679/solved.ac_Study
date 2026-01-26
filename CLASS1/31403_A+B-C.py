# 31403 A+B-C
# https://www.acmicpc.net/problem/31403

a = [] # 빈 리스트 a 선언

for i in range(3): # 3번 반복하여 리스트 a에 3개의 정수 입력
    a.append(int(input()))
    
print(a[0] + a[1] - a[2]) # 정수 연산 A + B - C 출력
print(int(str(a[0])+str(a[1]))-a[2]) 
# a[0]과 a[1]은 문자열로 변환하여 + 연산을 통해 이어붙인다.
# - 연산은 문자 연산이 불가 즉, 정수 연산이 필요하다.
#  str로 형변환하여 a+b를 수행한 후 다시 정수로 변환하여 - a[2] 연산을 수행한다.
