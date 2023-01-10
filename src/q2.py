import numpy as np

n = 100
u = 5
v = 25
s = v**0.5
edge = 1.96
size = 10000

count = 0

# 乱数生成
random_std = np.random.normal(
  loc=u,
  scale=s/(n**0.5),
  size=size,
  )

for i in range(len(random_std)):
  random = random_std[i]

  # 式１が成立した回数をcountに記録
  if u >= random - ((v/n)**0.5)*edge and u <= random + ((v/n)**0.5)*edge:
    count += 1

print(count)
