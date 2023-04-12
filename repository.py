import db
from models import Product

def add_product(name: str, price: float) -> None:
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?,?)", (name, price))
    conn.commit()
    conn.close()


def update_product(product: Product) -> None:
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=?, price=? WHERE id=?", 
                   (product.name, product.price, product.id))
    conn.commit()
    conn.close()


def get_product(id: int) -> Product:
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (id,))
    row = cursor.fetchone()
    product = Product(row[0], row[1], row[2])
    conn.commit()
    conn.close()
    return product


def delete_product(id: int) -> None:
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()


def get_all_products() -> list:
    products = []
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        product = Product(row[0], row[1], row[2])
        products.append(product)
    return products 

