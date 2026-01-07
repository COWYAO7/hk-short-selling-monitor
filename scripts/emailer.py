"""
邮件发送模块
负责发送变化通知邮件
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def generate_html_email(change_record, website_url=None):
    """
    生成HTML格式的邮件内容
    
    Args:
        change_record: 变化记录字典
        website_url: 网站URL（可选）
        
    Returns:
        str: HTML邮件内容
    """
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background: white;
                border-radius: 12px;
                padding: 30px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .header {{
                text-align: center;
                padding-bottom: 20px;
                border-bottom: 3px solid #3b82f6;
                margin-bottom: 30px;
            }}
            .header h1 {{
                margin: 0;
                color: #1e293b;
                font-size: 24px;
            }}
            .header .date {{
                color: #64748b;
                font-size: 14px;
                margin-top: 8px;
            }}
            .stats {{
                display: flex;
                justify-content: space-around;
                margin: 20px 0;
                padding: 20px;
                background: #f8fafc;
                border-radius: 8px;
            }}
            .stat {{
                text-align: center;
            }}
            .stat-value {{
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 5px;
            }}
            .stat-label {{
                font-size: 12px;
                color: #64748b;
                text-transform: uppercase;
            }}
            .stat-value.positive {{
                color: #00ff88;
            }}
            .stat-value.negative {{
                color: #ff6b6b;
            }}
            .section {{
                margin: 25px 0;
            }}
            .section-title {{
                font-size: 16px;
                font-weight: 600;
                color: #1e293b;
                margin-bottom: 15px;
                padding-left: 12px;
                border-left: 4px solid #3b82f6;
            }}
            .stock-list {{
                background: #f8fafc;
                border-radius: 8px;
                padding: 15px;
            }}
            .stock-item {{
                padding: 10px;
                margin: 5px 0;
                background: white;
                border-radius: 6px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            .stock-code {{
                font-weight: 600;
                color: #3b82f6;
                font-family: 'Courier New', monospace;
            }}
            .stock-name {{
                flex: 1;
                margin: 0 15px;
            }}
            .stock-currency {{
                color: #64748b;
                font-size: 12px;
            }}
            .added-badge {{
                background: #d1fae5;
                color: #065f46;
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 600;
            }}
            .removed-badge {{
                background: #fee2e2;
                color: #991b1b;
                padding: 4px 12px;
                border-radius: 12px;
                font-size: 12px;
                font-weight: 600;
            }}
            .footer {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #e2e8f0;
                text-align: center;
                color: #64748b;
                font-size: 13px;
            }}
            .button {{
                display: inline-block;
                padding: 12px 24px;
                background: #3b82f6;
                color: white !important;
                text-decoration: none;
                border-radius: 6px;
                margin: 10px 0;
                font-weight: 600;
            }}
            .empty-state {{
                text-align: center;
                padding: 20px;
                color: #94a3b8;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚨 港股卖空名单更新</h1>
                <div class="date">{change_record['date']}</div>
            </div>
            
            <div class="stats">
                <div class="stat">
                    <div class="stat-value">{change_record['new_total']}</div>
                    <div class="stat-label">当前总数</div>
                </div>
                <div class="stat">
                    <div class="stat-value positive">{len(change_record['added'])}</div>
                    <div class="stat-label">新增</div>
                </div>
                <div class="stat">
                    <div class="stat-value negative">{len(change_record['removed'])}</div>
                    <div class="stat-label">移除</div>
                </div>
                <div class="stat">
                    <div class="stat-value {'positive' if change_record['net_change'] > 0 else 'negative'}">{change_record['net_change']:+d}</div>
                    <div class="stat-label">净变化</div>
                </div>
            </div>
    """
    
    # 新增股票
    if change_record['added']:
        html += f"""
            <div class="section">
                <div class="section-title">📈 新增股票 ({len(change_record['added'])})</div>
                <div class="stock-list">
        """
        for stock in change_record['added']:
            html += f"""
                    <div class="stock-item">
                        <span class="stock-code">{stock['code']}</span>
                        <span class="stock-name">{stock['name']}</span>
                        <span class="stock-currency">{stock['currency']}</span>
                        <span class="added-badge">NEW</span>
                    </div>
            """
        html += """
                </div>
            </div>
        """
    
    # 移除股票
    if change_record['removed']:
        html += f"""
            <div class="section">
                <div class="section-title">📉 移除股票 ({len(change_record['removed'])})</div>
                <div class="stock-list">
        """
        for stock in change_record['removed']:
            html += f"""
                    <div class="stock-item">
                        <span class="stock-code">{stock['code']}</span>
                        <span class="stock-name">{stock['name']}</span>
                        <span class="removed-badge">REMOVED</span>
                    </div>
            """
        html += """
                </div>
            </div>
        """
    
    # 网站链接
    if website_url:
        html += f"""
            <div style="text-align: center; margin: 30px 0;">
                <a href="{website_url}" class="button">查看完整数据</a>
            </div>
        """
    
    # 页脚
    html += f"""
            <div class="footer">
                <p>此邮件由港股卖空名单监控系统自动发送</p>
                <p>上次更新: {change_record['old_total']} 只 → 本次更新: {change_record['new_total']} 只</p>
                <p style="margin-top: 10px; font-size: 11px;">
                    发送时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html


def send_email(change_record, gmail_address, gmail_password, website_url=None):
    """
    发送邮件通知
    
    Args:
        change_record: 变化记录字典
        gmail_address: Gmail邮箱地址
        gmail_password: Gmail应用专用密码
        website_url: 网站URL（可选）
        
    Returns:
        bool: 是否发送成功
    """
    try:
        # 创建邮件
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"🚨 港股卖空名单更新 - {change_record['date']} (新增{len(change_record['added'])} 移除{len(change_record['removed'])})"
        msg['From'] = gmail_address
        # 发送到两个邮箱：原配置的邮箱 + iwshgo@gmail.com
        msg['To'] = f"{gmail_address}, iwshgo@gmail.com"
        
        # 生成HTML内容
        html_content = generate_html_email(change_record, website_url)
        html_part = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(html_part)
        
        # 发送邮件
        print("正在连接Gmail SMTP服务器...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_address, gmail_password)
        server.send_message(msg)
        server.quit()
        
        print(f"✓ 邮件发送成功到 {gmail_address}")
        return True
        
    except Exception as e:
        print(f"✗ 邮件发送失败: {str(e)}")
        return False


if __name__ == '__main__':
    # 测试邮件生成（不实际发送）
    print("生成测试邮件HTML...")
    
    test_record = {
        'date': '2026-01-07',
        'old_total': 1234,
        'new_total': 1237,
        'net_change': 3,
        'added': [
            {'code': '00700', 'name': '腾讯控股', 'currency': 'HKD'},
            {'code': '09988', 'name': '阿里巴巴-SW', 'currency': 'HKD'},
            {'code': '01810', 'name': '小米集团-W', 'currency': 'HKD'},
        ],
        'removed': []
    }
    
    html = generate_html_email(test_record, 'https://example.github.io/hk-monitor')
    
    # 保存为文件查看
    with open('test_email.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✓ 已生成 test_email.html，可在浏览器中查看效果")
