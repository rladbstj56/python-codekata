# 배열 원소의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 10. 09:20:50

def solution(strlist):
    answer = list(map(len, strlist))
    return answer