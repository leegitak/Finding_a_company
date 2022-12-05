from csv import DictReader
from tkinter import *
import argparse
import re

window = Tk()
window.title('병특업체 목록')

scrollbar = Scrollbar(window)
scrollbar.pack(side='right', fill='both')

list_box = Listbox(yscrollcommand=scrollbar.set, height=1200, width=50)

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
업종: 철강 기계 전기 전자 화학 섬유 신발 
      시멘요업 생활용품 정보처라 게임S/W 
      영상게임 의료의약 식음료 농산물가공
      수산물가공 임산물가공 동물약품
      애니메이션 석탄채굴 일반광물채굴
      선광제련 에너지 국내건설 국외건설
      내항화물 외항화물 내항선박관리
      외항선박관리 근해 원양
      
주소: 강남구 강동구 강복구 강서구 관악구 
      광진구 구로구 금천구 노원구 도봉구 
      동대문구 동작구 마포구 서대문구 서초구
      성동구 성복구 송파구 양천구 영등포구 
      용산구 은평구 종로구 중구 중랑구''')
parser.add_argument('--sectors', help='--sectors 업종')
parser.add_argument('--address', help='--address 주소')
parser.add_argument('--company', help='--address 업체명')
args = parser.parse_args()


def list_box_insert():
    list_box.insert(END, f'업체명: {lines["업체명"]}')
    list_box.insert(END, f'선정년도: {lines["선정년도"]}')
    list_box.insert(END, f'주소: {lines["주소"]}')
    list_box.insert(END, f'업종: {lines["업종"]}')
    list_box.insert(END, f'기업규모: {lines["기업규모"]}')
    list_box.insert(END, '-------------------------------------')


def finding_company(file_lines):
    try:
        if args.company is not None:
            re_company = re.search(args.company, file_lines['업체명'])
            if re_company.group() == args.company:
                list_box_insert()

        elif args.sectors is not None and args.address is not None:
            if file_lines['업종'] == args.sectors and args.address == re_lines.group():
                list_box_insert()

        elif args.address is not None:
            if args.address == re_lines.group():
                list_box_insert()
        elif args.sectors is not None:
            if file_lines['업종'] == args.sectors:
                list_box_insert()

    except AttributeError:
        pass


with open('병역지정업체검색_221205.csv') as file:
    dict_file = DictReader(file)
    for lines in dict_file:
        re_lines = re.search('\S*구', lines['주소'])
        finding_company(lines)

if list_box.size() >= 1:
    list_box.pack()
else:
    list_box.insert(END, '회사정보가 없습니다.')
    list_box.pack()

window.mainloop()
