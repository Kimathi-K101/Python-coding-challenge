# Comment here with the runtime of your function, for example:
#       O(n^2) time complexity if every entry into the dictionary collides
#       O(nlogn) time complexity is a more accurate description of the runtime

def k_popular(nameList, k):

    #In conjunction with the assumption "the input list has at least k elements"
    #if k = 0, there's no need to execute the rest of the body
    if k == 0:
        return nameList

    #Dictionary created for its <key,value> pair. Hash table properties allow
    #for the quick retrieval of values to avoid linear search.
    #However, as the size of the list increases exponentialy, the probability of
    #collisons to occur slowly increases
    nameCount = {}
    
    # O(n): Iterates through entire nameList once to update popularity of names
    for name in nameList:
        #O(n) amortized worst case; if each consequitive added element collides 
        #but has an O(1) average case runtime
        if name in nameCount:
            nameCount[name] += 1
        else:
            nameCount[name] = 1

    #O(nlogn): Sorting dictionary into a list by item value (popularity)
    nameList = sorted( nameCount, key = nameCount.get, reverse = True )

    #Variable to hold the length of the list
    listLenght = len(nameList)
    #If the number of unique names is less than k, k unique elements cannot be outputted
    if listLenght < k:
        print( "Unique elements in the list =  "+ str(listLenght),end=': ')
        return nameList
                
    return nameList[:k] #O slicing list off at the k most popular names



#---------------------------TEST CASES-----------------------------------------------------
print( k_popular( [], 0 ) ) #no entries in list
print( k_popular([ "tom","tom","ben","tom",], 3 ) ) # <k unique elements

# this should print
#       ['Jane', 'John']
print(
    k_popular(
        [
            "John",
            "Jane",
            "Susan",
            "Jane",
            "John",
            "Jane"
        ],
        2
    )
)

# this should print
#       ['Jane', 'John']
# OR
#       ['Jane', 'Susan']
print(
    k_popular(
        [
            "John",
            "Jane",
            "Susan",
            "Jane",
            "John",
            "Jane",
            "Susan"
        ],
        2
    )
)

# this should print
#       ['Jane', 'John', 'Susan']
# OR
#       ['Jane', 'Susan', 'John']
print(
    k_popular(
        [
            "John",
            "Jane",
            "Susan",
            "Jane",
            "John",
            "Jane",
            "Susan"
        ],
        3
    )
)

# this should print
#       ['JoSEPH', 'joseph', 'Mackenzie', 'Kim' ]
# OR
#       ['JoSEPH', 'joseph','Kim', 'Mackenzie' ]
print(
    k_popular(
        ["JoSEPH",
         "Kim",
         "joseph",
         "JoSEPH",
         "Jaden",
         "JoSEPH",
         "Abi",
         "joseph",
         "Mackenzie",
         "Kim",
         "JoSEPH",
         "Ben",
         "Elasha",
         "joseph",
         "Mackenzie"
        ],
        4
    )
)
