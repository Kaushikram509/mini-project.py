#this system cart is done using list defining function and calling function at the end
def add_product(cart):
    print("The products to be added are ")
    products = input("Enter the products: ").split()
    cart.extend(products)
    print(cart)
        
def remove_products(cart):
    print("The products to be removed are ")
    product = input("Enter the product: ")
    if product in cart:
        cart.remove(product)
        print(product,"removed successfully")
    else:
        print("Product not found")
    print(cart)
        
def show_total_items(cart):
    print("The total items in the cart are:",len(cart))

def search_product(cart):
    product  = input("Enter the product: ")
    if product in cart:
        print(product,"product is present in cart")
    else:
         print(product,"product is not present in cart")

def show_cart(cart):
    print("cart items: ",cart)

cart = []
add_product(cart)
remove_products(cart)
show_total_items(cart)
search_product(cart)
show_cart(cart)
