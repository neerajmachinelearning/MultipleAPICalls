import requests, json
import xlrd
# import os.path as pth
from datetime import datetime

def make_api_request(url, token):
    result = requests.get(url, verify=False, headers={'Authorization': 'Bearer {}'.format(token), 'accept': 'application/json', 'cache-control': 'no-cache', 'host': 'stage-apigateway.delta.com'})
    print(result.headers, result.text)
    return result


def call_api(sheet):
    filename = r"C:\Neeraj Sharma\API-COE\Testing\output.log"

    with open(filename, 'a+') as f:
        now = datetime.now()
        print(f"\n=====================Log Generated at : {now}===================\n", file=f)
        for i in range(sheet.nrows):
            url = sheet.cell_value(i, 0)
            res = make_api_request(url, token)
            # print(res.json())
            # result = json.dumps(res)
            print(f"{url}: {res}: {res.text}", file=f)
            print(f"{url}: {res}: {res.text}")


if __name__=="__main__":
    token = input("Please enter the token: ")
    # outputFileName = "output_1.text"
    # outputFileName = outputFileName.replace("#", strftime("%Y-%m-%d_%H:%M:%S", gmtime()))
    loc = r"C:\Neeraj Sharma\API-COE\Testing\urlsheet.xlsx"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    call_api(sheet)








