# 导入 Streamlit 库，用于创建 Web 可视化应用
import streamlit as st

# 导入自定义模块
# load_data: 用于加载 COVID-19 数据
# plot_global_trend, plot_top_countries, plot_choropleth: 用于绘制不同图表
from src.data_load import load_data
from src.plot_charts import plot_global_trend, plot_top_countries, plot_choropleth

# 设置网页标题
st.title("🌍 Global COVID-19 Data Visualization Dashboard")

# 加载数据（返回一个 DataFrame）
df = load_data()

# -----------------------------
# 侧边栏选项
# -----------------------------
st.sidebar.header("Options")

# 多选下拉框，让用户选择要对比的国家
# df['location'].unique(): 获取所有国家/地区
# default: 默认选中的国家
country_select = st.sidebar.multiselect(
    "Select countries", 
    df['location'].unique(), 
    default=['United States', 'India']
)

# -----------------------------
# 全局趋势图
# -----------------------------
st.header("📈 Global Trend")
# 绘制全球新增病例折线图
plot_global_trend(df)

# -----------------------------
# 前10国家累计病例图
# -----------------------------
st.header("🏆 Top Countries by Total Cases")
# 绘制前10国家累计病例折线图
plot_top_countries(df)

# -----------------------------
# 全球每日病例地图
# -----------------------------
st.header("🗺️ Global Daily Cases Map")
# 绘制 Choropleth 地图（全球每日病例分布）
plot_choropleth(df)

# -----------------------------
# 国家对比折线图
# -----------------------------
st.header("🔍 Country Comparison")

# 遍历用户选择的国家
for country in country_select:
    # 筛选出该国家的数据
    country_data = df[df['location'] == country]
    # 绘制折线图（x: date，y: new_cases）
    # st.line_chart 会自动生成交互式图表
    st.line_chart(country_data.set_index('date')['new_cases'])
