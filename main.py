#calling Connection Class set as module
import Connection as myConnection
import Source as mySource

#Initialize Class Connection
conn = myConnection.Connection()
#Initialize Class Source 
src = mySource.Source()

#access Class method
greetings = conn.greetings()
print(greetings)

#print existing agama in pdt
src.get_agama_pdt()
