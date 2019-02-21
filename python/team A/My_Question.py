#EVALUATION SYSTEM FOR ABSOLUTE BEGINNERS

#create a class that test iq
class myquestion:
    tr = 0 #tr means Total result
    Result_Question = [] #Result_Question is a list that stores each answer

    #create a function that contains Instruction
    def Rule(self):
        print("Write your result in upper case")#Display instruction

    #create a function for question 1    
    def Question1(self):
        self.Rule() #Call instruction function
        '''
        Display question and prompt to answer
        check if the answer is correct
        if the answer is correct increase the total result by 1
        and add 1 to the list of result questions
        if the answer is wrong add 0 to total result
        and add 0 to the list of result question
        '''
        w = str(input("What is the name of this club?\n"))
        if w == "DSC":
            self.tr += 1
            return self.Result_Question.append(1)
        else:
            self.tr = self.tr
            return self.Result_Question.append(0)

    #create a function for question 2
    def Question2(self):
        self.Rule() #Call instruction function
        '''
        Display question and prompt to answer
        check if the answer is correct
        if the answer is correct increase the total result by 1
        and add 1 to the list of result questions
        if the answer is wrong add 0 to total result
        and add 0
        '''
        w = str(input("What is the name of your university?\n"))
        if w == "FUTA":
            self.tr += 1
            return self.Result_Question.append(1)
        else:
            self.tr = self.tr
            return self.Result_Question.append(0)

    #create a function for question 3
    def Question3(self):
        self.Rule() #Call instruction function
        '''
        Display question and prompt to answer
        check if the answer is correct
        if the answer is correct increase the total result by 1
        and add 1 to the list of result questions
        if the answer is wrong add 0 to total result
        and add 0
        '''
        w = str(input("What year did Nigeria gain independence?\n"))
        if w == "1960":
            self.tr += 1
            return self.Result_Question.append(1)
        else:
            self.tr = self.tr
            return self.Result_Question.append(0)

    #create a function for question 4
    def Question4(self):
        self.Rule() #Call instruction function
        '''
        Display question and prompt to answer
        check if the answer is correct
        if the answer is correct increase the total result by 1
        and add 1 to the list of result questions
        if the answer is wrong add 0 to total result
        and add 0
        '''
        w = str(input("How many jews did adoif hitler kill?\n"))
        if w == "6000000":
            self.tr += 1
            return self.Result_Question.append(1)
        else:
            self.tr = self.tr
            return self.Result_Question.append(0)

    #create a function for question 5
    def Question5(self):
        self.Rule() #Call instruction function
        '''
        Display question and prompt to answer
        check if the answer is correct
        if the answer is correct increase the total result by 1
        and add 1 to the list of result questions
        if the answer is wrong add 0 to total result
        and add 0
        '''
        w = str(input("Do you enjoy this Workshop?\n"))
        if w == "YES":
            self.tr += 1
            return self.Result_Question.append(1)
        else:
            self.tr = self.tr
            return self.Result_Question.append(0)

    #create a function for question 6
    def Question6(self):
        self.Rule() #Call instruction function
        '''
        Display question and prompt to answer
        check if the answer is correct
        if the answer is correct increase the total result by 1
        and add 1 to the list of result questions
        if the answer is wrong add 0 to total result
        and add 0
        '''
        w = str(input("Will you love to come next time?\n"))
        if w == "YES":
            self.tr += 1
            return self.Result_Question.append(1)
        else:
            self.tr = self.tr
            return self.Result_Question.append(0)

questions = myquestion() #create instance
