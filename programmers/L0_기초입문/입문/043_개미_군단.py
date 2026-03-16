# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 03. 16. 11:20:43

def solution(hp):
    rest = hp
    jang, rest = divmod(rest,5)
    byung, rest = divmod(rest,3)
    il, rest = divmod(rest,1)
    return jang + byung + il