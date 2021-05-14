import random

articles = [('shirt', 'S'), ('shirt', 'M'), ('shirt', 'L'), ('scarf', 'XXL'), ('scarf', 'M'), ('scarf', 'S'), ('glove', 'XL'), ('glove', 'S'), ('glove', 'M'), ('glove', 'L')]

articles = [ x * 10 for x in articles]


def restock(articles_type, size):
    articles.append((articles_type, size))
    print(articles)


def sell_any_article():
    random_article_to_sell = random.choice(articles)
    if random_article_to_sell in articles:
        articles.remove(random_article_to_sell)
        print(f'Article sold {random_article_to_sell}')
    else:
        print('Product out of stock')


def sell_last_article_added():
    last_article = articles.pop()
    print(last_article)


def holly_shop():
    sell_last_article_added()
    sell_any_article()
    restock('scarf', 'XXL')


if __name__ == "__main__":
    holly_shop()

 #requests
 #virtual env