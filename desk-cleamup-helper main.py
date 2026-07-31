import cv2

def main():
    print("=== AI 桌面雜物辨識小幫手啟動 ===")
    
    # 1. 開啟電腦內建鏡頭
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("無法開啟鏡頭！")
        return

    print("按下 's' 鍵拍照並模擬 AI 辨識，按下 'q' 鍵離開。")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("無法讀取畫面")
            break

        # 顯示即時畫面
        cv2.imshow('Desk Cleanup Helper', frame)

        key = cv2.waitKey(1) & 0xFF
        
        # 2. 模擬拍照與 AI 辨識觸發
        if key == ord('s'):
            print("\n[AI 辨識中...] 正在分析桌面物件...")
            # 這裡可以接你的影像辨識邏輯或輸出結果
            print("【辨識結果】發現：雜物（充電線、筆記本）")
            print("【整理建議】建議將充電線收進抽屜，筆記本放回書架！\n")
            
        # 3. 按 q 離開程式
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()