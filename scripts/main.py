"""
主程序入口
协调各个模块完成监控任务
"""

import os
import sys
from datetime import datetime

# 导入自定义模块
from fetcher import fetch_latest_list
from comparator import compare_lists, format_change_summary
from storage import load_current_list, save_current_list, save_change_record, update_stats, load_history
from emailer import send_email


def main():
    """主函数"""
    print("=" * 60)
    print("港股卖空名单监控系统")
    print(f"运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    try:
        # 1. 获取最新数据
        print("\n[1/5] 正在获取最新数据...")
        new_data = fetch_latest_list()
        
        # 2. 加载旧数据
        print("\n[2/5] 正在加载历史数据...")
        old_data = load_current_list()
        
        if old_data:
            print(f"  上次数据日期: {old_data['date']}")
            print(f"  上次股票数量: {old_data['total']}")
        else:
            print("  首次运行，无历史数据")
        
        # 3. 对比数据
        print("\n[3/5] 正在对比数据...")
        change_record = compare_lists(old_data, new_data)
        
        # 4. 保存数据
        print("\n[4/5] 正在保存数据...")
        save_current_list(new_data)
        
        if change_record:
            # 有变化，保存变化记录
            save_change_record(change_record)
            
            # 更新统计数据
            history = load_history()
            update_stats(new_data, history)
            
            # 打印变化摘要
            print("\n" + "=" * 60)
            print("检测到变化!")
            print("=" * 60)
            print(format_change_summary(change_record))
            print("=" * 60)
            
            # 5. 发送邮件通知
            print("\n[5/5] 正在发送邮件通知...")
            
            # 从环境变量获取邮箱配置
            gmail_address = os.getenv('GMAIL_ADDRESS')
            gmail_password = os.getenv('GMAIL_APP_PASSWORD')
            website_url = os.getenv('WEBSITE_URL', '')
            
            if not gmail_address or not gmail_password:
                print("⚠ 警告: 未配置Gmail凭据，跳过邮件发送")
                print("  请设置环境变量: GMAIL_ADDRESS 和 GMAIL_APP_PASSWORD")
            else:
                success = send_email(change_record, gmail_address, gmail_password, website_url)
                if success:
                    print("✓ 任务完成！已发送邮件通知")
                else:
                    print("⚠ 数据已保存，但邮件发送失败")
        else:
            # 无变化
            print("  名单无变化，无需发送通知")
            
            # 仍然更新统计数据（更新最后检查时间）
            history = load_history()
            update_stats(new_data, history)
            
            print("\n✓ 任务完成！名单无变化")
        
        print("\n" + "=" * 60)
        print("程序执行完毕")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        print(f"\n✗ 程序执行失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
