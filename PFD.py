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
