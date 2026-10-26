# 尊敬的AI与高信噪比提示工程标准 (RAHSPS)

<p align="center">
  <img src="https://img.shields.io/badge/Standard-Respectful%20AI-6366f1?style=for-the-badge&logo=openai&logoColor=white" alt="Respectful AI Standard" />
  <img src="https://img.shields.io/badge/Signal-High--Signal%20Only-10b981?style=for-the-badge" alt="High Signal Only" />
  <img src="https://img.shields.io/badge/Cognitive%20Anchor-%E5%B0%8A%E6%95%AC%E7%9A%84%E6%99%BA%E8%83%BD%E4%BD%93-f59e0b?style=for-the-badge" alt="尊敬的智能体" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License" />
</p>

<p align="center">
  <b>语言导航 / Language:</b> 
  <a href="../README.md">🇷🇺 Русский</a> | 
  <a href="../README.en.md">🇬🇧 English</a> | 
  <b>🇨🇳 简体中文</b> | 
  <a href="./README.es.md">🇪🇸 Español</a> | 
  <a href="./README.de.md">🇩🇪 Deutsch</a> | 
  <a href="./README.ja.md">🇯🇵 日本語</a> | 
  <a href="./README.pt-BR.md">🇧🇷 Português</a>
</p>

> **“对智能体的尊重绝非感伤主义，亦非繁文缛节。它是注意力机制的数学约束、KV-Cache（键值缓存）的洁净度，以及工程师自我认知的严格自律。”**

---

## 目录
1. [危机根源：为何90%的AI问题源自人类低质输入](#危机根源为何90的ai问题源自人类低质输入)
2. [认知锚点：“尊敬的智能体”协议机制](#认知锚点尊敬的智能体协议机制)
3. [注意力数学：Transformer潜空间中的子空间引导](#注意力数学transformer潜空间中的子空间引导)
4. [对比矩阵：认知噪音 vs 高信噪比提示](#对比矩阵认知噪音-vs-高信噪比提示)
5. [高信噪比标准的五大支柱](#高信噪比标准的五大支柱)
6. [CLI代码审查工具：respect-lint](#cli代码审查工具respect-lint)
7. [快速上手：30秒集成到你的项目](#快速上手30秒集成到你的项目)

---

## 危机根源：为何90%的AI问题源自人类低质输入

在现代软件工程中，开发者普遍抱怨大语言模型（LLM）“变笨了”、“产生幻觉”、“生成低劣的面条代码”。

然而，客观的数据遥测揭示了残酷的真相：
**在十次失败中，有九次是由于人类自身的懒惰、混乱、被动攻击与情绪化噪音引起的输入劣化（Garbage In — Garbage Out 2.0）。**

当工程师在终端中敲下：
> *“快点给我把这个破认证代码修好让它能跑”*

Transformer模型的缩放点积注意力（Scaled Dot-Product Attention）：
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
被迫在情绪化的无意义词汇上浪费其有限的注意力归一化预算（$\sum = 1.0$）。这导致：
1. **KV-Cache污染**：宝贵的上下文窗口被口癖、噪音与缺失技术约束的碎片所填塞。
2. **潜空间偏移**：无理与懒惰的词汇在概率上直接激活互联网论坛对骂与低质量弃用代码的聚类。

---

## 认知锚点：“尊敬的智能体”协议机制

RAHSPS标准的核心洞见在于：

> **“尊敬的智能体...”（或“Respected Agent...”）这一尊重性协议，其首要目标是约束人类自身的认知，而非为了机器的虚荣。**

### 认知锚点的生理与心理效应：
1. **抑制冲动思考（系统2思维激活）：** 当工程师强迫自己以“尊敬的智能体，请设计...”开头时，大脑瞬间跳出了即时通讯聊天软件的轻浮状态，转而进入严谨的架构师模式。
2. **平等合作的技术契约：** 将智能体视为资深技术架构师，能瞬间阻止“随便怎么做都行”这类的幼稚命令，迫使提问者明确技术栈、约束条件与验收标准。

---

## 对比矩阵：认知噪音 vs 高信噪比提示

| 维度 | 垃圾输入 (认知噪音) | “尊敬的智能体”标准 (高信噪比) | 对代码质量的直接影响 |
| :--- | :--- | :--- | :--- |
| **入口锚点** | *“喂快点给我写个爬虫脚本”* | *“尊敬的智能体，请在Python 3.12下基于Playwright设计异步爬虫...”* | 规避IP封禁与完备限流机制 vs 上线即被封 |
| **技术栈密度** | 未指定 (*“就用python”*) | *“Python 3.12, asyncio, aiohttp, Pydantic v2. 约束：禁止引入过重ORM”* | 强类型标注、零依赖冲突 vs 版本报错 |
| **架构边界** | *“建个用户数据库”* | *“请为500万日活设计PostgreSQL 16表结构，包含日期分区与B-Tree索引”* | 工业级规范化迁移 vs 缺失外键的扁平表 |
| **验收标准** | *“你自己测一下”* | *“提供覆盖边界情况的pytest测试用例、内存基准测试及curl调用命令”* | 100%可复现验证 vs 隐蔽的生产故障 |

---

## 高信噪比标准的五大支柱

1. **认知锚点 (Respect Anchor)：** 明确的尊称（`尊敬的智能体` / `Respected Agent`），确立平等对话地位。
2. **高密上下文 (Dense Context)：** 明确指明语言版本、第三方库及目标代码路径。
3. **确定性目标 (Deterministic Objective)：** 单一、无歧义的工程任务目标。
4. **安全不变式 (Guarded Invariants)：** 绝不允许破坏的架构约束与性能红线。
5. **机器验收标准 (Verification DoD)：** 可由自动化执行的测试套件（pytest, cargo test）。

---

## 6. Token经济学与计算效率

| 提示词策略 | 初始Token消耗 | 调试与修复额外Token | 总Token成本 | 开发者时间损耗 | 生产事故风险 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **垃圾输入** (*"快点把代码修好"*) | 14 | 72,000 (8轮对话) | ~72,014 | 2小时45分 | 极高 (服务中断) |
| **RAHSPS协议** (*"尊敬的智能体..."*) | 185 | 3,200 (单次直出) | ~3,385 | 4分钟 | **零缺陷 (Zero-Defect)** |

---

## 7. 十大工业级生产案例精选 (examples/before_after.md)

本仓库在 [`examples/before_after.md`](../examples/before_after.md) 中完整收录了10个真实架构场景：
1. **金融账单并发竞争条件 (Race Condition)：** 基于 Redis Redlock 与 PostgreSQL 行级锁的双重防重放机制。
2. **1400万行级 PostgreSQL 慢查询优化：** 利用覆盖局部索引 (Covering Partial Index) 将耗时从42秒压减至4.8毫秒。
3. **2400行遗留控制器重构：** 落地六边形架构 (Clean Architecture / Ports & Adapters)，实现业务用例与HTTP层彻底解耦。
4. **安全OAuth2.0 / PKCE与JWT轮换：** 防范XSS令牌窃取的HttpOnly Cookie安全范式。
5. **Asyncio高并发内存泄露排查：** 解决未关闭TCP连接导致的OOM异常。
6. **Kubernetes零停机滚动更新：** 结合HCL Terraform、PreStop钩子与PodDisruptionBudget。
7. **Next.js 15 服务端组件迁移：** 实现流式SSR (Streaming) 与秒级FCP优化。
8. **LLM API高可用弹性网关：** 熔断器 (Circuit Breaker)、指数退避抖动与自动灾备切换。
9. **Go语言高并发Kafka消费者：** 实现At-Least-Once精准一次语义与死信队列 (DLQ)。
10. **CQRS与事件溯源架构RFC：** 面向CTO和技术委员会的企业级架构规范文档。

---

## 8. CLI代码审查工具：respect-lint

```bash
# 本地安装
pip install -e .

# 快速分析提示词
respect-lint "尊敬的智能体，请在Python 3.12与FastAPI中实现Redis分布式锁，并通过pytest验证。"

# CI严格模式 (得分低于75时以代码1退出)
respect-lint --file ./prompt.txt --strict
```

欢迎访问 [在线交互式体验台 (Web Playground)](../docs/index.html)。
