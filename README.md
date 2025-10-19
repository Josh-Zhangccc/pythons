# Python 学习笔记与代码库

> **我是香港中文大学（深圳）2025级人工智能学院的学生**，这份仓库记录了我大一期间从 Python 基础到 AI 试用的学习旅程。  
> 学习过程：基本语法 → 数据处理 → 可视化 → 机器学习 → 大模型调用
> **重点内容位于 `saved codes` 文件夹**
> 我原本把这个文件夹取名叫pythonthings的，但是感觉太长了，就叫pythons了😊
---

## 📚 我的学习路线

### 1️⃣ **Python 基础语法** → `基础/`
- 变量、数据类型、控制流、函数、类
- 重点：**自己写一遍，跑一跑**，才能理解深入😊

### 2️⃣ **数据处理：NumPy & Pandas** → `numpy&pandas/`
- NumPy：数组操作、数学运算
- Pandas：DataFrame、数据清洗、聚合
- 应用 ：处理 `data collection/` 中的数据

### 3️⃣ **数据可视化：Matplotlib** → `matplotlib/`
- 学习绘图基础：折线图、柱状图、散点图
- 实战：用 `data collection/` 中的数据绘制可视化图表
- 💡 **注意**：数据路径是本机路径，使用时请修改为你的本地路径！
- ✨ 后续的包如`seaborn`我也会继续学习的💪
  
### 4️⃣ **机器学习入门：Scikit-learn** → `scikit learn/`
- 学习经典算法：线性回归、KNN、决策树
- 实战：用 `data collection/` 中的数据训练模型
- 举个例子： ***分析我们高中的初始学号和最终高考成绩的关联***（在`numpy&pandas/`的`综合运用`里面）

### 5️⃣ **大模型探索：OpenAI & 本地部署** → `openai_test.py` + `ollamatest.py`
- 受 **StanfordTown** [^1]项目启发，开始探索 LLM（大语言模型）
- 学习 `openai` 包：调用 API、处理响应、构建对话
- 实验：本地部署 **Qwen3:8B** 模型（`ollamatest.py`）
  - 🧪 **实验结论**：本地部署功能“一言难尽😅”，CPU、GPU烧爆了都跑不动🥲，更重要的是**蠢**！，不仅输入有限制，而且对于上下文的理解十分差！
  - ✨ **tips**： 上下文的问题可以用`向量数据库`来解决一部分，但是本地部署就是很难用的说
  - 💡 **建议**：选择厂商 API（如 OpenAI、Anthropic、阿里云等），花点小钱没什么问题哒💰
[^1]:这个是我们学校的课程项目之一，具体代码参考[Stanford_town](https://github.com/joonspk-research/generative_agents)
---

## 🌟 重点推荐：`saved codes` 文件夹

这是我在学习过程中整理的“**代码库**”，包含：

- 常用函数
- 项目实战的代码
- 可复用的脚本（这是真的，很多分析直接套用就可以了😅）

---

## 🛠️ 如何使用

1. 克隆仓库：
   ```bash
   git clone https://github.com/Josh-Zhangccc/pythons.git
   ```
2. 进入项目目录：
    ```bash
    cd pythons
    ```
3. 查看你需要的代码，在`saved code`中！
4. **注意！：** `data collection`中的数据路径是本机路径，如果需要使用，请修改为您的本机路径！

## 📶 未来计划
-[] 深入了解数据结构，算法等计算机编程相关知识
-[] 学习matplotlib、tkinker、sklearn的高阶的库
-[] 了解前端的开发和UI相关
-[] 学习强化学习的基本内容以及机械学习的算法

***
## 🙋‍♂️ 联系我
如果你对我的代码有任何问题，或者有相关的内容想要跟我探讨，又或者想要和我一起学习编程/AI，欢迎联系！
- GitHub：`@Josh-Zhangccc`
- Emali:`18136412760@163.com` or `zuoxiaozhang7@gmail.com`
- School:`CUHK(SZ)-SAI`

