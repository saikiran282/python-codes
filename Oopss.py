class a:
    def __init__(self,n,a,g,v):
        self.name=n
        self.age=a
        self.gender=g
        self.village=v
    def personaldetails(self):
        print(f'my name is {self.name},{self.age} years old,from {self.village}')

sum=a(input('What is your name'),input('How old are you'),input('What is your gender'),input('Where are you from'))
sum.personaldetails()
