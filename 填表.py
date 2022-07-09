# import json
#
# 銷售表_f = open('銷售表.json')
#
# 銷售表 = json.load(銷售表_f)
#
# 寫入 excel
global_config = {}
def find_by_商品id(銷售表,商品代號):
    result = []
    for 銷售 in 銷售表:
        if 銷售['商品代號']==商品代號:
            result.append(銷售)

    return result

def 讀取googleDrive上的config():
    """return dict"""
    import requests

    url = "https://www.googleapis.com/drive/v3/files/1t_OKy_0By8rUMbxiAoT4d4GImc5x5jTo?alt=media&key=AIzaSyDP4xaeRhOZHboKYlg89ZZr1P0JW76zf20"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers,
                                data=payload)

    # print(response.text.encode('utf8'))
    return response.json()

