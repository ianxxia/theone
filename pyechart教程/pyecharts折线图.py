#echarts是个由百度开源的数据可视化框架
import pyecharts
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

#得到折线图对象
line = Line()

#添加X轴对象
line.add_xaxis(["china","Hk","Uk"])
#添加Y轴对象
line.add_yaxis("GDP",[30,20,1000])

#设置全局配置项set_global_opts
#position 位置参数
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",
                         pos_left="center",
                         pos_bottom="1%"),#距离底部只有1%距离
    legend_opts = LegendOpts(is_show=True),#图例
    toolbox_opts=ToolboxOpts(is_show=True),#工具箱
    visualmap_opts=VisualMapOpts(is_show=True)#视觉映射

)





#生成图表
# line.render("D:/photo.html")
line.render()