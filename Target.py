#calling Connection Class set as module
import Connection as myConnection
class Target:
  def __init__(self):
      pass
  conn = myConnection.Connection()

  def get_siakad_agama(self,conn=myConnection.Connection()):
      siakad_cur= conn.siakad_connection()
      siakad_cur.execute('SELECT * from  dbo.MD_1_ref_agama')
      print("\n=== SIAKAD Destination Condition ===\n")
      for row in siakad_cur:
          print (row)


  def cek_jumlah_siakad_agama(self,conn=myConnection.Connection()):
      siakad_cur= conn.siakad_connection()
      siakad_cur.execute('SELECT count(*) from  dbo.MD_1_ref_agama')
      tgt_row_cnt = siakad_cur.fetchone()[0]
      return tgt_row_cnt
      #text = 'jumlah data Target : '
      #print ("\n{}{}".format(text,tgt_row_cnt)) 

  def get_sipmaba_agama(self,conn=myConnection.Connection()):
      sipmaba_cur= conn.sipmaba_connection()
      print("\n=== SIPMABA Destination Condition ===\n")
      sipmaba_cur.execute('SELECT * from  dbo.MD_2_ref_agama')
      for row in sipmaba_cur:
          print (row)


  def cek_jumlah_sipmaba_agama(self,conn=myConnection.Connection()):
      sipmaba_cur= conn.sipmaba_connection()
      sipmaba_cur.execute('SELECT count(*) from  dbo.MD_2_ref_agama')
      tgt_row_cnt = sipmaba_cur.fetchone()[0]
      return tgt_row_cnt
      #text = 'jumlah data Target : '
      #print ("\n{}{}".format(text,tgt_row_cnt)) 