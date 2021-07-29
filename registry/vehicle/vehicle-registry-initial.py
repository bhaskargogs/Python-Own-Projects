import random
import string


class OldVehicleRegistry:

    def generate_vehicle_id_old(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license_old(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:

    def register_vehicle_old(self, brand: string):
        # Create a registry instance
        registry = OldVehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id_old(12)

        # Generate a license plate for the vehicle
        # using the first two characters of the vehicle ID
        license_plate = registry.generate_vehicle_license_old(vehicle_id)

        # Compute the catalogue price
        catalogue_price_old = 0
        if brand == "Tesla Model 3":
            catalogue_price_old = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price_old = 35000
        elif brand == "BMW 5":
            catalogue_price_old = 45000

        # Compute tax percentage (default 5% of the catalogue_price_old, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # Calculate the payable tax
        payable_tax = tax_percentage * catalogue_price_old

        # print out the vehicle registration information
        print("Registration complete, Vehicle information:")
        print(f"Brand: {brand}")
        print(f"ID: {vehicle_id}")
        print(f"License Type: {license_plate}")
        print(f"Payable Tax: {payable_tax}")


app = Application()
app.register_vehicle_old("BMW 5")
