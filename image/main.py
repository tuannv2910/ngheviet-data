import os
from PIL import Image

ROOT_FOLDER = r"C:\Users\Admin\Documents\ngheviet\ngheviet-data\image"

def resize_image_inplace(file_path):
    try:
        with Image.open(file_path) as img:
            # Convert nếu cần (tránh lỗi PNG RGBA)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Tính kích thước mới (50%)
            new_width = img.width // 2
            new_height = img.height // 2

            # Resize
            img_resized = img.resize((new_width, new_height), Image.LANCZOS)

            # Ghi đè lại ảnh cũ
            img_resized.save(file_path, optimize=True, quality=75)

            print(f"✅ Done: {file_path}")

    except Exception as e:
        print(f"❌ Error: {file_path} - {e}")


def process_all_images(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(root, file)
                resize_image_inplace(file_path)


if __name__ == "__main__":
    process_all_images(ROOT_FOLDER)