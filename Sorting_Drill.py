#Python 3.6.5
#
#Nikita Portnoy
#
#Python Ascending Sort


#Initializing Function
def Init(Values):
    Index = 0 #Reset the index with every initialization
    EvalLoop(Values,Index)

#Evaluation Loop Function
def EvalLoop(Values,Index):
    while Index < len(Values)-1: #Checks to see that the index isn't larget than list
        if Values[Index] > Values[Index + 1]: #If first value larger than second run FlipValues
            return FlipValues(Index,Index+1,Values) #Ends the function and runs FlipValues     
        else: #If first Value is smaller than Second increment index to check next two values
            Index = Index + 1
    #If the whole list is run and sorted, output the list
    return print("\nHere's the sorted list: \n{}".format(Values)) 

#Flip Values Function
def FlipValues(A,B,Values):    
    New_List = Values.copy() #Making a new list for flipping the values
    #Flipping the values to a new list
    New_List[A] = Values[B]
    New_List[B] = Values[A]
    return Init(New_List) #Plug the new list back into the Initializing function

Init([67,45,2,13,1,998])
Init([89,23,33,45,10,12,45,45,45])
Init([12,12,1,2,1,1,13,535,567,856,345,75,3,1,23,634,73])
