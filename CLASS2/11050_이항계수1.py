# 11050_이항 계수 1

# 문제 핵심
# 이항 계수는 n! / (k! * (n-k)!)
# n과 k가 최대 10이므로, 팩토리얼 계산이 간단하다.

def factorial(num): # 팩토리얼 계산 함수
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

n, k = map(int, input().split()) # n과 k를 입력받음
result = factorial(n) // (factorial(k) * factorial(n - k)) # 이항 계수 계산
print(result) # 결과 출력