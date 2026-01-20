# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 김윤서
# 작성일: 2026. 01. 20. 12:04:46

def solution(angle):
    if 0< angle < 90:
        return 1
    elif angle == 90: 
        return 2
    elif angle < 180: 
        return 3
    elif angle == 180:
        return 4
    else:
        raise ValueError("0 < x <= 180 범위 내로만 입력 가능합니다.")