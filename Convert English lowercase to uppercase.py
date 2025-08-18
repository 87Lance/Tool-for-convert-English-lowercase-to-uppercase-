
def uppercase_sentence(sentence):
  """
  將英文句子中的所有小寫字母轉換成大寫。

  Args:
    sentence: 輸入的英文句子 (字串)。

  Returns:
    轉換成大寫的句子 (字串)。
  """
  return sentence.upper()


print("這是一個英文小寫轉大寫的程式")
print("輸入想要轉換的英文，或輸入 '0' 來結束程式。")
print("-" * 40)

while True: # 建立無限迴圈
    user_input = input("請輸入您的句子 (輸入 0 結束): ")

    if user_input == '0':
        print("您輸入了 '0'，程式即將結束。")
        break # 使用者輸入 '0'，則跳出迴圈，結束程式
    else:
        # 呼叫函數
        converted_sentence = uppercase_sentence(user_input)
        print("↓" * 40) 
        print(f"轉換後的大寫句子: {converted_sentence}")
        print("-" * 40) 