class A:
    def method_A(self):
        print("Method From A")

class B:
    def method_B(self):
        print("Method From B")

class C(A,B):
    def __method_C(self):
        print("Method From C")

test_obj = C()
print(test_obj.method_A)
test_obj.__method_A()