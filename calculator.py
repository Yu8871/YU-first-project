"""
简易计算器项目
这是一个初级 Python 练习，演示了：
- 函数的定义和调用
- 异常处理 (try-except)
- 循环控制 (while)
- 用户输入和输出
"""

def add(a, b):
    """
    函数功能：计算两个数的和
    参数：a (数字), b (数字)
    返回值：两个数的和
    """
    return a + b


def subtract(a, b):
    """计算两个数的差"""
    return a - b


def multiply(a, b):
    """计算两个数的积"""
    return a * b


def divide(a, b):
    """
    计算两个数的商
    注意：需要检查除数是否为0
    """
    if b == 0:
        return "错误：不能除以0"
    return a / b


def show_menu():
    """显示菜单选项"""
    print("\n" + "="*30)
    print("     简易计算器")
    print("="*30)
    print("请选择操作：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 退出")
    print("="*30)


def get_number(prompt):
    """
    获取用户输入的数字，带错误处理
    参数：prompt (输入提示语)
    返回值：用户输入的数字 (float 类型)
    """
    while True:
        try:
            # 用户输入字符串，需要转换为浮点数
            num = float(input(prompt))
            return num
        except ValueError:
            # 如果用户输入的不是有效数字，给出提示
            print("❌ 输入无效，请输入一个有效的数字")


def main():
    """
    主函数：控制计算器的整体流程
    使用 while 循环不断接收用户选择
    """
    print("👋 欢迎使用简易计算器")
    
    # while True 表示无限循环，直到用户选择退出
    while True:
        show_menu()
        choice = input("请输入选项 (1-5): ").strip()
        
        # 如果用户选择退出
        if choice == "5":
            print("\n👋 感谢使用计算器，再见！\n")
            break
        
        # 如果用户选择了无效的选项
        if choice not in ["1", "2", "3", "4"]:
            print("❌ 无效的选项，请重新选择")
            continue
        
        # 获取两个数字
        num1 = get_number("请输入第一个数字: ")
        num2 = get_number("请输入第二个数字: ")
        
        # 根据用户选择执行相应的操作
        if choice == "1":
            result = add(num1, num2)
            print(f"\n✅ {num1} + {num2} = {result}\n")
        
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\n✅ {num1} - {num2} = {result}\n")
        
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\n✅ {num1} × {num2} = {result}\n")
        
        elif choice == "4":
            result = divide(num1, num2)
            print(f"\n✅ {num1} ÷ {num2} = {result}\n")


# 程序入口
# if __name__ == "__main__" 确保只在直接运行此文件时执行
if __name__ == "__main__":
    main()
