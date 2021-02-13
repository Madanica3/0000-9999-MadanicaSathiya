single_digits = ["","One","Two","Three", "Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen", "Sixteen","Seventeen","Eighteen","Nineteen"];
two_digits = ["","Twenty","Thirthy","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"];
three_digits = ["","one hundred","two hundred", "three hundred", "four hundred","five hundred","six hundred", "sevevn hundred", "eight hundred","nine hundred"]
four_digits =["","one thousand","two thousand","three thousand","four thousand", "five thousand", "six thousand", "seven thousand","eight thousand","nine thousand", ]
n=int(input("ENTER THE NUMBER VALUE HERE:"))
if(n==0):
 print("zero")
elif(n<=19):
 print (single_digits[n])
elif(n<99):
  print(two_digits[n//10]+""+single_digits[n%10])
elif(n<=999):
  print(three_digits[n//100]+""+two_digits[(n%100)//10]+""+single_digits[n%10])
else:
  print(four_digits[n//1000]+""+three_digits[(n%1000)//100]+""+two_digits[((n%1000)//100)//10]+""+single_digits[n%10])



