import openpyxl

# ブックを取得
get_book = openpyxl.load_workbook("C:\Users\tamur\Desktop\lottery_notes.xlsx")
# シートを取得 
get_seat = ブック変数['シート名']
# セルを取得
get_seat.['セル番地'].value
get_seat.cell(row=行No.,column=列No.).value