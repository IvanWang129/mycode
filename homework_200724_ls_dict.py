
# 以字典和列表方式取excel中数据

class exceldata():
    # 初始化方法
    def __init__(self, data_path, sheetname):
        # 定义一个属性接收文件路径
        self.data_path = data_path
        # 定义一个属性接收工作表名称
        self.sheetname = sheetname
        # 使用xlrd模块打开excel表读取数据
        self.data = xlrd.open_workbook(self.data_path)
        # 使用工作表的名称获取工作表中的内容
        self.table = self.data.sheet_by_name(self.sheetname)
        # 获取第一行的所有内容，作为key
        self.keys = self.table.row_values(0)
        # 获取工作表的有效行数
        self.nrows = self.table.nrows
        # 获取工作表的有效列数
        self.ncols = self.table.ncols
    
    # 定义一个读取excel表的方法
    def read_excel_test(self):
        #定义一个空列表
        datas = []
        for i in range(1,self.nrows):
            # 定义一个空字典
            sheet_data = {}
            for j in range(0,self.ncols):
                # 获取单元格数据
                c_cell = self.table.cell_value(i,j)
                # 循环每一个有效单元格，将字段与值对应存储到字典中
                # 字典的key就是excel表中第一行的字段
                sheet_data[self.keys[j]] = c_cell
            # 将字典追加到列表中
            datas.append(sheet_data)
        # 返回从excel中获取的数据，以列表存字典的形式返回
        return datas
if __name__=="__main__":
    data_path = r'C:\Users\pc\Desktop\py\mycode\sample.xlsx'
    sheetname = 'Sheet1'
    get_data = exceldata(data_path, sheetname)
    datas = get_data.read_excel_test()
    print (datas)