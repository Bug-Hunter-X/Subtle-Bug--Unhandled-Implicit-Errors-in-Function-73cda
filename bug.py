def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a  # ZeroDivisionError, but not the focus
    elif a > 5:
        return a + b
    else:
        return a - b

result = function_with_uncommon_error(10, 5)
print(result) #This will execute fine

result = function_with_uncommon_error(2, 3)
print(result) #This will execute fine

result = function_with_uncommon_error(0, 5)
print(result) # This will raise ZeroDivisionError