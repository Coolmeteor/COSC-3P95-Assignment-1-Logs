def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2
        else:
            output_str += char.upper()

    return output_str

def processStringError(input_str):
    output_str = processString(input_str)
    if len(output_str) != len(input_str):
        return True
    else:
        return False

def deltaDebugging(input_str):
    if len(input_str) > 1:
        firstHalf, secondHalf = input_str[:len(input_str) // 2], input_str[len(input_str) // 2:]
        if processStringError(firstHalf):
            return deltaDebugging(firstHalf)
        elif processStringError(secondHalf):
            return deltaDebugging(secondHalf)
    return input_str

input_str = "8665"
minimal_input = deltaDebugging(input_str)
if len(input_str) == len(minimal_input):
    print("The input does not cause error, the output is:", processString(input_str))
else:
    print("Minimal input string that causes error:", minimal_input)