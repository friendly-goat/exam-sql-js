#ref. to data file, also assign to variable so we can use it down the road
log_file = open("um-server-01.txt")

#function decleration to print tuesdays information from data file, Log_file is paramater 
def sales_reports(log_file):
    #loop trough every element in data file, line is variable for each line during loop
    for line in log_file:
        #removes trailing characters
        line = line.rstrip()

        day = line[0:3]
        #conditional logic to only print out Tuesday's info
        if day == "Tue":
            #print element at 'index' point in the loop
            print(line)

#function call, var that was assigned to data file is arg
sales_reports(log_file)
