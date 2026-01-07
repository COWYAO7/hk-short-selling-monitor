# Gmail 应用专用密码配置指南

> 本指南将教你如何为监控系统创建 Gmail 应用专用密码。

---

## 📌 什么是应用专用密码？

应用专用密码是 Google 提供的一种安全机制：
- 🔒 **更安全**：避免泄露真实密码
- 🎯 **专用**：只能用于特定应用
- ✂️ **可撤销**：随时可以删除，不影响账号

---

## 🚀 快速配置（3步）

### 第一步：开启两步验证

1. 访问 [Google 账号安全设置](https://myaccount.google.com/security)
2. 在「登录 Google」部分找到「两步验证」
3. 点击进入并按照提示完成设置

> ⚠️ 需要绑定手机号用于接收验证码

### 第二步：创建应用专用密码

1. 访问 [应用专用密码管理页面](https://myaccount.google.com/apppasswords)
   
   > 💡 或者：账号设置 → 安全性 → 两步验证 → 应用专用密码

2. 如果提示登录，输入你的 Gmail 密码

3. 在「选择应用」下拉菜单中选择「**邮件**」

4. 在「选择设备」下拉菜单中选择「**其他（自定义名称）**」

5. 输入名称：`港股卖空监控`（或任何你喜欢的名称）

6. 点击「**生成**」按钮

### 第三步：保存密码

会显示一个 **16 位密码**，可能的格式：
```
abcd efgh ijkl mnop
```
或者
```
abcdefghijklmnop
```

> ⚠️ **重要：立即复制并保存这个密码！关闭后将无法再次查看。**

建议保存位置：
- 📱 手机备忘录
- 💻 电脑记事本
- 🔐 密码管理器（如 1Password、LastPass）

---

## 🔧 在项目中使用

复制刚才生成的16位密码，在 GitHub 项目中：

1. 进入 `Settings` → `Secrets and variables` → `Actions`
2. 点击 `New repository secret`
3. Name 填写：`GMAIL_APP_PASSWORD`
4. Value 粘贴：应用专用密码（可以包含空格，也可以去掉空格）
5. 点击 `Add secret`

---

## 📸 图文教程

### 1. 进入安全设置

![安全设置](https://i.imgur.com/example1.png)

### 2. 找到两步验证

![两步验证](https://i.imgur.com/example2.png)

### 3. 创建应用密码

![创建密码](https://i.imgur.com/example3.png)

### 4. 生成成功

![生成成功](https://i.imgur.com/example4.png)

---

## ❓ 常见问题

### Q1: 找不到「应用专用密码」选项？

**原因：** 可能还没开启两步验证。

**解决方法：**
1. 先按照上面的步骤开启两步验证
2. 等待几分钟
3. 重新访问应用专用密码页面

---

### Q2: 提示「账号不符合创建应用专用密码的条件」？

**可能原因：**
- 使用的是学校/公司的 Google 账号（管理员可能限制了此功能）
- 账号安全性不足

**解决方法：**
- 使用个人 Gmail 账号
- 联系管理员开启权限
- 或使用其他邮件服务（需要修改代码）

---

### Q3: 应用专用密码被泄露怎么办？

**解决方法：**
1. 访问 [应用专用密码管理页面](https://myaccount.google.com/apppasswords)
2. 找到对应的密码
3. 点击「撤销」
4. 重新生成一个新密码
5. 在 GitHub Secrets 中更新

**优点：** 不影响你的真实密码和其他应用

---

### Q4: 可以用普通密码代替吗？

**不推荐！** 原因：
- ❌ 安全风险高（泄露真实密码）
- ❌ 可能被 Google 拒绝登录
- ❌ 违反 Google 安全最佳实践

**强烈建议使用应用专用密码。**

---

## 🎯 测试配置

配置完成后，如何测试是否正确？

### 方法1：在项目中测试

1. 进入 GitHub Actions
2. 手动触发一次工作流
3. 查看日志，如果没有邮件相关错误，说明配置成功

### 方法2：本地测试（需要 Python）

```bash
cd scripts
pip install -r requirements.txt

# 设置环境变量（Windows PowerShell）
$env:GMAIL_ADDRESS="your-email@gmail.com"
$env:GMAIL_APP_PASSWORD="your-app-password"

# 运行测试
python -c "from emailer import send_email; print('配置正确！' if send_email else '配置有误')"
```

---

## 🔐 安全建议

✅ **推荐做法：**
- 为每个应用创建独立的应用专用密码
- 定期更换密码（如每半年一次）
- 不再使用时立即撤销

❌ **避免：**
- 将密码分享给他人
- 在不安全的地方存储密码
- 在多个应用中重复使用同一个密码

---

## 📚 延伸阅读

- [Google 两步验证官方文档](https://support.google.com/accounts/answer/185839)
- [应用专用密码说明](https://support.google.com/accounts/answer/185833)
- [Gmail SMTP 设置](https://support.google.com/mail/answer/7126229)

---

**配置完成后，记得在 GitHub Secrets 中添加！** 🎉
