import json


class Product():
    MIN_PRODUCT_NAME_LENGTH = 5
    MIN_PRICE = 1.00

    def __init__(self, product_id: int, product_name: str, price: float):
        print('PRODUCT CONSTRUCTOR')
        self.product_id = product_id
        if len(product_name)<self.MIN_PRODUCT_NAME_LENGTH:
            raise Exception(f'Error: product name too short should be at least {self.MIN_PRODUCT_NAME}') 
        self.product_name = product_name.title()
        if price < self.MIN_PRICE:
            raise Exception(f'Error: product price too low should be at least {self.MIN_PRICE}')
        self.price = price

    def __str__(self):
        return json.dumps({
            'product_id': self.product_id,
            'product_name': self.product_name,
            'price': f'{self.price} $'
        })


class Book(Product):
    MIN_PAGES = 20

    def __init__(self, product_id, product_name, price, author: str, pages: int):
        print('BOOK CONSTRUCTOR')
        super().__init__(product_id, product_name, price)
        if not author:
            raise Exception('Author should be specified')
        self.author = author.title()
        if pages < self.MIN_PAGES:
            raise Exception('This is not a book')
        self.pages = pages

    def __str__(self):
        return json.dumps({
            'product_type': 'Book',
            'product_id': self.product_id,
            'product_name': self.product_name,
            'price': f'{self.price} $',
            'author': self.author,
            'pages': self.pages
        })


if __name__ ==  "__main__":
    my_product = Product(1, 'nivea cream', 5.00)
    print(my_product)
    book = Book(2, 'Nivea cream', 5, 'Shakespeare', 120)
    print(book)
