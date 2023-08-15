import pandas as pd
from fpdf import FPDF

df = pd.read_csv('articles.csv')


class Receipt:
    def __init__(self, article):
        self.article = article

    def generate(self):
        content = f'''
        Receipt nr.{self.article.id}
        Article: {self.article.name}
        Price: {self.article.price}'''

        return content

    def to_pdf(self, filepath):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=0, h=12, txt=self.generate(), align='L', ln=1)
        pdf.output(filepath)


class Article:
    def __init__(self, id):
        self.id = id

    def in_stock(self):
        stock = df.loc[df['id'] == self.id, 'in stock'].squeeze()
        if stock <= 0:
            return False
        return True

    def purchase(self, n=1):
        df.loc[df['id'] == self.id, 'in stock'] -= n
        df.to_csv('articles.csv', index=False)
        return Receipt(self)

    @property
    def name(self):
        return df.loc[df['id'] == self.id, 'name'].squeeze()

    @property
    def price(self):
        return df.loc[df['id'] == self.id, 'price'].squeeze()

    @staticmethod
    def get_all():
        return df


print(Article.get_all())
id = int(input('Enter article id to buy: '))
article = Article(id)
if article.in_stock():
    print(article.purchase().to_pdf('reciept.pdf'))
else:
    print('Sorry, the article you selected is out of stock')
