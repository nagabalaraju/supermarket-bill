class Supermarket:
    def __init__(self):
        self.products = {
            'apple': 2.50,
            'banana': 1.50,
            'orange': 3.00,
            'bread': 2.00,
            'milk': 1.80
        }
        self.cart = {}

    def display_menu(self):
        print("Supermarket Product Menu:")
        for product, price in self.products.items():
            print(f"{product.capitalize()}: ${price:.2f}")

    def add_to_cart(self, product, quantity):
        if product in self.products:
            if product in self.cart:
                self.cart[product] += quantity
            else:
                self.cart[product] = quantity
            print(f"{quantity} {product}(s) added to the cart.")
        else:
            print("Invalid product.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for product, quantity in self.cart.items():
                price = self.products[product]
                total_price = price * quantity
                print(f"{product.capitalize()}: {quantity} x ${price:.2f} = ${total_price:.2f}")
            total_bill = sum(self.products[product] * quantity for product, quantity in self.cart.items())
            print(f"Total Bill: ${total_bill:.2f}")

    def generate_bill(self):
        self.view_cart()
        print("Thank you for shopping with us!")

def main():
    supermarket = Supermarket()

    while True:
        print("\nOptions:")
        print("1. Display Product Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Generate Bill")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            supermarket.display_menu()
        elif choice == "2":
            product = input("Enter the product you want to add to the cart: ").lower()
            quantity = int(input("Enter the quantity: "))
            supermarket.add_to_cart(product, quantity)
        elif choice == "3":
            supermarket.view_cart()
        elif choice == "4":
            supermarket.generate_bill()
            break
        elif choice == "5":
            print("Exiting the supermarket. Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()