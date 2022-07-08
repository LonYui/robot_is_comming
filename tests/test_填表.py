def test_填表_happy():
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
