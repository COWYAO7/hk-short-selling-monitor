"""
数据持久化模块
负责保存和读取数据文件
"""

import json
import os
from datetime import datetime
from pathlib import Path


# 数据目录路径
DATA_DIR = Path(__file__).parent.parent / 'docs' / 'data'


def ensure_data_dir():
    """确保数据目录存在"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_current_list():
    """
    加载当前保存的名单
    
    Returns:
        dict or None: 当前名单数据，如果不存在返回None
    """
    current_file = DATA_DIR / 'current.json'
    
    if not current_file.exists():
        return None
    
    try:
        with open(current_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"✗ 读取current.json失败: {str(e)}")
        return None


def save_current_list(data):
    """
    保存当前名单
    
    Args:
        data: 名单数据字典
    """
    ensure_data_dir()
    current_file = DATA_DIR / 'current.json'
    
    try:
        with open(current_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ 已保存当前名单到 {current_file}")
    except Exception as e:
        print(f"✗ 保存current.json失败: {str(e)}")
        raise


def load_history():
    """
    加载变化历史
    
    Returns:
        list: 历史变化记录列表
    """
    history_file = DATA_DIR / 'history.json'
    
    if not history_file.exists():
        return []
    
    try:
        with open(history_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"✗ 读取history.json失败: {str(e)}")
        return []


def save_change_record(change_record):
    """
    保存一条变化记录到历史
    
    Args:
        change_record: 变化记录字典
    """
    ensure_data_dir()
    history = load_history()
    
    # 添加新记录到列表开头（最新的在前面）
    history.insert(0, change_record)
    
    # 只保留最近100条记录（防止文件过大）
    history = history[:100]
    
    history_file = DATA_DIR / 'history.json'
    
    try:
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        print(f"✓ 已保存变化记录到历史")
    except Exception as e:
        print(f"✗ 保存history.json失败: {str(e)}")
        raise


def update_stats(current_data, history):
    """
    更新统计数据
    
    Args:
        current_data: 当前名单数据
        history: 历史变化记录
    """
    ensure_data_dir()
    
    # 计算统计数据
    stats = {
        'last_update': current_data['date'],
        'current_total': current_data['total'],
        'total_changes': len(history),
        'update_frequency': {},  # 按月统计更新频率
        'currency_distribution': {},  # 交易货币分布
        'recent_changes': []  # 最近变化摘要
    }
    
    # 统计交易货币分布
    for stock in current_data['stocks']:
        currency = stock.get('currency', 'Unknown')
        stats['currency_distribution'][currency] = stats['currency_distribution'].get(currency, 0) + 1
    
    # 统计每月变化次数
    for record in history:
        date = record['date']
        month = date[:7]  # YYYY-MM
        stats['update_frequency'][month] = stats['update_frequency'].get(month, 0) + 1
    
    # 最近10次变化摘要
    for record in history[:10]:
        stats['recent_changes'].append({
            'date': record['date'],
            'added_count': len(record['added']),
            'removed_count': len(record['removed']),
            'net_change': record['net_change']
        })
    
    # 保存统计数据
    stats_file = DATA_DIR / 'stats.json'
    
    try:
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        print(f"✓ 已更新统计数据")
    except Exception as e:
        print(f"✗ 保存stats.json失败: {str(e)}")


if __name__ == '__main__':
    # 测试代码
    print("测试数据存储模块...")
    ensure_data_dir()
    print(f"数据目录: {DATA_DIR}")
    
    # 测试加载
    current = load_current_list()
    print(f"当前名单: {current['total'] if current else 'None'}")
    
    history = load_history()
    print(f"历史记录数: {len(history)}")
