import sqlite3

def get_connection():
    return sqlite3.connect('data/products.db')

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, price, image FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, price, image FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product