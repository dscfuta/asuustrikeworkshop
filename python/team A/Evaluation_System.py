#EVALUATION SYSTEM FOR ABSOLUTE BEGINNERS 

#Import Instances from other group members

#import userdetails from User_details created by Joy
from User_Details import userdetails

#import questions from My_Question created by David
from My_Question import questions

#import iqsum from Evaluation_Sum created by Deji
from Evaluation_Sum import iqsum

#create a class to compile all the instances in an INIT function
class evaluation:
    #create init function
    def __init__(self):
        #call participant_details from userdetails
        userdetails.participant_details()
        #call all questions from questions
        questions.Question1()
        questions.Question2()
        questions.Question3()
        questions.Question4()
        questions.Question5()
        questions.Question6()
        #call the sum
        iqsum.iqsum()

    #create an output function to display result   
    def output(self):
        #display the results
        print("\nThank you very much this is your result") #display appreciation for participating in the test
        """
        Display result in this format
        Name:
        Gender:
        Age:
        IQ:
        """
        print("\nNAME:", userdetails.name,
              "\nGENDER:", userdetails.sex,
              "\nAGE:", userdetails.age,
              "\nIQ:", str(iqsum.qsum) + "%")

evaluation = evaluation() #create instance
evaluation.output() #call output function

#ask users for options
k = int(input("\nTo check your score type 1\nTo check for the questions you missed type 2\nTo quit enter 3\nInput number: "))

if k == 1:
    c = questions.tr
    print(c)
elif k == 2:
    c = questions.Result_Question
    print (c)
else:
    quit()
