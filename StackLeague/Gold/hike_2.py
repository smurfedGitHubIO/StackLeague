def hike(data):
  ans = 0
  cur = 0
  for i in data:
    if i == '+':
        cur += 1
    else:
        cur -= 1
    if cur == 0 and i == '+':
        ans += 1
  return ans