from deepfos.element.datatable import DataTableMySQL

try:
    from _debug import para1, para2
except ImportError:
    para1 = para2 = {}


def main(p1, p2):
    record_id = p2['record_id']
    Entity = p2['Entity']
    year = p2['year']
    period = p2['period']

    # record_id = '8996622822cb11edbdc5aa8613acf852'
    # Entity = 'FDC002'
    # year = '2022'
    # period = '8w05'

    df_dict = []
    report_id = ''

    MySQL_Table = DataTableMySQL("WeekReport_M")
    t = MySQL_Table.table

    MySQL_Plan_Table = DataTableMySQL("Plan")
    t_p = MySQL_Plan_Table.table

    this_report_id = MySQL_Table.select(['report_id'], where=(t.Entity == Entity) & (t.year == year) & (t.period == period))
    if this_report_id['report_id'].iloc[0] is None:
        df = MySQL_Table.select(['report_id'], where=(t.Entity == Entity))
        df = df.astype('str')
        df = df[df['report_id'] != 'None']
        if len(df) != 0:
            df.sort_values('report_id', inplace=True)
            df = df.tail(1)
            print("hello world")
            flag = int(df['report_id'].iloc[0][-3:]) + 1
            report_id = Entity + '_GZZB_' + format(flag, '03d')
        else:
            report_id = Entity + '_GZZB_001'

    df_old_report = MySQL_Table.select(['record_id'], where=(t.Entity == Entity) & (t.result_status == '03'))
    if df_old_report.empty == False:
        df_old_report = df_old_report.tail(1)
        old_record_id = df_old_report['record_id'].iloc[0]
        df_plan = MySQL_Plan_Table.select(where=(t_p.record_id == old_record_id))
        if len(df_plan) != 0:
            df_plan.rename(columns={'plan_id': 'summary_id'}, inplace=True)
            df_plan.insert(8, 'explain', None)
            df_plan[['record_id']] = record_id
            df_summary = df_plan.copy()
            df_dict = df_summary.to_dict(orient='records')

    res = {'report_id': report_id, 'plan': df_dict}
    return res


if __name__ == '__main__':
    main(para1, para2)
