# 报错 → 解法库

> 规则：报错原文照贴、原因一句话、解法可复制、日期/场景必填。这是未来的面试素材库。

## 001 Shift + ` 打出 ± 而不是 ~

- 报错/现象：按 Shift + 数字1左侧键输出 `±`；键盘显示器画出的键位与实体键帽不一致（Z 左边多一颗键）
- 原因：macOS 把键盘误识别为 ISO/JIS，叠加输入源非美式 ABC；系统只看「键盘类型 + 输入源」映射表，不看键帽印字
- 解法：系统设置 → 键盘 → 更改键盘类型 → 选 **ANSI**；输入源添加并切到 **ABC**；终端里固定 ABC
- 日期/场景：2026-10-30 / Day 3 命令行练习

## 002 fatal: not a git repository (or any of the parent directories): .git

- 报错/现象：在家目录跑 `git status` 报 fatal
- 原因：当前目录及所有父目录都没有 `.git`，git 不认为这里是仓库
- 解法：`cd` 到仓库根目录（有 `.git` 的那层）再跑；或先 `git init`
- 日期/场景：2026-11-02 / Day 3 首仓库

## 003 cp 成功但 ls 看不到 .gitignore

- 报错/现象：`cp 模板 .gitignore` 无报错，`ls` 却看不到文件
- 原因：以 `.` 开头的 dotfile 默认隐藏；且 cp 成功时本就无输出
- 解法：`ls -a`；养成「没报错但没结果」三查：`ls -a` → `pwd` → `cat 目标文件`
- 日期/场景：2026-11-02 / Day 3

## 004 remote: Invalid username or token. Password authentication is not supported for Git operations.

- 报错/现象：`git push` 输入账号密码后被拒
- 原因：GitHub 自 2021-08 起废除密码推送，只认 Token 或 SSH 密钥
- 解法：走密钥路线：`ssh-keygen -t ed25519` → 公钥贴 GitHub（Settings → SSH and GPG keys）→ `git remote set-url origin git@github.com:Pubchen/ai-ops-playground.git` → `git push -u origin main`
- 日期/场景：2026-11-02 / Day 3 上云

## 005 GitHub 网页打不开，但 ssh / push 正常

- 报错/现象：浏览器打不开 github.com；`curl` 直连 DNS 解析到的 IP 超时；换 DNS 无效
- 原因：DNS 给的新加坡 IP `20.205.243.166` 被链路层干扰；美国机房 IP 通畅（实测 140.82.112.3 / .113.4 / .114.3 均 200）
- 解法：`echo "140.82.112.3 github.com" | sudo tee -a /etc/hosts` + 刷缓存；失效时用 `--resolve` 四 IP 测速换行；回滚 `sudo sed -i '' '/140.82.112.3/d' /etc/hosts`
- 状态：截至 2026-11-04 该修复**尚未在本机执行**（/etc/hosts 中无此行）
- 日期/场景：2026-11-03 / Day 3 收尾

## 006 Kaggle 手机验证提示「无法满足识别需求」

- 报错/现象：注册后手机验证环节提示无法满足识别需求
- 原因：**Kaggle 调整了验证流程/通道**（并非账号风控）；人脸识别为替代通道
- 解法：改走人脸识别验证完成；随后账号页 phone verification 状态显示 **verified**
- 日期/场景：2026-11-04 / Day 4 账号注册

## 007 notebook 里跑手册代码报 SyntaxError: invalid syntax（箭头指向 ```python）

- 报错/现象：把 day5 手册的代码块整段粘进 Jupyter cell 后运行报语法错误
- 原因：``` 是 Markdown 代码围栏标记，不是 Python 语法；粘进 code cell 即非法字符
- 解法：只复制围栏**里面**的代码；手册顶部已加「复制纪律」提醒
- 日期/场景：2026-11-04 / Day 5 pandas 首练

## 008 cell 里写了 df.head()/df.shape/df.dtypes 却只看到 dtypes

- 报错/现象：以为 shape 没执行、数据丢了
- 原因：Jupyter 一个 cell 只自动显示**最后一个裸表达式**的值，其余执行了但不显示
- 解法：想全看就用 print() 包起来，或一格只看一件事；df.shape 是属性不加括号、df.head() 是方法加括号
- 日期/场景：2026-11-04 / Day 5 pandas 首练
