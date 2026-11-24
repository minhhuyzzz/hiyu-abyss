import os
import glob
from PIL import Image
import numpy as np

def get_dhash(image_path, hash_size=8):
    try:
        with Image.open(image_path) as img:
            img = img.convert('L').resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
            pixels = np.asarray(img)
            diff = pixels[:, 1:] > pixels[:, :-1]
            return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except Exception:
        return None

def hamming_distance(h1, h2):
    return bin(h1 ^ h2).count('1')

def main():
    slides = []
    for path in glob.glob("assets/templates/multislides/theme_*/slide_*.jpg"):
        parts = path.replace("\\", "/").split("/")
        theme_str = parts[-2]
        slide_str = parts[-1]
        stt = int(theme_str.replace("theme_", ""))
        h = get_dhash(path)
        if h is not None:
            slides.append((stt, slide_str, path, h))

    print(f"Total slides loaded: {len(slides)}")
    
    # Check for visual duplicates with Hamming distance <= 2
    # If hamming <= 2, check mean pixel diff
    visual_dup_pairs = []
    for i in range(len(slides)):
        for j in range(i + 1, len(slides)):
            t1, s1, p1, h1 = slides[i]
            t2, s2, p2, h2 = slides[j]
            dist = hamming_distance(h1, h2)
            if dist <= 2:
                # Check mean pixel difference on resized 100x100
                im1 = Image.open(p1).convert('RGB').resize((100, 100))
                im2 = Image.open(p2).convert('RGB').resize((100, 100))
                diff = np.mean(np.abs(np.array(im1, dtype=np.float32) - np.array(im2, dtype=np.float32)))
                if diff < 15.0: # Very close / same painting
                    visual_dup_pairs.append((t1, s1, t2, s2, dist, diff))

    print(f"Total visual duplicate pairs (diff < 15): {len(visual_dup_pairs)}")
    for t1, s1, t2, s2, dist, diff in visual_dup_pairs[:30]:
        print(f"  Theme {t1} {s1} <==> Theme {t2} {s2} (dist={dist}, diff={diff:.2f})")

if __name__ == "__main__":
    main()
