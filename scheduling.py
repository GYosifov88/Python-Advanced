jobs = [int(x) for x in input().split(', ')]

idx = int(input())

clock_cycles = 0
searched_job = int(jobs[idx])
jobs.remove(searched_job)
result = [element for element in jobs if element <= searched_job]
clock_cycles += searched_job + sum(result)

print(clock_cycles)
