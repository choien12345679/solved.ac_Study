# 1978_소수찾기

N = int(input()) # 테스트 케이스의 개수 입력
numbers = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받음
# 개수가 정해진게 아니기 때문에 리스트 형태로 입력받음

sosu = 0 # 소수의 개수를 저장할 변수 선언

for i in numbers: # 입력받은 수를 하나씩 반복하여 i에 넣음
    if i == 1:
        continue # 1은 소수가 아니므로 스킵
    for j in range(2, i): # 2부터 i전(i-1)까지 반복
        if i % j == 0: # 만약 i가 j로 나누어 떨어지면 소수가 아님
            break # 해당 for문 탈출
    else : # 아니라면, 소수일 가능성 있음. 
        sosu += 1 # 만약 j가 i-1까지 오고 나누어 떨어지지 않았다면 소수의 개수 1 증가 


print(sosu) # 소수의 개수 출력