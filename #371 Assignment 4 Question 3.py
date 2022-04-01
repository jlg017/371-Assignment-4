#371 Assignment 4 Question 3

#TODO:
#Read routing table from file forwardTableTest1.txt
    ##Format Requirements
    ## No column titles will be used in the file 
    ## Each line of data in the input file will contain the information in one row of the routing table. 
    ## Values within each line of the file will be separated by single tabs. 
    ## Values within each line of the file will be in the same order as the corresponding row of the table below

# Order routing table by mask length: longest -> shortest

# Print sorted routing table to screen

# Convert all input addr in routing table to binary

#For each pkt to forward:
    # read IP dest of pkt to fwd
    # convert IP dest to binary
    # implement fwding algorithm -> calculations done in binary
    # include use of metric
    # print(The destination IP address is <IP address in x.x.x.x format> )
    # print(The next hop IP address is <IP address in x.x.x.x format> )
    # print(The port the packet will leave through is <int port #>)

#After pkt forwarded: 
    # Ask if the user wishes to forward another packet
        #if yes: ask for dest IP addr of next pkt to fwd, repeat above
        #else: terminate program

#sample routing table
#Destination, Gateway address, Mask, Metric, Interface
routingTable = ['201.123.32.0', '*', '255.255.224.0', 0, 'eth1' ], 
['201.123.64.0', '123.122.0.2', '255.255.192.0', 1, 'eth2' ],
['201.123.64.0', '123.123.0.2', '255.255.192.0', 0, 'eth3' ],
['202.123.40.0', '*', '255.255.248.0', 0, 'eth4' ],
['124.124.0.0', '*', '255.255.254.0', 0, 'eth0' ],
['125.125.1.0', '124.124.1.1', '255.255.254.0', 0, 'eth0' ],
['0.0.0.0', '124.123.1.1', '0.0.0.0', 0, 'eth0' ]