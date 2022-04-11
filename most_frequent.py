#importing operator module 
import operator

#creating an empty dictionary set
myDict = {}

#defining the function
def most_frequent():
    #condition
    for letter in string:
        #taking the letter and counting its occurence and increasing if it is reapeted
        myDict[letter] = myDict.get(letter, 0) + 1            
    #prints the most frequent letters in a word
    #print(myDict,"\n") 
    
#taking string input from the user 
string = str(input("Enter a string: "))

#fucntion call   
most_frequent()

#itemgetter is used as a key argument in the sorted() funciton, to fetch the value field from each key value item of the dictionary while sorting.
sorted_dict = dict(sorted(myDict.items(), key=operator.itemgetter(1), reverse=True))
print("Sorted Dict: ")
#prints the descending order key values
print(sorted_dict)

