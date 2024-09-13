import csv
import datetime
import atexit

# print ("Current date and time = %s" % e)
# print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
# print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second)) test

def readBarcode(code):
    found = False
    index = None
    with open("Student Barcodes.csv") as file:
        csv_reader = csv.reader(file)
        #print("started")
        for row in csv_reader:
            #print("in row")
            for val in row:
                #print("in val")
                if code in val:
                    found = True
                    index = val
    if (found):
        return index
    else:
        return "Not found"

"""
def endProgram(time):
    f = open("Cheesebread.txt", "a")
    f.write("\nDate:    ", time)
    f.close()
"""

if __name__ == "__main__":
    startDate = datetime.datetime.now()

    counter = 0
    # startUpTime = "%s/%s/%s" % (startDate.month, startDate.day, startDate.year)

    print("-------------------------------\n|     Library Appender        |\n-------------------------------\n")
    print("To enter a student's name manually, enter their credentials with \"LastName, FirstName\"")
    print("i.e.\"Domingo, Dylan\"\n")
    print("Enter \"!count\" to view the student count")
    print("Enter \"!exit\" to exit the program\n")

    while (True):
        currTime = datetime.datetime.now()
        # atexit.register(endProgram, ("%s/%s/%s" % (currTime.month, currTime.day, currTime.year)))
        id = input()
        name = readBarcode(id)
        

        if id == "!exit":
            break

        if id == "!count":
            print("Count: ", counter, "\n")

        if name == "Not found":
            if id !="!count":
                print("Not found, please try again.\n")
        else:
            counter += 1

            f = open("List.txt", "a")

            f.write("%s \t%s\t%s/%s/%s" % (counter, name, currTime.month, currTime.day, currTime.year))
            f.write("\t%s:%s:%s\n" % (currTime.hour, currTime.minute, currTime.second))
            f.close()

            f = open("List.txt", "r")
            print(f.read())
    quit()
        