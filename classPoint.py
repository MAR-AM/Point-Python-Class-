class  Point ():
    def __init__(self, abscisse = 0 , ordonne = 0):
        self.__abscisse = abscisse
        self.__ordonne = ordonne

    def getabscisse(self):
        return self.__abscisse
    
    def getordonne(self):
        return self.__ordonne
    
    def setabscisse(self, abscisse):
         self.__abscisse = abscisse
    
    def setordonne(self, ordonne):
         self.__ordonne = ordonne

    def Distance (self,point1):
         print("the distance is : {}".format( 0.5**((point1.getabscisse())**2-((self.getabscisse())**2)+((point1.getordonne())**2)-((self.getordonne())**2))),"cm")
    
    def Norme(self):
        print("the distance is : {}".format(0.5**((self.ordonne())**2+(self.abscisse())**2),"cm"))
     

