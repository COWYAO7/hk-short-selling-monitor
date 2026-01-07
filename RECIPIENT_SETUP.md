# 📧 配置收件人邮箱 - 3分钟图文教程

## 🎯 目标
添加新的收件人邮箱：您自己的邮箱地址（或任何您想要的邮箱）

---

## 📝 步骤总览
```
1️⃣ 打开GitHub仓库
2️⃣ 进入设置页面
3️⃣ 添加新的Secret
4️⃣ 推送代码更新
5️⃣ ✅ 完成！
```

---

## 详细步骤

### 1️⃣ 打开GitHub仓库设置

**操作：**
1. 打开浏览器，访问：`https://github.com/COWA07/hk-short-selling-monitor`
2. 点击顶部的 **⚙️ Settings** 标签

**看到的界面：**
```
┌─────────────────────────────────────┐
│ < Code  Issues  Pull requests      │
│   Actions  ⚙️ Settings    >         │
└─────────────────────────────────────┘
```

---

### 2️⃣ 找到 Secrets 设置

**操作：**
1. 在左侧菜单中，向下滚动
2. 找到 **🔐 Secrets and variables**
3. 点击展开
4. 选择 **Actions**

**左侧菜单结构：**
```
📁 General
🔒 Security
  ├── 🔐 Secrets and variables
  │   └── ▶️ Actions  ← 点击这里
  └── ...
```

---

### 3️⃣ 添加新的 Secret

**操作：**
1. 点击右上角的 **New repository secret** 按钮
2. 填写表单：

```
┌─────────────────────────────────────┐
│ Name *                              │
│ ┌─────────────────────────────────┐ │
│ │ RECIPIENT_EMAIL                 │ │
│ └─────────────────────────────────┘ │
│                                     │
│ Secret *                            │
│ ┌─────────────────────────────────┐ │
│ │ your@gmail.com, recipient2@example.com│ │
│ └─────────────────────────────────┘ │
│                                     │
│   [Add secret]                      │
└─────────────────────────────────────┘
```

**填写内容：**
- **Name（名称）**：`RECIPIENT_EMAIL`（必须完全一致，区分大小写）
- **Secret（值）**：
  - 单个邮箱：`recipient@example.com`
  - 多个邮箱：`first@example.com, second@example.com`

3. 点击 **Add secret** 保存

---

### 4️⃣ 验证配置

**检查 Secrets 列表：**
```
您应该看到以下 Secrets：

✅ GMAIL_ADDRESS
✅ GMAIL_APP_PASSWORD
✅ RECIPIENT_EMAIL        ← 新添加的
✅ WEBSITE_URL
```

**重要提示：**
- ⚠️ 添加后您将**无法查看**Secret的值（安全特性）
- ✅ 但可以随时**编辑**或**删除**

---

### 5️⃣ 推送代码更新

**为什么需要这一步？**
- 我们修改了 `emailer.py` 和 `monitor.yml`
- 需要将这些更改推送到GitHub

**操作方法（选择一种）：**

#### 方法A：使用GitHub Desktop
1. 打开 GitHub Desktop
2. 在 "Changes" 中勾选：
   - ✅ `scripts/emailer.py`
   - ✅ `.github/workflows/monitor.yml`
   - ✅ `SECURITY_GUIDE.md`（新文档）
3. 在底部输入提交信息：
   ```
   🔒 增强安全性：使用环境变量配置收件人
   ```
4. 点击 **Commit to main**
5. 点击 **Push origin**

#### 方法B：使用命令行
```bash
git add scripts/emailer.py
git add .github/workflows/monitor.yml
git add SECURITY_GUIDE.md
git commit -m "🔒 增强安全性：使用环境变量配置收件人"
git push
```

---

### 6️⃣ 验证配置是否生效

#### 手动触发工作流测试
1. 进入仓库的 **Actions** 标签
2. 选择 "港股卖空名单监控" 工作流
3. 点击 **Run workflow** > **Run workflow**
4. 等待运行完成（约1-2分钟）

#### 查看日志
1. 点击最新的运行记录
2. 展开 "运行监控脚本" 步骤
3. 查找这一行：
   ```
   ✓ 邮件发送成功到 ***
   ```
   （实际邮箱地址会被屏蔽为***，这是安全特性）

#### 检查邮箱
1. 登录您配置的邮箱
2. 检查收件箱（或垃圾邮件箱）
3. 应该收到一封主题为 "🚨 港股卖空名单更新" 的邮件

---

## ✅ 完成！

恭喜！您已成功配置收件人邮箱，并且：

✅ **安全性提升**
- 邮箱地址不再硬编码在代码中
- 所有敏感信息都在 GitHub Secrets 中
- 完全加密存储

✅ **灵活性提升**
- 可以随时修改收件人
- 无需修改代码
- 支持多个收件人

✅ **隐私保护**
- 邮箱地址不会公开
- 即使仓库是公开的也安全
- 日志中自动屏蔽

---

## 🔧 高级配置

### 更换收件人
1. Settings > Secrets and variables > Actions
2. 点击 `RECIPIENT_EMAIL` 右侧的 ✏️ **Update**
3. 修改值并保存

### 添加更多收件人
在 Secret 值中用逗号分隔：
```
email1@gmail.com, email2@gmail.com, email3@gmail.com
```

### 删除收件人配置
1. Settings > Secrets and variables > Actions
2. 点击 `RECIPIENT_EMAIL` 右侧的 **Remove**
3. 系统会自动发送到 `GMAIL_ADDRESS`（发件人自己）

---

## ❓ 常见问题

### Q: 为什么看不到 Secret 的值？
**A:** 这是GitHub的安全特性，添加后无法查看，但可以编辑或删除。

### Q: 邮件会发送给多少人？
**A:** 取决于您在 `RECIPIENT_EMAIL` 中配置的邮箱数量。

### Q: 可以不配置 RECIPIENT_EMAIL 吗？
**A:** 可以！不配置时，邮件会发送到 `GMAIL_ADDRESS`（发件人自己）。

### Q: 配置后立即生效吗？
**A:** 是的，但需要先推送代码更新到GitHub。

---

## 📞 需要帮助？

参考完整文档：
- 📖 [SECURITY_GUIDE.md](./SECURITY_GUIDE.md) - 安全性详解
- 📖 [README.md](./README.md) - 项目说明
- 📖 [DEPLOYMENT.md](./DEPLOYMENT.md) - 部署指南

---

**教程版本**: v1.0  
**最后更新**: 2026-01-07  
**预计完成时间**: 3分钟
