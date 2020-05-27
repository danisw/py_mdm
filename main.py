#calling Connection Class set as module
import Connection as myConnection
import Source as mySource
import Target as myTarget

#Initialize Class Connection
conn = myConnection.Connection()
#Initialize Class Source 
src = mySource.Source()
#Initialize Class Target 
tgt = myTarget.Target()

#access Class method
greetings = conn.greetings()
print(greetings)

#get existing agama in pdt
src.get_agama_pdt()
#get existing agama in target siakad
tgt.get_siakad_agama()

#cek jumlah agama in pdt
jumlah_source = src.cek_jumlah_agama_pdt()
print("jumal data source : "+str(jumlah_source))
#cek jumlah data di database target (SIAKAD-SIPMABA)
jumlah_target = tgt.cek_jumlah_siakad_agama()
print("jumlah data target : "+str(jumlah_target))

