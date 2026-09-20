from pyscript import display, document

def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = " "
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("stock_qty").value

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + stock_qty.zfill(4)

    display("SKU: " + sku, target=('sku_output'))

def create_order(e):
    '''displays the order summary based on the items selected'''
    document.getElementById("show").innerHTML = " "
    item1 = document.getElementById("item1").value
    item2 = document.getElementById("item2").value
    item3 = document.getElementById("item3").value
    item4 = document.getElementById("item4").value
    item5 = document.getElementById("item5").value
    

    order_summary = item1 + "\n" + item2 + "\n" + item3 + "\n" + item4 + "\n" + item5
    display("Your order includes:\n" + order_summary, target=('show'))
