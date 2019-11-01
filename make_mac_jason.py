# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:22:23 2019

@author: 蘇
"""

"""
生成的数据如下
task_list = [
    {
        "exhib_id": "2833",
        "exhib_name": "东风雷诺_武汉",
        "mbox_list": [],
        "exhib_type": 1,
        "exhib_date": "2019-03-01&2019-03-04",
        "actual_time": "09:00:00&17:30:00",
        "exclude_time": ""
    },
        {
        "exhib_id": "2850,2843",
        "exhib_name": "东风日产/东风雷诺_中山",
        "mbox_list": ["20180111","20180774","20180756","20180748","20180928","20180931","20180936","20180929"],
        "exhib_type": 3,
        "exhib_date": "2019-03-08&2019-03-10",
        "actual_time": "09:00:00&17:00:00",
        "exclude_time": ""
    },
]

import json

with open("tmp.txt", "w") as fp:
    fp.write(json.dumps(tmp,indent=4))

"""
import pymysql
import pandas as pd
import time
import json

dfdata = pd.read_excel('监测设备信息汇总表-10.10.xlsx')
task_list = []
sql_data = []
exhib_id_index = dfdata.columns.get_loc("站点ID")
exhib_city_index = dfdata.columns.get_loc("监测站点\n（城市名）")
exhib_brand_index = dfdata.columns.get_loc("有客流监测的品牌")
mbox_list_index = dfdata.columns.get_loc("Mbox设备ID")
exhib_date_index = dfdata.columns.get_loc("监测日期")
actual_time_index = dfdata.columns.get_loc("监测时间")

for i in range(len(dfdata)):
    info_dict = {
        "exhib_id": "",
        "exhib_name": "",
        "mbox_list": [],
        "exhib_type": '',
        "exhib_date": "",
        "actual_time": "",
        "exclude_time": ""
        }
    # 车展
    if pd.isna(dfdata.iloc[i,exhib_id_index]) is  False and pd.isna(dfdata.iloc[i,mbox_list_index]):
        info_dict['exhib_type'] = 1
    #mbox
    elif pd.isna(dfdata.iloc[i,exhib_id_index]) and pd.isna(dfdata.iloc[i,mbox_list_index]) is False:
        info_dict['exhib_type'] = 2
    #车展+mobx
    else:
        info_dict['exhib_type'] = 3
        
    if pd.isna(dfdata.iloc[i,exhib_id_index]) is  False:
        info_dict['exhib_id'] = ','.join(dfdata.iat[i,exhib_id_index].split('/'))
        exhib_id_list = dfdata.iat[i,exhib_id_index].split('/')
        # 连接database
        conn = pymysql.Connect(
                host='',
                port = ,
                user='',password= '',
                database='mbox_web',charset='utf8')
         # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 定义要执行的SQL语句
        sql = """
        SELECT station_id,mac_id FROM active_station_info LEFT JOIN  machine_status_view on active_station_info.station_id = machine_status_view.store_id
        WHERE station_id in ({0}) 
        and site_type = 4 
        and machine_status_view.machine_type = 2
        """.format(info_dict['exhib_id'])
        # 执行SQL语句
        cursor.execute(sql)
        results = cursor.fetchall()
        # 关闭光标对象
        cursor.close()
        # 关闭数据库连接
        conn.close()
        
        #site_type = 4 的情况
        
        if type(results) is list:
            for station in results:
                if str(station['station_id']) in exhib_id_list:
                    exhib_id_list.remove(str(station['station_id']))
                info_dict['mbox_list'].append(station['mac_id'])
            info_dict['exhib_id'] = ','.join(exhib_id_list)
            if len(exhib_id_list) == 0:
                info_dict['exhib_type'] = 2

    info_dict['exhib_name'] = dfdata.iat[i,exhib_brand_index]+'_'+dfdata.iat[i,exhib_city_index]
    
    if pd.isna(dfdata.iloc[i,mbox_list_index]) is False:
        info_dict['mbox_list'] = dfdata.iloc[i,mbox_list_index].split('/')
    if pd.isna(dfdata.iloc[i,exhib_date_index]) is False:
        exhib_date_all_list = dfdata.iloc[i,exhib_date_index].split('-')
        exhib_date_list = []
        for date in exhib_date_all_list:
            date_python = time.strptime(date, "%Y/%m/%d")
            date_str = time.strftime("%Y-%m-%d", date_python)
            exhib_date_list.append(date_str)
        exhib_date = '&'.join(exhib_date_list)
        info_dict['exhib_date'] = exhib_date
    if pd.isna(dfdata.iloc[i,actual_time_index]) is False:
        actual_time_all_list = dfdata.iloc[i,actual_time_index].split('-')
        actual_time_list = []
        for actual_time_info in actual_time_all_list:
            time_python = time.strptime(actual_time_info, '%H：%M')
            time_str = time.strftime('%H:%M:%S', time_python)
            actual_time_list.append(time_str)
        actual_time = '&'.join(actual_time_list)
        info_dict['actual_time'] = actual_time

    task_list.append(info_dict)
    
with open("tmp.txt", "w") as fp:
    fp.write(json.dumps(task_list,indent=4,ensure_ascii=False))
        
    
