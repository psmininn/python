class Bird:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def lay(self):
        print(f"{self.name}가(이) 알을 낳습니다.")

class Flyable:
    def flt(self):
        print("날아 다닙니다.")

class Eagle(Bird,Flyable):
    def crawl(self):
        print(f"{self.name}이 사냥합니다.")

class Penguine(Bird):
    def seim(self):
        print(f"{self.name}이 수영합니다.")
