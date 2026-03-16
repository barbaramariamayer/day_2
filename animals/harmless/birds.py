class Birds:
    def __init__(self):
        self.members = ["sparrow", "robin", "duck"]

    def printMembers(self):
        print("We print all members of the bird class:")
        for member in self.members:
            print(f"\t{member}")