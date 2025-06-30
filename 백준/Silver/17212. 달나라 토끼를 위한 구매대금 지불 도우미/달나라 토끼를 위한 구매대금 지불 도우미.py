N = int(input())
coins = [1, 2, 5, 7]
INF = int(1e9)

dp = [INF] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)
#점화식 dp[i] = min(dp[i - coin] + 1 for coin in [1, 2, 5, 7] if i - coin >= 0)

print(dp[N])

