# 股票估值对比网页 - 使用说明

## 文件结构

```
stock-valuation/
├── index.html      # 网页主文件（含密码保护）
├── data.csv        # 股票数据文件
└── README.md       # 本说明文件
```

## 部署步骤

### 1. 修改密码

打开 `index.html`，找到配置区域：

```javascript
const CONFIG = {
    password: "value2024",    // ← 修改成你自己的密码
    csvUrl: "data.csv",
    sessionDuration: 8        // 登录有效期（小时）
};
```

### 2. 准备 CSV 数据

`data.csv` 格式要求：

```csv
市场,股票名称,股票代码,股价,P/E,EV/EBITDA
A股,贵州茅台,600519.SH,1523.00,25.5,18.2
港股,腾讯控股,0700.HK,385.20,16.8,10.5
```

- 第一行是表头（必须是这6列）
- 市场字段支持：A股/港股/日股/美股（会显示对应颜色标签）
- 支持逗号或制表符分隔
- 数据可以是 Excel 另存为 CSV 格式

### 3. 部署到 GitHub Pages（免费）

1. 注册/登录 [GitHub](https://github.com)
2. 新建一个仓库（Repository），命名为 `stock-valuation`
3. 上传 `index.html` 和 `data.csv` 到仓库
4. 进入仓库 Settings → Pages
5. Source 选择 "Deploy from a branch"，Branch 选 "main"，文件夹选 "/ (root)"
6. 点击 Save，等待 1-2 分钟
7. 页面会显示访问链接，如：`https://你的用户名.github.io/stock-valuation/`

### 4. 每日更新数据

方法 A（简单）：
1. 在 Excel 中更新数据
2. 另存为 CSV 格式（覆盖原文件）
3. 上传到 GitHub 仓库，替换 `data.csv`
4. 等待 1-2 分钟自动更新

方法 B（使用 GitHub Desktop）：
1. 下载 [GitHub Desktop](https://desktop.github.com)
2. 克隆你的仓库到本地
3. 每天替换本地 `data.csv` 文件
4. 在 GitHub Desktop 中填写提交信息，点击 "Commit to main" → "Push origin"

## 网页功能

- 密码保护（默认密码：value2024）
- 按列排序（点击表头）
- 实时搜索（右上角搜索框）
- 响应式设计（手机也能看）
- 自动显示数据更新时间
- 市场颜色标签区分

## 安全说明

- 前端密码保护是**基础级别**的防护，防止 casual access
- 密码在源代码中可见，不适合存放敏感金融数据
- 如需更高安全性，建议使用 Cloudflare Access 或 Netlify Identity

## 自定义

### 修改登录页外观
编辑 `index.html` 中 `.login-box` 和 `#login-screen` 的 CSS。

### 添加更多列
如需添加市值、股息率等列：
1. 修改 CSV 表头和新列数据
2. 修改 `parseCSV()` 函数解析新列
3. 在 `<thead>` 和 `renderTable()` 中添加新列显示

### 修改主题色
搜索 `#667eea` 和 `#764ba2`，替换为你喜欢的颜色。
