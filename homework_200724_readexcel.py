import xlrd
def read_excel():
    workbook = xlrd.open_workbook(r'C:\Users\pc\Desktop\py\mycode\sample.xlsx')
    sheet1 = workbook.sheet_by_index(0)
    for i in range (sheet1.nrows):
        rows = sheet1.row_values(i)
        print (rows)
if __name__=='__main__':
    read_excel()