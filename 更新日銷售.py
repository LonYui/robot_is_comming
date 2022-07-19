''''''
import datetime
import os

db_path=os.getenv('db_path')
def ftp_每日銷售報表():
    ''
    import os
    db_path = os.getenv('db_path')
    設定_f = open(f'{db_path}/設定.json')

    import json
    設定 = json.load(設定_f)
    from ftplib import FTP
    ftp = FTP('pngscftpsec.tradevan.com.tw')
    for ptb in 設定:
        file_name = f"{ptb['ptvcod']}{datetime.date.today().strftime('%Y%m%d')}sal.csv"
        ftp.login(ptb['ptvcod'], ptb['ftp密碼'])
        ftp.retrbinary(f"RETR {file_name}",open(file_name, 'wb').write)
        os.system(f'mv {file_name} {db_path}/下載/{file_name}')

def get_日銷售(貨號):
    ''''''