from deepfos.element.datatable import DataTableMySQL
import datetime
import pandas as pd

try:
    from _debug import para1, para2
except ImportError:
    para1 = para2 = {}


def main(p1, p2):
    user = p1.get("user")
    system_time = datetime.datetime.now()
    MySQL_Table_M = DataTableMySQL("WeekReport_M")
    t = MySQL_Table_M.table
    MySQL_Table_R = DataTableMySQL("WeekReportRecord")
    df = pd.DataFrame(columns=['record_id', 'result_status'])
    for row in p2:
        df_temp = MySQL_Table_M.select(['record_id', 'result_status'], where=(t.record_id == row['record_id']) & (t.result_status == '02'))
        df = df.append(df_temp, ignore_index=True)
    df[['result_status']] = '03'
    for index, row in df.iterrows():
        MySQL_Table_M.update({'result_status':row['result_status']}, where=t.record_id==row['record_id'])
    df_insert = df.copy()
    df_insert['partition_id'], df_insert['operate_user'], df_insert['process_operation_id'], df_insert['line_no'], df_insert['operate_time'] = ['0', user, '985993', '3', str(system_time)]
    MySQL_Table_R.insert_df(df_insert, chunksize=5000, auto_fit=True)


if __name__ == '__main__':
    main(para1, para2)
