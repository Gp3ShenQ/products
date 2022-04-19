import os # os 全寫 -> operating system

#讀取檔案 #檢查檔案是否存在
def read_file(filename):
    products = []
        #讀取檔案
    with open (filename, 'r', encoding = 'utf-8')as f:
        for line in f :
            if '商品,價格' in line:
                continue #跳過
            name, price = line.strip().split(',') #strip 去頭尾空格''   split 使用(?)切割
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('輸入商品名稱: ')
        if name == 'q':
            break
        price = input('輸入商品價格: ')
        price = int(price)
        products.append([name, price])  #這種寫法
    print(products)
    return products
        #等同於下面寫法
        # p =[]
        # p.append(name)
        # p.append(price)
        #----
        # p = [name, price] #直接建立一格清單
    

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename , products):
    with open(filename, 'w', encoding='utf-8') as f:  #txt 一般記事本存檔   csv可以用excel打開
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
        #檢查檔案是否存在
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('yeah!找到')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv' , products)


main()