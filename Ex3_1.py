def collatz_cojecture(number1):

  step = []
  while number1 != 1:
      if number1 % 2 == 0:
        number1 = number1/2
        step.append(number1)
      else:
          number1 = number1 * 3 + 1
          step.append(number1)
  return len(step)

x = int(input("please enter your number : "))
print(collatz_cojecture(x))