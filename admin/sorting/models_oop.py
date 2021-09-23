from dataclasses import dataclass

@dataclass
class Calculator(object):
    num1 = int
    num2 = int

    @property
    def num1(self)-> int: return self._num1
    @num1.setter
    def num1(self, num1): self._num1 = num1
    @property
    def num2(self) -> int: return self._num2
    @num1.setter
    def num2(self, num2): self._num2 = num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def mulitple(self):
        return self.num1 * self.num2
    def divice(self):
        return self.num2 / self.num2


@dataclass
class Contacts(object):
    name = str
    phone = str
    email= str
    address = str

    def to_string(self):
        print(f'Infor \n name : {self.name} \n phone : {self.phone}\n email: {self.email} \n address : {self.address}')

    def set_contact(self)-> object:
        return

    def get_contact(self):
        ls = [self.name, self.email, self.email, self.address]
        i.to_string for i in ls

    def del_contact(self):
        for i, j in 



@dataclass
class Grade(object):
    pass





