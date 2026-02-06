# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 06. 14:13:39

def solution(s1, s2):
    cnt = 0
    for s in s2:
        for a in s1:
            if s == a:
                cnt += 1
    return cnt
        