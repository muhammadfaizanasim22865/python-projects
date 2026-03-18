import random

class FortuneTeller:
    def __init__(self):
        self.responses = [
            "Yes, definitely! ✨",
            "No way! ❌",
            "Maybe... 🤔",
            "Ask again later... ⏳","sochna bhi matt 😂",
            "It's possible! 😃"
        ]
        

    def tell_fortune(self):
        return random.choice(self.responses)

fortune = FortuneTeller()

while True:
    input("Ask a question and press Enter...   ")
    print(f" {fortune.tell_fortune()}")


