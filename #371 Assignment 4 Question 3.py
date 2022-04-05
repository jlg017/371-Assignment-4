#371 Assignment 4 Question 3
#TODO:
#Read routing table from file forwardTableTest1.txt
    ##Format Requirements
    ## No column titles will be used in the file 
    ## Each line of data in the input file will contain the information in one row of the routing table. 
    ## Values within each line of the file will be separated by single tabs. 
    ## Values within each line of the file will be in the same order as the corresponding row of the table below

# Convert all input addr in routing table to binary

#For each pkt to forward:
    # read IP dest of pkt to fwd
    # convert IP dest to binary
    # implement fwding algorithm -> calculations done in binary
    # include use of metric
    # print(The destination IP address is <IP address in x.x.x.x format> )
    # print(The next hop IP address is <IP address in x.x.x.x format> )
    # print(The port the packet will leave through is <int port #>)


#Convert Address to Binary String Method | April 4
def addressToBinaryString(addr):
    addr = addr.split(".")
    addrBinArr = []
    for num in addr:
        num = int(num)
        numBin = binaryConvert(num)
        addrBinArr.append(numBin)
    #print("Address in Binary ")
    #print(addrBinArr)
    addrBinStr = ''.join(addrBinArr)    
    #print("complete Address in Binary ")
    #print(addrBinStr)
    return addrBinStr

def printRTable(rTable):
    print("[")
    for row in rTable:
        print("\t{},".format(str(row)))
    print("]")

#Convert to Binary Method - May need to tweak | April 3rd
#converts a given decimal number to binary
#returns string, need to manipulate return value to represent binary
def binaryConvert (deciNum):
    binaryNum = ""
    convertedNum = bin(deciNum).replace("0b","")

    #Fills in 0s if num is not 8 bits
    if(len(convertedNum)!=8):
        zeros = ""
        for i in range(8-len(convertedNum)):
            zeros+="0"
        binaryNum = zeros+convertedNum
    else:
        binaryNum = convertedNum

    return binaryNum

## Date modified: April 3rd, 2022 8PM
## MAIN - while loop for processing addresses

##Variables
finished = False

##Loop
while (finished != True):
    ##1. get information for forwarding table file-----------------------------------------------------------
    print("1. Getting information from user ...")
    destIP = input("Enter the IP address for your packet destination:\n")
    #created file with test routing table information | Apr 4th
    #table = input("Enter the file name for your forwarding table:\n")
    #TODO: change below to take in table (before submission)
    fTable = open('forwardTableTest1.txt', 'r')
    rFileLines = []
    rFileLines = fTable.readlines()

    ##2. Print Routing Table (Sorted) to screen-----------------------------------------------------------
    print("2. Routing Table (Sorted) ")
    # Order routing table by mask length: longest -> shortest
    rFileLines.sort(reverse=True, key = lambda x: x[2])
    
    rTableRows = []
    
    for line in rFileLines:
        #splits line into list of entries separated by tab
        rTableRow = line.split("\t")
        rTableRows.append(rTableRow)
        #print("each table entry:")
        #print(rTableRow)

    #print("rTableEntries:")
    printRTable(rTableRows)

    ##3. Convert Addresses to Binary 8-bits-----------------------------------------------------------
    #use lists???
    print("3. Converting addresses to binary 8-bits ... ")
    
    rTableBin = []
    for row in rTableRows:
        #convert addresses to binary
        rowBin = []
        for i in range(0, len(row)):
            if i == 0: # Destination address 
                destAddrBin = addressToBinaryString(row[i])
                rowBin.append(destAddrBin)
            elif i == 1: # Gateway address
                if row[i] == '*':
                    rowBin.append('*')
                else:
                    gateAddrBin = addressToBinaryString(row[i])
                    rowBin.append(gateAddrBin)
            elif i == 2: # Mask
                maskAddrBin = addressToBinaryString(row[i])
                rowBin.append(maskAddrBin)
            elif i == 3: # Metric
                rowBin.append(row[i])
            elif i == 4: # Interface
                rowBin.append(row[i].strip())
            else:
                print("error")
                print(row[i])
        rTableBin.append(rowBin)

    print("rTableBin:")
    printRTable(rTableBin)
    ##4. Forwarding Part-----------------------------------------------------------
    print("4. Forwarding addresses ...")

    ##5 After Forwarding: Ask for User Input - change Y,N option?-----------------------------------------------------------
    formatCorrect = False

    while (formatCorrect != True):
        print("Would you like to forward another packet?")
        userAnswer = input("Enter 'Y' for yes, 'N' for no : ")
        parsedAnswer = userAnswer.capitalize()

        if(parsedAnswer == 'N'):
            formatCorrect = finished = True
        elif (parsedAnswer == 'Y'):
            print("Continue ... \n")
            formatCorrect = True
        else:
            print("Input unrecognized. Please try again.\n")
            formatCorrect = False

#Program ends
print("Program will now exit.")
