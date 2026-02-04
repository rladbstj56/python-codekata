# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 02. 04. 23:54:06

def solution(numbers):
    max_num = max(numbers)
    numbers.remove(max_num)
    max_num2 = max(numbers)
    return max_num * max_num2