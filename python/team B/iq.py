from QUESTION import question
from test import evaluate
from newfile import enoch

class Question:
    def quest(self):
        
        print("Pick an Option")

        list = [
        "Oliver Twist was published by who? (A)  Oliver Twist, (B) Charles Dickens: ",
        "What was the name of Alexander the great's horse? (A) Alonso, (B) Bucaphalus: ",
        "According to greek mythology, who is the god of thunder? (A) Ogun, (B) Thor: "
        ]

        score = []
        
        for el in list:
            question1 = question.ask_question(el)
            scoree = evaluate.evaluate_response(question1,"B")
            score.append(scoree)
        print(score)
        tiq = sum(score)

        print("Your IQ is:", tiq)        

        

Question = Question()

if __name__ == "__main__":
    enoch.welcome()

    
    Question.quest()

    enoch.goodbye()