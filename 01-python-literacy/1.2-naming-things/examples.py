# ============================================
#  1.2 课堂示例：给东西起名字
#
#  从上到下读一遍，感受变量赋值的各种写法。
# ============================================

# ------ 基本赋值：给值贴标签 ------

username = "Timmy"
age = 25
is_learning = True

print(username)       # 输出：Timmy
print(age)            # 输出：25
print(is_learning)    # 输出：True


# ------ 标签可以"换贴" ------

mood = "开心"
print(mood)           # 输出：开心

mood = "超级开心"
print(mood)           # 输出：超级开心（覆盖了旧值）


# ------ 用计算结果赋值 ------

base_price = 100
discount = 0.8
final_price = base_price * discount

print(final_price)    # 输出：80.0

# 你在Excel里写 =A1*0.8 就是同一件事


# ------ 用别的变量赋值 ------

city_a = "深圳"
city_b = city_a       # city_b 也变成了 "深圳"

print(city_b)         # 输出：深圳


# ------ 一行赋多个值 ------

x, y, z = 10, 20, 30
print(x)              # 10
print(y)              # 20
print(z)              # 30


# ------ 好名字 vs 烂名字 ------

# ❌ 别人看到一脸懵
a = 3
b = 50
c = a * b

# ✅ 一目了然
quantity = 3
unit_price = 50
total_cost = quantity * unit_price

# 两段代码做的事完全一样，但第二段你一眼就懂


# ------ f-string 里用变量（回顾1.1的疑问） ------

product = "Python课程"
price = 0
print(f"{product}的价格是{price}元")  # 输出：Python课程的价格是0元

# f"..." 里的 {变量名} 会被替换成变量的值
# 不加f的话，{product} 就是原样输出的普通文字
