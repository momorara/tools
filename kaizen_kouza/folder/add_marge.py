"""
tel_addとmail_addをマージします。

"""
import os
import csv

# ------------ 環境確認 ------------------------
path = os.getcwd() + '/'  # 現在のパスを取得
print(path)

# 自分のいるフォルダ名を取得
# フォルダ名 os.path.dirname()
dir = os.path.dirname(path)
print('dir:', dir)
# index =dir.rfind("kaizen_kouza") +13
index =dir.rfind('/') +1
if index < 1 :
    index = dir.rfind('\\') + 1  # バックスラッシュの検索はややこしいね。
print('index:',index)
folderName1 = dir[index:]
print('folderName1:', folderName1)
folderDir1 = dir[:index]
print('folderDir1:', folderDir1)

folderDir2 = folderDir1[:-1]
print('folderDir2:', folderDir2)
index = folderDir2.rfind('\\') + 1
# print('index:',index)
folderName2 = folderDir2[index:]
print('folderName2:', folderName2)

# ------------ 人名、所属データ読み込み ------------------------
# 2要素を辞書型でcsvから読み込む
tel_address = {}
try:
    with open(folderDir1 + 'kihon_data\\' + 'tel_address.csv', mode='r') as inp:
        reader = csv.reader(inp)
        tel_address = {rows[4]:(rows[0],rows[2],'no_mail') for rows in reader}
except:
    with open(folderDir1 + 'kihon_data/' + 'tel_address.csv', mode='r',encoding="cp932") as inp:
        reader = csv.reader(inp)
        tel_address = {rows[4]:(rows[0],rows[2],'no_mail') for rows in reader}
# key:内線　名前、所属、mailの入れ物
# print(tel_address)

# 名前と所属をmail_addにあわせて整形
for i in range(2000,8000):
    if str(i) in tel_address:
        name,bushiyo,mail = tel_address[str(i)]
        name = name.replace('　',' ')
        bushiyo = bushiyo.replace(' ','')
        bushiyo = bushiyo.replace('エンジニアリング事業本部','')
        tel_address[str(i)] = name,bushiyo,mail
# print(tel_address)

# ------------ 人名、所属データ読み込み ------------------------
# csvからリストで読み込む
from csv import reader
try:
    with open(folderDir1 + 'kihon_data\\' + 'mail_Address.csv', mode='r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        mail_address = list(csv_reader)
except:
    with open(folderDir1 + 'kihon_data/' + 'mail_Address.csv', mode='r',encoding="utf-8") as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        mail_address = list(csv_reader)
# no、名前、所属、役職、メール
# print(mail_address[5])


# --------tel_addressにmail_addressのmailをマージ ------------------------
# 全ての内線
for tel_no in range(2000,8000):
    # 存在する内線
    if str(tel_no) in tel_address:
        name,bushiyo,mail = tel_address[str(tel_no)]
        name_mach = []
        for no in range(len(mail_address)):
            if mail_address[no][1] == name:
                name_mach.append(no)
        if len(name_mach) == 0:# 一致した名前がない
            pass
        if len(name_mach) == 1:# 一件のみ名前が一致した。
            mail = mail_address[name_mach[0]][4]
        if len(name_mach) > 1:
            # 複数名前が一致した。
            # 部署が一致するものを探す
            for test_no in name_mach:
                if mail_address[test_no][2] == bushiyo:
                    mail = mail_address[test_no][4]
                    break
        tel_address[str(tel_no)] = name,bushiyo,mail
print()
print(tel_address['4812'])





# key:名前　所属、メール
# print(mail_address)


# name,bushiyo,mail = tel_address[str(4812)]
# print(name,bushiyo,mail)

# bushiyo1,mail = mail_address[name]
# print(name,bushiyo1,mail)

# tel_address[str(4812)] = name,bushiyo,mail
# name,bushiyo,mail = tel_address[str(4812)]
# print(name,bushiyo,mail)

# できた辞書をcsvで保存する。

# with open(r'test.csv','w',encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = ['内線','名前','所属','mail'])
#     writer.writeheader()
#     writer.writerows(tel_address)

# with open(r"test.csv","w") as csvfile:
#     writerfile = csv.writer(csvfile)
#     writerfile.writerow(tel_address.keys())
#     writerfile.writerows(zip(*tel_address.values()))

# with open(path + 'test.txt', mode='w') as f: #上書き
#     f.write(tel_address)

# print(list(zip(tel_address.keys(), tel_address.values())))

# with open(r"test.csv","w") as csvfile:
#     writerfile = csv.writer(csvfile)
#     writerfile.writerow(tel_address.keys())
#     writerfile.writerows(zip(tel_address.keys(), tel_address.values()))

# with open(r"test.csv","w") as csvfile:
#     writerfile = csv.writer(csvfile)
#     data = tel_address.values(),tel_address.keys()
#     writerfile.writerows(data)

# tel_address = {}
# try:
#     with open(path + 'test.csv', mode='r') as inp:
#         reader = csv.reader(inp)
#         print(reader)
#         tel_address = {rows[0]:(rows[1],rows[2],rows[3]) for rows in reader}
# except:
#     with open(path + 'test.csv', mode='r',encoding="utf-8") as inp:
#         reader = csv.reader(inp)
#         print(reader)
#         tel_address = {rows[0]:(rows[1],rows[2],rows[3]) for rows in reader}
# # key:内線　名前、所属、mailの入れ物
# print(tel_address)

# tel_list = []
# for tel_no in range(2000,8000):
#     # 存在する内線
#     if str(tel_no) in tel_address:
#         name,bushiyo,mail = tel_address[str(tel_no)]
#         tel_list.append([name,bushiyo,mail,tel_no])
# print(tel_list)
# with open('test.csv', 'w', newline='') as file:
#     writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=',')
#     writer.writerows(tel_list)