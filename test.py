import json
from pathlib import Path

class StockApp:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, stock):
        found = self.find_product(name)
        if found is not None:
            return False
        new_product = {"name": name, "stock": stock}
        self.products.append(new_product)
        return True

    def show_products(self):
        if self.products == []:
            print("商品がありません")
            return
        
        for product in self.products:
            print(f"name:{product['name']}\nstock:{product['stock']}")
    
    def find_product(self, name):
        for product in self.products:
            if product["name"] == name:
                return product
        return None

    def update_stock(self, name, new_stock):
        update_product = self.find_product(name)
        if update_product is None:
            return False
        update_product["stock"] = new_stock
        return True

    def delete_product(self, name):
        del_product = self.find_product(name)
        if del_product is None:
            return None
        self.products.remove(del_product)
        return del_product

    def save_to_file(self):
        with open("products.json","w", encoding="utf-8") as f:
            json.dump(self.products, f)
        print("保存できました")

    def load_from_file(self):
        if not Path("products.json").exists():
            return
        with open("products.json","r", encoding="utf-8") as f:
            self.products = json.load(f)

#mainに付随する機能
def ask_name():
    while True:
        name = input("商品名を入力してください").strip()
        if name == "":
            print("空白は無効です。商品名を入力してください")
        else:
            return name
    
def ask_int():
    while True:
        stock = input("数量を入力してください").strip()
        try:
            stock = int(stock)
            if stock < 0:
                print("0以上を入力してください")
            else:
                return stock
        except ValueError:
            print("数字を入力してください")

def show_all_products(rows):
    if rows == []:
        print("商品がありません")
        return
    for name, stock in rows:
        print(f"name:{name}, stock:{stock}")

#SQL
def add_product_db(conn, name, stock):
    cursor = conn.cursor()
    sql = "INSERT INTO products (name, stock) VALUES (?,?)"
    cursor.execute(sql, (name, stock))
    conn.commit()

def get_all_products(conn):
    cursor = conn.cursor()
    sql = "SELECT name, stock FROM products"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def find_product_db(conn, name):
    cursor = conn.cursor()
    sql = "SELECT name, stock FROM products WHERE name = ?"
    cursor.execute(sql(name,))
    result = cursor.fetchone()
    return result

def update_stock_db(conn, name, new_stock):
    product = find_product_db(name)
    if product is None:
        return False
    cursor = conn.cursor()
    cursorexe

def main():
    app = StockApp()
    app.load_from_file()
    while True:
        print("商品在庫管理アプリ")
        print("1: 追加")
        print("2: 一覧表示")
        print("3: 検索")
        print("4: 数量更新")
        print("5: 商品削除")
        print("6: 保存")
        print("0: 終了")
        select = input("メニューから機能を選んでください").strip()

        if select == "1":
            name = ask_name()
            stock = ask_int()
            result = app.add_product(name, stock)
            if result:
                print("追加に成功しました")
            else:
                print("すでに登録されています")

        elif select == "2":
            rows = get_all_products(conn)
            show_all_products(rows)

        elif select == "3":
            name = ask_name()
            result = find_product_db(conn, name)
            if result is None:
                print("商品が見つかりませんでした")
            else:
                name, stock = result
                print("次の商品が見つかりました")
                print(f"name:{name}\nstock:{stock}")

        elif select == "4":
            name = ask_name()
            new_stock = ask_int()
            result = app.update_stock(name, new_stock)
            if result:
                print("次の商品の数量を変更しました")
                print(f"name:{name}\nstock:{new_stock}")
            else:
                print("商品が見つかりませんでした")

        elif select == "5":
            name = ask_name()
            deleted = app.delete_product(name)
            if deleted is None:
                print("商品が見つかりませんでした")
            else:
                print("次の商品を削除しました")
                print(f"name:{deleted['name']}\nstock:{deleted['stock']}")

        elif select == "6":
            app.save_to_file()

        elif select == "0":
            break
        else:
            print("1~5,0の数字を入力してください")

if __name__ == "__main__":
    main()
        