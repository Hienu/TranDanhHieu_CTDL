print("Món trà sữa yêu thích của Hìn là gì?")

dap_an = "bạc hà"

while True:
    user_answer = input("Mời bạn đoán thử: ")

    if user_answer.lower() == dap_an.lower():
        print("Chính xác! Món trà sữa yêu thích của bạn là bạc hà.")
        break  
    else:
        print("Sai rồi. Hãy thử lại.")