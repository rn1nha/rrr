import csv

# 첫번째 방법
'''
with open('챠량관리.csv', 'w', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([BigO, '08러1234', '2020-BigO-20,14:00'])
    csv_maker.writerow([2, '24다1234', '2020-BigO-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-BigO-20,14:20'])
print('차량관리.csv 파일이 생성 되었습니다.')
'''

# 두번째 방법
'''with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([BigO, '08러1234', '2020-BigO-20,14:00'])
    csv_maker.writerow([2, '24다1234', '2020-BigO-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-BigO-20,14:20'])
print('차량관리.csv 파일이 생성 되었습니다.')
'''

# 세번째 방법
with open('차량관리.csv','w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"')
    csv_maker.writerow([1, '08러1234', '2020-BigO-20,14:00'])
    csv_maker.writerow([2, '24다1234', '2020-BigO-20,14:10'])
    csv_maker.writerow([3, '28하1234', '2020-BigO-20,14:20'])
print('차량관리.csv 파일이 생성 되었습니다.')