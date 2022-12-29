vote = {}


def check_vote(name):
    if vote.get(name):
        print("kick them out")
    else:
        vote[name] = True
        print("Let them vote")


check_vote("ezra")
check_vote("ezra")
check_vote("mania")
