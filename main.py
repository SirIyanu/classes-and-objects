class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name: str = name
        self.age: int = age
        self.tracks: list = tracks
        self.score: float = score

    print("details of new student:")
    
    def change_name(self, new_name):
            self.name = new_name
            print("Name: ", self.name)

    def change_age(self, new_name):
            self.name = new_name
            print("Name: ", self.name)

    def add_track(self, new_name):
            self.name = new_name
            print("Name: ", self.name)

    def get_score(self, new_name):
            self.name = new_name
            print("Name: ", self.name)

            



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(70.5)
