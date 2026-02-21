# 1181_단어 정렬

# 문제 핵심
# 단어의 개수 N을 입력받고 N번의 반복을 통해 단어를 입력받는다.
# 1. 단어의 길이가 짧은 것부터 길이가 같으면 사전 순으로 정렬한다.
# 2. 중복된 단어는 하나만 남기고 제거한다.

N = int(input()) # 단어의 개수를 입력받을 변수 N 선언

words = set() # 단어의 중복을 제거하기 위해 set 자료형을 선언한다. set은 중복을 허용하지 않는다.

for _ in range(N): # N번 반복하여 단어를 입력받는다.
    word = input() # 단어를 입력받는다.
    words.add(word) # 입력받은 단어 word를 set 자료형인 words에 추가하여 중복을 방지한다.
    # 단어를 정렬하는데, 단어는 길이가 짧고, 길이가 같다면 사전 순서이다.

sorted_words = sorted(words, key = lambda x: (len(x), x)) # sorted 함수를 사용하여 words를 정렬한다.
# key 매개변수에 lambda 함수를 사용하여 정렬 기준을 설정한다. 
# 먼저 단어의 길이(len(x))로 정렬하고, 길이가 같다면 사전 순서(x)로 정렬한다.

for word in sorted_words: # 정렬된 단어들을 하나씩 출력한다.
    print(word) # 단어를 출력한다.
