# Надо разобраться с классами и подклассами и ооп
# сегодня учил гит
# class Person:
  
#     def __init__(self, name):
#         self.name = name
#         print("Создан человек с именем", self.name)
     
#     def __del__(self):
#         print("Удален человек с именем", self.name)
  
# tom = Person("Tom")
# class lol:
#     def __init__(self, name, age):
#         self._name = name    # имя человека
#         self.age = age 
# lol2 = lol('Art', 22)
# print(lol2._name('Arthur'))
# print(lol._name())
class codewars:    
    def matrix(self, array): 
        self.array = array
        resu = array
        i = 0
        while len(resu) < i:
            if (resu[i][i]) < 0:
                (resu[i][i]) = 0
            else:
                (resu[i][i]) = 1
            i+=1
        return (resu)
           
matem = codewars
print(matem.matrix([[-1, 4, -5, -9, 3], 
                    [6, -4, -7, 4, -5], 
                    [3, 5, 4, -9, -1], 
                    [1, 5, -7, -8, -9], 
                    [-3, 2, 1, -5, 6]]))
