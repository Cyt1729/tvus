def find_max_k(Q, queries):
    # 初始化K的区间范围为全体整数区间
    left = -float('inf')
    right = float('inf')

    # 遍历每个提示更新区间
    for M, D in queries:
        current_left = M - D
        current_right = M + D

        # 更新K的取值区间
        left = max(left, current_left)
        right = min(right, current_right)

        # 如果区间无效，返回-1
        if left > right:
            return -1

    # 如果最终有解，返回最大值
    return right


# 读取输入
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 输出结果
result = find_max_k(Q, queries)
print(result)
