import pygsheets

client = pygsheets.authorize(service_file='google_credentials.json')

sheet = client.open('TestAPIConnection')
wks = sheet.sheet1

names = [["Keyword", "Search Volume", "CPC", "Competition", "Number of Results", "Trends"]]

data = "Keyword;Search Volume;CPC;Competition;Number of Results;Trends\nseo;110000;14.82;0.5;678000000;0.81,1.00,1.00,1.00,1.00,0.81,0.81,0.81,0.81,0.81,0.81,0.81"
result = data.split("\n")
data = result[1].split(';')
names.append(data)

for idx, item in enumerate(names):
    wks.insert_rows(idx, number=1, values=item, inherit=False)

full_sheet = pygsheets.datarange.DataRange(start='A1', end='F100', worksheet=wks)
full_sheet.update_borders(top=True, right=True, bottom=True, left=True, inner_horizontal=True, inner_vertical=True, style='SOLID', width='1')

headers_cells = pygsheets.datarange.DataRange(start='A1', end='F1', worksheet=wks)

for i, column in enumerate(headers_cells.cells[0]):
    cell_style = column
    cell_style.color = (0.21, 0.35, 0.70, 1)
    cell_style.set_text_format('foregroundColor', (1,1,1,1))
    cell_style.set_text_format('bold', True)

# changes to be made