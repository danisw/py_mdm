#calling Connection Class set as module
import Connection as myConnection
class Target:
  def __init__(self):
      pass
  conn = myConnection.Connection()

  def get_siakad_agama(self,conn=myConnection.Connection()):
      siakad_cur= conn.siakad_connection()
      siakad_cur.execute('SELECT * from  dbo.MD_1_ref_agama')
      print("\n=== Destination Condition ===\n")
      for row in siakad_cur:
          print (row)


  def cek_jumlah_siakad_agama(self,conn=myConnection.Connection()):
      siakad_cur= conn.siakad_connection()
      siakad_cur.execute('SELECT count(*) from  dbo.MD_1_ref_agama')
      tgt_row_cnt = siakad_cur.fetchone()[0]
      return tgt_row_cnt
      #text = 'jumlah data Target : '
      #print ("\n{}{}".format(text,tgt_row_cnt)) 