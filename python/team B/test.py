from QUESTION import question

class evaluate:
    def evaluate_response(self, response, answer):
        if response.upper() == answer:
            score = 10
        else:
            score = 0
            
        return score

evaluate = evaluate()
