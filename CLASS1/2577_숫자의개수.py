# 2577_숫자의개수
# 자연수 A, B, C가 주어진다.
# A * B * C 연산 결과에 0~9까지의 숫자가 몇번씩 쓰였는지 count한다.

Numbers_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
# 0~9까지의 숫자를 문자열로 리스트안에 넣어둔다.
# 향후 문자열과 비교하기 위하여 문자열로 저장한다.

n = [] # 자연수 A, B, C를 저장할 리스트를 생성한다.
for _ in range(3): # 3번 반복하여 n 리스트에 A, B, C의 값을 append한다.
    n.append(int(input())) # 자연수 A, B, C를 한줄에 한번씩 입력받아 append한다.

result = n[0] * n[1] * n[2] # A * B * C 연산 결과를 result 변수에 저장한다.
result_str = str(result) # result 변수를 문자열로 형변환하여 문자열로 만든다.

for i in Numbers_str: # 기존 만들어뒀던 Numbers_str 리스트의 요소들을 하나씩 반복한다.(0부터 9까지의 문자)
    count = result_str.count((i)) # count 변수에 result_str 문자열에서 i의 개수를 세어 count 변수에 저장한다.
    print(count) # count 변수의 값을 출력한다.