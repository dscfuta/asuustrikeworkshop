#EVALUATION SYSTEM FOR ABSOLUTE BEGINNERS

#Import My_Question
from My_Question import questions

#create your class to sum results
class iq_sum:
    #create a function
    def iqsum(self):
        #Create a variable that takes the total result(tr) from questions
        #divide the tr by 6 and multiply by 100 to get the variable in percentage
        #recall in My_Question 6 questions were asked and graded as 1 point
        #that is why we are dividing tr by 6
        self.qsum = int((questions.tr/6)*100)

#create the instance     
iqsum = iq_sum()
