""" Table Reference AGAMA """

import pyodbc
pdt_conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.199.16.69;'
                      'Database=PDT;'
                      'Trusted_Connection=no;'
                      'UID=sa;'
                      'PWD=Akreditasi2019!;')

siakad_conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.199.16.69;'
                      'Database=SIAKAD;'
                      'Trusted_Connection=no;'
                      'UID=sa;'
                      'PWD=Akreditasi2019!;')

sipmaba_conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.199.16.69;'
                      'Database=SIPMABA;'
                      'Trusted_Connection=no;'
                      'UID=sa;'
                      'PWD=Akreditasi2019!;')

""" Select Data PDT """
print("=== Source Condition ====\n")
cursor_1 = pdt_conn.cursor()
cursor_1.execute('SELECT * FROM dbo.MD_ref_agama')
for row in cursor_1:
    print (row)

""" Check jumlah data PDT """
cursor_2 = pdt_conn.cursor()
cursor_2.execute('SELECT count(*) FROM dbo.MD_ref_agama')
src_row_cnt = cursor_2.fetchone()[0]
text = 'jumlah data Source : '
print ("\n{}{}".format(text,src_row_cnt))

""" Cek kondisi target """
cursor_3= siakad_conn.cursor()
cursor_3.execute('SELECT count(*) from  dbo.MD_1_ref_agama')
tgt_row_cnt = cursor_3.fetchone()[0]
text = 'jumlah data Target : '
print("\n=== Destination Condition ===\n")
for row in cursor_1:
    print (row)
print ("\n{}{}".format(text,tgt_row_cnt))

""" Bandingkan sum_src dan sum_dest """
print("\n === Membandingkan jumlah Source dan Destination ===\n")
if(src_row_cnt==tgt_row_cnt):
    val="Jumlah Sama : "
    print("{}{}".format(val,tgt_row_cnt))
else:
    print("Jumlah Tidak sama")
    val_s="Source Row : "
    val_t="Target Row : "
    print("{}{}\n".format(val_s,src_row_cnt))
    print("{}{}\n".format(val_t,tgt_row_cnt))

""" Operasi Pengisian Target """
if(tgt_row_cnt==0):
    i=0
    cursor_2.execute('SELECT id_agama, nama_agama from [PDT].dbo.MD_ref_agama')
    for row in cursor_2.fetchall():
        id_agama, nama_agama = row
        cursor_3.execute('INSERT INTO [SIAKAD].dbo.MD_1_ref_agama VALUES (?,?)', id_agama,nama_agama)
        siakad_conn.commit()
        rc = cursor_3.rowcount
        i=i+rc
    print(i," rows Already Inserted")
else:
    print("row by row comparation Continue")

""" Cek hasil Inputan """
cursor_2 = pdt_conn.cursor()
cursor_2.execute('SELECT count(*) FROM dbo.MD_ref_agama')
src_row_cnt = cursor_2.fetchone()[0]

cursor_3= siakad_conn.cursor()
cursor_3.execute('SELECT count(*) from  dbo.MD_1_ref_agama')
tgt_row_cnt = cursor_3.fetchone()[0]

""" Bandingkan dgn row_sum """
if(src_row_cnt==tgt_row_cnt):
    val="Jumlah Sama : "
    print("{}{}".format(val,tgt_row_cnt))
    print("Finish !")
else:
    print("Jumlah Tidak sama")
    val_s="Source Row : "
    val_t="Target Row : "
    print("{}{}\n".format(val_s,src_row_cnt))
    print("{}{}\n".format(val_t,tgt_row_cnt))
    print("Ulangi Proses")
