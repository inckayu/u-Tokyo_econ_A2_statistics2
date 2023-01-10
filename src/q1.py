import matplotlib.pyplot as plt
import numpy as np

def random_bio(n, p, size):
  """
  input
  n: 試行回数
  p: 確率
  size: 標本数

  output
  std: 二項分布bin(n, p)のsize個の標本平均を標準化した値
  """
  nums = np.random.binomial(n, p, size) / n # 二項分布から生成したsize個の確率変数(標本)
  sample_mean = sum(nums) / size # 標本平均
  std = (sample_mean - p) * ((n/(p*(1-p)))**0.5) # 標本平均を標準化
  return std

n = 10
p = 0.5
size = 10

sample_size = 1000

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = [12, 9]
plt.hist(
  [random_bio(n, p, size) for i in range(sample_size)],
  bins=30,
  )

plt.title(f"sample size: {sample_size}\ndistribution: bin({n}, {p})")
plt.savefig(f"images/sample size={sample_size}, distribution=bin({n}, {p}).png")
plt.show()
