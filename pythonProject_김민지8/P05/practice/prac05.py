ticket = {'성인': 8000, '청소년': 5000, '어린이': 3000}
for data in ticket:
    print(f"<{data} 입장료 - {ticket[data]}원>")
#dic의 반복변수는 key 이므로 value 뽑고 싶으면 이름[key]