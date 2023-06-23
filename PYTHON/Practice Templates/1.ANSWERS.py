#-------------------

## 17

# We declared a variable N for you.
# Your task is to print all values from 0 to N (inclusive).

N = 11 # Write your answer below


#------------------------------------------------------------

# Print all numbers from 42 to 59 (inclusive):

for i in range(42,60):
    print(i)


#----------------------------------------------------------------------
# We declared a variable N for you.
# Your task is to print all values from 0 to N (inclusive).

N = 11 # Write your answer below

for i in range(N+1): # +1 to get upto 11
    print(i)

#---------------------------------------------------------------------------





#-------------------
#------------------

## 23


# Print all items of the list one per line.
lines = ["My candle burns at both ends;", "It will not last the night;", "But ah, my foes, and oh, my friends —", "It gives a lovely light."]

# Write your answer below
for i in lines:
    print(i)

#---------------------------------------------------------

# Increase by one each value contained in the values list.
# Make the new list
values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 10, 14, 17, 14, 1, 16, 19, 7, 9, 19] # Write your answer below

values = [i+1 for i in values]
print(values)

#------------------------------------------------------------

# Define a reversed_values variable whose values are the values in the values list, but in reversed order.
values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 17, 14, 1, 9]

# Write your answer below

reversed_values = []
for i in range(len(values)):
    reversed_values.append(values[len(values) - i - 1])

print(reversed_values)

#------------------------------------------------------------------

# What will be the value of values_copy after we execute the following code:
values = [5, 4, 7, 8, 9, 3]

values_copy = []
for v in values:
    values_copy.append(v)

# ANSWER:
[5, 4, 7, 8, 9, 3]


#----------------------------------------------------------------


