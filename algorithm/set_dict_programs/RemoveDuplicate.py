# Set program: Remove duplicates from a list using a set

def setSymmatricDifference():
    set_value1 = {12, 14, 18 , }
    set_value2 = {15, 14, 12}
    print("Set 1 value : ", set_value1)
    print("Set 2 value : ", set_value2)

    print("Symmatric Differenc of 2 sets : ", set_value1.symmetric_difference(set_value2))

def removeElement():
    languages = {'Swift', 'Java', 'Python'}

    print('Initial Set:', languages)

    # remove 'Java' from a set
    removedValue = languages.discard('Java')

    print('Set after remove():', languages)

removeElement()
setSymmatricDifference()