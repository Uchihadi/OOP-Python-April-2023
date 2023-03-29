#lex_auth_01275045546160947226
class Athlete:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    def running(self):
        if(self.gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
                                        
athlete1 = Athlete("Maria", "girl")
print(athlete1.running)