products = []
while True:
    name = input('輸入商品名稱: ')
    if name == 'q':
        break
    price = input('輸入商品價格: ')

    products.append([name, price])  #這種寫法
    #等同於下面寫法
    # p =[]
    # p.append(name)
    # p.append(price)
    #----
    # p = [name, price] #直接建立一格清單
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:  #txt 一般記事本存檔   csv可以用excel打開
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')