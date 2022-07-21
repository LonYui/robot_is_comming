'''Warn:七月3號報表拿的是七月2號的資料'''
import datetime
import json
import math
import os

db_path=os.getenv('db_path') if os.getenv('db_path') else 'db' #default = db

設定_f = open(f'{db_path}/設定.json')
設定 = json.load(設定_f)

def main(日期=datetime.date.today().isoformat()):
    ''
    ftp_每日銷售報表(日期)
    for ptv in 設定:
        for 廠商 in ptv['廠商']:
            import openpyxl
            銷售報表_wb = openpyxl.load_workbook(f'{db_path}/{廠商["名稱"]}_銷售報表07.xlsx')
            銷售報表 = 銷售報表_wb.active
            # for index in range(len(廠商['商品清單'])):
            for index,商品code in enumerate(廠商['商品清單']):
                日期_datetime = datetime.datetime.fromisoformat(日期)
                日期減一_datetime = 日期_datetime - datetime.timedelta(1)
                日期減一禮拜幾 = 日期減一_datetime.weekday() #0 1 2 3 4 5 6
                日期減一 = 日期減一_datetime.date().isoformat()
                銷售報表[f'{chr(ord("C")+7*_第幾週(日期減一_datetime)+日期減一禮拜幾)}{11+4*index}']=get_日銷售(商品code,日期=日期減一)
            銷售報表_wb.save(f'{db_path}/{廠商["名稱"]}_銷售報表07.xlsx')
    None


def _第幾週(日期_datetime):
    ''' output: 0 1 2 3 4'''
    本月一號禮拜幾 = datetime.date(日期_datetime.year,日期_datetime.month,1).weekday()
    return math.floor((日期_datetime.day +7- 本月一號禮拜幾)/7)


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
    日期加一_datetime = 日期_datetime + datetime.timedelta(1)
    import pandas

    數據報表 = pandas.read_csv(
        f"{db_path}/下載/{_get_ptv_by貨號(貨號)}{日期加一_datetime.strftime('%Y%m%d')}sal.csv",
        encoding='Big5', dtype={'PRDTCODE': 'str'})

    return 數據報表[['PRDTMLQY', 'PRDTCODE']][數據報表['PRDTCODE'] == 貨號]['PRDTMLQY'].sum()


def _get_ptv_by貨號(貨號):
    for ptv in 設定:
        for 廠商 in ptv['廠商']:
            if 貨號 in 廠商['商品清單']:
                return ptv['ptvcod']

    return None
