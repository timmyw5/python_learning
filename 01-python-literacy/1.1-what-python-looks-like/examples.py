# ============================================
#  1.1 课堂示例：Python长什么样？
#  
#  这个文件是给你"看"的，不是给你"写"的。
#  打开它，从上到下读一遍，感受Python的长相。
# ============================================

# ------ 示例1：你认识的JSON，在Python里叫"字典" ------

student = {
    "name": "Timmy",
    "level": "beginner",
    "interests": ["爬虫", "AI", "机器学习"],
    "enrolled": True
}

# 读取字典里的值（和JSON的逻辑一样）
print(student["name"])        # 输出：Timmy
print(student["interests"])   # 输出：['爬虫', 'AI', '机器学习']


# ------ 示例2：函数 = 你自定义的Excel公式 ------

def greet(name):
    """跟某人打招呼"""
    print(f"你好，{name}！欢迎来到Python的世界。")

# 调用函数（就像在Excel里写 =SUM(A1:A10) ）
greet("Timmy")
greet("同学")


# ------ 示例3：条件判断 = Excel的IF函数 ------

score = 78

if score >= 90:
    grade = "优秀"
elif score >= 70:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "需要加油"

print(f"分数{score}，等级：{grade}")


# ------ 示例4：循环 = 对一堆东西逐个处理 ------

cities = ["北京", "上海", "深圳", "广州"]

for city in cities:
    print(f"正在查询{city}的天气...")

# 上面的循环会输出：
# 正在查询北京的天气...
# 正在查询上海的天气...
# 正在查询深圳的天气...
# 正在查询广州的天气...


# ------ 示例5：一个"真实"的小工具 ------

def weather_report(city_name):
    """一个迷你天气查询工具"""
    database = {
        "北京": {"temp": 22, "weather": "晴天"},
        "上海": {"temp": 19, "weather": "多云"},
        "深圳": {"temp": 28, "weather": "雷阵雨"},
    }

    if city_name in database:
        data = database[city_name]
        print(f"🌤️ {city_name}：{data['temp']}°C，{data['weather']}")
    else:
        print(f"❌ 没有找到{city_name}的天气数据")

# 试试看
weather_report("深圳")
weather_report("成都")
