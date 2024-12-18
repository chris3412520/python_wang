def show_menu(name):
    """
    显示主菜单
    """
    print("----------主菜单----------")
    print(f"{name}, 您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额    [输入1]")
    print("存款        [输入2]")
    print("取款        [输入3]")
    print("退出        [输入4]")
    choice = input("请输入您的选择：")
    return choice


def query_balance(name, balance):
    """
    查询余额
    """
    print("----------查询余额----------")
    print(f"{name}, 您好，您的余额剩余：{balance}元")


def deposit(name, balance):
    """
    存款操作，用户输入存款金额后更新余额
    """
    print("----------存款----------")
    amount_str = input("请输入要存入的金额：")
    # 校验输入
    if not amount_str.isdigit():
        print("输入金额有误，请输入正整数！")
        return balance

    amount = int(amount_str)
    if amount > 0:
        balance += amount
        print(f"{name}, 您好，您存款{amount}元成功")
        print(f"{name}, 您好，您的余额剩余：{balance}元")
    else:
        print("存款金额必须大于0")
    return balance


def withdraw(name, balance):
    """
    取款操作，用户输入取款金额后更新余额
    """
    print("----------取款----------")
    amount_str = input("请输入要取出的金额：")
    if not amount_str.isdigit():
        print("输入金额有误，请输入正整数！")
        return balance

    amount = int(amount_str)
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"{name}, 您好，您取款{amount}元成功")
            print(f"{name}, 您好，您的余额剩余：{balance}元")
        else:
            print("余额不足，无法取款！")
    else:
        print("取款金额必须大于0")
    return balance


def main():
    # 初始化数据
    name = "周杰伦"
    balance = 5000000

    while True:
        choice = show_menu(name)
        if choice == '1':
            # 查询余额
            query_balance(name, balance)
        elif choice == '2':
            # 存款
            balance = deposit(name, balance)
        elif choice == '3':
            # 取款
            balance = withdraw(name, balance)
        elif choice == '4':
            # 退出
            print("欢迎下次使用，再见！")
            break
        else:
            print("输入有误，请重新输入！")


if __name__ == "__main__":
    main()