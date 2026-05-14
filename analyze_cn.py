import json
from collections import Counter

f = open(r'G:\my-novel-project\产品\历史上的今天\history_in_today.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()

# 中国相关关键词
cn_keywords = ["中国","中华","毛泽东","周恩来","邓小平","秦始皇","汉武帝",
    "唐朝","宋朝","明朝","清朝","抗日","北京","上海","长征","解放军","新中国",
    "共产","国民党","台湾","香港","澳门","中日","中美","中苏","汉","唐","宋",
    "明","清","秦","周","春秋","战国","三国","晋","隋","元","乾隆","康熙",
    "雍正","朱元璋","李世民","嬴政","孔子","老子","孟子","孙中山","鲁迅",
    "溥仪","袁世凯","蒋介石","毛主席","周总理","邓小平","江泽","胡锦","习近平",
    "长城","黄河","长江","故宫","天安","改革开放","辛亥","五四","九一八",
    "七七","南京","红军","八路","新四军","志愿军","两弹一星","神舟","嫦娥",
    "天宫","高铁","一带一路","汉朝","唐朝","宋朝","明朝","清朝","华夏",
    "太监","科举","皇帝","诸侯","丞相","尚书","匈奴","突厥","契丹","女真",
    "蒙古","满清","鸦片","甲午","戊戌","义和团","南昌","井冈山","延安",
    "重庆谈判","三大战役","开国大典","抗美援朝","大跃进","文革","改革开放",
    "浦东","奥运","世博","辽宁舰","歼","东风","北斗"]

cn_count = 0
cn_items = []
for item in data:
    desc = item["data"]
    if any(kw in desc for kw in cn_keywords):
        cn_count += 1
        cn_items.append(item)

total = len(data)
print(f"总条目: {total}")
print(f"中国相关: {cn_count} ({cn_count*100/total:.1f}%)")
print(f"非中国: {total-cn_count} ({(total-cn_count)*100/total:.1f}%)")

# 各月分布
month_cn = Counter()
for item in cn_items:
    month_cn[item["month"]] += 1
print(f"\n各月中国事件:")
for m in range(1,13):
    print(f"  {m}月: {month_cn[m]} 条")

# 看今天的例子
print(f"\n5月14日中国事件:")
today = [x for x in data if x["month"]==5 and x["day"]==14]
cn_today = [x for x in today if any(kw in x["data"] for kw in cn_keywords)]
print(f"  全部: {len(today)} 条，中国: {len(cn_today)} 条")
for item in cn_today[:10]:
    t = {1:"事件",2:"出生",3:"逝世"}.get(item["type"],"?")
    print(f"  [{t}] {item['year']}: {item['data'][:80]}")
