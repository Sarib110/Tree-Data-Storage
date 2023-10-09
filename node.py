class Data:
    def __init__(sarib,value=None):
        sarib.data = value
        sarib.child = []
class Node:
    def __init__(sarib):
        sarib.root = Data()
    def Insert(sarib,word):
        word += "$"
        lst , index = sarib.search_by_letter(word,sarib.root.child,0)
        for i in range(index,len(word)):
            new_word = Data(word[i])
            lst.append(new_word)
            lst = lst[len(lst)-1].child
    def search_by_letter(sarib,word,lst,index):
        found = False
        var = None
        for element in lst:
            if element.data == word[index]:
                found = True
                var = element
        if found:
            return sarib.search_by_letter(word,var.child,index+1)
        return lst, index
    def Search(sarib,word):
        word += "$"
        lst , index = sarib.search_by_letter(word,sarib.root.child,0)
        if index == len(word):
            return True
        return False
project = Node()
project.Insert("Sarib")
print(project.Search("Sarib"))