# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 15. 00:54:13

def solution(n):
    answer = 0
    a, b = divmod(n, 10)
    while a != 0:
        answer += b
        n = int(n/10)
        a, b = divmod(n, 10)
    answer += b
    return answer