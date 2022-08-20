# SWEA 1216
# 이차원 배열

for t in range(10):
    tc = int(input()) # 테스트 케이스 입력
    arr = [list(input()) for _ in range(100)] # 행렬입력
    trans_arr = list(zip(*arr))               # 수직방향 탐색 위한 전치행렬
    breker = True      # while 문 중단을 위한 breaker
    breker2 = True
    word_len, trans_len = 100, 100   # 길이가 큰 회문부터 검증
    while word_len > 1 and breker:
        for i in range(100):
            for j in range(100-word_len+1):
                if arr[i][j:j+word_len] == arr[i][j:j+word_len][::-1]:
                    breker = False              # 만약 회문이면 반복문을 종료하고 나온다.
                    break
        word_len -= 1            # 반복문을 종료할 때 한번 실행됨
    while trans_len > 1 and breker2:
        for i in range(100):
            for j in range(100-trans_len+1):
                if trans_arr[i][j:j+trans_len] == trans_arr[i][j:j+trans_len][::-1]:
                    breker2 = False       # 위와 동일
                    break
        trans_len -= 1
    print(f"#{tc} {trans_len+1 if trans_len>word_len else word_len+1}")   # 반복문 실행으로 인해 각 값에 1 더한 값으로 비교


