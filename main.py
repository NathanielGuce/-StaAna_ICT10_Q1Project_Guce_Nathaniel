from pyscript import display, document

def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = " "
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("stock_qty").value

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + stock_qty.zfill(4)

    display("SKU: " + sku, target=('sku_output'))