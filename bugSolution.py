def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return str(a) + str(b)

result = function(5, "hello")
print(result)

#Alternative solution using f-strings for string formatting:

def function_fstring(a, b):
    return f"{a}{b}"

result_fstring = function_fstring(5, "hello")
print(result_fstring)