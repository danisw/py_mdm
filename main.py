#calling Connection Class set as module
import Connection as myConnection
import Source as mySource
import Operation as myOperation

#Initialize Class Connection
conn = myConnection.Connection()
#Initialize Class Source 
src = mySource.Source()
#Initialize Class Target 

#get all data quque
i=0
data_queue = src.get_queue_data_agama()
jumlah_data = len(data_queue)
print(jumlah_data)
#print(data_changed)
while i < jumlah_data:
    queue_changed_agama = src.get_queue_data_agama()
    operation = myOperation.Operation()
    opt = operation.execute_agama(queue_changed_agama)
    print(opt)
    i += 1

#get queue changed 
#queue_changed_agama = src.get_queue_data_agama()
#print (queue_changed_agama)

#Start Operation : insert / delete sesuai mapping nya
#operation = myOperation.Operation()
#opt = operation.execute_agama(queue_changed_agama)
#print(opt)

'''
#access Class method
greetings = conn.greetings()
print(greetings)

#get existing agama in pdt
src.get_agama_pdt()
#get existing agama in target siakad
tgt.get_siakad_agama()
#get existing agama in target sipmaba
tgt.get_sipmaba_agama()

#cek jumlah agama in pdt
jumlah_source = src.cek_jumlah_agama_pdt()
print("jumal data source : "+str(jumlah_source))
#cek jumlah data di database target (SIAKAD-SIPMABA)
jumlah_target_siakad = tgt.cek_jumlah_siakad_agama()
print("jumlah data target siakad : "+str(jumlah_target_siakad))
#cek jumlah data di database target (SIAKAD-SIPMABA)
jumlah_target_sipmaba = tgt.cek_jumlah_sipmaba_agama()
print("jumlah data target sipmaba : "+str(jumlah_target_sipmaba))

'''