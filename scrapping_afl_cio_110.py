
import requests
from bs4 import BeautifulSoup
import pandas as pd

# target url of webscraping
base_url = "https://aflcio.org/paywatch/company-pay-ratios?industry=All&state=All&sp500=0&combine=&page="

result_file_name = 'result_pay_ratios_110.csv'

full_page_num = 110

# reset the column names for result data
df_columns = ['Ticker', 'Company', 'Median Worker Pay', 'Pay Ratio']

data = []
for page_num in range(full_page_num):
    print(page_num)
    URL = base_url+str(page_num)
    page = requests.get(URL)
    # get page contnet with BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find("body")
    tbl_content = body.find("table",class_ = "cols-4")
    tbody = tbl_content.find("tbody")
    tr_list = tbody.find_all("tr")
    td_list = tr_list[0].find_all("td")
    for num in range(len(tr_list)):
        row_data = []
        for td_num in range(len(td_list)):
            temp = tr_list[num].find_all("td")[td_num].text
            #temp_value = tr_list[1].find_all("td")[td_num].text
            row_data.append(temp)
            #print(temp)
        data.append(row_data)

# Make the data as Dataframe using Python Pandas 
df = pd.DataFrame(data,columns = df_columns)

# saving the dataframe to CSV data
df.to_csv(result_file_name,index = False) 

# print some rows of output dataframe
print(df.head())