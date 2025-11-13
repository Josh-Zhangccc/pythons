class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # 存储子节点
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def __str__(self, level=0):
        # 美化打印树结构
        ret = "  " * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# 创建公司组织树
ceo = TreeNode("CEO (张三)")

# 添加部门
tech_dept = TreeNode("技术部")
sales_dept = TreeNode("销售部")
hr_dept = TreeNode("人力资源部")

ceo.add_child(tech_dept)
ceo.add_child(sales_dept)
ceo.add_child(hr_dept)

# 技术部下设团队
backend_team = TreeNode("后端团队")
frontend_team = TreeNode("前端团队")
ai_team = TreeNode("AI团队")

tech_dept.add_child(backend_team)
tech_dept.add_child(frontend_team)
tech_dept.add_child(ai_team)

# 添加员工
backend_team.add_child(TreeNode("工程师A"))
backend_team.add_child(TreeNode("工程师B"))
ai_team.add_child(TreeNode("AI研究员"))

print("公司组织架构:")
print(ceo)