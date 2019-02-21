#EVALUATION SYSTEM FOR ABSOLUTE BEGINNERS

#create a class to collect users data
class userdetails:
    #create a function to prompt users to input name
    def participant_details(self):
        self.name = input("Please enter your name:\n")#store name in self.name
        self.sex = input("What is your gender?\n")#store gender in self.sex
        self.age = input ("What is your present age?\n")#store age in self.age
        #display welcome message with username
        print("Welcome",self.name,"to DSCFUTA python group1 IQ evaluation system\nRemember instruction is a key!!!\n")

#create instance
userdetails = userdetails()
