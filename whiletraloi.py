print("Vị trà sữa yêu thích của Hìn là gì?")

dap_an = "bạc hà"

while True:
    user_answer = input("Mời bạn đoán thử: ")

    if user_answer.lower() == dap_an.lower():
        print("Hên đấy, sai lần nữa chết với bà!")
        break  
    else:
        print("Xin chúc mừng bạn đã đoán sai rồi :D Hãy thử lại.")