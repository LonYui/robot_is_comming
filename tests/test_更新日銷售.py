def test_更新日銷售():
    '''跑 7/3 更新，確定更加好有更新'''

    # 建立測試資料
    import os
    os.system('cp test_更新日銷售_測試資料/更加好_銷售報表07.02.xlsx  db_test/更加好_銷售報表07.xlsx')
    os.system('cp test_更新日銷售_測試資料/設定.json  db_test')

    # 執行主程式()
    """驗證填寫前後"""
    from openpyxl import load_workbook

    更加好報表_機器人_wb = load_workbook('tests/db_test/更加好_銷售報表07.xlsx')
    更加好報表_機器人 = 更加好報表_機器人_wb.active

    更加好報表_手打_wb = load_workbook('tests/7月/更加好_銷售報表07.03.xlsx')
    更加好報表_手打 = 更加好報表_手打_wb.active

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



    # 刪除測試資料
    os.system('rm db_test/更加好_銷售報表07.xlsx ')
    os.system('rm db_test/設定.json ')

def test_ftp_每日銷售報表():
   assert True
