''''''
import datetime
import json
import os

db_path=os.getenv('db_path') if os.getenv('db_path') else 'db' #default = db

設定_f = open(f'{db_path}/設定.json')
設定 = json.load(設定_f)

def main(date=datetime.date.today()):
    ''

if __name__ == "__main__":
    main()

def ftp_每日銷售報表(日期=datetime.date.today().isoformat()):
    ''
    日期_datetime = datetime.datetime.fromisoformat(日期)
    from ftplib import FTP
    ftp = FTP('pngscftpsec.tradevan.com.tw')
    for ptv in 設定:
        file_name = f"{ptv['ptvcod']}{日期_datetime.strftime('%Y%m%d')}sal.csv"
        ftp.login(ptv['ptvcod'], ptv['ftp密碼'])
        if 日期 != datetime.date.today().isoformat():
            ftp.cwd('Backup')
        ftp.retrbinary(f"RETR {file_name}",open(file_name, 'wb').write)
        os.system(f'mv {file_name} {db_path}/下載/{file_name}')
    ftp.close()

def get_日銷售(貨號,日期=datetime.date.today().isoformat()):
    ''''''
    日期_datetime = datetime.datetime.fromisoformat(日期)
    # 銷售報表_f = open(    f"{db_path}/下載/{_get_ptv_by貨號(貨號)}{日期_datetime.strftime('%Y%m%d')}sal.csv",'r', encoding='Big5')
    import pandas

    數據報表 = pandas.read_csv(
        f"{db_path}/下載/{_get_ptv_by貨號(貨號)}{日期_datetime.strftime('%Y%m%d')}sal.csv",
        encoding='Big5', dtype={'PRDTCODE': 'str'})

    return 數據報表[['PRDTMLQY', 'PRDTCODE']][數據報表['PRDTCODE'] == 貨號]['PRDTMLQY'].sum()


def _get_ptv_by貨號(貨號):
    for ptv in 設定:
        for 廠商 in ptv['廠商']:
            if 貨號 in 廠商['商品清單']:
                return ptv['ptvcod']

    return None
