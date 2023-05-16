class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def getReal(self):
        return self.real
    def getImaginary(self):
        return self.imaginary
    def __str__(self):
        string = str(self.real) + "+" + str(self.imaginary) + "i"
        return string
    def negate(self):
        self.real *= -1
        self.imaginary *= -1
    def add_result(self, complexNum):
        newComplex = Complex(self.real + complexNum.real, self.imaginary + complexNum.imaginary)
        return newComplex
    def mul(self, complexNum):
        #(a + bi)x(c + di) = (ac - bd) + (ad + cb)i
        real = (self.real * complexNum.real) - (self.imaginary * complexNum.imaginary)
        comp = (self.real * complexNum.imaginary) + (complexNum.real * self.imaginary)
        newComplex = Complex(real, comp)
        return newComplex

def main():
    c1 = Complex(1,2)
    print("c1:", c1)
    c2 = Complex(3,4)
    print("c2:", c2)
    #print(c1.add_result(c2))
    print(c1.mul(c2))
    #(1 + 2i) * (3 + 4i) = (1*3 - 2*4) + (1*4 + 3*2)i = (-5) + 10i 



if __name__ == "__main__":
    main()
    