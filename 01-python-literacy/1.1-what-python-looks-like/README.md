# 1.1 Python长什么样？

> 🎯 **本节目标**：看到一段Python代码，不慌，能认出它的基本"长相"。
>
> ⏱️ **预计用时**：5-10分钟阅读 + 5分钟测验
>
> 📌 **不用背**：本节出现的所有细节都不需要记忆，只需要建立"见过"的感觉。

---

## 🌉 从你已经认识的东西出发

你说你认识JSON。太好了，看看这个：

```json
{
    "name": "Timmy",
    "age": 25,
    "hobbies": ["爬虫", "AI", "学Python"],
    "is_student": true
}
```

现在看Python版本的同一件事：

```python
person = {
    "name": "Timmy",
    "age": 25,
    "hobbies": ["爬虫", "AI", "学Python"],
    "is_student": True
}
```

**发现了吗？** 几乎一模一样！只有两个小区别：
1. Python里多了 `person = ` —— 这叫**赋值**（给这个数据起个名字）
2. `true` 变成了 `True` —— Python的布尔值首字母大写

> 💡 **你已经会读Python的字典了。** JSON本来就是从编程语言的数据结构借来的。

---

## 👀 Python代码的"长相"特征

我们来看一段完整的Python代码，不需要理解每一行，只需要感受它的**外观特征**：

```python
# 这是一个简单的天气查询工具

def check_weather(city):
    """查看指定城市的天气"""
    weather_data = {
        "北京": {"temp": 22, "condition": "晴"},
        "上海": {"temp": 19, "condition": "多云"},
        "深圳": {"temp": 28, "condition": "雷阵雨"},
    }

    if city in weather_data:
        info = weather_data[city]
        print(f"{city}：{info['temp']}°C，{info['condition']}")
    else:
        print(f"抱歉，没有{city}的数据")

# 使用这个工具
check_weather("深圳")
check_weather("成都")
```

别被吓到！你不需要理解每一行。我们只看**长相**：

### 特征1：# 号 = 注释（给人看的，电脑忽略）

```python
# 这是一个简单的天气查询工具
```

就像Word文档里的批注。以 `#` 开头的内容是写给人看的笔记，Python执行时会直接跳过。

> 🔗 **Excel类比**：像Excel单元格里的备注/批注，不参与计算。

### 特征2：缩进 = 层级关系（Python的灵魂）

```python
def check_weather(city):
    weather_data = {        # ← 往右缩进了，表示"属于"上面那行
        "北京": {"temp": 22},
    }
    if city in weather_data: 
        info = weather_data[city]  # ← 又缩进了，表示"属于"if
```

Python用**缩进（空格）** 来表示"谁属于谁"。这是Python最独特的地方——大多数其他语言用 `{ }` 花括号，Python用空格。

> 🔗 **JSON类比**：JSON也有缩进对吧？但JSON的缩进只是为了好看。Python的缩进**有实际意义**——缩进错了，代码就报错！

### 特征3：def = 定义一个功能（函数）

```python
def check_weather(city):
```

`def` 是 "define"（定义）的缩写。这行在说："我定义了一个叫 `check_weather` 的功能，它需要一个 `city` 参数。"

> 🔗 **Excel类比**：你在Excel里用 `=SUM(A1:A10)`，`SUM` 就是一个函数。`def` 就是在创建你自己的 `SUM`。

### 特征4：if/else = 做选择

```python
if city in weather_data:
    # 找到了，显示天气
else:
    # 没找到，说抱歉
```

> 🔗 **Excel类比**：就是 `=IF(条件, 结果A, 结果B)`，只是换了个写法。

### 特征5：冒号 `:` = "接下来是我的内容"

注意到了吗？`def`、`if`、`else` 后面都有个冒号 `:`。

```python
def check_weather(city):    # ← 冒号
    ...
if city in weather_data:    # ← 冒号
    ...
else:                       # ← 冒号
    ...
```

冒号的意思是："下面缩进的内容都归我管。" 就像文章里写"注意以下几点："然后列要点。

---

## 📋 总结卡片

| 你看到的 | 它是什么 | 一句话解释 |
|---------|---------|-----------|
| `#` | 注释 | 给人看的笔记，电脑忽略 |
| 缩进（空格） | 代码层级 | 谁属于谁，缩进错了会报错 |
| `def xxx():` | 函数定义 | 创建一个可复用的功能 |
| `if/else` | 条件判断 | 像Excel的IF函数 |
| `:` | 冒号 | "下面的内容归我管" |
| `= ` | 赋值 | 给数据起个名字 |
| `{ }` 在Python中 | 字典 | 你认识的JSON，几乎一样 |
| `True/False` | 布尔值 | 和JSON的true/false一样，只是首字母大写 |

> 📌 **再说一次：以上都不用背。** 下次看到代码时能"嗯，这个我见过"就够了。

---

## 接下来

完成下面的小测验，通过后我们进入 1.2「给东西起名字」。

👉 **测验文件**：[`quiz_1_1.py`](./quiz_1_1.py)

