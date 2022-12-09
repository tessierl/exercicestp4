#Crée par Lucas tessier
#Groupe 402

class StringFoo():
    def __init__(self):
        self.message = ""

    def set_string(self, string):
        self.message = string

    def print_string(self, ):
        print(self.message.upper())

kevun = StringFoo()
kevun.set_string("Encore le pick up de Kévun!")
kevun.print_string()

