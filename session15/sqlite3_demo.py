import sqlite3
db = sqlite3.connect('stocks.db')
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 153.48),
    ('FB', 150, 168.42),
    ('MSFT',100, 74.69),
    ('SNAP', 75, 14.53)
]
c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

for row in db.execute('select * from portfolio'):
    print(row)


min_price = 100

print('\nExpensive Stocks:')
for row in db.execute('select * from portfolio where price > ?',
                         (min_price,)):
    print(row)    
