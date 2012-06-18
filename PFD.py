#!/usr/bin/env python

# -------------
# sort_and_search
# -------------
def sort(rules, numberOfVerticies, numberOfRules) :
    """
    This function first lengthens the rules list to match the total
    number of verticies in the input with all values not present being
    set to [-1].  Then because we know no duplicate values will be
    present this function is capable of sorting the list of rules in
    O(n) time.  It accomplishes this by making a second list of the exact
    same size as the total number of verticies and then scanning throught
    the original list copying the rules to the second array in the location
    matching the number of the vertex but in reverse sorted order.  It then
    returns this reverse sorted list of rules with verticies for which no rules
    were present conatining the value [-1]
    """
    a = [-1]
    b = []
    location = -1
    counter = numberOfRules
    while counter < numberOfVerticies :
        rules.append(a)
        counter += 1
    counter = 0
    while counter < numberOfVerticies :
        b.append(a)
        counter += 1
    counter = 0
    assert counter == 0
    while counter < numberOfRules :
        location = int(rules[counter][0])
        location = location - numberOfVerticies
        if location < 0 :
            location = location * (-1)
        out = location
        b[location] = rules[counter]
        counter += 1
    #rulesFound = 0
    #counter = 0
    #noPredacessors = []
    """
    while counter < numberOfVerticies :
        if b[counter][0] > 0 :
            rules[rulesFound] = b[counter]
            rulesFound += 1
        else:
            location = counter
            location = location - numberOfVerticies
            if location < 0 :
                location = location * (-1)
            noPredacessors.append(location)
        counter += 1
    """
    return b

# -------------
# find_no_preds
# -------------

def find_no_preds (rules, numberOfVerticies) :
    """
    This function scans the list of rules returning a list
    of the verticies that have no predacessors
    """
    noPreds = []
    counter = 0
    location = -1
    while counter < numberOfVerticies :
        if rules[counter][0] == -1 :
            location = counter
            location = location - numberOfVerticies
            if location < 0 :
                location = location * (-1)
            noPreds.append(location)
        counter += 1
    return noPreds
    
    

# -------------
# generate_successors_list
# -------------

def generate_successors_list (rules) :
    successors = []
    successorsList = []
    val = 0
    counter = 0
    lengthOfRules = len(rules)
    while counter < lengthOfRules:
        val = rules[counter][0]
        successors = get_successors(rules, val, counter)
        assert len(successors) > 0
        successorsList.append(successors)
        counter += 1
    return successorsList

# -------------
# is_a_successor
# -------------

def is_a_successor (rule, val) :
    """
    Returns true if the vertex from the rule is a successor
    of the value specified.
    """
    counter = 2
    length = len(rule)
    while counter < length :
        if int(rule[counter]) == val:
            return True
        if rule[counter] == val:
            return True
        counter += 1
    return False

# -------------
# get_successors
# -------------

def get_successors (rules, val, ignore) :
    if val < 0 :
        location = ignore
        location = location - len(rules)
        if location < 0 :
            location *= (-1)
        val = location
    assert val > 0
    counter = 0
    counter2 = 0
    successors = []
    numVals = -1
    lengthOfRules = len(rules)
    number = -1
    
    while counter < lengthOfRules :
        """
        if rules[counter][0] == val :
            counter += 1
            continue
        if rules[counter][0] == -1 :
            counter += 1
            continue
        """
        if rules[counter][0] == -1 :
            counter += 1
            continue
        if counter == ignore :
            counter += 1
            continue
        else:
            numVals = len(rules[counter])
            assert numVals >= 3
            number = rules[counter][0]
            assert number > 0
            rule = rules[counter]
            if is_a_successor(rule, val):
                successors.append(number)
            counter += 1
    numSuccessors = len(successors)
    if val == 3 :
        assert numSuccessors > 0
    if numSuccessors < 1 :
        successors.append(-1)
    return successors

# -------------
# noPreds_sort
# -------------
def noPreds_sort (noPreds):
    lengthOfList = len(noPreds)
    index = lengthOfList - 1
    moveVal = noPreds[index]
    index = index - 1   
    while index >= 0:
        if noPreds[index] > moveVal:
            break
        index = index - 1
    index2 = lengthOfList - 2
    index3 = index2+1
    temp = noPreds[lengthOfList - 1]
    while index2 > index :
        noPreds[index3] = noPreds[index2]
        index2 = index2 - 1
        index3 = index3 - 1
    noPreds[index + 1] = temp
        
    
    
# -------------
# update
# -------------
def update (valAdded, noPreds, rules, successorList) :
    noPreds.remove(valAdded)
    lengthOfRules = len(rules)
    locationOfSuccessors = valAdded - lengthOfRules
    if locationOfSuccessors < 0:
        locationOfSuccessors = locationOfSuccessors * (-1)
    successors = successorList[locationOfSuccessors]
    counter = 0
    location2 = -1
    while counter < len(successors) :
        if successors[0] == -1 :
            break
        location2 = int(successors[counter])
        location2 = location2 - lengthOfRules
        if location2 < 0:
            location2 = location2*(-1)
        x = int(rules[location2][1]) - 1
        rules[location2][1] = x
        if x == 0:
            noPreds.append(int(rules[location2][0]))
            rules[location2] = [-1]
            if len(noPreds) > 1:
                noPreds_sort(noPreds)
        counter += 1
        


# -------------
# generate_solution
# -------------
def generate_solution (noPreds, rules, successorList) :
    """
    This function takes in the list of values with no predacessors,
    the list of predacessor rules, and the successorList.  It then
    uses this data to generate the output as an list.  Finally it
    copies this list into a string and returns this string
    """
    out = []
    endPointer = -1
    valAdded = -1
    while(len(noPreds) > 0) :
        endPointer = len(noPreds) - 1
        out.append(noPreds[endPointer])
        valAdded = noPreds[endPointer]
        update(valAdded, noPreds, rules, successorList)
    counter = 0
    outputString = ""
    lengthOfOutput = len(out)
    secondLast = lengthOfOutput - 1
    while counter < lengthOfOutput:
        if counter < secondLast:
            outputString = outputString + str(out[counter])
            outputString = outputString + " "
        else:
            outputString = outputString + str(out[counter])
        counter += 1
    return outputString
        

# -------------
# pfd_compute
# -------------
def pfd_compute (r) :
    s = "-1"
    s = r.readline()
    if s == "":
        out = "-1"
        return out
    l = s.split()
    numberOfVerticies = int(l[0])
    numberOfRules = int(l[1])
    readCount = 0
    rules = []
    while readCount < numberOfRules :
        s = r.readline()
        l = s.split()
        rules.append(l)
        readCount += 1
    #out = rules[0][0]
    rules = sort(rules, numberOfVerticies, numberOfRules)
    noPredacessors = find_no_preds(rules, numberOfVerticies)
    #out = noPredacessors[0]
    #out = rules[0]
    successorsList = generate_successors_list(rules)
    #out = successorsList
    #out = rules
    #out = noPredacessors
    out = generate_solution(noPredacessors, rules, successorsList)
    return out


# -------------
# pfd_print
# -------------

def pfd_print (w, output) :
    """
    prints out the integers passed into it
    from the output array on a single line
    with a space between each and terminated
    with a newline character
    """

    """
    x = len(output)
    x = x - 1
    i = 0
    while i < x :
        w.write(str(output[i]) + " ")
        i += 1
    w.write(str(output[x] + "\n")
    """
    w.write(str(output))



# -------------
# collatz_solve
# -------------

def pfd_solve (r, w) :
    """
    r is a reader and it is passed 
    to the function pfd_compute
    w is a writer which is passed along
    with the output array to pfd_print
    
    """
    output = pfd_compute(r)
    pfd_print(w, output)
