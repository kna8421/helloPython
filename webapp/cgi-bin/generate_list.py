import athletemodel
import yate
import glob
from athletemodel import get_namesId_from_store

#glob 模組 可以印出資 料夾底下所指定的檔案名稱
data_files = glob.glob("data/*.txt")

#athletes = athletemodel.put_to_store(data_files)
athletes = get_namesId_from_store()
#-----start-----
print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))

#開始產生表單 > generate_list.py 把資料送往另一個程式
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Selectan athlete fron the list to work with:"))

for athlete in athletes:
    #print(yate.radio_button("athlete", athletes[athlete].name))
    print(yate.radio_button("athlete", athlete[0],athlete[1]))
#表單最後產生Select按鈕
print(yate.end_form("Select"))


#html底部加入可以回首頁的連結
print(yate.include_footer({"Home": "/index.html"}))

'''若是在UNIX系統下運行 要在terminal輸入:
chmmod + x generate_list.py
設定執行位元 只需做一次
並在程式開頭處加上:
#! /user/local/bn/python3'''

'''測試:
windows: 在webapp資料夾下開啟cmd
執行simple_httpd.py 建立web server
'''