class Mammals:
    def __init__(self):
        self.members = ["tiger", "elephant", "wildcat"]

    def printMembers(self):
        print("We print all the animals of  the mammal class:")
        for member in self.members:
            print(f"\t{member}")
