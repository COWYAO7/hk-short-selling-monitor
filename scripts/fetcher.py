"""
数据爬取模块
负责从港交所网站获取最新的卖空名单数据
"""

import requests
import re
import csv
from io import StringIO
from datetime import datetime
from bs4 import BeautifulSoup


def fetch_latest_csv_url():
    """
    从港交所页面获取最新CSV文件的下载链接
    
    Returns:
        tuple: (CSV URL, 生效日期)
    """
    base_url = "https://www.hkex.com.hk/Services/Trading/Securities/Securities-Lists/Designated-Securities-Eligible-for-Short-Selling?sc_lang=zh-HK"
    
    # 添加User-Agent，避免被拒绝访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(base_url, headers=headers, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找第一个CSV下载链接（即最新的）
        csv_links = soup.find_all('a', href=re.compile(r'ds_list\d{8}_c\.csv'))
        
        if not csv_links:
            raise Exception("未找到CSV下载链接")
        
        # 获取最新的链接
        latest_link = csv_links[0]['href']
        
        # 提取日期 (格式: ds_list20260109_c.csv -> 20260109)
        date_match = re.search(r'ds_list(\d{8})_c\.csv', latest_link)
        if date_match:
            date_str = date_match.group(1)
            # 转换为 YYYY-MM-DD 格式
            effective_date = f"{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]}"
        else:
            effective_date = datetime.now().strftime('%Y-%m-%d')
        
        # 构建完整URL
        if latest_link.startswith('http'):
            csv_url = latest_link
        else:
            csv_url = f"https://www.hkex.com.hk{latest_link}"
        
        print(f"✓ 找到最新CSV: {csv_url}")
        print(f"✓ 生效日期: {effective_date}")
        
        return csv_url, effective_date
        
    except Exception as e:
        print(f"✗ 获取CSV链接失败: {str(e)}")
        raise


def parse_csv_data(csv_url):
    """
    下载并解析CSV数据
    
    Args:
        csv_url: CSV文件的URL
        
    Returns:
        list: 股票列表，每个元素是一个字典
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(csv_url, headers=headers, timeout=30)
        response.encoding = 'utf-8-sig'  # 处理BOM
        
        # 使用csv模块正确解析（避免字段中的逗号导致错误）
        csv_reader = csv.reader(StringIO(response.text))
        lines = list(csv_reader)
        
        # 找到表头行（包含"數目,股份代號,股份簡稱"）
        header_index = -1
        for i, row in enumerate(lines):
            if any('股份代號' in cell for cell in row):
                header_index = i
                break
        
        if header_index == -1:
            raise Exception("CSV格式不正确：未找到表头")
        
        # 解析数据
        stocks = []
        for row in lines[header_index + 1:]:
            # 跳过空行
            if not row or not row[0].strip():
                continue
            
            if len(row) >= 4:
                stock = {
                    'number': row[0].strip(),
                    'code': row[1].strip(),
                    'name': row[2].strip(),
                    'currency': row[3].strip(),
                    'type': row[4].strip() if len(row) > 4 else '',
                    'exempt': row[5].strip() if len(row) > 5 else '',
                    'remarks': row[6].strip() if len(row) > 6 else ''
                }
                stocks.append(stock)
        
        print(f"✓ 成功解析 {len(stocks)} 只股票")
        return stocks
        
    except Exception as e:
        print(f"✗ 解析CSV失败: {str(e)}")
        raise


def fetch_latest_list():
    """
    获取最新的卖空名单
    
    Returns:
        dict: 包含日期和股票列表的字典
    """
    csv_url, effective_date = fetch_latest_csv_url()
    stocks = parse_csv_data(csv_url)
    
    return {
        'date': effective_date,
        'total': len(stocks),
        'stocks': stocks,
        'fetched_at': datetime.now().isoformat()
    }


if __name__ == '__main__':
    # 测试代码
    print("开始获取最新卖空名单...")
    data = fetch_latest_list()
    print(f"\n生效日期: {data['date']}")
    print(f"股票总数: {data['total']}")
    print(f"\n前5只股票:")
    for stock in data['stocks'][:5]:
        print(f"  {stock['code']} - {stock['name']}")
