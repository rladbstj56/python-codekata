# 뒤집힌 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 21. 11:10:34

def solution(my_string):
    new = ''
    for c in my_string:
        new = c+new
    return new