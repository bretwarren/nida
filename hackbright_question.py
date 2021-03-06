# Write a function that takes a list of integers as an argument. The function should return T/F depending on whether the list, representing characters in a
# numeric passphrase (aka list of numbers),is valid.

# A passphrase is valid if:
# - All numbers are smaller than the first number AND
# - The length of the passphrase is at least 5 numbers long

# Here are some valid passphrases:
# [8, 3, 2, 4, 5]
# [5, 2, 1, 2, 3]
# [11, 4, 10, 2, 3, 4]

# Here are some invalid passphrases:
# [5, 3, 2, 4, 5]     Not all numbers less than first
# [11, 4, 10, 2,]     Not long enough

passphrase = [11, 4, 10, 2]

def passphraseTester(testPassphrase):
    if len(testPassphrase) < 5: # only need to check once
        return False; # return immediately if fail
    listCopy = list(testPassphrase); # copy list so you don't change the passed list
    firstItem = listCopy.pop(0); # remove first item from list copy and save it for reference
    for i in listCopy:
        if i >= firstItem: # check for fail, not pass
            return False # return immediately if fail
    return True # got here, everything passed!

print(passphraseTester(passphrase))
