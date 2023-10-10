


def linearSearchProduct(productList, targetProduct):
   indices = []

   for index, product in enumerate(productList):
     if product == targetProduct:
       indices. apppend(index)

   return indices

product=["shoes","boot","loafer","shoes","sandol","shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(product, target2)
print(result)