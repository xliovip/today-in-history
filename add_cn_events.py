"""
补充中国特有的历史事件、传统节日、近现代大事到现有数据集。
格式与现有数据一致：{"type": int, "year": int, "month": int, "day": int, "data": str}
type: 1=事件, 2=出生, 3=逝世
"""
import json
from collections import defaultdict

# ========== 中国特有传统节日（以常见公历日期为准）==========
cn_festivals = [
    {"type": 1, "month": 1, "day": 1, "data": "元旦，公历新年开始。"},
    {"type": 1, "month": 2, "day": 2, "data": "龙抬头（春龙节），中国传统节日。"},
    {"type": 1, "month": 4, "day": 5, "data": "清明节，中国传统祭祖节日。"},
    {"type": 1, "month": 5, "day": 5, "data": "端午节，中国传统节日，纪念屈原。"},
    {"type": 1, "month": 7, "day": 7, "data": "七夕节，中国传统情人节。"},
    {"type": 1, "month": 7, "day": 15, "data": "中元节（盂兰盆节），中国传统祭祖节日。"},
    {"type": 1, "month": 8, "day": 15, "data": "中秋节，中国传统团圆节日。"},
    {"type": 1, "month": 9, "day": 9, "data": "重阳节，中国传统敬老节日。"},
    {"type": 1, "month": 12, "day": 8, "data": "腊八节，中国传统节日。"},
    {"type": 1, "month": 12, "day": 23, "data": "小年（北方），中国传统祭灶节日。"},
    {"type": 1, "month": 12, "day": 30, "data": "除夕，中国传统岁末团圆日。"},
]

# ========== 二十四节气（以典型公历日期为准）==========
solar_terms = [
    {"type": 1, "month": 2, "day": 4, "data": "立春，二十四节气之首，春季开始。"},
    {"type": 1, "month": 2, "day": 19, "data": "雨水，二十四节气之一。"},
    {"type": 1, "month": 3, "day": 6, "data": "惊蛰，二十四节气之一，春雷始鸣。"},
    {"type": 1, "month": 3, "day": 21, "data": "春分，二十四节气之一，昼夜等长。"},
    {"type": 1, "month": 4, "day": 5, "data": "清明，二十四节气之一。"},
    {"type": 1, "month": 4, "day": 20, "data": "谷雨，二十四节气之一。"},
    {"type": 1, "month": 5, "day": 6, "data": "立夏，二十四节气之一，夏季开始。"},
    {"type": 1, "month": 5, "day": 21, "data": "小满，二十四节气之一。"},
    {"type": 1, "month": 6, "day": 6, "data": "芒种，二十四节气之一。"},
    {"type": 1, "month": 6, "day": 21, "data": "夏至，二十四节气之一，白昼最长。"},
    {"type": 1, "month": 7, "day": 7, "data": "小暑，二十四节气之一。"},
    {"type": 1, "month": 7, "day": 23, "data": "大暑，二十四节气之一。"},
    {"type": 1, "month": 8, "day": 7, "data": "立秋，二十四节气之一，秋季开始。"},
    {"type": 1, "month": 8, "day": 23, "data": "处暑，二十四节气之一。"},
    {"type": 1, "month": 9, "day": 8, "data": "白露，二十四节气之一。"},
    {"type": 1, "month": 9, "day": 23, "data": "秋分，二十四节气之一，昼夜等长。"},
    {"type": 1, "month": 10, "day": 8, "data": "寒露，二十四节气之一。"},
    {"type": 1, "month": 10, "day": 23, "data": "霜降，二十四节气之一。"},
    {"type": 1, "month": 11, "day": 7, "data": "立冬，二十四节气之一，冬季开始。"},
    {"type": 1, "month": 11, "day": 22, "data": "小雪，二十四节气之一。"},
    {"type": 1, "month": 12, "day": 7, "data": "大雪，二十四节气之一。"},
    {"type": 1, "month": 12, "day": 22, "data": "冬至，二十四节气之一，白昼最短。"},
]

# ========== 中国重大历史事件（补充维基缺失的）==========
cn_major_events = [
    # 远古-先秦
    {"type": 1, "year": -221, "month": 1, "day": 1, "data": "秦始皇统一中国，建立中国历史上第一个中央集权制国家——秦朝。"},

    # 近现代（1840-1949）
    {"type": 1, "year": 1840, "month": 6, "day": 28, "data": "第一次鸦片战争爆发，英国发动对华侵略战争。"},
    {"type": 1, "year": 1842, "month": 8, "day": 29, "data": "清廷与英国签订《南京条约》，中国开始沦为半殖民地半封建社会。"},
    {"type": 1, "year": 1851, "month": 1, "day": 11, "data": "洪秀全发动金田起义，太平天国运动开始。"},
    {"type": 1, "year": 1856, "month": 10, "day": 23, "data": "第二次鸦片战争爆发。"},
    {"type": 1, "year": 1860, "month": 10, "day": 6, "data": "英法联军火烧圆明园。"},
    {"type": 1, "year": 1894, "month": 7, "day": 25, "data": "中日甲午战争爆发。"},
    {"type": 1, "year": 1895, "month": 4, "day": 17, "data": "清廷与日本签订《马关条约》，割让台湾及澎湖列岛。"},
    {"type": 1, "year": 1898, "month": 6, "day": 11, "data": "戊戌变法（百日维新）开始。"},
    {"type": 1, "year": 1900, "month": 6, "day": 21, "data": "八国联军侵华战争爆发。"},
    {"type": 1, "year": 1901, "month": 9, "day": 7, "data": "清廷与十一国签订《辛丑条约》。"},
    {"type": 1, "year": 1911, "month": 10, "day": 10, "data": "武昌起义爆发，辛亥革命开始。"},
    {"type": 1, "year": 1912, "month": 1, "day": 1, "data": "中华民国成立，孙中山就任临时大总统。"},
    {"type": 1, "year": 1912, "month": 2, "day": 12, "data": "清帝溥仪退位，清朝灭亡，中国两千多年封建帝制结束。"},
    {"type": 1, "year": 1919, "month": 5, "day": 4, "data": "五四运动爆发，新民主主义革命开端。"},
    {"type": 1, "year": 1921, "month": 7, "day": 23, "data": "中国共产党第一次全国代表大会在上海开幕。"},
    {"type": 1, "year": 1924, "month": 1, "day": 20, "data": "中国国民党第一次全国代表大会召开，第一次国共合作开始。"},
    {"type": 1, "year": 1926, "month": 7, "day": 9, "data": "国民革命军誓师北伐。"},
    {"type": 1, "year": 1927, "month": 8, "day": 1, "data": "南昌起义爆发，中国共产党独立领导武装斗争开始。"},
    {"type": 1, "year": 1927, "month": 9, "day": 9, "data": "秋收起义爆发。"},
    {"type": 1, "year": 1927, "month": 10, "day": 27, "data": "毛泽东率秋收起义部队上井冈山，创建第一个农村革命根据地。"},
    {"type": 1, "year": 1931, "month": 9, "day": 18, "data": "九一八事变爆发，日本侵占中国东北。"},
    {"type": 1, "year": 1934, "month": 10, "day": 16, "data": "中国工农红军开始长征。"},
    {"type": 1, "year": 1935, "month": 1, "day": 15, "data": "遵义会议召开，确立毛泽东在党和红军中的领导地位。"},
    {"type": 1, "year": 1936, "month": 10, "day": 22, "data": "红军三大主力在甘肃会宁会师，长征胜利结束。"},
    {"type": 1, "year": 1936, "month": 12, "day": 12, "data": "西安事变爆发。"},
    {"type": 1, "year": 1937, "month": 7, "day": 7, "data": "卢沟桥事变（七七事变）爆发，全民族抗日战争开始。"},
    {"type": 1, "year": 1937, "month": 12, "day": 13, "data": "南京沦陷，日军开始南京大屠杀。"},
    {"type": 1, "year": 1940, "month": 8, "day": 20, "data": "八路军发起百团大战。"},
    {"type": 1, "year": 1945, "month": 8, "day": 15, "data": "日本宣布无条件投降，中国人民抗日战争胜利。"},
    {"type": 1, "year": 1945, "month": 9, "day": 2, "data": "日本正式签署投降书，第二次世界大战结束。"},
    {"type": 1, "year": 1945, "month": 9, "day": 3, "data": "中国人民抗日战争胜利纪念日。"},
    {"type": 1, "year": 1946, "month": 6, "day": 26, "data": "国民党发动全面内战，解放战争开始。"},
    {"type": 1, "year": 1948, "month": 9, "day": 12, "data": "辽沈战役开始。"},
    {"type": 1, "year": 1948, "month": 11, "day": 6, "data": "淮海战役开始。"},
    {"type": 1, "year": 1948, "month": 11, "day": 29, "data": "平津战役开始。"},
    {"type": 1, "year": 1949, "month": 1, "day": 31, "data": "北平和平解放。"},
    {"type": 1, "year": 1949, "month": 4, "day": 23, "data": "中国人民解放军占领南京，国民党在大陆统治结束。"},

    # 新中国（1949-至今）
    {"type": 1, "year": 1949, "month": 9, "day": 21, "data": "中国人民政治协商会议第一届全体会议在北平召开。"},
    {"type": 1, "year": 1949, "month": 10, "day": 1, "data": "中华人民共和国成立，毛泽东在天安门城楼宣告中央人民政府成立。"},
    {"type": 1, "year": 1950, "month": 10, "day": 19, "data": "中国人民志愿军跨过鸭绿江，抗美援朝战争开始。"},
    {"type": 1, "year": 1950, "month": 6, "day": 30, "data": "《中华人民共和国土地改革法》颁布。"},
    {"type": 1, "year": 1951, "month": 5, "day": 23, "data": "西藏和平解放。"},
    {"type": 1, "year": 1953, "month": 7, "day": 27, "data": "《朝鲜停战协定》签署，抗美援朝胜利结束。"},
    {"type": 1, "year": 1954, "month": 9, "day": 20, "data": "第一届全国人民代表大会通过《中华人民共和国宪法》。"},
    {"type": 1, "year": 1955, "month": 4, "day": 18, "data": "周恩来率团出席万隆会议，提出和平共处五项原则。"},
    {"type": 1, "year": 1956, "month": 9, "day": 15, "data": "中国共产党第八次全国代表大会召开。"},
    {"type": 1, "year": 1964, "month": 10, "day": 16, "data": "中国第一颗原子弹爆炸成功。"},
    {"type": 1, "year": 1967, "month": 6, "day": 17, "data": "中国第一颗氢弹爆炸成功。"},
    {"type": 1, "year": 1970, "month": 4, "day": 24, "data": "中国第一颗人造地球卫星『东方红一号』发射成功。"},
    {"type": 1, "year": 1971, "month": 10, "day": 25, "data": "中华人民共和国恢复在联合国的合法席位。"},
    {"type": 1, "year": 1972, "month": 2, "day": 21, "data": "美国总统尼克松访华，中美关系正常化开始。"},
    {"type": 1, "year": 1978, "month": 12, "day": 18, "data": "中共十一届三中全会召开，确定改革开放基本国策。"},
    {"type": 1, "year": 1979, "month": 1, "day": 1, "data": "中美正式建立外交关系。"},
    {"type": 1, "year": 1979, "month": 1, "day": 28, "data": "邓小平访问美国，新中国领导人首次访美。"},
    {"type": 1, "year": 1979, "month": 12, "day": 27, "data": "邓小平提出『小康』概念。"},
    {"type": 1, "year": 1980, "month": 8, "day": 26, "data": "深圳、珠海、汕头、厦门经济特区成立。"},
    {"type": 1, "year": 1982, "month": 12, "day": 4, "data": "新《中华人民共和国宪法》通过。"},
    {"type": 1, "year": 1984, "month": 12, "day": 19, "data": "中英签署关于香港问题的联合声明。"},
    {"type": 1, "year": 1987, "month": 4, "day": 13, "data": "中葡签署关于澳门问题的联合声明。"},
    {"type": 1, "year": 1992, "month": 1, "day": 18, "data": "邓小平南巡，推动改革开放进入新阶段。"},
    {"type": 1, "year": 1997, "month": 7, "day": 1, "data": "香港回归祖国。"},
    {"type": 1, "year": 1999, "month": 12, "day": 20, "data": "澳门回归祖国。"},
    {"type": 1, "year": 2001, "month": 7, "day": 13, "data": "北京获得2008年奥运会主办权。"},
    {"type": 1, "year": 2001, "month": 11, "day": 10, "data": "中国正式加入世界贸易组织（WTO）。"},

    # 21世纪中国大事
    {"type": 1, "year": 2003, "month": 10, "day": 15, "data": "神舟五号载人飞船发射成功，杨利伟成为中国首位航天员。"},
    {"type": 1, "year": 2005, "month": 10, "day": 12, "data": "神舟六号载人飞船发射成功，费俊龙、聂海胜执行任务。"},
    {"type": 1, "year": 2006, "month": 7, "day": 1, "data": "青藏铁路全线通车。"},
    {"type": 1, "year": 2008, "month": 5, "day": 12, "data": "四川汶川发生8.0级特大地震。"},
    {"type": 1, "year": 2008, "month": 8, "day": 8, "data": "第29届夏季奥林匹克运动会在北京开幕。"},
    {"type": 1, "year": 2008, "month": 9, "day": 25, "data": "神舟七号发射，翟志刚完成中国首次太空行走。"},
    {"type": 1, "year": 2010, "month": 5, "day": 1, "data": "上海世界博览会开幕。"},
    {"type": 1, "year": 2010, "month": 11, "day": 12, "data": "第16届亚洲运动会在广州开幕。"},
    {"type": 1, "year": 2011, "month": 9, "day": 29, "data": "天宫一号目标飞行器发射成功。"},
    {"type": 1, "year": 2012, "month": 6, "day": 16, "data": "神舟九号发射，刘洋成为中国首位女航天员。"},
    {"type": 1, "year": 2012, "month": 11, "day": 8, "data": "中国共产党第十八次全国代表大会召开。"},
    {"type": 1, "year": 2013, "month": 12, "day": 14, "data": "嫦娥三号探测器在月球软着陆，中国航天器首次降落地外天体。"},
    {"type": 1, "year": 2014, "month": 12, "day": 12, "data": "南水北调中线一期工程正式通水。"},
    {"type": 1, "year": 2015, "month": 9, "day": 3, "data": "纪念中国人民抗日战争暨世界反法西斯战争胜利70周年阅兵式。"},
    {"type": 1, "year": 2016, "month": 9, "day": 4, "data": "二十国集团（G20）峰会在杭州举行。"},
    {"type": 1, "year": 2016, "month": 11, "day": 3, "data": "中国最大推力运载火箭长征五号首飞成功。"},
    {"type": 1, "year": 2017, "month": 5, "day": 14, "data": "第一届『一带一路』国际合作高峰论坛在北京举行。"},
    {"type": 1, "year": 2017, "month": 10, "day": 18, "data": "中国共产党第十九次全国代表大会召开。"},
    {"type": 1, "year": 2018, "month": 10, "day": 24, "data": "港珠澳大桥正式通车。"},
    {"type": 1, "year": 2019, "month": 1, "day": 3, "data": "嫦娥四号探测器在月球背面软着陆，人类首次。"},
    {"type": 1, "year": 2019, "month": 12, "day": 1, "data": "首例新型冠状病毒肺炎病例确诊，新冠疫情开始。"},
    {"type": 1, "year": 2020, "month": 1, "day": 23, "data": "武汉因新冠疫情封城，中国进入全面抗疫状态。"},
    {"type": 1, "year": 2020, "month": 4, "day": 8, "data": "武汉解封，中国疫情防控取得阶段性成果。"},
    {"type": 1, "year": 2020, "month": 7, "day": 23, "data": "天问一号火星探测器发射成功。"},
    {"type": 1, "year": 2020, "month": 11, "day": 24, "data": "嫦娥五号发射，中国首次地外天体采样返回任务。"},
    {"type": 1, "year": 2020, "month": 12, "day": 17, "data": "嫦娥五号返回器携带月球样品着陆地球。"},
    {"type": 1, "year": 2021, "month": 2, "day": 25, "data": "全国脱贫攻坚总结表彰大会召开，中国宣布消除绝对贫困。"},
    {"type": 1, "year": 2021, "month": 5, "day": 15, "data": "天问一号成功着陆火星，中国成为第二个成功着陆火星的国家。"},
    {"type": 1, "year": 2021, "month": 7, "day": 1, "data": "中国共产党成立100周年庆祝大会在天安门广场举行。"},
    {"type": 1, "year": 2021, "month": 10, "day": 16, "data": "神舟十三号发射，中国空间站开启长期驻留时代。"},
    {"type": 1, "year": 2022, "month": 2, "day": 4, "data": "第24届冬季奥林匹克运动会在北京开幕，北京成为首个『双奥之城』。"},
    {"type": 1, "year": 2022, "month": 10, "day": 16, "data": "中国共产党第二十次全国代表大会召开。"},
    {"type": 1, "year": 2022, "month": 11, "day": 29, "data": "神舟十五号发射，中国空间站首次实现两艘载人飞船同时在轨。"},
    {"type": 1, "year": 2023, "month": 5, "day": 30, "data": "神舟十六号发射，中国空间站应用与发展阶段首次载人任务。"},
    {"type": 1, "year": 2023, "month": 10, "day": 26, "data": "神舟十七号发射，中国空间站进入常态化运营。"},
    {"type": 1, "year": 2024, "month": 4, "day": 25, "data": "神舟十八号发射，中国空间站持续运营。"},
    {"type": 1, "year": 2024, "month": 6, "day": 2, "data": "嫦娥六号探测器在月球背面着陆，人类首次月背采样。"},
    {"type": 1, "year": 2024, "month": 6, "day": 25, "data": "嫦娥六号返回器携带月球背面样品成功着陆地球。中国载人航天工程第四批预备航天员选拔完成。"},
]

# ========== 合并到现有数据 ==========
print("读取现有数据...")
with open(r'G:\my-novel-project\产品\历史上的今天\history_in_today.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

print(f"现有数据: {len(existing)} 条")

# 合并所有中国补充数据（仅含年份的事件，排除无年份的传统节日/节气）
all_new = cn_major_events

# 去重（基于相同年/月/日/描述）
existing_keys = set()
for item in existing:
    key = (item["year"], item["month"], item["day"], item.get("data","")[:30])
    existing_keys.add(key)

new_count = 0
for item in all_new:
    key = (item["year"], item["month"], item["day"], item["data"][:30])
    if key not in existing_keys:
        existing.append(item)
        existing_keys.add(key)
        new_count += 1

print(f"新增: {new_count} 条")
print(f"总计: {len(existing)} 条")

# 写回
with open(r'G:\my-novel-project\产品\历史上的今天\history_in_today.json', 'w', encoding='utf-8') as f:
    json.dump(existing, f, ensure_ascii=False, separators=(',', ':'))

# 统计
from collections import Counter
type_c = Counter(x["type"] for x in existing)
print(f"类型: 事件={type_c[1]}, 出生={type_c[2]}, 逝世={type_c[3]}")
