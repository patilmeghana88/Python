# numbers = [1,2,3,4,5,6,98,999,91,89,95]

# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")



number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number:
    print("The number is negative.")
else:
    print("The number is zero.")
if number > 0:
    for i in range (1,number +1):
        print(i)
