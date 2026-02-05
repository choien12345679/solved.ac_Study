# 15829_Hashing

L = int(input()) # 문자열의 길이를 입력받을 변수 L 선언
hash_string = str(input()) # 해시값을 구할 문자열을 입력받을 hash_string 선언

hash_value = 0 # 해시값을 저장할 변수 hash_value 선언

for i in range(L): # 문자열의 길이만큼 반복
    hash_value += (ord(hash_string[i]) - 96) * (31 ** i) 
    # ord 함수를 통해 문자를 아스키/유니코드 정수로 변환 후 -96을 하여 a = 1, b = 2, ... z = 26 형식으로 변환하고
    # 31의 i 제곱을 곱하여 문자열 ab와 ba를 다르게 만들고, 그 값을 hash_value에 누적 합산
print(hash_value % 1234567891)
# 마지막에 큰 수가 될 수 있어 MOD 연산을 통해 1234567891로 나눈 나머지를 출력