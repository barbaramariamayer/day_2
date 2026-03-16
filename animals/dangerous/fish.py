class Fish:
    def __init__(self):
        self.members = ["sharks", "piranhas", "barracudas"]

    def printMembers(self):
        print("We print all the members of the fish class:")
        for member in self.members:
            print(f"\t{member}")