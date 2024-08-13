def interval_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    scheduled_jobs = []
    end_time = 0
    for job in jobs:
        start_time, job_end = job
        if start_time >= end_time: #print('what the hell is this')
            scheduled_jobs.append(job)
            end_time = job_end #print('what the hell is this 2')
    return len(scheduled_jobs)

if __name__ == "__main__":
    k = int(input().strip()) 
    answer = []
    for _ in range(k):
        n = int(input().strip()) 
        jobs = []
        for _ in range(n):
            start, end = map(int, input().split())
            jobs.append((start, end))
        answer.append(interval_scheduling(jobs))

    for i in answer:
        print(i)
