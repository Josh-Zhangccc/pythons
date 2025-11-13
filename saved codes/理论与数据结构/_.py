class DecisionTree:
    def __init__(self, question, yes_node=None, no_node=None):
        self.question = question
        self.yes = yes_node
        self.no = no_node
    
    def make_decision(self):
        print(f"问题: {self.question}")
        answer = input("回答 (y/n): ").lower().strip()
        
        if answer == 'y':
            if self.yes is None:
                print("✓ 决策完成!")
                return True
            return self.yes.make_decision()
        else:
            if self.no is None:
                print("✓ 决策完成!")
                return False
            return self.no.make_decision()

# 创建简单的决策树：是否出门
decision_tree = DecisionTree("今天下雨吗?",
    yes_node=DecisionTree("有重要事情吗?",
        yes_node=DecisionTree("带伞了吗?", 
            yes_node=DecisionTree("那就出门吧!"),
            no_node=DecisionTree("在家待着吧")),
        no_node=DecisionTree("在家休息")),
    no_node=DecisionTree("天气很好，出门吧!"))

# 运行决策树
print("=== 决策树示例 ===")
decision_tree.make_decision()