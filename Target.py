#calling Connection Class set as module
import Connection as myConnection
class Target:
  def __init__(self):
      pass
    
  conn = myConnection.Connection()

  def insert_agama (self, data):
      
      id_agama = data[0]
      nama_agama = data[1]
      status=[];

      try:
          conn = myConnection.Connection()
          siakad_cur= conn.siakad_connection()
          siakad_cur.execute('INSERT INTO [SIAKAD].dbo.MD_1_ref_agama VALUES (?,?)', id_agama,nama_agama)
          siakad_cur.commit()
          #update null on pdt
          try:
              pdt_curr = conn.pdt_connection()
              pdt_curr.execute('update [PDT].[dbo].[audits_ref_agama] SET is_executed = 1, time_executed= getdate() where id_agama = ?', id_agama)
              pdt_curr.commit()
              status.append("succeess siakad & success pdt update",)
          except:
              #fail update = set null lagi ke pdt biar nanti di eksekusi ulang
              pdt_curr = conn.pdt_connection()
              pdt_curr.execute('update [PDT].[dbo].[audits_ref_agama] SET is_executed = null , time_executed= null where id_agama = ?', id_agama)
              pdt_curr.commit()
              status.append("success siakad & failed pdt")

      except:
          status.append("failed siakad & no update pdt")
          #status.append("successed siakad")
      #return status

      try:
          conn = myConnection.Connection()
          sipmaba_cur = conn.sipmaba_connection()
          sipmaba_cur.execute('INSERT INTO [SIPMABA].dbo.MD_2_ref_agama VALUES (?,?)', id_agama,nama_agama)
          sipmaba_cur.commit()
          try:
              pdt_curr = conn.pdt_connection()
              pdt_curr.execute('update [PDT].[dbo].[audits_ref_agama] SET is_executed = 1, time_executed= getdate() where id_agama = ?', id_agama)
              pdt_curr.commit()
              status.append("success sipmaba & success pdt")
          except:
              #set is_executed null 
              pdt_curr = conn.pdt_connection()
              pdt_curr.execute('update [PDT].[dbo].[audits_ref_agama] SET is_executed = null , time_executed= null where id_agama = ?', id_agama)
              pdt_curr.commit()
              status.append("success sipmaba & failed pdt")
              
      except:
          status.append("failed sipmaba & no update pdt")
          #status.append("successed siakad")

      return status       

      


'''
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
'''