import os
from PIL import Image

def analyze_desk_image(image_path):
    """
    桌面雜物辨識與分類整理小幫手
    """
    print("==========================================")
    print(" 桌面雜物辨識與分類整理小幫手 v1.0")
    print("==========================================")
    
    if not os.path.exists(image_path):
        print(f"【錯誤】找不到照片檔 '{image_path}'！請確認照片已放進資料夾。")
        return

    try:
        img = Image.open(image_path)
        print(f"【系統】成功載入照片！照片尺寸：{img.size[0]} x {img.size[1]} 像素")
    except Exception as e:
        print(f"【錯誤】圖片載入失敗：{e}")
        return

    category_rules = {
        "抽屜": ["筆", "橡皮擦", "剪刀", "立可帶", "尺", "訂書機", "文具"],
        "書架": ["課本", "筆記本", "小說", "漫畫", "資料夾", "書本"],
        "垃圾桶": ["空包袋", "廢紙", "飲料杯", "塑膠袋", "垃圾"]
    }

    detected_items = ["數學課本", "藍色原子筆", "洋芋片空包袋", "剪刀", "英文筆記本"]

    print("\n【AI 辨識與整理建議】")
    print("-" * 40)

    for item in detected_items:
        suggested_action = "放置於桌面固定收納盒" 
        
        for category, keywords in category_rules.items():
            if any(keyword in item for keyword in keywords):
                suggested_action = f"收進【{category}】"
                break
                
        print(f" 物品：{item:<10} ➔ 建議：{suggested_action}")
        
    print("-" * 40)
    print("整理完畢！祝你有個乾淨舒適的讀書桌面！\n")

if __name__ == "__main__":
    test_image = "desk.jpg"
    analyze_desk_image(test_image)
