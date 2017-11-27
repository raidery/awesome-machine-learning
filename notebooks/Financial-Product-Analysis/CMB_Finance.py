# 招商银行个人理财产品 http://www.cmbchina.com/cfweb/personal/default.aspx

# 导入第三方包
import requests
import re
import time
import pandas as pd

# 设置请求头
headers = {'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
          }

# 拼接URL，用于翻页爬虫
url_phase1 = 'http://www.cmbchina.com/cfweb/svrajax/product.ashx?op=search&type=m&pageindex='
url_phase2 = '&salestatus=&baoben=&currency=&term=&keyword=&series=01&risk=&city=&date=&pagesize=40&orderby=ord1&t=0.8683289736280901'

urls = []
for i in range(1,29):
    urls.append(url_phase1+str(i)+url_phase2)

# 构造空列表，用于后面的数据存储
Finacing = []

# 通过for循环完成URL的遍历
for url in urls:
    # 获取源代码
    res = requests.get(url, headers = headers).text
    # 正则表达式完成信息的获取
    ProdCode = re.findall('PrdCode:"(.*?)",',text)
    ProdName = re.findall('PrdName:"(.*?)",',text)
    TypeCode = re.findall('TypeCode:"(.*?)",',text)
    AreaCode = re.findall('AreaCode:"(.*?)",',text)
    BeginDate = re.findall('BeginDate:"(.*?)",',text)
    EndDate = re.findall('EndDate:"(.*?)",',text)
    ExpireDate = re.findall('ExpireDate:"(.*?)",',text)
    Status = re.findall('Status:"(.*?)",',text)
    NetValue = re.findall('NetValue:"(.*?)",',text)
    IsNewFlag = re.findall('IsNewFlag:"(.*?)",',text)
    NetValue = re.findall('NetValue:"(.*?)",',text)
    Term = re.findall('Term:"(.*?)",',text)
    Style = re.findall('Style:"(.*?)",',text)
    InitMoney = re.findall('InitMoney:"(.*?)",',text)
    IncresingMoney = re.findall('IncresingMoney:"(.*?)",',text)
    Risk = re.findall('Risk:"(.*?)",',text)
    FinDate = re.findall('FinDate:"(.*?)",',text)
    SaleChannel = re.findall('SaleChannel:"(.*?)",',text)
    SaleChannelName = re.findall('SaleChannelName:"(.*?)",',text)
    IsCanBuy = re.findall('IsCanBuy:"(.*?)"}',text)
    
    # 数据存储到字典中
    Finacing.append({'ProdCode':ProdCode,'ProdName':ProdName,'TypeCode':TypeCode,'AreaCode':AreaCode,
            'BeginDate':BeginDate,'EndDate':EndDate,'ExpireDate':ExpireDate,'Status':Status,
            'NetValue':NetValue,'IsNewFlag':IsNewFlag,'NetValue':NetValue,'Term':Term,
            'Style':Style,'InitMoney':InitMoney,'IncresingMoney':IncresingMoney,'Risk':Risk,
            'FinDate':FinDate,'SaleChannel':SaleChannel,'SaleChannelName':SaleChannelName,'IsCanBuy':IsCanBuy})
    
    # 睡眠3秒
    time.sleep(3)

# 将数据转换为数据框
CMB_Finance = pd.concat([pd.DataFrame(data) for data in Finacing])    
# 数据导出
CMB_Finance.to_excel('CMB_Finance.xlsx', index = False)


# 读取数据
cmb = pd.read_excel('CMB_Finance.xlsx')
# 查看数据集的行列数
cmb.shape
# 查看数据前几行
cmb.head()
#  查看数据集的数据类型
cmb.dtypes

# 数据类型转换
# 将FinDate（期限）字段转换为数值型，用于了解其数值分布
cmb.FinDate = cmb.FinDate.str[:-1].astype('int')
# 将NetValue（收益率）字段转换为数值型
cmb.NetValue = cmb.NetValue.str[:-1].astype('float')/100

# 预期收益率最高的3个产品
NetValue_sort_desc = cmb[['ProdCode', 'NetValue']].sort_values(by = 'NetValue', ascending=False)
NetValue_duplicate_top = NetValue_sort_desc.drop_duplicates(subset = 'NetValue').head(3)

# 预期收益率最低的3个产品
NetValue_sort_asc = cmb[['ProdCode', 'NetValue']].sort_values(by = 'NetValue', ascending=True)
NetValue_duplicate_last = NetValue_sort_asc.drop_duplicates(subset = 'NetValue').head(3)

# 预期收益率最高和最低的3种产品
# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置图形的显示风格
plt.style.use('ggplot')

# 为了让多张子图在一张图中完成，设置子图的位置
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0))

# 绘制条形图
ax1.bar(range(3), NetValue_duplicate_top.NetValue, align = 'center', color = 'steelblue', alpha = 0.7)
# y轴范围
ax1.set_ylim(0.045,0.051)
# x轴刻度标签
ax1.set_xticks(np.arange(3)) 
ax1.set_xticklabels(NetValue_duplicate_top.ProdCode)
# x轴标签
ax1.set_xlabel('产品编号')
# y轴刻度标签
ax1.set_yticks(np.arange(0.045,0.051,0.001))
ax1.set_yticklabels([str(i*100) + '%' for i in np.arange(0.045,0.051,0.001)])
# y轴标签
ax1.set_ylabel('预期收益率')
# 标题
ax1.set_title('预期收益率最高的5类产品')


ax2.bar(range(3), NetValue_duplicate_last.NetValue,  align = 'center',color = 'steelblue', alpha = 0.7)
ax2.set_ylim(0.045,0.048)
ax2.set_xticks(np.arange(3)) 
ax2.set_xticklabels(NetValue_duplicate_last.ProdCode)
# x轴标签
ax2.set_xlabel('产品编号')
# y轴刻度标签
ax2.set_yticks(np.arange(0.045,0.048,0.001))    
ax2.set_yticklabels([str(i*100) + '%' for i in np.arange(0.045,0.048,0.001)])
# y轴标签
ax2.set_ylabel('预期收益率')
ax2.set_title('预期收益率最低的5类产品')

# 调整子图之间的高度间距
plt.subplots_adjust(hspace=0.5)
# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')

# 图形显示
plt.show()


stats = cmb.Risk.value_counts()
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0,4)
plt.ylim(0,4)

explode = [0,0,0.1,]  
colors=['#9999ff','#ff9999','#7777aa'] # 自定义颜色

# 绘制饼图
plt.pie(x = stats.values, # 绘图数据
        explode=explode, # 突出显示大专人群
        labels=stats.index, 
        colors=colors, # 设置饼图的自定义填充色
        autopct='%.1f%%', # 设置百分比的格式，这里保留一位小数
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance = 1.15, 
        startangle = 180, # 设置饼图的初始角度
        radius = 1.5, # 设置饼图的半径
        counterclock = False, # 是否逆时针，这里设置为顺时针方向
        wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},# 设置饼图内外边界的属性值
        textprops = {'fontsize':12, 'color':'k'}, # 设置文本标签的属性值
        center = (1.8,1.8), # 设置饼图的原点
        frame = 1 )# 是否显示饼图的图框，这里设置显示

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('理财产品风险类型分布')

# 显示图形
plt.show()


# 理财产品期限的描述性统计
cmb.FinDate.describe()


# 理财产品期限的直方图
plt.hist(cmb.FinDate, # 绘图数据
        bins = np.arange(cmb.FinDate.min(),cmb.FinDate.max(),30), # 指定直方图的组距
        normed = True, # 设置为频率直方图
        color = 'steelblue', # 指定填充色
        edgecolor = 'k') # 指定直方图的边界色

# 设置坐标轴标签和标题
plt.title('理财产品期限直方图')
plt.xlabel('期限（天数）')
plt.ylabel('频率')

# 生成正态曲线的数据
x1 = np.linspace(cmb.FinDate.min(), cmb.FinDate.max(), 1000)
normal = mlab.normpdf(x1, cmb.FinDate.mean(), cmb.FinDate.std())
# 绘制正态分布曲线
line1, = plt.plot(x1,normal,'r-', linewidth = 2) 

# 生成核密度曲线的数据
kde = mlab.GaussianKDE(cmb.FinDate)
x2 = np.linspace(cmb.FinDate.min(), cmb.FinDate.max(), 1000)
# 绘制
line2, = plt.plot(x2,kde(x2),'g-', linewidth = 2)

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')

# 显示图例
plt.legend([line1, line2],['正态分布曲线','核密度曲线'],loc='best')
# 显示图形
plt.show()


# 如果将其划分到不同的Risk（风险类型）中，期限的分布是否存在差异
FinDate = []
Risks = cmb.Risk.unique()
Risks.sort()
for Risk in Risks:
    FinDate.append(cmb.loc[cmb.Risk==Risk,'FinDate'])

# 绘图
plt.boxplot(x = FinDate, 
            patch_artist=True,
            labels = Risks, # 添加具体的标签名称
            showmeans=True, 
            boxprops = {'color':'black','facecolor':'#9999ff'}, 
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'},
            meanprops = {'marker':'D','markerfacecolor':'indianred'},
            medianprops = {'linestyle':'--','color':'orange'})

# 设置坐标轴标签和标题
plt.title('不同风险类型下的产品期限差异盒形图图')
plt.xlabel('风险类型')
plt.ylabel('期限')

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')

# 显示图形
plt.show()