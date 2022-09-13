import numpy
import pandas
from deepfos.element.datatable import DataTableMySQL
from deepfos.element.dimension import Dimension, DimMember
from deepfos.lib.sysutils import complete_cartesian_product
import datetime
import uuid

try:
    from _debug import para1, para2
except ImportError:
    para1 = para2 = {}


def main(p1, p2):
    if not p2[0]['period']:
        raise Exception("期间必填")
    user = p1['user']
    para_dict = p2[0]
    period = para_dict['period']
    year = para_dict['year']
    system_year = datetime.datetime.today().year
    system_time = datetime.datetime.now()
    if year is None:
        year = str(system_year)

    MySQL_Table_M = DataTableMySQL("WeekReport_M")
    t = MySQL_Table_M.table
    df = MySQL_Table_M.select()

    MySQL_Table_R = DataTableMySQL("WeekReportRecord")

    dimension1 = Dimension("Entity")
    dim1 = dimension1.query('Base(OrganizationalStructure,0);', fields=['name', 'is_active'])
    dim_exist = []
    dim_not_exist_name = []
    dim_exist_name = []
    for m in dim1:
        if m.name in df['Entity'].values:
            dim_exist.append({'name': m.name, 'is_active': str(m.is_active)})
            if str(m.is_active) == 'True':
                dim_exist_name.append(m.name)
        else:
            if str(m.is_active) == 'True':
                dim_not_exist_name.append(m.name)
    old_Entity_dimension = ';'.join(dim_exist_name)
    Entity_dimension = ';'.join(dim_not_exist_name)

    dimension2 = Dimension("period")
    dim2 = dimension2.query('Base(TotalWeek,0);', fields=['name'])
    dim_period_name_list = []
    for m in dim2:
        dim_period_name_list.append(m.name)
    dim_period_name_list = dim_period_name_list[dim_period_name_list.index(period):]
    dim_period_name = ';'.join(dim_period_name_list)

    df_insert = pandas.DataFrame(columns=df.columns.values)

    df_old_year = df[['year']].copy()
    df_old_year.drop_duplicates(inplace=True)
    if year not in df_old_year['year'].values:
        if old_Entity_dimension:
            fix = {'Entity': old_Entity_dimension, 'year': year, 'period': dim_period_name, 'result_status': '01',
                   'partition_id': '0', 'process_operation_id': '0', 'operate_user': user, 'ygzt': 'True'}
            df_insert1 = complete_cartesian_product(fix=fix, df=df_insert)
            for index, row in df_insert1.iterrows():
                row['record_id'] = str(uuid.uuid1()).replace('-', '')
            df_insert1[['operate_time']] = system_time
            MySQL_Table_M.insert_df(df_insert1, chunksize=5000, auto_fit=True)
            MySQL_Table_R.insert_df(
                df_insert1[['result_status', 'operate_user', 'operate_time', 'record_id', 'partition_id',
                            'process_operation_id']], chunksize=5000, auto_fit=True)
    else:
        df_update = pandas.DataFrame(columns=df.columns.values)
        for d in dim_exist:
            if (df[(df['Entity'] == d['name']) & (df['year'] == year) & (df['period'] == period)]['ygzt']).iloc[0] != d['is_active']:
                df_temp = df[(df['Entity'] == d['name']) & (df['year'] == year)].copy()
                this_index = df_temp[(df_temp['Entity'] == d['name']) & (df_temp['year'] == year) & (df_temp['period'] == period)].index[0]
                df_temp = df_temp[df_temp.index >= this_index]
                df_temp[['ygzt']] = d['is_active']
                df_update = df_update.append(df_temp)
        df_update[['where']] = ''
        if len(df_update) > 0:
            for index, row in df_update.iterrows():
                df_update.at[index, 'where'] = f"record_id='{row['record_id']}'"
            MySQL_Table_M.update_from_dataframe(df_update)

    if Entity_dimension:
        fix = {'Entity': Entity_dimension, 'year': year, 'period': dim_period_name, 'result_status': '01',
               'partition_id': '0', 'process_operation_id': '0', 'operate_user': user, 'ygzt': 'True'}
        df_insert = complete_cartesian_product(fix=fix, df=df_insert)
        for index, row in df_insert.iterrows():
            row['record_id'] = str(uuid.uuid1()).replace('-', '')
        df_insert[['operate_time']] = system_time
        MySQL_Table_M.insert_df(df_insert, chunksize=5000, auto_fit=True)
        MySQL_Table_R.insert_df(df_insert[['result_status', 'operate_user', 'operate_time', 'record_id', 'partition_id',
                                           'process_operation_id']], chunksize=5000, auto_fit=True)


if __name__ == '__main__':
    main(para1, para2)
