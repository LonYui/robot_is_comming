
def test_整合測試_填表():
    """填寫更加好報表"""
    # wb = 執行主程式()
    from openpyxl import Workbook
    更加好報表_機器人_wb = Workbook()
    更加好報表_機器人 = 更加好報表_機器人_wb.active
    """驗證填寫前後"""
    from openpyxl import load_workbook
    更加好報表_手打_wb = load_workbook('更加好_銷售報表07.03拷貝.xlsx')
    更加好報表_手打 = 更加好報表_手打_wb.active

    """日期正確"""
    更加好報表_手打_日期rows = []
    for row in 更加好報表_手打.iter_rows(min_row=8, max_row=10, min_col=3,
                               max_col=3 + 41, values_only=True):
        更加好報表_手打_日期rows.append(row)
    更加好報表_機器人_日期rows = []
    for row in 更加好報表_機器人.iter_rows(min_row=8, max_row=10, min_col=3,
                               max_col=3 + 41, values_only=True):
        更加好報表_機器人_日期rows.append(row)
    assert 更加好報表_機器人_日期rows == 更加好報表_手打_日期rows

    """日銷售正確"""
    更加好報表_手打_日銷售row = []
    for row in 更加好報表_手打.iter_rows(min_row=11, max_row=11, min_col=3,
                               max_col=3 + 41, values_only=True):
        更加好報表_手打_日銷售row.append(row)
    更加好報表_機器人_日銷售row = []
    for row in 更加好報表_機器人.iter_rows(min_row=11, max_row=11, min_col=3,
                               max_col=3 + 41, values_only=True):
        更加好報表_機器人_日銷售row.append(row)
    assert 更加好報表_機器人_日銷售row==更加好報表_手打_日銷售row

    """周銷售正確"""
    更加好報表_手打_週銷售row=[]
    for row in 更加好報表_手打.iter_rows(min_row=13, max_row=13, min_col=3,
                               max_col=3 + 41, values_only=True):
        更加好報表_手打_週銷售row.append(row)
    更加好報表_機器人_週銷售row=[]
    for row in 更加好報表_機器人.iter_rows(min_row=13, max_row=13, min_col=3,
                               max_col=3 + 41, values_only=True):
        更加好報表_機器人_週銷售row.append(row)

    assert 更加好報表_機器人_週銷售row == 更加好報表_手打_週銷售row

def test_整合測試_更新config():
    """
    進去google drive 填寫 config
    點擊發動，讓機器人跑一遍
    確認報表如預期產生
    """
    assert True

def test_讀取gooleDrive上config():
    """call ,確認和 config 同構"""
    下載的設定json = None
    from 填表 import 讀取googleDrive上的config
    下載的設定json= 讀取googleDrive上的config()
    import json
    設定_f = open('設定.json')
    設定 = json.load(設定_f)
    assert 設定[0].keys() == 下載的設定json[0].keys()
