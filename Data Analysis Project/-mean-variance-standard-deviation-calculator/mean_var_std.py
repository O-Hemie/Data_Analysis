import numpy as np


def calculate(input_list):
  if len(input_list) != 9:
    raise ValueError("List must contain nine numbers")

  data = np.array(input_list).reshape((3, 3))

  mean = [
      data.mean(axis=0).tolist(),
      data.mean(axis=1).tolist(),
      np.mean(data).tolist()
  ]

  variance = [
      data.var(axis=0).tolist(),
      data.var(axis=1).tolist(),
      np.var(data).tolist()
  ]

  std_dev = [
      data.std(axis=0).tolist(),
      data.std(axis=1).tolist(),
      np.std(data).tolist()
  ]

  max = [
      data.max(axis=0).tolist(),
      data.max(axis=1).tolist(),
      np.max(data).tolist()
  ]

  min = [
      data.min(axis=0).tolist(),
      data.min(axis=1).tolist(),
      np.min(data).tolist()
  ]

  sum = [
      data.sum(axis=0).tolist(),
      data.sum(axis=1).tolist(),
      np.sum(data).tolist()
  ]
  return {
      'mean': mean,
      'variance': variance,
      'std_dev': std_dev,
      'max': max,
      'min': min,
      'sum': sum
  }
