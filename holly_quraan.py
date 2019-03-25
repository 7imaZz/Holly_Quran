pfile = open("Holly_Quran.txt", encoding = "utf-8")
dic = dict()
plist = list()
str = pfile.read()
words = str.split()
for word in words:
    dic[word] = dic.get(word,0)+1
for word in words:
    if "و" in word[0]:
        word = word[1:]
        dic[word] = dic.get(word,0)+1
plist = sorted(plist, reverse=True)
str = input("أدخل كلمة:")
str = str.strip()
str2 = str[2:]
try:
    if str.startswith("ال") and str!="الله":
        print("عدد مرات تكرار كلمة",str,"فقط :",dic[str],"مرة")
        try:
            print("عدد مرات تكرار كلمة",str,"أو",str2,":",dic[str]+dic[str2],"مرة")
            count = 0
            for word in words:
                if str2 in word:
                    count += 1   
            print("عدد مرات تكرار كل الكلمات التي تحتوي على",str2,":",count,"مرة")
        except:
            str2 = 0
    else:
        count = 0
        for word in words:
            if str in word:
                count += 1 
        print("عدد مرات تكرار كلمة",str,"فقط:",dic[str],"مرة")
        print("عدد مرات تكرار كل الكلمات التي تحتوي على",str,":",count,"مرة") 
except:
    print(str,"dosen't exist!")