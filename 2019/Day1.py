import math

def calcFuel(mass):
    val = mass
    final_fuel = 0

    while val > 0:
        val = math.floor(val/3.0)-2
        if val > 0:
            final_fuel += val
    
    return final_fuel
        

def main():
    file_name='Day1Input.txt'

    module_masses=[]

    # Save off the masses
    with open(file_name) as fp:
        for line in fp:
            module_masses.append(int(line))

    fuel_needed = 0

    for mass in module_masses:
        fuel_needed += calcFuel(mass)

    print(f"Fuel Needed: {fuel_needed}")

if __name__ == "__main__":
    main()