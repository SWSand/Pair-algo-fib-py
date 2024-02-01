#create a function that outputs the 'n'th element of the fibonacci sequence starting with (0,1)
#fibonacci : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# 0+1 = 1


def fibonacci(n):
  answer = 0
  num1 = 0
  num2 = 1
  for i in range(n - 1) :
    answer = num1 + num2
    num1 = num2
    num2 = answer
  return answer

print(fibonacci(8))


