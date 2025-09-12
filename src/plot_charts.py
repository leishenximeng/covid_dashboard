# 导入绘图库
import matplotlib.pyplot as plt  # 用于绘制传统静态图
import seaborn as sns            # 在 matplotlib 基础上增强绘图美观
import plotly.express as px      # 用于交互式绘图

# -----------------------------
# 函数：绘制全球每日新增病例折线图
# -----------------------------
def plot_global_trend(df):
    # 按日期聚合所有国家的新增病例
    daily = df.groupby('date')['new_cases'].sum().reset_index()
    
    # 创建一个图形窗口，大小为 12x6 英寸
    plt.figure(figsize=(12,6))
    
    # 使用 seaborn 绘制折线图
    sns.lineplot(x='date', y='new_cases', data=daily)
    
    # 设置标题和坐标轴标签
    plt.title('Global Daily New Cases')
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    
    # 自动调整子图布局，防止标签重叠
    plt.tight_layout()
    
    # 显示图形
    plt.show()


# -----------------------------
# 函数：绘制累计病例前 top_n 个国家的柱状图
# -----------------------------
def plot_top_countries(df, top_n=10):
    # 获取最新日期的数据
    latest = df[df['date'] == df['date'].max()]
    
    # 按累计病例排序，取前 top_n 个国家
    top = latest.sort_values('total_cases', ascending=False).head(top_n)
    
    # 使用 Plotly 绘制交互式柱状图
    fig = px.bar(
        top, 
        x='location', 
        y='total_cases', 
        title=f'Top {top_n} Countries by Total Cases'
    )
    
    # 显示图形
    fig.show()


# -----------------------------
# 函数：绘制全球每日新增病例地图（Choropleth）
# -----------------------------
def plot_choropleth(df):
    # 获取最新日期的数据
    latest = df[df['date'] == df['date'].max()]
    
    # 使用 Plotly 绘制交互式 Choropleth 地图
    fig = px.choropleth(
        latest,
        locations='location',          # 国家名称列
        locationmode='country names',  # 根据国家名称匹配地图
        color='new_cases',             # 用每日新增病例数量着色
        hover_name='location',         # 鼠标悬停显示国家名称
        color_continuous_scale='Reds', # 颜色渐变
        title='Global Daily New Cases' # 标题
    )
    
    # 显示地图
    fig.show()
