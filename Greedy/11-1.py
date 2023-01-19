n = int(input())
indicator = list(map(int, input().split()))
indicator.sort(reverse=True)
group = []

for i in indicator:
  group.append([])