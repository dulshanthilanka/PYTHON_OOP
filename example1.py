class employee():
    __name = None
    __age = 0

    def __inputname(self):
        self.__name = input("please enter the name : ")
    
    def __inputage(self):
        self.__age = int(input("please enter the age in number : "))

    def callmethod(self):
        self.__inputname()
        self.__inputage()
        print(self.__name)
        print(self.__age)
        
# ENCAPSULATION AND INHARITANCE IN SAME FILE