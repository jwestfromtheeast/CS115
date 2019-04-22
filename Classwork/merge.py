'''
Created on Apr 10, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

def num_matches(list1, list2):
    """
    Returns the number of elements the two lists have in common
    """
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while(i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            matches += 1
            i += 1
            j += 1
    return matches

def keep_matches(list1, list2):
    """
    Returns the elements the two lists have in common
    """
    list1.sort()
    list2.sort()
    matches = []
    i = j = 0
    while(i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            matches.append(list1[i])
            i += 1
            j += 1
    return matches

def drop_matches(list1, list2):
    """
    Returns the elements the two lists DO NOT have in common
    """
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    return result

print(drop_matches([7,3,21,5,6,8,4,1,2], [6,5,4,3,2,1]))