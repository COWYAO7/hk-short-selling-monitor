"""
数据对比模块
负责比较新旧名单，检测变化
"""

from datetime import datetime


def compare_lists(old_data, new_data):
    """
    比较新旧名单，检测变化
    
    Args:
        old_data: 旧名单数据字典（可以为None）
        new_data: 新名单数据字典
        
    Returns:
        dict: 包含变化信息的字典，如果无变化返回None
    """
    # 如果是首次运行（没有旧数据）
    if old_data is None:
        print("✓ 首次运行，初始化数据")
        return None
    
    # 提取股票代码集合
    old_codes = {stock['code'] for stock in old_data['stocks']}
    new_codes = {stock['code'] for stock in new_data['stocks']}
    
    # 检测新增和删除
    added_codes = new_codes - old_codes
    removed_codes = old_codes - new_codes
    
    # 如果没有变化
    if not added_codes and not removed_codes:
        print("✓ 名单无变化")
        return None
    
    # 构建详细的变化信息
    added_stocks = [
        stock for stock in new_data['stocks'] 
        if stock['code'] in added_codes
    ]
    
    removed_stocks = [
        stock for stock in old_data['stocks'] 
        if stock['code'] in removed_codes
    ]
    
    # 按股票代码排序
    added_stocks.sort(key=lambda x: x['code'])
    removed_stocks.sort(key=lambda x: x['code'])
    
    change_record = {
        'date': new_data['date'],
        'timestamp': datetime.now().isoformat(),
        'old_total': old_data['total'],
        'new_total': new_data['total'],
        'net_change': len(added_codes) - len(removed_codes),
        'added': added_stocks,
        'removed': removed_stocks
    }
    
    print(f"✓ 检测到变化:")
    print(f"  新增: {len(added_stocks)} 只")
    print(f"  移除: {len(removed_stocks)} 只")
    print(f"  净变化: {change_record['net_change']:+d} 只")
    
    return change_record


def format_change_summary(change_record):
    """
    格式化变化摘要（用于日志和通知）
    
    Args:
        change_record: 变化记录字典
        
    Returns:
        str: 格式化的摘要文本
    """
    lines = []
    lines.append(f"更新日期: {change_record['date']}")
    lines.append(f"总数变化: {change_record['old_total']} → {change_record['new_total']} ({change_record['net_change']:+d})")
    
    if change_record['added']:
        lines.append(f"\n新增 {len(change_record['added'])} 只股票:")
        for stock in change_record['added']:
            lines.append(f"  [{stock['code']}] {stock['name']} ({stock['currency']})")
    
    if change_record['removed']:
        lines.append(f"\n移除 {len(change_record['removed'])} 只股票:")
        for stock in change_record['removed']:
            lines.append(f"  [{stock['code']}] {stock['name']}")
    
    return '\n'.join(lines)


if __name__ == '__main__':
    # 测试代码
    print("测试数据对比模块...")
    
    # 模拟数据
    old = {
        'date': '2026-01-01',
        'total': 3,
        'stocks': [
            {'code': '00001', 'name': '长和', 'currency': 'HKD'},
            {'code': '00002', 'name': '中电控股', 'currency': 'HKD'},
            {'code': '00003', 'name': '香港中华煤气', 'currency': 'HKD'},
        ]
    }
    
    new = {
        'date': '2026-01-07',
        'total': 3,
        'stocks': [
            {'code': '00001', 'name': '长和', 'currency': 'HKD'},
            {'code': '00002', 'name': '中电控股', 'currency': 'HKD'},
            {'code': '00700', 'name': '腾讯控股', 'currency': 'HKD'},
        ]
    }
    
    changes = compare_lists(old, new)
    if changes:
        print("\n" + format_change_summary(changes))
