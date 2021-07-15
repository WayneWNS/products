import os # operating system 作業系統模組


#理想的function只做一件事。 refactor(重構程式)的核心概念，就是把程式碼不斷改寫成越來越小的function，讓function"盡量"只做一件事。
# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 繼續
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        products.append([name, price]) # 簡化版2
    print(products)
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1]) # 將小清單內的數值都印出來，並附上說明

# 寫入檔案；加入encoding='utf-8'來解決中文亂碼問題
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f: # 檔案也可存成txt/csv檔，csv較常用
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') # f.write 才是真正的寫入

def main(): # 程式最好有一個main() function 為程式的進入點
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在; 
        print('已存在檔案!')
        products = read_file(filename)
    else:
        print('未有紀錄。')

    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()

# refactor 重構