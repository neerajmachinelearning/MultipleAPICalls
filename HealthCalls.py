import requests, json
import xlrd

# yQIv7IC1Aqx0PB31IBybUZluf48Y
def make_api_request(url, token):
    result = requests.get(url, headers={'Authorization': 'Bearer {}'.format(token)})
    print(result.headers, result.text)
    return result


def call_api(sheet):
    with open(r'C:\Neeraj Sharma\API-COE\Testing\output.txt', 'w') as f:
        for i in range(sheet.nrows):
            url = sheet.cell_value(i, 0)
            res = make_api_request(url, token)
            # print(res.json())
            # result = json.dumps(res)
            print(f"{url}: {res}: {res.text}", file=f)
            print(f"{url}: {res}: {res.text}")

if __name__=="__main__":
    token = input("Please enter the token: ")
    loc = r"C:\Neeraj Sharma\API-COE\Testing\urlsheet.xlsx"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    call_api(sheet)








