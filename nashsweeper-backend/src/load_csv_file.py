import pandas as pd

page_num = 1

while page_num < 212:
    url = 'https://www.sailboatlistings.com/cgi-bin/saildata/db.cgi?db=default&uid=default&view_records=1&ID=*&sb=date&so=descend&nh=' + \
        str(page_num)
    df = pd.read_html(url)[1]

    file_save_path = './data_set/boat_data_'+str(page_num)+'.csv'
    df.to_csv(file_save_path)
    page_num += 1
