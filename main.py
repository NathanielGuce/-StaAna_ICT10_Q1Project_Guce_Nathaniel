from pyscript import display, document

def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = " "
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("stock_qty").value

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + stock_qty.zfill(4)

    display("SKU: " + sku, target=('sku_output'))

def create_order(e):
    document.getElementById("show").innerHTML = ""

    items = [
        ("Shirts","item1"),
        ("Pants","item2"),
        ("Heavy-Duty Shades","item3"),
        ("Jacket","item4"),
        ("Shorts","item5")
    ]

    order = []
    total = 0

    for name, item_id in items:
        item = document.getElementById(item_id)

        if item.checked:
            price = int(item.value)
            order.append(name + " - ₱" + str(price))
            total += price

    if len(order) == 0:
        display("select at least one item.", target="show")
    else:
        display("Your order includes:", target="show")

        for item in order:
            display(item, target="show")

        display("Total: ₱" + str(total), target="show")
