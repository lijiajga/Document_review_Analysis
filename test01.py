#31455
import pandas as pd

def remove_specific_rows(file_path, sheet_name, column_name, keywords):
    # 使用 pandas 读取 Excel 文件
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

    # 输出列名以确认
    print(df.columns)

    # 构建正则表达式以匹配含有"-新-"或其他指定的关键字的行
    pattern = '|'.join(keywords)

    # 过滤掉包含指定关键字的行
    df_filtered = df[~df[column_name].str.contains(pattern, na=False)]

    # 将修改后的数据保存回 Excel
    with pd.ExcelWriter('test01.xlsx', engine='openpyxl') as writer:
        df_filtered.to_excel(writer, sheet_name=sheet_name, index=False)

# 文件路径和相关参数
file_path = "审单报错数据_v3.xlsx"
sheet_name = "Sheet2"
column_name = 'OPERATE_DETAIL'  # or use 0 for zero-indexed column reference
keywords = [
    '"-新-"的作业岛修改为',
    "任务令添加异常备注成功",
    "配置规则维护:",
    "Online printing of custom labels:",
    "定制化固资号采集(无标签):",
    "定制标签在线打印:",
    "获取定制编码",
    "删除定制资产编号:",
    "发布定制方案成功:",
    "定制方案提交审批:",
    "接收TSD推送过来的定制化软件信息数据",
    "定制方案撤回DIY成功",
    "删除定制资产编号:",
    "Publish the customized plan successfully",
    "Obtain the custom code",
    "此任务令当前状态不能审单,请确认!",
    "定制标签在线打印",
    "Custom Label Printing Online-Re-labeling according to barcode",
    "Customized plan submission for approval",
    "Barcode 2106194DWEX3R2000001",
    "Barcode 2106194DWEX3R2000002",
    "The Ali mission order needs to be maintained on the front line to ensure that the order number, business",
    "ASM DeptemptynewasmDept modify ",
    "pls check the items basic attribute",
    "The byte task order product encoding must be maintained in the encoding extension parameter",
    "Byte task order requires the frontline to maintain AVAP materials",
    "The scheme number has been copied successfully!",
    "Custom scheme withdrawn DIY success",
    "The slot or configuration command of the custom solution",
    "The scheme number has been copied successfully",
    "class: java.lang.String; method: substring"
]

remove_specific_rows(file_path, sheet_name, column_name, keywords)
