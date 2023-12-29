# Take p, N, R as input from user
P = float(input('please input principle in INR:'))
N = float(input('please number of year:'))
R = float(input('please enter the rate of interest :'))
# Calculate simple intrest
I = P*N*R/100

# Calculate the total amount
A = P + I 

# Print above resuts
print(f'Simple Intrest : {I:.2f} INR')
print(f'Total amount is : {A:.2f} INR')

