# 二維清單 = 清單之中包含清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price]) # 簡化版2

print(products)

for p in products:
	print(p[0], '的價格是', p[1]) # 將小清單內的數值都印出來，並附上說明

# 寫入檔案時加入encoding='utf-8'來解決中文亂碼問題
with open('products.csv', 'w', encoding = 'utf-8') as f: # 檔案也可存成txt/csv檔，csv較常用
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # f.write 才是真正的寫入