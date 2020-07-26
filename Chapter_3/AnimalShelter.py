from Chapter_3.MyQueue import *


class AnimalShelter:

    def __init__(self):
        self.dogsQueue = MyQueue()
        self.catsQueue = MyQueue()
        self.allAnimalsQueue = MyQueue()

    def enqueue(self, animalType, animalId):
        if animalType == "dog":
            self.dogsQueue.add(animalId)
        if animalType == "cat":
            self.catsQueue.add(animalId)

        animalInfo = {
            "Type": animalType,
            "Id": animalId
        }
        self.allAnimalsQueue.add(animalInfo)

    def dequeueAny(self):
        print("Dequeued next in line..............")
        animalInfo = self.allAnimalsQueue.remove()
        animalType = animalInfo['Type']
        if animalType == "dog":
            self.dogsQueue.remove()
        if animalType == "cat":
            self.catsQueue.remove()

    def dequeueDog(self):
        print("Dog dequeued..............")
        dequeuedId = self.dogsQueue.remove()
        self.removeAnimalFromGeneralQueue(dequeuedId)

    def dequeueCat(self):
        print("Cat dequeued..............")
        dequeuedId = self.catsQueue.remove()
        self.removeAnimalFromGeneralQueue(dequeuedId)

    def printAllAnimals(self):
        print('')
        print("Current queue.............")
        current = self.allAnimalsQueue.first
        while current is not None:
            print(current.data)
            current = current.next

    def removeAnimalFromGeneralQueue(self, animalId):
        if self.allAnimalsQueue.first.data["Id"] == animalId:
            self.allAnimalsQueue.first = self.allAnimalsQueue.first.next
        else:
            current = self.allAnimalsQueue.first
            previous = current
            while current.data["Id"] != animalId:
                previous = current
                current = current.next
            previous.next = current.next


AnimalShelter = AnimalShelter()
AnimalShelter.enqueue("dog", 1)
AnimalShelter.enqueue("dog", 2)
AnimalShelter.enqueue("cat", 3)
AnimalShelter.enqueue("cat", 4)

AnimalShelter.printAllAnimals()

AnimalShelter.dequeueCat()
AnimalShelter.printAllAnimals()

AnimalShelter.dequeueAny()
AnimalShelter.printAllAnimals()
