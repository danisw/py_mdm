#calling Connection Class set as module
import Connection as myConnection
class Source:
  def __init__(self):
      pass
#Initialize Class Connection
  conn = myConnection.Connection()

  #PDT get data agama
  def get_agama_pdt(self, conn=myConnection.Connection()):
      pdt_curr = conn.pdt_connection()
      pdt_curr.execute('SELECT * FROM dbo.MD_ref_agama')
      for row in pdt_curr:
          print (row)