import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(by=['event_day', 'emp_id'], as_index=False)['total_time'].sum().rename(columns={'event_day':'day'})