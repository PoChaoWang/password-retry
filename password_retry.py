password = 'a123456'
n = 0
y = 3
while n < 3:
    pw = input('請輸入密碼： ')
    if n == 2:
        print('密碼錯誤，已無輸入機會')
        break
    else:
        if pw == password:
            print('登入成功！')
            break
        else:
            y -= 1
            print('密碼錯誤！還有', y,'次機會')
            n += 1