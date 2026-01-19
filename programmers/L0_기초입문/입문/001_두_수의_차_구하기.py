# 두 수의 차 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120803
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 19. 11:29:38

def solution(num1, num2):
    if num1>50000 or num1<-50000 or num2>50000 or num2<-50000:
        raise ValueError("-50000~50000 사이의 값만 입력할 수 있습니다") 
    answer = num1 - num2
    return answer