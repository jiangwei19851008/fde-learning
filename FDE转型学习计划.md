# FDE 前沿部署工程师 · 学习计划

> 基于移动通信 BSS 行业背景的转型路线图（6-9 个月）

---

## 你为什么适合转 FDE

FDE = Forward Deployed Engineer，前沿部署工程师。三栖角色：

| 能力 | FDE 需要 | 你有的 |
|------|----------|--------|
| 业务理解 | 懂行业痛点和工作流 | BSS 十几年 + 产品经理 |
| 客户沟通 | 需求翻译 + 驻场交付 | 项目经理 + ToB 经验 |
| 工程落地 | 能端到端跑通 AI 应用 | 能看代码，捡起来很快（短板可补） |
| 质量把控 | 测试/评测 Agent 效果 | 测试工程师经验 |

**核心优势：行业经验 + 跨角色能力，是纯程序员没有的。** FDE 不要求代码大神，要求"写得出能跑的代码 + 听得懂客户的话"。

---

## 第一阶段：补代码 + AI 基础（2-3 个月）

**目标：捡回编程 + 跑通第一个 AI Demo**

- Python 速成（pandas、requests、async/await）
  - 练 10 个小脚本：爬数据、调 API、处理 Excel
- 大模型基础
  - Prompt 工程、Function Calling、RAG 原理
  - 用 Coze / Dify 搭 3 个 Agent（客服、数据查询、文档总结）
- LangChain 或 LlamaIndex（二选一）
  - 搭一个"基于内部文档问答"的 RAG Demo
- GitHub 上至少 3 个能跑的小项目

---

## 第二阶段：FDE 核心技能（3-4 个月）

**目标：能独立交付一个企业 AI 应用**

- Agent 编排：LangGraph、MCP 协议、多 Agent 协作
- Prompt 进阶：Context Engineering、结构化输出、评测集
- 工程部署：Docker + 简单云服务 + 向量数据库（Chroma/Milvus）
- 评测体系：Ragas 或 LangSmith 给 Agent 建评测集
- **关键产出**：一个 BSS 场景 AI 应用（如工单智能分派 + 知识库查询），能给同事演示

---

## 第三阶段：包装 + 求职（1-2 个月）

**目标：写出能打动人的简历，对内推渠道**

- 重写简历：用 FDE 语言讲 BSS 故事（不说"我做了个产品"，说"面对 X 客户 Y 痛点，设计 Z 方案交付落地"）
- 准备 2-3 个 BSS AI 化方案（智能客服、套餐推荐、故障诊断辅助）
- 脉脉 + 猎聘 + LinkedIn 搜"前沿部署工程师"或"FDE"
- 找熟人内推 > 海投

---

## 学习资源（免费/低成本）

| 类别 | 资源 |
|------|------|
| Python | B 站搜"Python 速成 2026"，20 小时以内教程 |
| LangChain | 官方文档 python.langchain.com + B 站"LangChain 从零到一" |
| RAG | LlamaIndex blog + 搜"RAG 论文 2026 最新进展" |
| Agent | Anthropic 官方 Agent 教程 + LangGraph 教程 |
| 实战 | GitHub awesome-llm-apps 挑小项目仿写 |

---

## 现在就能做的 3 件小事

1. **写 20 行 Python** 调通大模型 API（DeepSeek/豆包有免费额度），让它帮你分析 BSS 工单流程
2. **用 Coze / Dify 搭一个 BSS Agent** —— 比如"客服套餐推荐"，半天搞定
3. **收集 10 条 FDE JD**，把共同要求列出来当 checklist

---

_你的 BSS 经验就是最值钱的护城河。6-9 个月后，你比纯 CS 应届硕士更懂客户、更懂业务、更能交付。_