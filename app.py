from flask import Flask, render_template, abort
from models.product_model import get_all_products, get_product_by_id

app = Flask(__name__)

@app.route('/')
def home():
    products = get_all_products()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
