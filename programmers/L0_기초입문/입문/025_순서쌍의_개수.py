# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 09. 09:57:26

def solution(n):
    cnt = 0
    for i in range(n): # 0~n-1
        if n%(i+1) == 0:
            cnt+=1
    return cnt