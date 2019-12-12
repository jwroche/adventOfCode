def parseIntCodes(intcodes):
    val = intcodes[0]
    i = 0
    while val != 99:
        i1=intcodes[intcodes[i+1]]
        i2=intcodes[intcodes[i+2]]
        outp = intcodes[i+3]
        if val == 1:
            intcodes[outp] = i1 + i2
        elif val == 2:
            intcodes[outp] = i1 * i2

        i += 4
        val = intcodes[i]
    
    return intcodes

def main():
    file_name='Day2Input.txt'

    intcodes = []

    with open(file_name) as fp:
        intcodes = [int(x) for x in fp.read().split(',')]

    intcodes[1]=12
    intcodes[2]=2

    final_codes = parseIntCodes(intcodes)
    
    print(f"First Value: {final_codes[0]}")

if __name__ == "__main__":
    main()