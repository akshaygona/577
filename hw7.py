def weighted_interval_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    dp = [0] * len(jobs)
    dp[0] = jobs[0][2]
    for i in range(1, len(jobs)):
        dp[i] = max(jobs[i][2], dp[i - 1])
        for j in range(i-1, -1, -1):
            if jobs[j][1] <= jobs[i][0]:
                dp[i] = max(dp[i], jobs[i][2] + dp[j])
                break
    print(dp[-1])


num_instances = int(input())
for _ in range(num_instances):
    n = int(input())
    instances = []
    for _ in range(n):
        instance = list(map(int, input().split()))
        instances.append(instance)
    weighted_interval_scheduling(instances)