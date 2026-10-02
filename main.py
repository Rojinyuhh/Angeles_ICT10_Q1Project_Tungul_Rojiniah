from pyscript import document

# Variable for all of the producs and their prices (dictionary)
products = { 
    "chickjoy": ("Chickenjoy", 106),
    "yburger": ("Yumburger", 40),
    "spag": ("Jolly Spaghetti", 78),
    "bsteak": ("Burger Steak", 84),
    "rice": ("Rice", 46),
    "fries": ("Jolly Crispy Fries", 67),
    "gravy": ("Chickenjoy Gravy", 18),
    "pjuice": ("Pineapple Juice", 66),
    "ilat": ("Iced Latte", 87),
    "oj": ("Minute Maid Orange Juice", 77),
    "cokef": ("Coke Float", 84)
}

# this is the input part where when the checkbox is checked, the quantity input box will appear
def toggle_quantity(event):
    item_id = event.target.id


#it just means find the HTML element whose id is equal to ID + qty and assigning it to store in the variable quantity.

    quantity = document.querySelector(f"#{item_id}_qty")
    
    if event.target.checked: 
        quantity.style.display = "inline-block"
    else:
        quantity.style.display = "none"

#This is the main part of the code where the total price of the order will be calculated. 
def create_order(event):
    total = 0

# This part goes through the products dictionary one product at a time
    for item_id, product in products.items():
        name = product[0]
        price = product[1]

        checkbox = document.querySelector(f"#{item_id}")
        receipt_item = document.querySelector(f"#{item_id}_receipt") #this is important for the receipt part

        if checkbox.checked:
            quantity_box = document.querySelector(f"#{item_id}_qty") 
            quantity = int(quantity_box.value)

        #This makes sure that the quantity is always atleast 1
            if quantity <1:
                quantity = 1
                quantity_box.value = "1"

            item_total = price * quantity
            total = total + item_total
            receipt_item.style.display = "flex"
                
            document.querySelector(f"#{item_id}_name").innerText = f"{name} - {quantity}"
            document.querySelector(f"#{item_id}_price").innerText = f"₱{item_total}"
        else: 
            receipt_item.style.display = "none"

    document.querySelector("#receipt_total").innerText = f"₱{total}"
    document.querySelector("#receipt").style.display = "block"

# This is the for the SKU generator where it will generate a code based on the outputs of the user
def generate_sku(event):
    category = document.querySelector("#category").value
    product = document.querySelector("#product").value
    stock = document.querySelector("#stock").value

    if category == "" or product == "" or stock == "":

        document.querySelector("#sku_code").innerText = "Please complete all fields."
        document.querySelector("#sku_details").innerText = ""
        return
    
    category_code = category[:2].upper()
    product_code = product.replace(" ", "")[:3].upper()
    stock_code = str(stock)

    sku = category_code + product_code + stock_code

    sku= sku[:8]

    document.querySelector("#sku_code").innerText = sku
    document.querySelector("#sku_details").innerText = (f"Category: {category} |" f"Product: {product} |" f"Stock: {stock}")
