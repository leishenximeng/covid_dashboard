# 导入 pandas，用于数据处理
import pandas as pd

# 定义一个函数用于加载 COVID-19 数据
# 参数 file_path: 数据文件路径，默认指向 'data/owid-covid-data.csv'
def load_data(file_path='data/owid-covid-data.csv'):
    # 读取 CSV 文件，并把 'date' 列解析为日期类型
    df = pd.read_csv(file_path, parse_dates=['date'])
    
    # 只保留需要的列
    # date: 日期
    # location: 国家或地区
    # new_cases: 新增确诊
    # total_cases: 累计确诊
    # new_deaths: 新增死亡
    # total_deaths: 累计死亡
    df = df[['date', 'location', 'new_cases', 'total_cases', 'new_deaths', 'total_deaths']]
    
    # 将缺失值（NaN）填充为 0
    # 因为有些国家/日期没有数据，用 0 代替方便计算和绘图
    df.fillna(0, inplace=True)
    
    # 返回处理后的 DataFrame
    return df
