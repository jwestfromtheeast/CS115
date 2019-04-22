'''
Created on Apr 15, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

MENU = \
'''Enter a letter to choose an option: 
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit\n'''
import os.path

# List utility functions
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
    
# Music recommender functions
def updatePrefs(userName, userDict):
    """
    Takes care of the enter preferences option from the main menu.
    Updates the preferred artists of a user in the dictionary.
    """
    userList = []
    while True:
        userInput = input("Enter an artist that you like (Enter to finish): ")
        if not userInput:
            break
        userList.append(userInput)
    userList.sort()
    userDict[userName] = userList
    
def findBestUser(userName, userDict):
    """
    Finds the user with the most artists in common with the given user.
    Excludes private users denoted by '$'
    """
    users = userDict.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = num_matches(userDict[userName], userDict[user])
        if score > bestScore and user[-1] != '$' and userName != user:
            if len(drop_matches(userDict[userName], userDict[user])):
                bestScore = score
                bestUser = user
    return bestUser
    
def getRecs(userName, userDict):
    """
    Gets recommendations for a user based on the user they have the
    most in common with.
    """
    bestUser = findBestUser(userName, userDict)
    if bestUser:
        recs = drop_matches(userDict[userName], userDict[bestUser])
        return recs
    else:
        return []

def mostPopularName(userDict):
    """
    Returns the artist most liked by users. If there is a tie, print
    all artists with the most likes. List format to account for all answers
    """
    artists = []
    maxScore = 0
    artistScore = {}
    for userName, lst in userDict.items():
        for artist in lst:
            if artist in artistScore and userName[-1] != '$':
                artistScore[artist] += 1
            elif artist not in artistScore and userName[-1] != '$':
                artistScore[artist] = 1    
    for artist, score in artistScore.items():
            if score > maxScore:
                artists = [artist]
                maxScore = score
            elif score == maxScore:
                artists.append(artist)
    return artists

def mostPopularVotes(userDict):
    """
    Returns the # of likes of the artist most liked by users. If there is a tie, print
    the number once still.
    """
    maxScore = 0
    artistScore = {}
    for userName, lst in userDict.items():
        for artist in lst:
            if artist in artistScore and userName[-1] != '$':
                artistScore[artist] += 1
            elif artist not in artistScore and userName[-1] != '$':
                artistScore[artist] = 1    
    for score in artistScore.values():
            if score > maxScore:
                maxScore = score
    return maxScore

def mostPopularUser(userDict):
    """
    Returns the user with the most liked artists.
    """
    maxLen = 0
    user = []
    for userName, lst in userDict.items():
        if userName[-1] != '$' and len(lst) == maxLen:
            user.append(userName)
        elif userName[-1] != '$' and len(lst) > maxLen:
            maxLen = len(lst)
            user = [userName]
    return user
    
def loadUsers(fileName):
    """
    Loads the existing users from the file into a dictionary
    """
    inputDict = {}
    file = open(fileName, 'r')
    for line in file:
        if not line:
            break
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        inputDict[userName] = bandList
    file.close()
    return inputDict

def save(userDict, fileName):
    """
    Saves the current dictionary to the specified file
    """
    file = open(fileName, "w")
    for user in userDict:
        toSave = str(user) + ":" + ",".join(userDict[user]) + \
                    "\n"
        file.write(toSave)
    file.close()  
    
def main():
    """
    Runs the main functionality of the program.
    """
    if not os.path.isfile('musicrecplus.txt'):
        file = open('musicrecplus.txt', 'w')
        file.close()
    userDict = loadUsers('musicrecplus.txt')
    print("Welcome to the Music Recommender Plus.")
    name = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
    if name not in userDict:
        updatePrefs(name, userDict)
    while True:
        choice = input(MENU)
        if choice == 'e':
            updatePrefs(name, userDict)
        elif choice == 'r':
            recs = getRecs(name, userDict)
            if not recs:
                print("No recommendations available at this time")
            else:
                for rec in recs:
                    print(rec)
        elif choice == 'p':
            popular = mostPopularName(userDict)
            if not popular:
                print("Sorry, no artists found")
            else:
                for artist in popular:
                    print(artist)
        elif choice == 'h':
            popular = mostPopularVotes(userDict)
            if not popular:
                print("Sorry, no artists found")
            else:
                print(popular)
        elif choice == 'm':
            popular = mostPopularUser(userDict)
            if not popular:
                print("Sorry, no user found")
            else:
                for user in popular:
                    print(user)
        elif choice == 'q':
            save(userDict, 'musicrecplus.txt')
            break
        else:
            print("Invalid input")
        
   
if __name__ == "__main__": main()