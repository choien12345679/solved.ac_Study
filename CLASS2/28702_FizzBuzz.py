#28702 FizzBuzz

# [문제 핵심]
# - FizzBuzz 수열의 연속된 3개 값이 (각각 i, i+1, i+2번째) 3줄로 주어진다.
# - 이때 다음 값(즉 i+3번째 값)을 한 줄로 출력하는 문제다.
# - 주어진 3개 중 최소 1개는 숫자(정수 문자열)로 주어지므로,
#   그 숫자가 수열의 몇 번째 값인지 역추적해서 다음 숫자(target)를 구한 뒤,
#   target에 FizzBuzz 규칙을 적용해 출력하면 된다.

a = input().strip()  # 첫 번째 줄 입력(수열의 i번째 값)
b = input().strip()  # 두 번째 줄 입력(수열의 i+1번째 값)
c = input().strip()  # 세 번째 줄 입력(수열의 i+2번째 값)

start = None  # i(첫 번째 입력 a가 몇 번째 수인지)를 저장할 변수

if a.isdigit():              # 첫 줄이 숫자라면 (a == i)
    start = int(a)           # i = a
elif b.isdigit():            # 둘째 줄이 숫자라면 (b == i+1)
    start = int(b) - 1       # i = b - 1
else:                        # 셋째 줄이 숫자라면 (c == i+2) (문제 특성상 여기서도 숫자가 나옴)
    start = int(c) - 2       # i = c - 2

target = start + 3  # 우리가 구해야 할 값은 i+3번째 수이므로 target = i + 3

if target % 15 == 0:         # 3과 5의 공배수(15)면 "FizzBuzz"
    print("FizzBuzz")        # 결과 출력
elif target % 3 == 0:        # 3의 배수면 "Fizz"
    print("Fizz")            # 결과 출력
elif target % 5 == 0:        # 5의 배수면 "Buzz"
    print("Buzz")            # 결과 출력
else:                        # 그 외는 숫자 그대로 출력
    print(target)            # 결과 출력