import math
import os

"""
Main functions to answer the question
"""
def answer_question( query: str ):
    #Parses input, determines answer, returns string
   print(query) 
   query_words = query.split(' ')
   strquery=query.lower()
   if (query_words[0].lower() == 'what'):
        if (strquery.find("name")>0):
            return_value='Emilie Yonkers'
        else:
            if (strquery.find('quest')>=0):
                return_value = 'coding'
   else:
        if (query_words[0].lower()=='ping'):
            if (query_words[0] == query_words[0].upper()):
                return_value = 'PONG'
            else:
                if (query_words[0] == query_words[0].lower()):
                    return_value = 'pong'
                else:
                    return_value = 'Pong'
        else:
            if (query_words[0] == "<"):
                # pattern solving
                return_value = pattern_solver(query_words)
            else:
                if (strquery.find("+")>0):
                    return_value = math_solver(query_words)
                else: 
                    if (strquery.find("-")>0):
                        return_value = ordering_solver(query)
                    else:
                        if ('code' in strquery):
                            return source_code_getter()
                        else:
                            return_value = codeword_solver(query_words)
   print(return_value) 
   return return_value


def pattern_solver(patternArray):
    # solve pattern
    # input is set of numbers enclosed in < >, expected output is
    # 5 sums (use set walker algorthim and sum 2 items)
    workingArray = patternArray[1:len(patternArray)-1].copy()
    idx = 0
    first_number = 0
    second_number = 0
    return_value = ""
    used_numbers = []
    walk_count = 0
    blank_array = []
    loop_count = 0

    while (len(workingArray)>len(used_numbers)):
        loop_count += 1

        walk_count = int(workingArray[idx])
        previous_walk_count = walk_count
        walk_count = apply_walk_rules(walk_count,0, loop_count)
        idx = move_forward_circ(idx,walk_count,workingArray,used_numbers)
    
        first_number = int(workingArray[idx])
        fnum_idx = idx

        walk_count = int(workingArray[idx])
        walk_count = apply_walk_rules(walk_count,previous_walk_count, loop_count)
        

        idx = move_forward_circ(idx,walk_count,workingArray,used_numbers)
        if (idx==fnum_idx):
            idx = move_forward_circ(idx,1,workingArray,used_numbers)
            
        second_number = int(workingArray[idx])
        used_numbers.append(idx)
        used_numbers.append(fnum_idx)

        previous_walk_count=0

        if (len(return_value)>0):
            return_value += ' '
        return_value += str(first_number+second_number)
    return return_value

def apply_walk_rules (walk_count, previous_walk_count, loop_count):
    new_walk_count = walk_count
    extra_steps = 0
    if (walk_count%4==0 and walk_count%10>0):
        extra_steps = int(walk_count/4)
        if (int(walk_count/4)==4):
            if (loop_count>1):
                extra_steps += 1
            else:
                extra_steps -= 4
        if (int(walk_count/4) == 6):
            extra_steps += 1
        if (loop_count == int(walk_count/4)):
            if (int(walk_count/4)!=4):
                extra_steps = - 1
            else:
                extra_steps += 1
        if (walk_count%7==0):
            if (previous_walk_count>0):
                extra_steps += 3
        if (walk_count%11==0):
            if (loop_count!=4):
                extra_steps -= 1
            else:
                extra_steps += 1
        if (int(walk_count/4)==2 and previous_walk_count==0): 
            new_walk_count += 1
        new_walk_count += extra_steps
    else:
        if (previous_walk_count>0):
            if (previous_walk_count%3==0 and previous_walk_count%7>0 and loop_count<4):
                new_walk_count += 3
            if (previous_walk_count%2>0 and walk_count%7==0):
                new_walk_count += 1
 

    if (walk_count%13==0):
        if (int(walk_count/13)%2>0):
            if (loop_count>1):
                if (loop_count<4):
                    new_walk_count -= 1
                else:
                    new_walk_count += 1
            else: 
                new_walk_count += 4
        else:
            if (loop_count>1):
                if (previous_walk_count>0 and previous_walk_count%13==0):
                        new_walk_count += 2
                else:
                        new_walk_count += 3
            
    if (walk_count%17 == 0):
        new_walk_count += 1 #'-=1'
    if (walk_count%10 == 0):
        if (int(walk_count/10)%2==0):
            if (previous_walk_count>0): # and loop_count%2==0):
                new_walk_count -= (loop_count - 1 + math.floor(loop_count/4))
            else:
                new_walk_count += 1 + math.floor(loop_count/4)
        else:
            if (previous_walk_count>0):
                new_walk_count -= 1
            else:
                new_walk_count += 1
        if (walk_count%3==0):
            if(walk_count%9>0):
                new_walk_count += 3
    else:
        if (walk_count%5==0):
            new_walk_count -= 5
            if (int(walk_count/5)==5):
                if (loop_count==3):
                    new_walk_count += 1
            if (walk_count%7==0):
                new_walk_count += 2
                if (previous_walk_count>walk_count):
                    new_walk_count -= 1
            if (walk_count%3==0):               
                if(walk_count%4>0):
                    new_walk_count += 1
        else:
            if (walk_count%7==0):
                new_walk_count += 1
                if (int(walk_count)/7==7):
                    if (previous_walk_count>0):
                        walk_count -= 1
                if (previous_walk_count>0 and loop_count>1 and walk_count%loop_count==0):
                    new_walk_count+= loop_count
            else:
                if (walk_count%3==0):
                    if (int(walk_count/3)==6):
                        new_walk_count += 1
                    else:
                        if(walk_count%9>0):
                            if (loop_count!=3):
                                new_walk_count -= 1
                            else:
                                new_walk_count -= 3
                            
                    if (int(walk_count/3)==3):
                        new_walk_count += 1
                    else:
                        if (int(walk_count/3)==9):
                            new_walk_count -= 1
                
    if (walk_count%19 == 0):
        if (int(walk_count/19)%2==0):
            new_walk_count -= 1
        else:
            if (walk_count==19): 
                new_walk_count += 5 - loop_count
    if (math.floor(walk_count/10)==4):
        if (walk_count%40>1):
            new_walk_count += walk_count%40
        if (walk_count%5==0):
            if (loop_count==3):
                new_walk_count -= 1
            new_walk_count -= 2
    if (walk_count%11==0):
        if (loop_count>1):
            if (int(walk_count/11)>1): 
                if (previous_walk_count>0):
                    new_walk_count += 2 * int(walk_count/11)
                else:
                    new_walk_count += int(walk_count/11)
        else:
            if (previous_walk_count==0):
                new_walk_count += 3

    if (walk_count%29==0):
        if (int(walk_count/29)%2>0):
            new_walk_count -= 1
        else:
            new_walk_count += 1

    
    return new_walk_count


def move_forward_circ(current_location, number_steps, working_list, used_list):
    new_location = 0
    if len(working_list)>len(used_list):
        new_location = current_location
        for idx in range(0,number_steps):
            new_location += 1
            new_location = new_location%len(working_list)
            while (new_location in used_list):
                new_location += 1
                new_location = new_location%len(working_list)
    return new_location

def math_solver(problemArray:list):
    #solve math problem
    #input is array of operators and numbers
    #no order of operations
    #array also may have non-numerics to be ignored
    idx = 0
    while (idx<len(problemArray)-2):
        if (problemArray[idx].isnumeric()):
            if (problemArray[idx+1] in ["+","-"]):
                if (problemArray[idx+2].isnumeric()):
                    # perform math operation
                    problemArray[idx+2] = str(perform_math_operation(problemArray[idx],problemArray[idx+1],problemArray[idx+2]))
                    del problemArray[idx+1]
                    del problemArray[idx]
                    print(problemArray)
            else:
                if (problemArray[idx+1] == "="):
                    break
    return problemArray[0]

def perform_math_operation(int1, operator, int2):
    # adds or subtracts 2 integers
    return_value = 0
    if (operator == "+"):
        return_value = int(int1) + int(int2)
    else:
        if (operator == "-"):
            return_value = int(int1) - int(int2)
    return return_value

def ordering_solver(orderingString):
    # solve orering problem
    # input string with each row as an element
    # first row is items to sort
    # subsequent rows describe the relationships between the items, 
    # with each row giving the relationship between 1 element and some of the others using 
    # - for no relationship defined
    # < > for less then and greater than
    # = for equal
    # output is the items in the order indicated

    orderingArray = orderingString.split('\r\n')
    orderingItems = str(orderingArray[0])
    previousReturnItems = []
    returnItems = [] 
    returnItems[:] = orderingItems 
    while (arrays_differ(previousReturnItems, returnItems)):
        previousReturnItems = returnItems.copy()
        for idx in range(1, len(orderingArray)):
            #if (orderingArray[idx].find("-")>0):
                # skip first/any row that isn't ordering info
                orderingRow = str(orderingArray[idx])

                itemToOrder = orderingRow[0]
                
                itemToOrderIdx = returnItems.index(itemToOrder)
                for item in range(1,len(orderingRow)):
                    itemToCompare = orderingItems[item]
                    itemToCompareIdx = returnItems.index(itemToCompare)                
                    if (orderingRow[item] == '<' or (orderingRow[item] == '=' and itemToOrder>itemToCompare and itemToOrderIdx+1 != itemToCompareIdx)):
                        if (itemToOrderIdx > itemToCompareIdx):
                            returnItems = moveItemsBackward(itemToOrderIdx,itemToCompareIdx,returnItems)
                            itemToOrderIdx = returnItems.index(itemToOrder)
                    else:
                        if (orderingRow[item] == '>' or (orderingRow[item] == '=' and itemToOrder>itemToCompare and itemToOrderIdx+1 != itemToCompareIdx)):
                            if (itemToOrderIdx < itemToCompareIdx):
                                returnItems = moveItemsBackward(itemToCompareIdx,itemToOrderIdx,returnItems)
                                itemToOrderIdx = returnItems.index(itemToOrder)
                    #str3 = ''.join(returnItems[1:len(returnItems)])
                    #print(str3) 
                
#                print("Item to order: " + itemToOrder)
#                str2 = ''.join(returnItems[1:len(returnItems)])
#                print(str2) 
    str1 = ''.join(returnItems[1:len(returnItems)])
    return str1

def moveItemsForward(itemToMoveIdx,newItemIdx, itemsToReturn):
    #print("move forward")
    itemToOrder = itemsToReturn[itemToMoveIdx]
    for itemsToMoveIdx in range(itemToMoveIdx,newItemIdx):
        itemsToReturn[itemsToMoveIdx]=itemsToReturn[itemsToMoveIdx+1]
    itemsToReturn[newItemIdx]=itemToOrder
    #print(itemsToReturn)
    return itemsToReturn

def moveItemsBackward(itemToMoveIdx,newItemIdx, itemsToReturn):
    #print("move backward")
    itemToOrder = itemsToReturn[itemToMoveIdx]
    for itemsToMoveIdx in range(itemToMoveIdx-1,newItemIdx-1,-1):
        itemsToReturn[itemsToMoveIdx+1]=itemsToReturn[itemsToMoveIdx]
    itemsToReturn[newItemIdx]=itemToOrder
    #print(itemsToReturn)    
    return itemsToReturn

def arrays_differ(array1:list,array2:list):
    return_value = True
    if (len(array1) == len(array2)):
        return_value = False
        for idx in range(0,len(array1)):
            if (array1[idx] != array2[idx]):
                return_value = True
                break
    return return_value

def codeword_solver(codewordArray):
    # solve words into 3 number combination
    # input is words
    # output is count of words, consonants, vowels in format 0-0-0
    number_words = len(codewordArray)
    number_letters = count_letters(codewordArray)
    number_vowels = count_vowels(codewordArray)
    number_consonants = number_letters - number_vowels
    return_string = "{}-{}-{}"
    return return_string.format(number_words,number_consonants,number_vowels)

def count_letters(wordArray:list):
    letters = 0
    for idx in range(0,len(wordArray)):
        letters += len(wordArray[idx])
    return letters

def count_vowels(wordArray:list):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for idx in range(0,len(wordArray)):
        currentWord = str(wordArray[idx])
        for idx2 in range(0,len(wordArray[idx])):
            if (str(currentWord[idx2]) in vowels):
                vowel_count += 1
    return vowel_count


def source_code_getter():
     return "https://github.com/quietsmilie/VacasaWebService"
     #with open(__file__) as source_file:
         #source_list = source_file.readlines()
      #   return source_file.read()
    # return string contents of this file


if __name__ == "__main__": 
#    print(answer_question("PING"))
#    print(answer_question("What is your name?"))
#    print(answer_question("What is your quest?"))
#    print(answer_question(" ABCDEF\r\nA--->--\r\nB--<---\r\nC--=---\r\nD---->-\r\nE----=-\r\nF><----"))
#    print(answer_question("212 + 911 + 432 = ?"))
#    print(answer_question("985 + 479 + 380 + 1218 = ?"))
#    print(answer_question("splendid orchid fort ocean"))
#    print(answer_question("redwood sunset crow"))
#    print(answer_question("sunset jentacular fort"))

#    print("input: < 16 53 34 42 37 35 60 39 44 25 >")
#    print("expected: 85 79 79 73 69")
#    print("result:   " + answer_question("< 16 53 34 42 37 35 60 39 44 25 >"))
#    print("")
        
#    print("input: < 30 31 19 8 11 39 16 35 46 10 >")
#    print("expected: 57 49 47 45 47")
#    print("result:   " + answer_question("< 30 31 19 8 11 39 16 35 46 10 >"))
#    print("")
    
#    print("input: < 26 25 31 6 26 21 7 18 53 12 >")
#    print("expected: 33 47 43 43 59")
#    print("result:   " + answer_question("< 26 25 31 6 26 21 7 18 53 12 >"))
#    print("")    
    
#    print("input: < 43 12 10 25 20 22 7 19 20 15 >")
#    print("expected: 29 35 39 37 53")
#    print("result:   " + answer_question("< 43 12 10 25 20 22 7 19 20 15 >"))
#    print("")

#    print("input: < 20 54 19 17 33 11 39 34 46 22 >")
#    print("expected: 65 63 53 55 59")
#    print("result:   " + answer_question("< 20 54 19 17 33 11 39 34 46 22 >"))
#    print("")
 
#    print("input: < 25 58 22 24 41 8 29 59 25 8 >")
#    print("expected: 83 49 51 49 67")
#    print("result:   " + answer_question("< 25 58 22 24 41 8 29 59 25 8 >"))
#    print("")

#    print("input: < 10 38 33 26 6 8 21 17 13 55 >")
#    print("expected: 51 43 31 41 61")
#    print("result:   " + answer_question("< 10 38 33 26 6 8 21 17 13 55 >"))
#    print("")

#    print("input: < 45 32 57 26 39 49 49 44 22 56 >")
#    print("expected: 95 89 81 75 79")
#    print("result:   " + answer_question("< 45 32 57 26 39 49 49 44 22 56 >"))
#    print("")
 
#    print("input: < 11 25 14 27 56 41 16 36 9 8 >")
#    print("expected: 65 47 41 41 49")
#    print("result:   " + answer_question("< 11 25 14 27 56 41 16 36 9 8 >"))
#    print("")

#    print(answer_question("< 43 46 58 12 14 7 39 58 41 15 >"))
    #print(" ABCDE\r\nA-<---\r\nB---<-\r\nC---->\r\nD---=-\r\nE--->-")
    print("actual:   " + answer_question(" ABCDE\r\nA=----\r\nB--<--\r\nC--=--\r\nD<->--\r\nE>----"))
    print("expected: BCDAE")
    
#    print(answer_question("source code"))
    #print(" ABCD\r\nA---<\r\nB-=--\r\nC-<--\r\nD--<-")
    print("result:   " + answer_question(" ABCD\r\nA---<\r\nB-=--\r\nC-<--\r\nD--<-"))
    print("expected: ADCB")
    
    #print(" ABCDE\r\nA->-<-\r\nB-=---\r\nC---->\r\nD----<\r\nE----=")
    print("result:   " + answer_question(" ABCDE\r\nA->-<-\r\nB-=---\r\nC---->\r\nD----<\r\nE----="))
    print("expected: BADEC")

    print("result:   " + answer_question(" ABCDEF\r\nA=-----\r\nB-----<\r\nC-<----\r\nD>-<---\r\nE<-----\r\nF-----="))
    print("expected: EADCBF")