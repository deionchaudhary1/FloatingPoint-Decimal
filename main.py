#take input
print("Type you 32-bit IEEE754 Floating Point Number: ")
x = input()

class floating_point:
  def __init__(self,inp):
    self.mant = inp[1:9]
    self.deci = "1"+ inp[9:33]
    self.sign = inp[0]

  def signs(self):
    bin = ""
    neg = "-"
    if self.sign == '1':
      bin=neg
    self.bini = bin
  #find negative or pos

  def mantissa(self):
    ex = 0
    conv = 128
    for i in range (0,7):
      #takes each value of the mantissa and multiplies it accordingly
      int_mant = int(self.mant[i])
      ex= ex + int_mant*conv
      conv = conv/2
    ex = ex-127
    self.exp = ex
  #print("Mantissa is: " + str(b))
  
  def decimal(self):
    global exponent
    global decimal
    global int_deci
    ec = self.exp
    exponent = 2**ec
    int_deci = 0
    if self.exp:
      for i in range (0, 23):
      #change each index of the string to a int, then multi
        int_bin = int(self.deci[i])
        int_deci = int_deci + (int_bin*exponent)
        exponent = exponent/2

    #make int_deci into a string
    final = self.bini + str(int_deci)
    print("Here is your number in decimal: " + final)

p1 = floating_point(x)
p1.signs()
p1.mantissa()
p1.decimal()