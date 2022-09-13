import pandas
import numpy
from deepfos.element.datatable import DataTableMySQL
from deepfos.element.rolestrategy import RoleStrategy
from deepfos.element.dimension import Dimension, DimMember

try:
    from _debug import para1, para2
except ImportError:
    para1 = para2 = {}


def main(p1, p2):
    user = p1['user']

    rs = RoleStrategy("WeekReport", folder_id='WeekReport', path='/Application/PermissionScheme/WeekReport')
    r = rs.query(user=user, role='001')
    r_r = r.records
    if r_r:
        this_record_id = p2['record_id']

        Business_Table = DataTableMySQL('WeekReport_M')
        t1 = Business_Table.table
        year_period = Business_Table.select(['sys_id', 'year', 'period'], where=(t1.record_id == this_record_id))
        sys_id = year_period['sys_id'].iloc[0]
        year = year_period['year'].iloc[0]
        period_now = year_period['period'].iloc[0]

        dim_expression = r_r[0].dim_expr[0]
        Entity_dimension = Dimension("Entity")
        Entity_info = Entity_dimension.query(dim_expression, as_model=True, role="WeekReport")
        name_list = []
        for m in Entity_info:
            name_list.append(m.name)
        df_origin = Business_Table.select(
            where=(t1.year == year) & (t1.period == period_now) & (t1.result_status == '02'))

        record_id = ''
        '''
            上一条
        '''
        if not df_origin.empty:
            df_origin = df_origin.iloc[::-1]
            df_origin.reset_index(drop=True, inplace=True)
            for index, row in df_origin.iterrows():
                if row['Entity'] in name_list and row['sys_id'] < sys_id:
                    record_id = row['record_id']
                    break
        if record_id:
            return record_id
        else:
            raise Exception("暂无待审批数据！")
    else:
        raise Exception("暂无权限，禁止操作！")


if __name__ == '__main__':
    main(para1, para2)
