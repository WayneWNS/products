# 二維清單 = 清單之中包含清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name, price] # 簡化版1
	products.append(p)
print(products)
products[0][0]
