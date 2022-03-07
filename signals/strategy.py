import numpy as np


def sum_func(sum_list):
  sum_list = np.array(sum_list)

  
  sum = np.sum(sum_list)
  return sum

def minus_list(minus_list):
  minus_list = np.array(minus_list)

  
  minus=0
  for i in range(len(minus_list)):
    if i == 0:
      minus = minus_list[i] - minus_list[i+1]
    elif i != len(minus_list)-1:
      minus -= minus_list[i+1]
  
  return minus

def multiple_list(multiple_list):
  multiple_list = np.array(multiple_list)


  multiple=0
  for i in range(len(multiple_list)):
    if i == 0:
      multiple = multiple_list[i] * multiple_list[i+1]
    elif i != len(multiple_list)-1:
      multiple *= multiple_list[i+1]

  return multiple


def devide_list(devide_list):
  devide_list = np.array(devide_list)

  devide=0
  for i in range(len(devide_list)):
    if i == 0 and devide_list[i]!= 0 and devide_list[i+1]!=0 :
      devide = devide_list[i] / devide_list[i+1]
    elif i != len(devide_list)-1 and  devide_list[i+1]!=0:
      devide /= devide_list[i+1]

  return devide


def if_result(condition_bool,result_true=None,result_false=None):
  if condition_bool == True:
    return result_true
  else:
    return result_false

def greater_than(a,b):
  a = np.array(a)
  b = np.array(b)
  result = (a>b)
  return result

def greater_than_equal(a,b):
  a = np.array(a)
  b = np.array(b)
  result = (a >= b)
  return result

def less_than(a,b):
  a = np.array(a)
  b = np.array(b)
  result = (a<b)
  return result

def less_than_equal(a,b):
  a = np.array(a)
  b = np.array(b)
  result = (a <= b)
  return result

def equal(a,b):
  a = np.array(a)
  b = np.array(b)
  result = (a==b)
  return result

def not_equal(a,b):
  a = np.array(a)
  b = np.array(b)
  result = (a!=b)
  return result

def and_logic_bitwise(a,b):
  result = np.logical_and(a,b)
  return result

def or_logic_bitwise(a,b):
  result = np.logical_or(a,b)
  return result

def not_logic(a):
  return not a.all()

def and_logic(a,b):
  result = a.all() and b.all()
  return result

def or_logic(a,b):
  result = a.all() or b.all()
  return result

def multiple_bitwise(a,b):
  return np.multiply(a,b)

def devide_bitwise(a,b):
  return np.divide(a,b)


def sum_bitwise(a,b):
  a=np.array(a)
  b=np.array(b)
  return a+b

def minus_bitwise(a,b):
  a=np.array(a)
  b=np.array(b)
  return a-b
