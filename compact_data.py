import json
from collections import defaultdict

# 读取原始数据（新格式：year/month/day 为整数）
with open(r'G:\my-novel-project\产品\历史上的今天\history_in_today.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"原始数据: {len(data)} 条")

type_map = {1: "事件", 2: "出生", 3: "逝世"}

# 按 M-D 分组
grouped = defaultdict(list)
for item in data:
    m = str(item["month"]) if not isinstance(item["month"], int) else str(item["month"])
    d = str(item["day"]) if not isinstance(item["day"], int) else str(item["day"])
    y = str(item["year"]) if not isinstance(item["year"], int) else str(item["year"])
    t = type_map.get(item["type"], "其他")
    key = f"{m}-{d}"
    grouped[key].append({"y": y, "t": t, "d": item["data"]})

# 排序
output = {}
for key in sorted(grouped.keys(), key=lambda k: (int(k.split('-')[0]), int(k.split('-')[1]))):
    entries = grouped[key]
    entries.sort(key=lambda e: (int(e['y']) if e['y'].lstrip('-').isdigit() else -9999, e['y']))
    output[key] = entries

# 写入 compact JSON
with open(r'G:\my-novel-project\产品\历史上的今天\data_compact.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, separators=(',', ':'))

# 写入 data.js
with open(r'G:\my-novel-project\产品\历史上的今天\data_compact.json', 'r', encoding='utf-8') as f:
    compact = f.read()
with open(r'G:\my-novel-project\产品\历史上的今天\data.js', 'w', encoding='utf-8') as f:
    f.write('const HISTORY_DATA = ')
    f.write(compact)
    f.write(';')

import os
size_js = os.path.getsize(r'G:\my-novel-project\产品\历史上的今天\data.js')
size_json = os.path.getsize(r'G:\my-novel-project\产品\历史上的今天\data_compact.json')
total = sum(len(v) for v in output.values())
print(f"总条目: {total}")
print(f"涵盖天数: {len(output)}")
print(f"data_compact.json: {size_json/1024/1024:.1f} MB")
print(f"data.js: {size_js/1024/1024:.1f} MB")

# 验证年份范围
years_set = set()
for entries in output.values():
    for e in entries:
        if e['y'].lstrip('-').isdigit():
            years_set.add(int(e['y']))
print(f"年份范围: {min(years_set)} ~ {max(years_set)}")
