import os
import re


def extract_sort_key(filename):
    # 例: book_01.jpg → (1, 0), book_01 (1).jpg → (1, 1)
    name, _ = os.path.splitext(filename)

    # ベース番号を抽出（例: book_01 → 01）
    num_match = re.search(r"(\d+)", name)
    number = int(num_match.group(1)) if num_match else 0

    # ページ番号を抽出（例: book_01 (2) → 2）
    page_match = re.search(r"\((\d+)\)", name)
    page = int(page_match.group(1)) if page_match else 0

    return (page, number)


def rename_images_logically(image_folder, digits=3):
    # 対象ファイルの一覧を取得し、カスタムキーでソート
    images = sorted(
        [
            f
            for f in os.listdir(image_folder)
            if f.lower().endswith(("jpg", "jpeg", "png", "bmp", "gif", "pdf"))
        ],
        key=extract_sort_key,
    )

    # ソート後に連番でリネーム
    for i, filename in enumerate(images):
        ext = os.path.splitext(filename)[1]
        new_name = f"{str(i + 1).zfill(digits)}{ext}"
        src = os.path.join(image_folder, filename)
        dst = os.path.join(image_folder, new_name)
        os.rename(src, dst)
        print(f"{filename} → {new_name}")


# 使用例
if __name__ == "__main__":
    image_folder = r"C:\Users\keigo\OneDrive\ドキュメント\python\imgcombine\img"
    rename_images_logically(image_folder, digits=3)
