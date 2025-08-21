from PIL import Image
import os
import math


def create_image_grid(base_folder, cols, output_file):
    # 画像フォルダのパス
    image_folder = os.path.join(base_folder, "img")

    # フォルダ内の画像ファイルをファイル名の逆順で取得
    images = sorted(
        [
            os.path.join(image_folder, f)
            for f in os.listdir(image_folder)
            if f.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif"))
        ],
        reverse=False,  # True:逆順 False:順番通り
    )

    if len(images) == 0:
        raise ValueError("フォルダ内に画像が見つかりませんでした。")

    # 横方向の数から縦方向の数を計算
    total_images = len(images)
    rows = math.ceil(total_images / cols)

    # 最初の画像のサイズを基準にする
    sample_image = Image.open(images[0])
    width, height = sample_image.size

    # グリッド全体のサイズを計算
    grid_width = cols * width
    grid_height = rows * height

    # 新しいキャンバスを作成（白背景）
    grid_image = Image.new("RGB", (grid_width, grid_height), color=(255, 255, 255))

    # 画像をキャンバスに貼り付け（左上→右下へ）
    for index, image_path in enumerate(images):
        image = Image.open(image_path)
        image = image.resize((width, height))  # サイズ統一
        x = (index % cols) * width
        y = (index // cols) * height
        grid_image.paste(image, (x, y))

    # 出力ファイルとして保存
    output_path = os.path.join(base_folder, output_file)
    grid_image.save(output_path)
    print(f"画像を保存しました: {output_path}")


# 使用例
if __name__ == "__main__":
    base_folder = r"C:\Users\keigo\OneDrive\ドキュメント\python\imgcombine"
    output_file = "output_grid.jpg"  # 合成画像の出力先ファイル名
    cols = 9  # 横方向の数（指定するだけで縦方向は自動計算）

    create_image_grid(base_folder, cols, output_file)
