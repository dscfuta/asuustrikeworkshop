class Enoch:

    def welcome(self): # 
        self.name = input("Enter name: ") #asking for the user's name
        self.age = input("Enter age: ") #asking for the user's age
        self.sex = input("Enter your sex; enter (M) for Male and (F) for Female: ")
        self.sex = self.sex.upper() #setting self.sex in uppercase

        if self.sex == 'M':
            print("HEllo,",'Mr.',self.name,'you are welcome online')

        elif self.sex == "F":
            print('Hello,',"Mrs.",self.name,"you are welcome online")

        else:
            print("Hello,",self.name,"you are welcome online ")


    def goodbye(self):
          print("Getting out of here so soon!")
          if self.sex == 'M':
              print("Goodbye,",'Mr.',self.name,'have a nice day')

          elif self.sex == "F":
              print('Goodbye,',"Mrs.",self.name,"have a nice day")

          else:
              print("Goodbye,",self.name,"have a nice day")

enoch = Enoch()