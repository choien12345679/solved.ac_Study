# 4153_직각삼각형

while True: # 테스트 케이스의 개수가 정해져있지 않기때문에 무한루프
    a, b, c = map(int, input().split()) # 각 변의 길이를 한줄에 입력받음
    if a == 0 and b == 0 and c == 0:
        break # 만약 세변의 길이가 모두 0인경우 반복문을 종료
    triangle = sorted([a, b, c]) # 입력받은 세 변의 길이를 오름차순으로 정렬하여 리스트에 저장
    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2: 
        # a**2 + b**2 == c**2 피타고라스 정리를 바탕으로 조건문 작성
        print("right") # 직각삼각형일 시 right 출력
    else :
        print("wrong") # 직각삼각형이 아닐 경우 wrong 출력