import sqlite3
conn=sqlite3.connect("review.db")
cursor=conn.cursor()
name=request.form['name']
review=request.form['review']
cursor.execute("insert into reviews(name,review)values (?,?)"(name,review))
conn.commit()
conn.close()