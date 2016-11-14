# Author: Partha Pratim Neog
# Email: thisisppn@gmail.com
# Usage: Initialize the value of the variable num with the output of the hash(the_string)
# Output: The output should be the required string.
ref = "acdegilmnoprstuw";
num = 680131659347
final = []

def decrypt(num):
    for i in range(0,16):
        test = num - i
        mod = test%37
        if mod == 0:
            final.append(ref[i])
            break
    if test < 37:
        return 1

    decrypt(test/37)

decrypt(num)
reversedOut = "".join(final)[::-1]
print(reversedOut[1:])