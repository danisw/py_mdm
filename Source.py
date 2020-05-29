#calling Connection Class set as module
import Connection as myConnection
class Source:
  def __init__(self):
      pass
#Initialize Class Connection
  conn = myConnection.Connection()

  def get_all_changed_agama(self, conn=myConnection.Connection()):
    pdt_cur = conn.pdt_connection()
    pdt_cur.execute('SELECT * FROM [dbo].[audits_ref_agama]')
    result = pdt_cur.fetchall()
    return result

 #PDT get changeable table
  def get_queue_data_agama(self, conn=myConnection.Connection()):
    pdt_cur = conn.pdt_connection()
    pdt_cur.execute('SELECT top 1 id_agama, nama_agama,operation FROM [dbo].[audits_ref_agama] where is_executed is null order by updated_at asc')
    result = pdt_cur.fetchall()

    #cast tuples to list
    data = result[0]
    list_data = list(data)
    id_agama = list_data[0]
    nama_agama = list_data[1]
    opt = list_data[2]

    list_baru = [id_agama,nama_agama,opt]

    return list_baru

  #PDT get data agama
  def get_agama_pdt(self, conn=myConnection.Connection()):
      pdt_curr = conn.pdt_connection()
      pdt_curr.execute('SELECT * FROM dbo.MD_ref_agama')
      print("======== Source Condition ============")
      for row in pdt_curr:
          print (row)

  #PDT cek jumlah data agama
  def cek_jumlah_agama_pdt(self, conn=myConnection.Connection()):
      pdt_curr = conn.pdt_connection()
      pdt_curr.execute('SELECT count(*) FROM dbo.MD_ref_agama')
      src_row_cnt = pdt_curr.fetchone()[0]
      return src_row_cnt
      #text = 'jumlah data Source : '
      #print ("\n{}{}".format(text,src_row_cnt))