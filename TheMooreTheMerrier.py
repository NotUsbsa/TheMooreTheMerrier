# Beginning
print("Project one (01) - Part C: The Moore the Merrier")

# User Input
number_of_transistors = int(input("Starting Number of transistors: "))
starting_year = int(input("Starting Year: "))
total_years = int(input("Total number of Years: "))

# Flops
flops = 50
# starting year plus total year is the ending year
ending_year = starting_year + total_years


# Length of Number Function returns lengths
def lengthOfNum(num):
    return len(str(num))


# Unit Conversion Function
def unitConverter(num):
    thousands = 1000

    # temporary list which takes in the conversion of the inputed number
    temp = []

    # units
    SI_units = {"FLOPS": 1, "kiloFLOPS": 1000, "megaFLOPS": thousands**2,
                "gigaFLOPS": thousands**3, "teraFLOPS": thousands**4, "petaFLOPS": thousands**5, "exaFLOPS": thousands**6, "zettaFLOPS": thousands**7, "yottaFLOPS": thousands**8}

    # iterate through each unit
    for y in SI_units:
        if lengthOfNum(num) >= lengthOfNum(SI_units[y]):
            conversions = num / SI_units[y]
            temp.append(conversions)

    # gets the largest converted number which is always last
    converted = list(temp)[-1]
    # picks the largest unit based on the length of the list
    unit = list(SI_units)[len(temp) - 1]
    return '{:.2f} {}'.format(converted, unit)


# Displays the top part of the table
print("\nYEAR : TRANSISTORS : FLOPS:")
for x in range(starting_year, ending_year + 1, 2):
    # calculate total computing power
    totalFlops = flops * number_of_transistors

    print(f'{x} {number_of_transistors:,} {unitConverter(totalFlops)} {totalFlops:,}')
    # doubles # of transistors after each iteration
    number_of_transistors = number_of_transistors * 2


# Ending
print("\nEND: Project One (01) - Part C")
print("Jeffrey Yu jyu867 251354066")
