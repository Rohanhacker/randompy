import sqlite3
c = sqlite3.connect('mydb.db')
cursor = c.cursor()
while True:
    name = raw_input("enter name \n")
    username = raw_input("enter username\n")
    id = input("enter id\n")
    sql = ''' insert into student (name,username,id) values(:sname,:susername,:sid) '''
    cursor.execute(sql,{'sname':name,'susername':username,'sid':id})
    c.commit()
    cd = raw_input("got more students nigga ?(n or Y) \n")
    if cd == 'n':
        break
cursor.close()
