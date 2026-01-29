# 8958_OX퀴즈

n = int(input()) # 테스트 케이스의 개수 입력
for _ in range(n): # 테스트 케이스의 개수만큼 반복
    score = 0 # 점수를 저장할 변수 score 선언
    O_range = 0 # 연속된 O의 개수를 저장할 변수 O_range 선언
    OX_List = list(input()) # OX퀴즈의 결과를 한줄에 문자열로 입력받아 리스트로 변환하여 저장
    for i in OX_List: # OX_List의 요소들을 하나씩 입력하여 반복
        if i == 'O': # 만약 O일 경우
            O_range += 1 # 연속된 O의 개수를 저장할 변수에 1을 더하고
            score += O_range # 점수를 저장할 변수인 score에 O_range를 더한다.
        else: # 만약 O가 아닌 X일 경우
            O_range = 0 # 연속된 O의 개수를 0으로 초기화한다.
    print(score) # 각 테스트의 결과를 출력