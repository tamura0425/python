import openpyxl
import logging
import csv
import pprint

from openpyxl import load_workbook
from openpyxl import Workbook
import glob


def create_books():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'test_sheet_1'
    # シートを追加
    wb.create_sheet()
    wb.create_sheet(index=1,title="555555")
    
    # 保存する
    wb.save('C:\\Users\\tamur\\Desktop\\lottery_notes\\test2.xlsx')
    glob.glob("*.xlsx")

def create_book():
    wb = Workbook()
    # ワークブックの読み込み\
    wb.save('C:\\Users\\tamur\\Desktop\\lottery_notes\\myworkbook.xlsx')
    # ワークシートの選択
    ws = wb['Sheet']  # ワークシートを指定
    ws = wb.active  # アクティブなワークシートを選択
    print(f'sheet name: {ws.title}')  # sheet name: Sheet
    for sheet in wb:
        print(f'sheet name: {sheet.title}')


# ブックデータ取得メソッド
def lottery_notes():
    # ブックを取得
    get_book = openpyxl.load_workbook('C:\\Users\\tamur\\Desktop\\lottery_notes\\lottery_notes.xlsx')
    # シートを取得 
    get_seat = get_book["Sheet1"]
    # セルを１つずつ取得
    for cell1 in tuple(get_seat.rows):
        for cell2 in cell1:
            print(cell2.value)


# error logging作成
def create_log():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.error("エラーが発生しました")


create_log()

lottery_notes()

create_books()
create_book()