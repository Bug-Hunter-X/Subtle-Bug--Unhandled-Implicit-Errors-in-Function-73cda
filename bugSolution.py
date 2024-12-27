def function_with_uncommon_error_solution(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers.")
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    elif a > 5:
        return a + b
    else:
        return a - b

# Test cases
print(function_with_uncommon_error_solution(10, 5))  # Output: 15
print(function_with_uncommon_error_solution(2, 3))   # Output: -1
# This will now raise the exception:
try:
    print(function_with_uncommon_error_solution(0, 5))
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    print(function_with_uncommon_error_solution("abc", 5))
except TypeError as e:
    print(f"Error: {e}") #This will raise TypeError