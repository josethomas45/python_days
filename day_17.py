class Car:
    def __init__(self,brand,model,year,mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage


    def display_info(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Mileage: {self.mileage}')

    def drive(self,km):
        self.mileage += km
        print(f'\n\nDrove {km} km.\n New mileage: {self.mileage} km')

car1 = Car('Toyota','Corolla',2019,mileage=1000)
car2 = Car('Honda','Civic',2018,mileage=500)

print('Car 1 in detail:'
      '\n-----------------')
car1.display_info()
print('\nCar 2 in detail:'
      '\n-----------------')
car2.display_info()

car1.drive(100)
print('\n Car 1 after driving 100 km:'
      '\n-----------------------------')   
car1.display_info()


        