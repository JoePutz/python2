#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    #functions for working w/ files is built in.
    
    #myfile = open("textfile.txt", "w+")
    #w+ write a file, create a new one if it doesn't already exist

    
    # Open the file for appending text to the end
    myfile = open("textfile.txt", "a+")
    #"a+" append to end of existing file

    # write some lines of data to the file
    for i in range(10): 
        myfile.write("This is some text\n")
    
    # close the file when done
    myfile.close()
    
    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r")
    if myfile.mode =='r':
        contents = myfile.read()
        print(contents)
        #prints out to terminal obviously
        fl = myfile.readlines()
        for x in fl: 
            print(x)
        #this is the same, but we can edit the range to only print out certain sections

if __name__ == "__main__":
    main()
