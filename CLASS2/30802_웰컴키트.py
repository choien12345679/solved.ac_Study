# 30802_웰컴키트

N = int(input()) # 테스트 케이스의 개수 입력 받음
Size = list(map(int, input().split())) # 각 사이즈별 신청자 수를 공백으로 구분하여 입력
if N != sum(Size):
    print("ERROR") # 만약 입력받은 참가자의 수와 티셔츠 사이즈별 신청자의 수의 합이 다를 경우 에러 출력
T, P = map(int, input().split()) # 티셔츠와 펜의 묶음, T, P를 입력받는다

t_shirt = 0 # 티셔츠의 묶음 개수를 저장할 변수 선언
for i in Size: # 사이즈별 신청자 수를 하나씩 입력하여 반복
    if i % T == 0:
        t_shirt += i // T # 나누어 떨어지면 몫을 더한다.
    else:
        t_shirt += (i // T) + 1 # 나누어 떨어지지 않으면 몫에 1을 더하여 더한다.

pen = N // P # 펜의 묶음 개수를 N // P로 몫을 저장

print(t_shirt) # 티셔츠 묶음 개수 출력
print(pen, N % P) # 펜 묶음 개수와 나머지 출력