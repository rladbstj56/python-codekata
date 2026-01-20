# 나머지 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120810
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 20. 11:06:29

def solution(num1, num2):
    try:
        return num1%num2
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")