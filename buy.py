"""

"""
commodity={
    101:{'name':'屠龙刀','price':8000},
    102:{'name':'倚天剑','price':17000},
    103:{'name':'九阳神功','price':16000},
    104:{'name':'乾坤大挪移','price':14000},
}
new_oder=[]
# 流程
#    显示商品
#    输入对应的数字，选择购买，或者结算
def show_all():
    for itme in commodity:
        # print(itme)
        print(f"商品编号:{itme},商品名称：{commodity[itme]['name']},商品单价{commodity[itme]['price']}元")

def get_number(meseage):
    while True:
        try:
            n=int(input(meseage))
            return n
        except:
            pass

def get_id():
    while True:
        n=get_number('请输入商品编号:')
        if n in commodity:
            return n
        print('商品编号不存在')
def get_oder():
    cid=get_id()
    count=get_number('请输入数量：')
    dict_oder={'cid':cid,'count':count}
    new_oder.append(dict_oder)
    print('添加到购物车成功')
def show_oder():
    for itme in new_oder:
        value=commodity[itme['cid']]
        print(f'您购买的是{value["name"]},数量是{itme["count"]}')
def tato_money():
    tato=0
    for itme in new_oder:
        value=commodity[itme['cid']]
        tato+=value['price']*itme['count']
    return tato

def pay(tato):
    print(f"总共需要支付{tato}元")
    while True:
        money=get_number('请支付：')
        if money>=tato:
            print(f'支付成功，找回{money-tato}元')
            new_oder.clear()
            break
        else:
            print('支付金额不足：')

def buy():
    show_all()
    get_oder()

def payment():
    taot=tato_money()
    show_oder()
    pay(taot)

def max_price():
    max_=max(list(commodity.values()),key=lambda itme:itme['price'])
    print(f"最贵的商品是:{max_["name"]},价格是{max_["price"]}元")
def sort_ascending_order(commodit=None):
    global commodity
    price_oder=sorted(commodit.items(),key=lambda key:key[1]['price'],reverse=True)
    new_dict={key:valus for key,valus in price_oder}
    commodity=new_dict
    show_all()

def select():

    while True:
        n = get_number('1键购买，2键结算,3键最贵商品，4键价格排降序：')
        if n==1:
            buy()
        elif n==2:
            payment()
        elif n==3:
            max_price()
        elif n==4:
            sort_ascending_order(commodity)

def start():
    select()

start()