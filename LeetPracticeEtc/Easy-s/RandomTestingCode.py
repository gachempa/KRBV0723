
class MyCars:

    def __init__(self,make='',year='',color='') -> None:
        self.make=make
        self.year=year
        self.color=color
        self.stars=0.0
    
    def ohmy(self,b):
        out=MyCars(self.make)
        
        def stars():
            self.stars=b
            print(stars)
        out.stars=stars()
        

car1=MyCars('Honda','2017','Silver')
car1.ohmy(3)
car1.stars
