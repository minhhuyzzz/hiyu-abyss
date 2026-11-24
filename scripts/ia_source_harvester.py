#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hiyu Abyss - Internet Archive Source Harvester
Integrates archive.org API to query, inspect, and harvest primary texts,
authoritative books, and philosophical treatises for Hiyu Abyss research.
Supports Hard Gate G1 (Primary Text Verification) and HYA-02 source standards.
"""

import os
import json
import internetarchive as ia
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')

def search_archive_books(query, max_results=5, mediatype='texts'):
    """
    Search Internet Archive for items matching query.
    e.g. query: 'creator:"Marcus Aurelius" AND Meditations'
    """
    full_query = f"{query} AND mediatype:{mediatype}"
    search = ia.search_items(full_query)
    results = []
    for idx, item in enumerate(search):
        if idx >= max_results:
            break
        item_id = item['identifier']
        try:
            it = ia.get_item(item_id)
            meta = it.metadata
            files = [f.get('name') for f in it.files if f.get('name', '').endswith(('.pdf', '.epub', '_djvu.txt', '.txt'))]
            results.append({
                "identifier": item_id,
                "title": meta.get('title', 'Unknown Title'),
                "creator": meta.get('creator', 'Unknown Creator'),
                "date": meta.get('date') or meta.get('year', 'Unknown'),
                "description": meta.get('description', '')[:300],
                "canonical_url": f"https://archive.org/details/{item_id}",
                "download_url": f"https://archive.org/download/{item_id}",
                "available_files": files[:5]
            })
        except Exception as e:
            continue
    return results

def get_item_details(identifier):
    """Retrieve complete metadata and text files for an item identifier."""
    item = ia.get_item(identifier)
    return {
        "identifier": identifier,
        "metadata": item.metadata,
        "files": [f.get('name') for f in item.files]
    }

if __name__ == '__main__':
    print("=== TEST IA SOURCE HARVESTER ===")
    test_q = 'creator:"Schopenhauer" AND "Studies in Pessimism"'
    print(f"Searching: {test_q}")
    res = search_archive_books(test_q, max_results=2)
    for r in res:
        print(f"\n[+] Title: {r['title']}")
        print(f"    Author: {r['creator']}")
        print(f"    Year: {r['date']}")
        print(f"    URL: {r['canonical_url']}")
        print(f"    Files: {r['available_files']}")
