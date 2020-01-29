class A :
    att=0
    def get_p(self):
        print(self.att)

class B :
    att=10
    # def get_p(self):
    #     print("b")


class C :
    pass
    # def get_p (self):
    #     bonus=super().get_p()
    #     return bonus

class AB(B,A):
    pass

class AC(A,C):
    pass


gnu = AB()
gnu2=AC()


gnu.get_p()

gnu2.get_p()



