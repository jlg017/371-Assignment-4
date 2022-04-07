#371 Assignment 4 Question 3
#TODO:

#For each pkt to forward:
    # read IP dest of pkt to fwd - done
    # convert IP dest to binary - done
    # implement fwding algorithm -> calculations done in binary
    # include use of metric
    # print(The destination IP address is <IP address in x.x.x.x format> )
    # print(The next hop IP address is <IP address in x.x.x.x format> )
    # print(The port the packet will leave through is <int port #>)


#Convert Address to Binary String Method | April 4
#returns a tuple, the combined string and the list
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

## Prints Table
def printRTable(rTable):
    print("[")
    for row in rTable:
        print("\t{},".format(str(row)))
    print("]")

## Helper Function to 'addressToByte' and 'bitwiseAND' Method
## converts a decimal number to binary octet, returns as str
def binaryConvert (deciNum):
    binaryStr = ""
    convertedNum = bin(deciNum).replace("0b","")

    #Fills in 0s if num is not octets
    if(len(convertedNum)!=8):
        zeros = ""
        for i in range(8-len(convertedNum)):
            zeros+="0"
        binaryStr = zeros+convertedNum
    else:
        binaryStr = convertedNum

    return binaryStr

#Helper Method to bitwiseAND
    #Paramter: A string of 32 0s and 1s
    #Return: A list of 4 octets of 0s and 1s
def splitAddress (address):
    newList = []
    temp = ""
    for i in range(len(address)):
        if ((i+1)%8)!=0:
            temp+=address[i]
        else:
            temp+=address[i]
            newList.append(temp)
            temp = ""
    
    return newList

#Bitwise AND of 2 addresses
    #Parameters: Both are a string of 0s and 1s
    #Returns a string of 0s and 1s
def bitwiseAND (add1, add2):
    
    #split addresses into list of 4 octets
    convertAdd1 = splitAddress(add1)
    convertAdd2 = splitAddress(add2)

    newAddress = ""

    #Perform Bitwise AND for each octet set
    for i in range(4):
        #Python's bitwise AND
        byte1 = int(convertAdd1[i],2)
        byte2 = int(convertAdd2[i],2)
        result = byte1 & byte2

        #result gives us a decimal num, convert to binStr
        binResult = binaryConvert(result)
        newAddress+= binResult

    return newAddress

#count number of ones in bit mask| Date modified: April 7, 12PM
def countOnes(str):
    length = len(str)
    count = 0
    for i in range(length):
        if(int(str[i]) == 1):
            count += 1
        else:
            break
    
    return count

#forwarding algorithm ##TODO: delete print statements when done debugging | Date modified: April 7, 12PM
def forwardToRow(table, destIP):
    print("bit destination IP address = "+ destIP)
    #mask length of rowMatch
    longestMatch = 0
    #rowMatch = row that matches, get forwarding information from
    rowMatch = -1
    #go through forwarding table
    for row in table:
        rDest = row[0]
        mask = row[2]
        metric = row[3]
        #bitwise AND mask and destIP
        #netID = bAND(mask, destIP)
        netID = bitwiseAND(mask,destIP)

        #compare result to row destination IP
        if(netID == rDest):
            print("netID: "+ netID +" == rDest: "+ rDest)

            #find length of the mask
            lengthMatch = countOnes(mask)
            print("length of match's mask = " + str(lengthMatch))

            if(lengthMatch > longestMatch):
                print("new longestMatch, changing rowMatch")
                rowMatch = row
                longestMatch = lengthMatch

            elif(lengthMatch == longestMatch): 
                print("match found of same length")
                #choose lowest metric
                print("metric ="+str(metric)+", rowMatchMetric = "+str(rowMatch[3]))

                if(int(metric) < int(rowMatch[3])):
                    print("metric < previous rowMatch, changing rowMatch")
                    rowMatch = row 
                else: #if metric =>  no change to rowMatch
                    print("no change to rowMatch")
                    continue
        else:
            print("netID: "+ netID +" != rDest: "+ rDest)
    
    return rowMatch


## MAIN - while loop for processing addresses

##Variables
finished = False

##Loop
while (finished != True):
    ##1. get information for forwarding table file-----------------------------------------------------------
    print("1. Getting information from user ...")
    destIP = input("Enter the IP address for your packet destination:\n")
    #created file with test routing table information | Apr 4th 
    
    #TODO: change below to take in table (before submission)
    # #table = input("Enter the file name for your forwarding table:\n")
    
    fTable = open('forwardTableTest1.txt', 'r')
    rFileLines = []
    rFileLines = fTable.readlines()

    ##2. Print Routing Table (Sorted) to screen-----------------------------------------------------------
    
    # Order routing table by mask length: longest -> shortest
    rFileLines.sort(reverse=True, key = lambda x: x[2])
    print("Sorting table ...\n")
    
    rTableRows = []
    
    for line in rFileLines:
        #splits line into list of entries separated by tab
        rTableRow = line.split("\t")

        #Strips '\n' from the end of Interface item | April 6th - make more sophisticated | April 7 changed to strip() instead of replace()
        temp = rTableRow[len(rTableRow)-1].strip()
        rTableRow[len(rTableRow)-1] = temp
        rTableRows.append(rTableRow)
    
    print("2. Routing Table (Sorted) ")
    printRTable(rTableRows)

    ##3. Convert Addresses to Binary 8-bits-----------------------------------------------------------
    print("3. Converting addresses to binary 8-bits ... ")
    
    ## convert destination address
    destIPBin = addressToBinaryString(destIP)

    ## convert routing table
    rTableBin = []
    for row in rTableRows:
        #convert row of addresses to binary
        rowBin = []
        for i in range(0, len(row)):
            if i == 0: # Network address 
                netAddrBin = addressToBinaryString(row[i])
                rowBin.append(netAddrBin)

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
                rowBin.append(row[i])\

            elif i == 4: # Interface
                #extract port number from eth#, convert to int
                interface = int(row[i][len(row[i])-1])
                rowBin.append(interface)

            else:
                print("error: ")
                print(row[i])
        rTableBin.append(rowBin)
    
    # table with addresses converted to binary 
    print("rTableBin: (do not print in final implementation)")
    printRTable(rTableBin)

    ##4. Forwarding Part-----------------------------------------------------------
    print("4. Forwarding addresses ...")

    #Variables
    nextHopIP = "HOP"
    leavePort = 0

    #Algorithm begins here

    rowChosen = forwardToRow(rTableBin, destIPBin)
    print("row using = "+ str(rowChosen))
    port = int(rowChosen[4])

    #TODO: convert binary addresses back to IP address
    #netAddr = binToIP(rowChosen[0])
    
    #determine if next hop or destination
    #if(str(rowChosen[1]) == '*'):
        #nextHopIP = netAddr
        #dest = destIP
    #else:
        #nextHopIP = bintoIP(rowChosen[1])
        #dest = netAddr
   
    #print("The destination IP address is "+ dest)
    #print("The next hop IP address is "+ nextHopIP)
    #print("The port the packet will leave through is "+ port)

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
