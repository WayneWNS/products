# 二維清單 = 清單之中包含清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price]) # 簡化版2

print(products)
products[0][0]


for p in products:
	print(p) # 印出每一筆小清單
	print(p[0]) # 印出每個清單的第一個值，在這裡就是商品名稱
	print(p[0], '的價格是', p[1]) # 將小清單內的數值都印出來，並附上說明