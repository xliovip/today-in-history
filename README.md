<p align="center">
  <a href="https://xliovip.github.io/today-in-history/"><strong>在线访问 →</strong></a>
  ·
  <a href="#数据来源">数据来源</a>
  ·
  <a href="#本地使用">本地使用</a>
  ·
  <a href="#开发">开发</a>
</p>

<br>

**47,000+ 条历史事件**，覆盖公元前 4713 年至 2025 年，全年 366 天无空缺。纯静态页面，无需后端、无需 API，打开即用。

## 功能

- **历年今日** — 查看任意日期的历史事件、出生、逝世记录
- **年代筛选** — 按世纪分组浏览，从公元前到当代
- **分类切换** — 只看事件、出生或逝世
- **关键词搜索** — 在当日事件中快速定位
- **随机一日** — 点击 ✦ 按钮或按键盘 `R`，漫游历史
- **日期跳转** — 日历控件、前后日切换（键盘 `←` `→`）、`#5-14` 锚点直达
- **暗色主题** — 暖琥珀档案质感，护眼且沉浸

## 数据来源

| 数据 | 说明 |
|---|---|
| **基础数据** | 47,010 条（公元前 4713 — 2024），源于维基百科，取自 [zhoujinshi/history_in_today](https://github.com/zhoujinshi/history_in_today) |
| **2025 年补充** | 35 条，由本仓库维护者根据公开新闻报道整理 |
| **更新方式** | 数据增量追加，去重合并 |

数据格式统一为：`{ year, month, day, type(1=事件/2=出生/3=逝世), data(描述) }`。

## 本地使用

```bash
git clone https://github.com/xliovip/today-in-history.git
cd today-in-history
# 直接双击 index.html 即可浏览
```

或者用 Python 开一个本地服务器：

```bash
python3 -m http.server 8000
# 打开 http://localhost:8000
```

## 项目结构

```
today-in-history/
├── index.html               # 主页面（时间线 UI）
├── data.js                  # 数据集（4.5 MB）
├── history_in_today.json    # 原始 JSON 数据
├── data_compact.json        # 精简版 JSON
├── compact_data.py          # 数据构建脚本
└── add_2025_data.py         # 2025 年事件补全脚本
```

## 技术栈

- 纯 HTML / CSS / JavaScript，零依赖
- 数据以内嵌 JS 变量形式加载，无需网络请求
- GitHub Pages 静态托管

## 许可证

本项目数据部分遵循原上游仓库许可，代码部分 MIT。
