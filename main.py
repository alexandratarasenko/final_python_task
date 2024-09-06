import matplotlib.pyplot as plt
def read_sales_data(file_path):
    list_sales = []
    file = open(file_path, "r", encoding = "utf-8")
    lines = file.readlines()
    file.close()
    for line in lines:
        items_line = line.split(", ")
        for i in range(0, len(items_line)):
            items_line[i] = items_line[i].replace('\n', '')
        list_sales.append({"product_name": items_line[0], "quantity":  int(items_line[1]),
                           "price":  int(items_line[2]), "date":  items_line[3]})
    return list_sales

def total_sales_per_product(sales_data):
    total_sales = {}
    for sale in sales_data:
        if sale['product_name'] in total_sales:
            total_sales[sale['product_name']] += sale['quantity'] * sale['price']
        else:
            total_sales[sale['product_name']] = sale['quantity'] * sale['price']
    return total_sales

def sales_over_time(sales_data):
    total_sales = {}
    for sale in sales_data:
        if sale['date'] in total_sales:
            total_sales[sale['date']] += sale['quantity'] * sale['price']
        else:
            total_sales[sale['date']] = sale['quantity'] * sale['price']
    return total_sales

if __name__ == '__main__':
   list_sales = read_sales_data(input('Введите путь к файлу: '))
   total_sales = total_sales_per_product(list_sales)
   total_sales_date = sales_over_time(list_sales)
   print ("Наибольшую выручку принес продукт ", max(total_sales, key = total_sales.get), ": ",total_sales.get(max(total_sales, key = total_sales.get)))
   print("Наибольшая сумма продаж была ", max(total_sales_date, key=total_sales_date.get), ": ", total_sales_date.get(max(total_sales_date, key=total_sales_date.get)))
   x = []
   y = []
   for key, value in total_sales.items():
       x.append(key)
       y.append(value)
   figure, axis = plt.subplots(2,1, figsize=(15,6))
   axis[0].bar(x, y)
   for i in range(len(x)):
       axis[0].text(i, y[i] + 20, y[i], ha = 'center')
   axis[0].tick_params('x', rotation=65)
   axis[0].set_title('Общая сумма продажи по каждому продкуту')
   x.clear()
   y.clear()
   for key, value in total_sales_date.items():
       x.append(key)
       y.append(value)
   axis[1].bar(x, y)
   for i in range(len(x)):
       axis[1].text(i, y[i] + 20, y[i], ha = 'center')
   axis[1].set_title('Общая сумма продажи по дням')
   axis[1].tick_params('x', rotation = 65)
   plt.tight_layout()
   plt.show()