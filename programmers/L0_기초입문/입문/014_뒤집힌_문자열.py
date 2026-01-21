# 뒤집힌 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 21. 11:16:02

def solution(my_string):
    my_list = list(my_string)
    my_list.reverse() # reverse() 함수는 리스트 객체 메서드
    answer = ''.join(my_list)
    return answer