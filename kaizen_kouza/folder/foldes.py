"""
フォルダのリストを作る

複数フォルダーに対して、htmlデータを取得し、
登録 id telをリスト化します。
内線番号から氏名、所属を取得

"""
import os
import time




# ------------ 環境確認 ------------------------
path = os.getcwd() + '/'  # 現在のパスを取得
print(path)
html_path = path + 'reserveBoard.html' 

print('step1')
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
#print('folderDir1:', folderDir1)

folderDir2 = folderDir1[:-1]
#print('folderDir2:', folderDir2)
index = folderDir2.rfind('\\') + 1
# print('index:',index)
folderName2 = folderDir2[index:]
#print('folderName2:', folderName2)

# 同一パスにあるフォルダー(dir)のみリスト化する
files = os.listdir(path)
folders = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(folders)    # ['dir1', 'dir2']

time.sleep(0)
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


def html_read(html_path):# htmlデータを読み込む
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


import csv
# 2要素を辞書型でcsvから読み込む
address = {}
with open(folderDir1 + 'hinagata\\' + 'address.csv', mode='r') as inp:
    reader = csv.reader(inp)
    address = {rows[4]:(rows[0],rows[2]) for rows in reader}
# print(address)

#tel_number = '3000'
#ad1,ad2 = address[tel_number]
#print()
#print(ad1,ad2)


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
        try:
            ad1,ad2 = address[tel_number]
            print(tel_number,ad1,ad2)
        except:
            print(tel_number,'key errpr')
    
    # フォルダー毎にcsvファイルで出力
    with open(folder + '.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        for tel_number in touroku_tel:
            ad1,ad2 = address[tel_number]
            writer.writerow([tel_number,ad1,ad2])


