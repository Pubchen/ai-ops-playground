# 学习日志

> 每天 3–5 行：做了什么 / 卡在哪 / 明天从哪开始。费曼检查：能不能对同事讲清今天学的。

## Day 1（2026-10-29）速赢 + API 首调

- 百炼注册、API Key 进 ~/.zshrc、venv + dashscope 跑通 hello_qwen.py
- 卡点：无
- 明日：知识库机器人

## Day 2（2026-10-30）第一个 RAG

- 知识库 ops-runbook-kb 建成（3 份运维示例文档），索引「已就绪」
- Playground「知识问答」3 句全部带引用通过 = 检索链路成立
- 成本认知：0.04 元账单 = 规格费/排序费；决策 a（学习期保留知识库，约 0.72 元/天）
- 卡点：经典智能体应用 UI 在该账号已并入 Managed Agent，应用层推迟到第 21 周代码挂库

## Day 3（2026-11-02 ~ 11-03）命令行温故 + Git 上云

- E1–E6 全过（E2 与基准一致：[inventory] 10）；学会管道五步法与下钻
- 概念补课：shell/zsh/.zshrc/source/cat/> 与 >>/vim/ssh/mkdir/Tab 补全/DNS
- 首仓库 ai-ops-playground：init → 首提交 b24fe5f → ssh 密钥认证 → push 上云
- README markdown 修正提交（# 后空格、空行分段）
- 卡点：键盘类型误判、dotfile 看不见、密码推送被废、新加坡 IP 干扰（见 errors.md）

## Day 4（2026-11-04）环境核对 + 工具链 + 笔记体系

- 环境核对：python 3.15.2 / pip 26.2.2 / VS Code 1.144 / git 2.50 / ssh key 均在；conda 与 jupyter 缺
- 建学习专用 venv：~/venvs/ai-learn，装 numpy/pandas/matplotlib/jupyterlab
- 注册 Kaggle / 魔搭 / HuggingFace 三账号；Kaggle 验证通道调整，改人脸识别通过、phone verification 显示 verified（见 errors.md 006）；GPU 配额（约 30h/周）确认到账，Accelerator 可选 + nvidia-smi 实锤；魔搭昵称 pubchen，我的Notebook 免费实例确认：CPU 8核32G 长期有效 + GPU 8核32G/显存24G 剩余约36h（停止状态不计时）；HF 主站暂不可达，注册推迟——下载模型走 hf-mirror.com 不需账号，注册只影响第 19 周课程证书
- 笔记体系进仓库：notes/errors.md + notes/daily.md，用 git 管理 = 自动备份 + 作品集素材；提交 51cef6c 已推送，working tree clean

## Day 5（2026-11-04）日历固化 + 台账机制改版

- 日历：清除旧 4 条事件（AppleScript 对 iCloud 日历删除不持久化，改 GUI 手删，见 errors.md 待补），导入新版仅「工作日块 周一~五 09:00-17:00」；周末与每日底线不设
- 台账机制：周回顾改由助手按会话实时进度不定期维护（进度表/daily/errors + 跨周摘要）；本人只贴 checkpoint 输出 + 周日 30 秒核对并补实际耗时/自评
- pandas 首练完成：JupyterLab 六练输出与基准全对（inventory 10 / WARN&inventory 8 / rt 均524.7 最大2300）；存为 day5-pandas首练.ipynb 并入仓 notebooks/；踩坑：md 代码围栏```粘进 cell 致 SyntaxError、单 cell 只显示最后一个裸表达式
