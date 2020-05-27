#calling Connection Class set as module
import Connection as myConnection

#Initialize Class Connection
conn = myConnection.Connection()

#access Class method
greetings = conn.greetings()
print(greetings)

#Connect to PDT
pdt_curr = conn.pdt_connection()
pdt_curr.execute('SELECT * FROM dbo.MD_ref_agama')
for row in pdt_curr:
    print (row)
