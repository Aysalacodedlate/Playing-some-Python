#txt nomli string saqlovchi o'zgaruvchi berilgan. 
# txtdagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. 
# Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, 
# ostki chiziqcha keyingi harfdan keyin qo'yilsin. 
# Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

def add_underscore(txt):
    vowels = "aAiIoOuUeE"
    result = []  
    count = 0  
    for i, char in enumerate(txt):
        result.append(char)
        count += 1
        if count == 3:
            if char in vowels or (len(result) > 1 and result[-2] == '_'):
                continue  
            elif i != len(txt) - 1:  
                result.append('_')
            count = 0  

    return ''.join(result)

# sample 
txt = "Mandutormenovazam"
output = add_underscore(txt)
print(output)
