LOG = "/Users/runben/Desktop/千问/练习/sample_app.log"   # 学习期写死绝对路径，第2周学 os/pathlib 后改相对

counts = {}                                                # 空字典当计数器

with open(LOG) as f:
    for line in f:
        parts = line.split()                               # 按空格切成列表
        level = parts[2]                                  # 空1：级别是第几个字段？索引从0数：日期0 时间1 级别?
        counts[level] = counts.get(level, 0) + 1          # 空2：第一次遇到该级别时 get 应该返回什么才不报错？

for level, n in sorted(counts.items(), key=lambda x : x[1], reverse=True):   # 空3：按「次数」排而不是按「级别名」排，key 怎么写？
    print(level, n)