import json
import pandas as pd
import matplotlib.pyplot as plt

"""
    openJsonAndReturnNewDictionary function opens and reads names.json file,
    then stores it in a dictonary. And return this dictionary. Keys of
    this dictionary are numbers which start from 0 to (total number of names -1).
    Values of this dictionary are names.
"""
def openJsonAndReturnNewDictionary():
    # Opening JSON file
    f = open('./names.json')

    # Load json
    oldDictionary = json.load(f)

    newDictionary={}    
    
    for i in list(oldDictionary):
        newDictionary[int(i)-1]= oldDictionary[i]

    return newDictionary

"""
    readPickleAndEditDataFrame function reads data.pkl file and extracts task column. 
    It takes 'names' argument which comes from return value of openJsonAndReturnNewDictionary
    function. Then I changed 1 values in the task column of the dataframe with the values 
    in names dictionary orderly. When 1 values starts to appear, I choose the next name value
    and assign this name to 1 values until I see a  0 value. Returns a dataframe and task
    column of this dataframe
"""
def readPickleAndEditDataFrame(names):
    currentPlace=-1
    shouldChangeValue=False

    # Read pickle file
    df = pd.read_pickle('data.pkl')

    # Get task column
    tasksSection= df["task"]


    for i in range(len(tasksSection)):
        if(tasksSection[i] == 0):
            if(shouldChangeValue==True):
                shouldChangeValue=False
        
        else:
            if(shouldChangeValue==False):
                shouldChangeValue=True
                currentPlace= (currentPlace+1)%len(names)

            tasksSection[i]=names[currentPlace]

    return df,tasksSection



"""
    countWordRepetionAndWriteThem function calculates word repetitions in
    the dataframe. This function takes two arguments, which are namesDict
    and tasks. namesDict is the dictionary which includes numbers from 0 
    to (total number of names -1) as keys , and names as values.Tasks is 
    the task column of the dataframe. Here we create a new dictionary,
    which includes names as key values and initially 0 number as values.
    Then by using this dictionary we calculate word repetitions of names.
    Finally we return this dictionary.
"""

def countWordRepetionAndWriteThem(namesDict,tasks):
    newDictionary={}
    for value in namesDict.values():
        newDictionary[value]=0
    for i in tasks:
        if(i!=0):
            newDictionary[i]=newDictionary[i]+1
    return newDictionary

"""
    drawBarGraph function draws bar graph. It takes one argument which
    is a dictionary which includes names as keys and word repetitions of
    these names as values. This function uses this argument for drawing
    a graph.
"""
def drawBarGraph(countsDictionary):

    namesList=[]

    countsList=[]


    for key,value in countsDictionary.items():
        namesList.append(key)
        countsList.append(value)

    labelAndTitleFont = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 14,
        }


    plt.bar(namesList,countsList,color="green")
    plt.xticks(rotation = 90)
    plt.xlabel('Counted Names',fontdict=labelAndTitleFont)

    plt.ylabel('Count Values',fontdict=labelAndTitleFont)
                

    plt.title("Graph for Task1",fontdict=labelAndTitleFont)
    plt.tight_layout()
    plt.show()
"""
    Main function is the function which is called first. We call
    the other functions which we write inside this function.
"""
def main():
    # Open names.json file and store the information in a dictionary
    names= openJsonAndReturnNewDictionary()

    # Read data.pkl file and edit dataframe
    df,tasksSection= readPickleAndEditDataFrame(names)


    # Save dataframe to pickle file
    df.to_pickle('data.pkl')

    # Count Word Repetition
    countsDictionary=countWordRepetionAndWriteThem(names,tasksSection)

    #  Draw Graph of Word Count Values
    drawBarGraph(countsDictionary)


# Call main function
main()


    






