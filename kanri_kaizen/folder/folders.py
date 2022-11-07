"""
folders.py
フォルダのリストを作る
by.kawabata

複数フォルダーに対して、htmlデータを取得し、
登録 id telをリスト化します。
内線番号から氏名、所属を取得
tel_addressにはmailがないので、mail_addreeからmailを持ってきてマージする。

講座申込リストを講習日毎にcsvで作る。

2folder化 
20221107	AMPM対応
"""
import os
import time
import csv

kouza_folder_name = 'kaizen_kouza'
kanri_folder_name = 'kanri_kaizen'

# ------------ 環境確認 ------------------------
path = os.getcwd() + '/'  # 現在のパスを取得
print(path)
html_path = path + 'reserveBoard.html' 

print('ファィル読み込み中')
time.sleep(0)

# 自分のいるフォルダ名を取得
# フォルダ名 os.path.dirname()
dir = os.path.dirname(path)
#print('dir:', dir)
# index =dir.rfind("kaizen_kouza") +13
index =dir.rfind('/') +1
if index < 1 :
    index = dir.rfind('\\') + 1  # バックスラッシュの検索はややこしいね。
#print('index:',index)
folderName1 = dir[index:]
#print('folderName1:', folderName1)
folderDir1 = dir[:index]
print('folderDir1:', folderDir1)

folderDir2 = folderDir1[:-1]
#print('folderDir2:', folderDir2)
index = folderDir2.rfind('\\') + 1
# print('index:',index)
folderName2 = folderDir2[index:]
#print('folderName2:', folderName2)

# ------------ tel_address 人名、所属データ読み込み ------------------------
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

# ------------ mail_address 人名、所属、mailデータ読み込み ------------------------
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


print('作業開始')
# --------tel_address に mail_addressの mail をマージ ------------------------
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
                    # 最初に部署が一致した物を採用する。
                    # 仮に同姓同名が同じ部署にいればアウト
        tel_address[str(tel_no)] = name,bushiyo,mail
# print(tel_address['4812'])



# 同一パスにあるフォルダー(dir)のみリスト化する
files = os.listdir(path)
folders = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(folders)    # ['dir1', 'dir2']


#------------ ユニークな要素のみにし、登録データをリスト化 ------------------------
# 対象文字列を探す。
def data_seiri(htmlData):
    touroku_tel = []
    index = htmlData.find('_+') # 登録を探す
    while index != -1:
        touroku_tel.append(htmlData[index+2:index+6])
        #print(htmlData[index+2:index+6])
        index = index +10
        index = htmlData.find('_+',index)
    # print(len(touroku),touroku)
    # ユニークな要素だけにする
    touroku_tel = list(dict.fromkeys(touroku_tel))
    # print(len(touroku_tel),touroku_tel)

    touroku_id = []
    index = htmlData.find(':') # 登録を探す
    while index != -1:
        touroku_id.append(htmlData[index+1:index+7])
        # print(htmlData[index+1:index+7])
        index = index +4
        index = htmlData.find(':',index)
    # print(len(touroku),touroku)
    # ユニークな要素だけにする
    touroku_id = list(dict.fromkeys(touroku_id))
    # print(len(touroku_id),touroku_id)
    return touroku_tel,touroku_id


#------------ # htmlデータを読み込む ------------------------
def html_read(html_path):
    try:
        with open(html_path,encoding="shift-jis") as f:
            htmlData = f.read()
    except:
        try:
            with open(html_path,encoding="cp932") as f:
                htmlData = f.read()
        except:
            with open(html_path,encoding="utf-8") as f:
                htmlData = f.read()
    return htmlData


#------------ ここから実際の作業 ------------------------
# すべてのフォルダのディレクトリから掲示データを取得
for folder in folders:
    print(folder)
    html_path = path + folder + '/reserveBoard.html'

    htmlData = html_read(html_path)
    touroku_tel,touroku_id = data_seiri(htmlData)
    #print(len(touroku_tel),touroku_tel)
    #print(len(touroku_id),touroku_id)
    # 内線番号から名前、所属を取得
    for tel_number in touroku_tel:
        if str(tel_number) in tel_address:
            name,bushiyo,mail = tel_address[tel_number]
            print(tel_number,name,bushiyo,mail)

    # フォルダー毎にcsvファイルで出力
    with open(folder + '.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        for tel_number in touroku_tel:
            name,bushiyo,mail = tel_address[tel_number]
            writer.writerow([tel_number,name,bushiyo,mail])

print('作業終了')
