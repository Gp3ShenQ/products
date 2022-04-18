#讀取檔案
products = []
with open ('products.csv', 'r', encoding = 'utf-8')as f:
    for line in f :
        if '商品,價格' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])

print(products)

#讓使用者輸入
# products = []
while True:
    name = input('輸入商品名稱: ')
    if name == 'q':
        break
    price = input('輸入商品價格: ')
    price = int(price)
    products.append([name, price])  #這種寫法
    #等同於下面寫法
    # p =[]
    # p.append(name)
    # p.append(price)
    #----
    # p = [name, price] #直接建立一格清單
print(products)

#印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:  #txt 一般記事本存檔   csv可以用excel打開
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')