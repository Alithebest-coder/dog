class dog:
    species="mamal"
    def __init__(self,name,age):
        self.a=name
        self.g=age
obj=dog("dog",47)
obj2=dog("bob jr",10)
print (obj.species,obj.a,obj.g)
print (obj2.species,obj2.a,obj2.g)