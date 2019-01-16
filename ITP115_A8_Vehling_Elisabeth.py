"""
Elisabeth Vehling
A8
ITP 115, Fall 2018
vehling@usc.edu

Description: This program reads in a csv file of vehicle data from a year of the users choice, then searches through
the file for the minimum and maximum highway MPG. Then writes a list of the matching cars to a new file that the user specifies.



"""

#function readInFile: takes the year the user wants and reads in that csv file
#input: year from user input as int
#output: copy of the data read in
def readInFile(yearInput):
    if yearInput == 2008:
        file = open("epaVehicleData2008.csv", "r")
        file.readline()
        copy= []
        for line in file:
            line = line.strip()
#split each line along delimiter of "," to separate data
            line = line.split(",")
#append data of each line to a list to make it searchable by index
            copy.append(line)
    else:
        file = open("epaVehicleData2009.csv","r")
        file.readline()
        copy= []
        for line in file:
            line = line.strip().split(",")
            copy.append(line)
    file.close()
    return copy

#function calculations: finds MPG minimum and max on the data set the user chooses
#input: list reuturned from readInFIle
#output: two values, max and min from input year
def calculations(readInData):
    data=readInData
    max = 0
    min = 50
    for line in data:
#if the word "van" or "truck" appears in the first index position, pass over the line
        if "VAN" in line[0] or "TRUCK" in line[0]:
            pass
        else:
            calc = int(line[9])
#if the number in index position 9 (the MPG column) is greater than the max, set that as new max
            if calc > max:
                max = calc
            else:
                pass
# if the number in index position 9 (the MPG column) is less than the min, set that as new min
            if calc < min:
                min = calc
            else:
                pass
    return max, min

#function: carList: appends all car names matching the min and max values from calculations() to two lists
#input: min and max highway MPGs from calculations()
#output: two lists of car names, maxs and mins
def carList(datalist, maximum, minimum):
    maxList = []
    minList = []
    list = datalist
    max = maximum
    min = minimum
    for line in list:
        if "VAN" in line[0] or "TRUCK" in line[0]:
            pass
#^^if the word van or truck appears in the 0 index position of the line, pass
        else:
            if int(line[9]) == max:
#if index position 9 of this line equals the max, assign the line's 1 and 2 index positions to variable car
#these index positions are the make and model of the car
                car = line[1], line[2]
#append this information to the list of cars with maximum MPG
                maxList.append(car)
#same process for minimum
            elif int(line[9]) == min:
                car = line[1], line[2]
                minList.append(car)
            else:
                pass
    return maxList, minList

#function: wrtieNewFile: writes the data calculated above to file user wants
#input: file name from user, lists of max cars and min cars
#output: none
def writeNewFile(newFileName, maximumCars, minimumCars,max, min, year):
    file = open(newFileName, "w")

    print("MILEAGE DATA FOR", year, file=file)
#write information to file name user puts in
    print("\nThe cars with maximum MPG of", max ,"are:", file=file)
#join each string in the list of maximum cars with a space
    for line in maximumCars:
        print(" ".join(line), file=file)
    print("\nThe cars with minimum MPG of", min, "are:", file=file)
    for line in minimumCars:
        print(" ".join(line), file=file)
    file.close



def main():
    whatYear = input("What year would you like to see mileage data for? (2009/2008)?")
#error checking while loop
    while whatYear != "2009" and whatYear != "2008":
        print("Sorry, there's no data for that year.")
        whatYear = input("What year would you like to see data for? (2009/2008)?")
    whatYear = int(whatYear)
    newFile = input("Enter a file name to write your data to:")
#assign output of readInFileFunction to variable data
    data = readInFile(whatYear)
#assign output of calculations function to variable calculation
    calculation = (calculations(data))
#assign output of carList function to variable listOfCars
#for calculation arguments, used index position to reference the mins and maxs returned to the calculation variable
    listsOfCars = carList(data, calculation[0], calculation[1])
#call write new file function
#did the same thing as above and used index positions to reference the mins and max returns of each previous function
    writeNewFile(newFile,listsOfCars[0],listsOfCars[1], calculation[0], calculation[1],whatYear)
    print("Success! Mileage data has been written to", newFile)

main ()









