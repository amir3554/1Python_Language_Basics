class product():
    def __init__(self, id, name, price, count,) -> None:
        self._id = id
        self.name = name
        self._price = price
        self.count = count
        self.__SSN = "1234-5678-9012"
         
    def info(self):
        return f'the ID is : {self._id}, Name : {self.name}, Price : {self._price}, How much pieces are in the store {self.count}'
    
    def set_price(self, price):#داخل هذا التابع يمكن اضافة الشيفرات الازمة من اجل حماية من التعديل مثل التسجيل الى الموقع و امتلاك الصلاحيات الازمة
        self._price = price#يجب استدعاء التابع هذا من اجل تمرير السعر الديد اليه 

    def get_price(self):
        return f'The price is {str(self._price)} $'

    def discount(self, ratio):
        self._price = self._price - self._price * ratio
        return f'the discount has been made, the price is {self._price}, with ratio about {ratio}'
    
    def ADD_products(self, id, name = ''):
        pass

    def REMOVE_products(self, id, name = ''):
        pass

class Mobile(product):
    def __init__(self, id, name, price, count, battary, camera, selfi_camera, access_5G, storage, brand) -> None:
        super().__init__(id, name, price, count)
        self.battary = battary
        self.camera = camera
        self.selfi_camera = selfi_camera
        self.access_5G = access_5G
        self.storage = storage
        self.brand = brand

    def get_the_camara(self):
        return f'This mobile has a {self.camera} M pexel as the Main camera , and a {self.selfi_camera} M pexel as front camera.'
    
    def access_5g(self):
        if self.access_5G:
            print('This device can run 5 G.')
        else:
            print("This device can not run 5 G. ")

    def get_battary_info(self):
        return f'The device has {self.battary} M O battary.'
    

class Computer(product):
    def __init__(self, id, name, price, count, CPU, Grafics, RAM, disk_space, mother_board) -> None:
        super().__init__(id, name, price, count)
        self.CPU = CPU
        self.Grafics = Grafics
        self.RAM = RAM
        self.disk_space = disk_space
        self.mother_board = mother_board

    def Computer_Info(self):
        return f'The Name if the cumputer is {self.name}, The Price is {self._price} $, CPU: {self.CPU}, Grafics: {self.Grafics}, RAM: {self.RAM} GB, Disk Space :{self.disk_space}, The Mother Board is: {self.mother_board}'

class Monitor(product):
    def __init__(self, id, name, price, count) -> None:
        super().__init__(id, name, price, count)



