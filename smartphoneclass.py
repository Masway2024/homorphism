# Parent class - Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.__battery_percentage = battery_percentage  # Encapsulated attribute

    # Method to check battery percentage
    def check_battery(self):
        return f"The battery percentage is {self.__battery_percentage}%"
    
    # Method to simulate charging the phone
    def charge(self, amount):
        if 0 < amount <= 100:
            self.__battery_percentage = min(self.__battery_percentage + amount, 100)
        return f"Charging... Battery now at {self.__battery_percentage}%"

    # Public method to get the battery status
    def get_battery(self):
        return self.__battery_percentage

# Subclass - Smartphone with Face Recognition
class SmartPhoneWithFaceID(Smartphone):
    def __init__(self, brand, model, battery_percentage, face_recognition_enabled):
        super().__init__(brand, model, battery_percentage)
        self.face_recognition_enabled = face_recognition_enabled
    
    # Overriding the check_battery method to add more functionality
    def check_battery(self):
        base_message = super().check_battery()
        return f"{base_message} - Face Recognition: {'Enabled' if self.face_recognition_enabled else 'Disabled'}"

# Creating an object of Smartphone
phone1 = Smartphone("Samsung", "Galaxy S21", 85)
print(phone1.check_battery())
print(phone1.charge(10))

# Creating an object of SmartphoneWithFaceID
phone2 = SmartPhoneWithFaceID("Apple", "iPhone 13", 75, True)
print(phone2.check_battery())
