#question object
class question:
    def ask_question(self,question):
        response = input(question)
        return response

question = question()