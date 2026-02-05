# 2231_분해합

N = int(input()) # 자연수 N 입력 받음
# M 자체와 본인의 자릿수를 모두 더한 값이 N이 되는 값을 생성자라고 한다. 이를 구하는 문제

def d(n): # 분해합을 구하는 함수 d(n) 정의
    total = n # 먼저 n 자체를 더함
    for i in str(n): # n을 문자열로 변환하여 각 자리수를 하나씩 반복
        total += int(i) # 각 자리수를 정수형으로 변환하여 total에 더함
    return total # 최종적으로 total 반환

for i in range(1, N+1): # 1부터 N까지 반복
    if d(i) == N: # 만약 d(i)가 N과 같다면
        print(i) # i 출력
        break # 반복문 탈출
else: # 반복문이 정상적으로 종료되었을 때(즉, 분해합을 찾지 못했을 때)
    print(0) # 0 출력