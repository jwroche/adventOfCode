def parseIntCodes(intcodes):
    val = intcodes[0]
    i = 0
    max_val = len(intcodes)

    wrk_array = intcodes.copy()
    while val != 99:
        i1=wrk_array[wrk_array[i+1]]
        i2=wrk_array[wrk_array[i+2]]
        outp = wrk_array[i+3]
        if val == 1:
            wrk_array[outp] = i1 + i2
        elif val == 2:
            wrk_array[outp] = i1 * i2

        i += 4
        if i < max_val:
            val = wrk_array[i]
        else:
            val = 99
    
    return wrk_array

def main():
    file_name='Day2Input.txt'

    intcodes = []

    with open(file_name) as fp:
        intcodes = [int(x) for x in fp.read().split(',')]

    for i in range(0,99, 1):
        for j in range(0,99,1):

            intcodes[1]=i
            intcodes[2]=j

            final_codes = parseIntCodes(intcodes)

            if final_codes[0] == 19690720:
                print (f"Noun: {i}\nVerb: {j}")
                result = 100 * i + j
                print (f"100*N+V = {result}")

if __name__ == "__main__":
    main()