import os
import shutil
import re


def copy_images_with_reversed_renaming(base_folder):
    imgfolders_path = os.path.join(base_folder, "imgfolders")
    img_output_path = os.path.join(base_folder, "img")

    os.makedirs(img_output_path, exist_ok=True)

    for subfolder in sorted(os.listdir(imgfolders_path)):
        subfolder_path = os.path.join(imgfolders_path, subfolder)
        if not os.path.isdir(subfolder_path):
            continue

        # .jpg のみを対象とし、数値でソート（降順）
        jpg_files = [
            f for f in os.listdir(subfolder_path) if f.lower().endswith(".jpg")
        ]
        jpg_files = sorted(
            jpg_files, key=lambda x: int(re.search(r"(\d+)", x).group()), reverse=True
        )

        for i, filename in enumerate(jpg_files):
            new_number = str(i + 1).zfill(3)  # 3桁の連番を振る
            new_name = f"{subfolder}{new_number}.jpg"
            src = os.path.join(subfolder_path, filename)
            dst = os.path.join(img_output_path, new_name)

            shutil.copy2(src, dst)
            print(f"コピー: {src} → {dst}")


# 使用例
if __name__ == "__main__":
    base_folder = r"C:\Users\keigo\OneDrive\ドキュメント\python\imgcombine"
    copy_images_with_reversed_renaming(base_folder)
