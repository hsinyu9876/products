import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #繼續,直接跳下一迴(不執行第7.8行)
            name,price = line.strip().split(',')
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_productions(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename,'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) +'\n')


def main():
    products = []
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案在不在同資料夾相對路徑
        print('yeah!找到檔案!')
        products = read_file(filename)
    else:
        print('找不到檔案QQ')
    products = user_input(products)
    print_productions(products)
    write_file(filename, products)

if __name__ == '__main__':
    main() #這邊如果不執行的話 那這個py檔什麼事都不做