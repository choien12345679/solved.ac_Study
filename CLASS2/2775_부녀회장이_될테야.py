# 2775_부녀회장이_될테야

T = int(input()) # 테스트 케이스의 수 T를 입력받음

for _ in range(T): # 테스트 케이스 T 만큼 반복
    k = int(input()) # 층 k를 입력받음
    n = int(input()) # 호 n를 입력받음

    # 0층의 i호에는 i명이 살고 있음.
    # k층의 n호에는 k-1층의 1호부터 n호까지 사람들의 수의 합만큼 사람이 살고 있다.
    people = [i for i in range(1, n+1)] # 0층의 사람 수를 리스트로 초기화
    for floor in range(1, k+1): # 1층부터 k층까지 반복
        for house in range(1, n): # 1호부터 n-1호까지 반복
            people[house] += people[house - 1] # 현재 호수의 사람 수에 이전 호수의 사람 수를 더함
        # 누적합을 이용하여 k층의 사람 수를 계산
        # k층 n호 = (k-1층 n호) + (k층 n-1호)
    print(people[n - 1]) # k층의 n호에 사는 사람 수 출력

