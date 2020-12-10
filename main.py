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


n_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]    # number of input
actual_running_time = [0 for num in range(len(n_array))]  # actual running time

for iter, n in enumerate(n_array):

    n_running_time_sum = 0.0    # 한 n값에 대해 10번 새로 수행하는 데에 걸린 시간을 더함
    for n_iter in range(10):    # 하나의 n당 10번씩 실행 (running time의 평균을 내기위함)
        value = []
        weight = []
        for idx in range(n):    # value 설정
            randNum = random.randint(1, 2 * n)  # 1 <= vi <= 2n
            value.append(randNum)
        for idx in range(n):    # weight 설정
            weight.append(idx+1)     # wi = i
        W = math.floor(n*n/2)   # total weight of knapsack

        # print("value(vi): ", value)
        # print("weight(wi): ", weight)
        # print("W: ", W)

        start = time.time()     # 시작 시간
        output = Knapsack_01(value, weight, W)  # optimal solution의 value값 계산
        end = time.time()-start # 실행 시간 = 종료 시간 - 시작 시간

        n_running_time_sum += end   # 한 n에서의 수행 시간을 더함

        print("value of optimal solution: ", output)    # Knapsack_01() 함수를 통해 구한 optimal solution의 value 출력

    actual_running_time[iter] = n_running_time_sum/10   # 한 n에서의 수행 시간의 평균을 저장


# average actual running time 출력
# for iter, n in enumerate(n_array):
#     print("n = ", n, ", actual running time : ", actual_running_time[iter])



# Plot

plt.plot(n_array, actual_running_time, marker='o', color='b')
plt.title('Value of optimal solution')
plt.xlabel('n')
plt.ylabel('running time')
plt.xticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) # x축 단위 설정

plt.show()

