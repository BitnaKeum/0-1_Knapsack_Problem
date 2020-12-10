import random
import math
import time
from matplotlib import pyplot as plt

def max(num1, num2):    # 더 큰 값 반환
    if num1 < num2:
        return num2
    else:
        return num1

# 0-1 Knapsack problem에 대한 optimal solution의 value를 계산
def Knapsack_01(value, weight, W):
    n = len(value)  # value 배열의 길이는 n

    # 배열 c의 0행과 0열의 값은 0, 그 외에는 값을 -1로 초기화
    c = [[-1 for col in range(W + 1)] for row in range(n + 1)]  # (n+1)x(W+1)
    for row in range(n + 1):
        c[row][0] = 0
    for col in range(W + 1):
        c[0][col] = 0

    for i in range(1, n+1):     # 1<=i<=n
        for w in range(1, W+1): # 1<=w<=W
            if weight[i-1] > w:
                c[i][w] = c[i-1][w] # 이전 행의 값을 가져옴 
            else:   # weight[i-1] <= w
                # i번째 item을 넣는 경우와 넣지 않는 경우 중 value가 더 큰 경우를 선택
                c[i][w] = max(value[i-1]+c[i-1][w-weight[i-1]], c[i-1][w])

    # 계산 완료된 c 배열 출력하기
    # for i in range(0, n+1):
    #     for j in range(0, W+1):
    #         print(c[i][j], end="\t")
    #     print()

    return c[i][w]  # 최종 value 반환


n = 5
value = []
weight = []
for idx in range(n):    # value 설정
    randNum = random.randint(1, 2 * n)  # 1 <= value <= 2n
    value.append(randNum)
for idx in range(n):    # weight 설정
    weight.append(idx+1)     # weight = i
W = math.floor(n*n/2)   # total weight of knapsack

print("value: ", value)
print("weight: ", weight)
print("W: ", W)

output = Knapsack_01(value, weight, W)  # optimal solution의 value값 계산

print("value of optimal solution: ", output)    # Knapsack_01() 함수를 통해 구한 optimal solution의 value 출력
