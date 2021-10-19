class ComplexNumbers:
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def __add__(self, other):
        my_num_1 = self.arg_1 + other.arg_1
        my_num_2 = self.arg_2 + other.arg_2
        return complex(my_num_1, my_num_2)


    def __mul__(self, other):
        my_num_1 = self.arg_1 * other.arg_1 - self.arg_2 * other.arg_2
        my_num_2 = self.arg_2 * other.arg_1 - self.arg_1 * other.arg_2
        return complex(my_num_1, my_num_2)


my_complex_num_1 = ComplexNumbers(3, -2)
my_complex_num_2 = ComplexNumbers(6, 9)

print(my_complex_num_1 + my_complex_num_2)
print(my_complex_num_1 * my_complex_num_2)