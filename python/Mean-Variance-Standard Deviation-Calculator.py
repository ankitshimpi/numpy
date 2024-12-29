import numpy as np
def calculate(data):
  if len(data) != 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.reshape(data, (3, 3))
  statistics = {
      'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.flatten().mean()],
      'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.flatten().var()],
      'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.flatten().std()],
      'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.flatten().max()],
      'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.flatten().min()],
      'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.flatten().sum()]
  }
  for key, value in statistics.items():
    for i in range(len(value)):
      value[i] = value[i].tolist()
  return statistics
