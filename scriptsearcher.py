
#
#  A small utility to search directories of text files by keyword or phrase,
#  useful for finding a script from audio recordings. Assumes text files are
#  grouped together in directories one level deep.
#
#  Place this in the root directory containing all the script directories.
#

import os

print('Script Search\n')
print(' 1. Open up audio with missing or unknown script, listen to some files\n 2. Enter a word or phrase you hear (the shorter the better, start with single words)\n 3. Each subsequent search will be performed on the previously found script directory.\n    Keep going until you\'ve narrowed it down sufficiently. Check sound files to confirm.')

scriptList = []
while True:
    if not scriptList:
        for item in os.listdir('.'):
            if os.path.isdir(item):
                scriptList.append(item)
    searchKey = input('\nEnter word or phrase: ').lower()
    newResults = []
    for item in scriptList:
        for file in os.listdir(item):
            if file.endswith('.txt'):
                filePath = os.path.join(item, file)
                searchResult = open(filePath, 'r').read().lower().find(searchKey)
                if searchResult > 0:
                    newResults.append(item)
                    break
    if newResults:
        scriptList = []
        scriptList = newResults[:]
        for item in scriptList:
            print(item)
    else:
        print('No matches, try again...')
