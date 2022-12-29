from collections import deque
def person_is_seller(name):
    return name [-1] == 'm'
graph = {}
graph["you"]=["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jhonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"] = []
graph["jhonny"] = []

def search(name):
    search_queue = deque()
    search_queue += [name]
    searched = set()