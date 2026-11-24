#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Harvest Financial Philosophy & Money Psychology from Internet Archive (archive.org)
Queries primary source texts on money, wealth, greed, debt, and conspicuous consumption:
1. Arthur Schopenhauer - The Wisdom of Life / Studies in Pessimism ("What a Man Has")
2. Seneca - On Benefits / Letters from a Stoic (Wealth & Freedom)
3. Thorstein Veblen - The Theory of the Leisure Class (Conspicuous Consumption)
4. Benjamin Franklin - The Way to Wealth
5. Epictetus - Discourses (Property & Freedom)

Outputs: data/harvested_financial_primary_sources.json
"""

import os
import json
import internetarchive as ia
from dotenv import load_dotenv

load_dotenv('.env')

TARGET_WORKS = [
    {
        "author": "Arthur Schopenhauer",
        "title": "The Wisdom of Life",
        "query": 'creator:"Schopenhauer" AND "Wisdom of Life" AND mediatype:texts',
        "topic": "Bản chất của tài sản & Lòng tham vô tận",
        "key_concept": "Tiền bạc giống như nước biển: Càng uống càng khát. Sự giàu có là những gì ta bảo toàn, không phải những gì ta phô trương."
    },
    {
        "author": "Seneca",
        "title": "On Benefits",
        "query": 'creator:"Seneca" AND "Benefits" AND mediatype:texts',
        "topic": "Tâm lý nợ nần & Quà tặng có toan tính",
        "key_concept": "Nhận một món quà độc hại từ kẻ xảo quyệt là tự bán đi sự tự do của chính mình."
    },
    {
        "author": "Thorstein Veblen",
        "title": "The Theory of the Leisure Class",
        "query": 'creator:"Veblen" AND "Leisure Class" AND mediatype:texts',
        "topic": "Tiêu dùng phô trương (Conspicuous Consumption)",
        "key_concept": "Người ta mua sắm xa xỉ không phải vì công năng của đồ vật, mà để mua sự ghen tị và công nhận từ xã hội."
    },
    {
        "author": "Benjamin Franklin",
        "title": "The Way to Wealth",
        "query": 'creator:"Benjamin Franklin" AND "Way to Wealth" AND mediatype:texts',
        "topic": "Kỷ luật chi tiêu & Tự do tài chính",
        "key_concept": "Người đi vay là nô lệ của người cho vay, và kẻ mắc nợ phải cúi đầu trước chủ nợ."
    },
    {
        "author": "Epictetus",
        "title": "Discourses",
        "query": 'creator:"Epictetus" AND "Discourses" AND mediatype:texts',
        "topic": "Tài sản và Vòng tròn kiểm soát Khắc kỷ",
        "key_concept": "Của cải bên ngoài không thuộc quyền kiểm soát của bạn; chỉ có thái độ và nhu cầu của bạn mới là thứ bạn làm chủ."
    }
]

def harvest_sources():
    print("=== BẮT ĐẦU CÀO VĂN BẢN GỐC TÀI CHÍNH TỪ INTERNET ARCHIVE (archive.org) ===")
    os.makedirs('data', exist_ok=True)
    harvested_data = []

    for target in TARGET_WORKS:
        print(f"\n🔍 Đang tra cứu: {target['author']} — {target['title']}")
        search = ia.search_items(target['query'])
        found = False
        for item in search:
            item_id = item['identifier']
            try:
                it = ia.get_item(item_id)
                meta = it.metadata
                title = meta.get('title', target['title'])
                date = meta.get('date') or meta.get('year', 'Unknown')
                text_files = [f.get('name') for f in it.files if f.get('name', '').endswith(('.pdf', '_djvu.txt', '.epub', '.txt'))]
                
                record = {
                    "author": target['author'],
                    "target_title": target['title'],
                    "archive_id": item_id,
                    "title": title,
                    "date": date,
                    "canonical_url": f"https://archive.org/details/{item_id}",
                    "download_url": f"https://archive.org/download/{item_id}",
                    "available_files": text_files[:4],
                    "core_topic": target['topic'],
                    "primary_insight": target['key_concept']
                }
                harvested_data.append(record)
                print(f"  ✓ Tìm thấy: {title} ({date})")
                print(f"    URL: https://archive.org/details/{item_id}")
                print(f"    Files: {text_files[:2]}")
                found = True
                break
            except Exception as e:
                print(f"  ⚠️ Lỗi đọc item {item_id}: {e}")
                continue
        if not found:
            print(f"  ⚠️ Không tìm thấy bản scan phù hợp cho query: {target['query']}")

    output_path = 'data/harvested_financial_primary_sources.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(harvested_data, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Đã lưu {len(harvested_data)} nguồn văn bản gốc vào: {output_path}")

if __name__ == '__main__':
    harvest_sources()
