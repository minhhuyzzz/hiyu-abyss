import json
import os
import glob
from collections import defaultdict

with open("scripts/duplicates_1_to_300_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

print(f"Total clusters: {len(report)}")

# We want to identify for each slide in themes 1-300 which ones are duplicates across DIFFERENT themes
inter_theme_dups = []
intra_theme_dups = []

for c in report:
    slides = c["slides"]
    stts = set(s["stt"] for s in slides)
    if len(stts) > 1:
        # Duplicates across different themes!
        inter_theme_dups.append(c)
    else:
        # Same theme having multiple files with same image (e.g. slide_1.jpg and slide_1_establishing.jpg)
        intra_theme_dups.append(c)

print(f"Clusters spanning MULTIPLE different themes: {len(inter_theme_dups)}")
print(f"Clusters within the SAME theme (aliases): {len(intra_theme_dups)}")

total_inter_slides = sum(len(c["slides"]) for c in inter_theme_dups)
print(f"Total slide instances in cross-theme duplicate clusters: {total_inter_slides}")

# Print the cross-theme duplicate clusters
print("\n=== TOP CROSS-THEME DUPLICATE CLUSTERS ===")
affected_themes = set()
for c in inter_theme_dups[:25]:
    stt_list = sorted(list(set(s["stt"] for s in c["slides"])))
    for stt in stt_list:
        affected_themes.add(stt)
    print(f"\nCluster #{c['cluster_id']} (Themes: {stt_list}):")
    for s in c["slides"]:
        print(f"   Theme {s['stt']} ({s['folder']}): {s['filename']}")

for c in inter_theme_dups:
    for s in c["slides"]:
        affected_themes.add(s["stt"])

print(f"\nTotal distinct themes affected by cross-theme duplicates: {len(affected_themes)} / 300")
