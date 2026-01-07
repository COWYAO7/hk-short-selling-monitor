# 部署教程

> 本教程将手把手教你如何部署港股卖空名单监控系统。整个过程约需 **15 分钟**。

---

## 📋 准备工作

在开始之前，你需要：

- ✅ 一个 GitHub 账号
- ✅ 一个 Gmail 邮箱
- ✅ 基本的网页操作能力（会复制粘贴即可）

> 💡 **不需要任何编程知识！**

---

## 第一步：Fork 项目

### 1.1 访问项目页面

打开原始项目地址（如果你从别处获得此项目，请替换为源地址）：
```
https://github.com/原作者/hk-short-selling-monitor
```

### 1.2 点击 Fork

在页面右上角找到 **Fork** 按钮，点击它。

![Fork按钮](https://docs.github.com/assets/cb-23088/images/help/repository/fork_button.png)

### 1.3 创建 Fork

- 保持默认设置不变
- 点击绿色的 **Create fork** 按钮

等待几秒钟，项目就复制到你的账号下了！

---

## 第二步：配置 Gmail（重要！）

### 2.1 开启两步验证

1. 访问 [Google 账号安全设置](https://myaccount.google.com/security)
2. 找到「登录 Google」部分
3. 点击「两步验证」
4. 按照提示完成设置（需要手机号）

> ⚠️ **必须先开启两步验证才能创建应用专用密码！**

### 2.2 创建应用专用密码

1. 访问 [应用专用密码](https://myaccount.google.com/apppasswords)
2. 在「选择应用」下拉菜单中选择「邮件」
3. 在「选择设备」下拉菜单中选择「其他（自定义名称）」
4. 输入名称：`港股监控`
5. 点击「生成」

### 2.3 保存密码

会显示一个 **16 位密码**，格式类似：`abcd efgh ijkl mnop`

> ⚠️ **重要：立即复制保存这个密码，关闭后无法再次查看！**

建议保存到：
- 📝 记事本
- 🔐 密码管理器
- 📱 手机备忘录

---

## 第三步：配置 GitHub Secrets

### 3.1 进入设置页面

在你 Fork 的项目页面：

1. 点击顶部的 **Settings**（设置）
2. 在左侧菜单找到 **Secrets and variables**
3. 点击 **Actions**

### 3.2 添加第一个 Secret

点击绿色的 **New repository secret** 按钮。

**Name（名称）：** 填写
```
GMAIL_ADDRESS
```

**Value（值）：** 填写你的Gmail邮箱地址，例如：
```
your-email@gmail.com
```

点击 **Add secret**。

### 3.3 添加第二个 Secret

再次点击 **New repository secret**。

**Name（名称）：** 填写
```
GMAIL_APP_PASSWORD
```

**Value（值）：** 粘贴刚才保存的16位密码，例如：
```
abcd efgh ijkl mnop
```

> 注意：可以包含空格，也可以去掉空格，都可以。

点击 **Add secret**。

### 3.4 添加第三个 Secret（可选）

这个是网站地址，如果想在邮件中添加查看详情的链接，可以配置。

**Name（名称）：** 填写
```
WEBSITE_URL
```

**Value（值）：** 填写你的网站地址，例如：
```
https://你的用户名.github.io/hk-short-selling-monitor/
```

> 💡 将「你的用户名」替换为你的 GitHub 用户名

点击 **Add secret**。

### 3.5 检查配置

确认你已经添加了这些 Secrets：
- ✅ GMAIL_ADDRESS
- ✅ GMAIL_APP_PASSWORD
- ✅ WEBSITE_URL（可选）

---

## 第四步：启用 GitHub Pages

### 4.1 进入 Pages 设置

1. 在项目页面点击 **Settings**
2. 在左侧菜单找到 **Pages**

### 4.2 配置部署源

在「Build and deployment」部分：

**Source（源）：** 选择
```
Deploy from a branch
```

**Branch（分支）：** 选择
- Branch: `main`
- Folder: `/docs`

点击 **Save**。

### 4.3 等待部署

大约 1 分钟后，页面顶部会显示：

> ✅ Your site is live at https://你的用户名.github.io/hk-short-selling-monitor/

---

## 第五步：首次运行

### 5.1 进入 Actions 页面

在项目页面点击顶部的 **Actions**。

### 5.2 手动触发工作流

1. 在左侧点击「港股卖空名单监控」
2. 在右侧点击 **Run workflow** 下拉按钮
3. 点击绿色的 **Run workflow** 按钮

### 5.3 查看运行状态

- 🟡 黄色圆点 = 正在运行
- ✅ 绿色勾 = 运行成功
- ❌ 红色叉 = 运行失败

点击工作流可以查看详细日志。

### 5.4 首次运行说明

⚠️ **首次运行不会发送邮件**，因为还没有历史数据可对比。

从第二次运行开始，如果检测到变化，就会发送邮件。

---

## 第六步：验证部署

### 6.1 访问网站

在浏览器打开：
```
https://你的用户名.github.io/hk-short-selling-monitor/
```

### 6.2 检查数据

你应该能看到：
- ✅ 首页显示当前名单总数
- ✅ 完整名单页面可以搜索
- ✅ 历史记录页面（首次可能为空）
- ✅ 统计分析页面

### 6.3 等待自动运行

从现在开始，系统会在每天：
- 🕘 **北京时间 9:00**
- 🕕 **北京时间 18:00**

自动检查名单变化。

---

## 🎉 部署完成！

现在你可以：

- 📧 等待邮件通知（有变化时才会发送）
- 🌐 随时访问网站查看最新数据
- 📊 查看历史变化趋势

---

## 🔧 进阶配置

### 修改运行时间

如果想改变自动运行的时间：

1. 进入项目，点击 `.github/workflows/monitor.yml`
2. 点击右上角的 ✏️ 编辑
3. 修改 `cron` 时间（使用 UTC 时间，比北京时间慢 8 小时）：

```yaml
schedule:
  - cron: '0 1 * * *'    # UTC 1:00 = 北京时间 9:00
  - cron: '0 10 * * *'   # UTC 10:00 = 北京时间 18:00
```

例如，改成每天中午12点和晚上10点：
```yaml
schedule:
  - cron: '0 4 * * *'    # UTC 4:00 = 北京时间 12:00
  - cron: '0 14 * * *'   # UTC 14:00 = 北京时间 22:00
```

4. 点击 **Commit changes**

### 手动触发运行

随时可以在 Actions 页面手动触发运行，无需等待定时任务。

---

## ❓ 遇到问题？

### 问题1：Actions 运行失败

**解决方法：**
1. 点击失败的工作流查看日志
2. 检查 Secrets 是否配置正确
3. 确认 Gmail 应用专用密码是否有效

### 问题2：没有收到邮件

**可能原因：**
- 首次运行不会发邮件（没有历史数据对比）
- 名单确实没有变化
- Gmail 配置有误

**检查方法：**
1. 查看 Actions 日志，搜索「邮件」
2. 检查 Gmail 的垃圾邮件文件夹
3. 确认 Secrets 中的邮箱地址正确

### 问题3：网站打不开

**解决方法：**
1. 确认 GitHub Pages 已启用
2. 检查是否选择了 `main` 分支和 `/docs` 文件夹
3. 等待 1-2 分钟让部署完成
4. 清除浏览器缓存后重试

---

## 📞 获取帮助

如果遇到问题：

1. 查看 [常见问题](README.md#常见问题)
2. 在 GitHub 项目提交 Issue
3. 查看 Actions 运行日志寻找错误信息

---

**祝你部署顺利！🎊**
