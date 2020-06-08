# creates data 
import string


reviewData = open("data/data.txt", 'r')
cleanData = open("data/cleanData.txt", 'w')
cleanDataPunc = open("data/cleanData_withPunc.txt", 'w')
cleanData.truncate(0)

onReview = 0
# iterates through each line and breaks the text into the review as well as cleans each line of punctuation and capitals
for line in reviewData:
    curLine = ""
    for word in line.split():
        if(word == "\"reviewText\":"):
            onReview = 1
        if(word == "\"summary\":" or word == "\"overall\":"):
            onReview = 0
            break
        if(onReview == 1):
            curLine += word + " "
            
    # removes new line characters 
    curLine = curLine.replace('\\n', ' ')
    curLine = curLine.replace('  ', ' ')


    cleanDataPunc.write(curLine[15:-3])
    cleanDataPunc.write("\n")
    
    #get rid of punctuation
    curLine = curLine.translate(str.maketrans('', '', string.punctuation))

    #trims beginning and end of line
    cleanData.write(curLine[11:])

    #adds newline
    cleanData.write("\n")

cleanData.close()