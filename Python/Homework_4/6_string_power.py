str = input("Enter the string s: ")
k = int(input("Enter the integer k: "))

# remove leading and tailing whitespaces
str = str.strip()

if k < 0:
    # split the string into k equal parts and check their equality:
    # if equal, print one of them, else print "undefined".
    # if (k != -1) and the strig does not contain a repeating pattern, print "undefined"
    
    undef = True

    str_size = len(str)
    # check, if it is divisible by k
    if str_size % k != 0:
        undef = True
    else:
        chunk_size = abs(str_size // k)
        chunks = list(str[i:i+chunk_size] for i in range(0, str_size, chunk_size))
        print(chunks)
        for chunk in chunks:
            if chunk != chunks[0]:
                undef = True
            else:
                undef = False

    print(chunks[0] if undef == False else "undefined")
            
elif k > 0:
    # repeat the string k times
    print(f"{k * str}")
else:
    # when k == 0, return an empty string
    print("")