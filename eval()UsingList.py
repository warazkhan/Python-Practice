#Initialize your list and read in the value of n followed by n lines of commands where each command will be list built-in methods append,remove,reverse,print,insert,sort or pop. Iterate through each command in order and perform the corresponding operation on your list.
#Input Format:
#The first line contains an integer, , denoting the number of commands. Each line  of the  subsequent lines contains one of the commands.
#Constraints:
#The elements added to the list must be integers.
#Output Format:
#For each command of type print, print the list on a new line.


if __name__ == '__main__':
    linesOfCommands = int(input())
    resultList=[]
    
    for i in range(linesOfCommands):
        checkList= input().split()
        checkCondition= checkList[0]
        integerInputAndIndex= checkList[1:]
        
        if checkCondition!="print":
            
            #eval(expression, [globals[, locals]])  
            
            eval(f"resultList.{checkCondition}({','.join(integerInputAndIndex)})")
        else:
            eval(f"{checkCondition}({resultList})")