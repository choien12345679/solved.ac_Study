# 2920_음계

m = list(map(int, input().split())) # 8개의 음계 숫자를 한 줄에 입력받아 m 리스트에 삽입한다.

ascending = [1, 2, 3, 4, 5, 6, 7, 8] # 오름차순일 경우 ascending인 리스트 생성 
# 추후 위 리스트와 입력값을 비교하여, ascending 리스트와 같은지 확인하기 위함
descending = [8, 7, 6, 5, 4, 3, 2, 1] # 내림차순일 경우 descending인 리스트 생성
# 추후 위 리스트와 입력값을 비교하여, descending 리스트와 같은지 확인하기 위함

if m == ascending: # 만약 m 리스트가 ascending 리스트와 같다면
    print("ascending") # ascending 출력
elif m == descending: # 만약 m 리스트가 descending 리스트와 같다면
    print("descending") # descending 출력
else: # 위 두 조건이 모두 아니라면
    print("mixed") # mixed 출력