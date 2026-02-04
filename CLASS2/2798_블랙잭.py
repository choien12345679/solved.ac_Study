#2798_블랙잭

N, M = map(int, input().split()) # 카드의 개수 N과 목표 숫자 M을 입력받는다
cards = list(map(int, input().split())) # 카드의 숫자들을 입력받을 리스트 cards를 선언한다
max_sum = 0 # M을 넘지 않은 카드의 합의 최댓값을 저장할 변수 max_sum 선언

# 풀이 알고리즘
# 1~3까지의 합을 M보다 작으면 max_sum에 저장, M과 같다면 max_sum에 저장 후 종료.
# 2~4까지의 합을 max_sum보다 크고 M보다 작으면 max_sum에 저장, M과 같다면 max_sum에 저장 후 종료.
# 위 과정 N-2까지 반복

for i in range(N): # 입력받은 카드의 개수 N만큼 반복
    for j in range(i+1, N):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k] # 카드 3장의 합을 계산
            if card_sum <= M and card_sum > max_sum: # 카드의 합이 M보다 작거나 같고, max_sum보다 크다면
                max_sum = card_sum # max_sum을 카드의 합 최댓값으로 갱신
            if max_sum == M:
                break # max_sum이 M과 같다면 반복문 종료

print(max_sum) # 최종적으로 max_sum 출력