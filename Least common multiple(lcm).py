numberLargest = int(input("Enter the largest number:"))
numberSmallest = int(input("Enter the smallest number:"))

# store original values for LCM calculation
num1 = numberLargest
num2 = numberSmallest

# find LCM
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

hcf = numberLargest

# formula for lcm
lcm = (num1 * num2) 

print("LCM is:", lcm)
