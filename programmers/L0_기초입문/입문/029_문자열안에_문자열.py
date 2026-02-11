# 문자열안에 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 11. 09:15:50

def solution(str1, str2):
    answer = str1.split(str2)
    if len(answer) == 1:
        return 1
    else:
        return 2