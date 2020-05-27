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
src.cek_jumlah_agama_pdt()
#cek jumlah data di database target (SIAKAD-SIPMABA)
tgt.cek_jumlah_siakad_agama()
