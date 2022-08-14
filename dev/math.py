
class Maths:

    def __init__(self):
        pass
    
    def add_num(self, a, b):
        return (a + b)
    
    def divide(self, a, b):
        if a == 0:
            raise ZeroDivisionError("denominator value is zero can not divide")
        else:
            return int(b/a)
        
    def data(self, a):
        if a < 1:
            raise ValueError("less the 1 Error")
    
      

if __name__ == "__main__":
    cl_ = Maths()
    print(cl_.add_num(1, 2))
    print(cl_.divide(2, 4))
    print(cl_.data(0))