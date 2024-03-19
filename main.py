nric = input('Enter an NRIC number: ')

# Type your code below
valid = False
if len(nric) == 9 and nric[0].upper() in "STFG" and nric[1:8].isdigit() and  nric[8].isalpha():
  weight = 0 + int(nric[0].upper() in "TG") * 4
  digit_weight =  [2,7,6,5,4,3,2]
  for i in range (1,8):
    weight += int(nric[i]) * digit_weight[i-1]
  weight = weight % 11
  if nric[0].upper() in "ST":
    weight += 11
  check_chr = "XWUTRQPNMLKJZIHGFEDCBA"
  if nric[8].upper() == check_chr[weight]:
    valid = True
if valid: 
  print("NRIC is valid.")
else: 
 print("NRIC is invalid.")