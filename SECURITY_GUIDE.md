# 🔒 安全性说明与配置指南

## 📋 目录
- [安全性保证](#安全性保证)
- [配置新的收件人邮箱](#配置新的收件人邮箱)
- [安全最佳实践](#安全最佳实践)
- [常见问题](#常见问题)

---

## 🔒 安全性保证

### ✅ 完全安全的部分

#### 1. **邮箱密码（应用专用密码）**
```
存储位置：GitHub Secrets
安全级别：⭐⭐⭐⭐⭐（最高）

✅ AES-256 加密存储
✅ 只有仓库所有者可以访问
✅ 不会出现在代码中
✅ 不会出现在日志中（自动***屏蔽）
✅ 不会出现在网页中
✅ 即使仓库公开也完全安全
```

#### 2. **邮箱地址**
```
存储位置：GitHub Secrets（推荐）
安全级别：⭐⭐⭐⭐⭐

✅ 现在已改为使用环境变量
✅ 不会在代码中硬编码
✅ 可以随时修改
✅ 完全私密
```

### 📊 安全对比

| 项目 | 存储位置 | 安全性 | 会泄露吗 |
|------|----------|--------|----------|
| 应用专用密码 | GitHub Secrets | ⭐⭐⭐⭐⭐ | ❌ 不会 |
| GMAIL_ADDRESS | GitHub Secrets | ⭐⭐⭐⭐⭐ | ❌ 不会 |
| RECIPIENT_EMAIL | GitHub Secrets | ⭐⭐⭐⭐⭐ | ❌ 不会 |
| 数据文件 | GitHub仓库 | ⭐⭐⭐⭐ | ✅ 公开（设计如此） |

---

## 📧 配置新的收件人邮箱

### 方法：使用 GitHub Secrets（推荐）

#### 第1步：进入仓库设置
1. 打开您的GitHub仓库页面
2. 点击顶部的 **Settings（设置）**

#### 第2步：添加新的 Secret
1. 在左侧菜单中找到 **Secrets and variables** > **Actions**
2. 点击 **New repository secret** 按钮

#### 第3步：配置收件人邮箱
```
名称：RECIPIENT_EMAIL
值：your_email@gmail.com, recipient2@example.com
```

**重要说明：**
- ✅ **单个收件人**：直接填写一个邮箱
  ```
  your_email@gmail.com
  ```
  
- ✅ **多个收件人**：用逗号分隔
  ```
  first@gmail.com, second@gmail.com, third@gmail.com
  ```

- ✅ **不配置**：如果不配置此项，邮件会默认发送到 `GMAIL_ADDRESS`（发件人自己）

#### 第4步：保存
1. 点击 **Add secret** 保存
2. ✅ 完成！下次运行时会自动使用新配置

---

## 🛡️ 安全最佳实践

### 1. **使用应用专用密码** ✅
- ✅ 已正确配置
- ✅ 不是真实Gmail密码
- ✅ 可以随时撤销
- ✅ 权限受限

### 2. **定期更换密码**
```
建议频率：每3-6个月

步骤：
1. 访问 https://myaccount.google.com/security
2. 撤销旧的应用专用密码
3. 生成新的应用专用密码
4. 更新GitHub Secret中的 GMAIL_APP_PASSWORD
```

### 3. **监控异常活动**
```
定期检查：
1. Gmail → 设置 → 安全性
2. 查看"最近的安全活动"
3. 检查登录设备和位置
4. 如发现异常，立即撤销应用专用密码
```

### 4. **限制仓库访问权限**
```
✅ 不要添加不信任的协作者
✅ 定期检查仓库访问权限
✅ 使用私有仓库（如需要）
```

---

## ❓ 常见问题

### Q1: 我的邮箱地址会被别人看到吗？
**A:** ❌ 不会！

使用最新配置后：
- ✅ 邮箱地址存储在 GitHub Secrets 中
- ✅ 只有您能看到
- ✅ 不会出现在代码中
- ✅ 不会出现在日志中

---

### Q2: 我的邮箱密码安全吗？
**A:** ✅ 绝对安全！

- ✅ 使用的是应用专用密码，不是真实密码
- ✅ 存储在 GitHub Secrets 中（AES-256加密）
- ✅ GitHub Actions 日志会自动屏蔽显示为 `***`
- ✅ 即使有人访问了您的仓库，也看不到密码

---

### Q3: 如何验证邮件发送到了正确的地址？
**A:** 检查 GitHub Actions 日志

```
步骤：
1. 进入仓库的 Actions 标签
2. 点击最新的工作流运行
3. 查看日志输出
4. 找到这一行：
   ✓ 邮件发送成功到 your_email@gmail.com, recipient2@example.com
```

---

### Q4: 可以发送给多个邮箱吗？
**A:** ✅ 可以！

在 `RECIPIENT_EMAIL` 中用逗号分隔：
```
email1@gmail.com, email2@gmail.com, email3@gmail.com
```

---

### Q5: 如何更换收件人？
**A:** 3个步骤

```
1. 进入 Settings > Secrets and variables > Actions
2. 点击 RECIPIENT_EMAIL 右侧的编辑按钮
3. 修改值并保存
```

✅ 立即生效，无需修改代码！

---

### Q6: 不小心公开了邮箱地址怎么办？
**A:** 不用担心

```
风险评估：
❌ 泄露邮箱地址 → 可能收到垃圾邮件
✅ 密码依然安全 → 不会被盗号
✅ 可以开启Gmail垃圾邮件过滤
```

如果担心，可以：
1. 开启Gmail的强力垃圾邮件过滤
2. 设置邮件规则，只接收来自GitHub Actions的邮件
3. 考虑使用新的邮箱地址专门用于此项目

---

### Q7: GitHub Actions 的日志会泄露信息吗？
**A:** ❌ 不会

GitHub Actions 自动保护敏感信息：

**日志示例：**
```
正在连接Gmail SMTP服务器...
登录邮箱: ***
使用密码: ***
✓ 邮件发送成功到 ***
```

所有来自 Secrets 的值都会被自动替换成 `***`

---

### Q8: 仓库是公开的，安全吗？
**A:** ✅ 完全安全

```
公开的内容：
✅ 代码（无敏感信息）
✅ 监控数据（股票列表，本就公开）

私密的内容：
✅ 邮箱地址（在Secrets中）
✅ 邮箱密码（在Secrets中）
✅ Secrets永远不会公开
```

---

## 🔍 如何检查当前配置

### 方法1：查看 GitHub Secrets
```
1. 进入仓库 Settings
2. Secrets and variables > Actions
3. 检查是否有这些 Secrets：
   ✅ GMAIL_ADDRESS
   ✅ GMAIL_APP_PASSWORD
   ✅ RECIPIENT_EMAIL （可选）
   ✅ WEBSITE_URL
```

### 方法2：查看 Actions 日志
```
1. 进入 Actions 标签
2. 点击最新的运行记录
3. 查看 "运行监控脚本" 步骤
4. 确认日志中显示：
   ✓ 邮件发送成功到 ***
```

---

## 📝 配置示例

### 示例1：发送到单个邮箱
```yaml
RECIPIENT_EMAIL: myemail@gmail.com
```

### 示例2：发送到多个邮箱
```yaml
RECIPIENT_EMAIL: first@gmail.com, second@gmail.com
```

### 示例3：不配置（发送给自己）
```
不添加 RECIPIENT_EMAIL Secret
系统会自动发送到 GMAIL_ADDRESS
```

---

## 🎯 总结

### 当前安全状态：⭐⭐⭐⭐⭐
✅ **密码**：完全安全  
✅ **邮箱地址**：完全安全  
✅ **数据传输**：HTTPS加密  
✅ **存储**：GitHub Secrets加密  

### 风险等级：🟢 极低风险
- 所有敏感信息都使用 GitHub Secrets 保护
- 无硬编码信息
- 所有通信都是加密的
- 符合行业最佳安全实践

---

## 📞 需要帮助？

如果您有任何安全方面的疑问：
1. 查看本文档的常见问题部分
2. 检查 GitHub Actions 的运行日志
3. 访问 [GitHub Secrets 官方文档](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

**最后更新**: 2026-01-07  
**版本**: v1.0 - 安全增强版
