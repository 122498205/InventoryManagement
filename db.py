import pymysql


class DB:
    def __init__(self):

        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='test')
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql,parm=None):
        try:
            self.cur.execute(sql,parm)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
db = DB()

def add_product(prodcts):
    product_name =str(prodcts[0])
    product_description =prodcts[1]
    unit =prodcts[2]
    unit_price =prodcts[3]
    print(type(product_name),product_description,unit,unit_price)

    sql =f"INSERT INTO Product (product_name, product_description, unit,unit_price) VALUES (%s,%s,%s,%s);"

    db.exec(sql,(product_name,product_description,unit,unit_price))

if __name__ == '__main__':
    add_product(["生抽","酱油","瓶",1])
    # add_product(["生抽","酱油","瓶","单价"])