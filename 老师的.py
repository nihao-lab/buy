# 体现过程，隐藏实现。

# 数据
dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []

def show_all_info():
    """
    打印商品所有信息
    Returns:

    """
    for key,valus in dict_commodity_info.items():
        print('商品编号：%s,商品名称：%s，商品单价：%s'%
              (key,valus['name'],valus['price']))

def get_id():
    """
    获取商品编号
    Returns:

    """
    while True:
        id=int(input('请输入商品编号：'))
        if id in dict_commodity_info:
            return id
        print('编号不存在，请重新输入')
def count_order():
    id=get_id()
    count=int(input('请输入购买的数量：'))
    order={'cid':id,'count':count}
    return order
def buying():
    """
    购买，只需要获取用户输入的数量信息，和商品编号。组成一个子订单
    Returns:

    """
    show_all_info()
    order=count_order()
    list_order.append(order)
    print('添加购物车成功')
def calculate_total_price():
    """
    计算总价，通过客户输入的信息，去遍历客户输入的信息，去跟商品店里直接拿
    Returns:

    """
    tato=0
    for oder in list_order:
        commodity=dict_commodity_info[oder['cid']]['price']
        count=oder['count']
        tato+=commodity*count
        print(tato)
    return tato
def show_order():
    """
    通过子订单，客户输入的信息，去商品店里那对应的信息，然后打印
    Returns:

    """
    for itme in list_order:
        order=dict_commodity_info[itme['cid']]
        print('商品：%s,单价：%s，数量：%s'%
              (order['name'],order['price'],itme['count']))
def pay(tato):
    """
    用户支付
    Args:
        tato:

    Returns:

    """
    while True:
        money=int(input('总价：%d元，请支付:'%tato))
        if money>=tato:
            print('支付成功，找回%s元'%(money-tato))
            list_order.clear()
            break
        else:
            print('金额不足')
def settle():
    """
    把结算需要准备的，打印商品信息，让用户支付
    Returns:

    """
    show_order()
    tato=calculate_total_price()
    pay(tato)

def mian():
    """主程序"""
    while True:
        print('1键购买，2键结算')
        number=int(input('请输入：'))
        if number==1:
            buying()
        elif number==2:
            settle()
mian()