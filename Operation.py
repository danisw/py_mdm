import Connection as myConnection
import Target as myTarget

class Operation:
  def __init__(self):
      pass

  def execute_agama(self, data_agama):

      #cek operator
      operator = data_agama[2]
      if operator == 'INS':
          try:
              #set id agama, anama agama
              id_agama = data_agama[0]
              nama_agama = data_agama[1]
              data_agama_2 = (id_agama,nama_agama)

              #calling insert method
              inserting_data = myTarget.Target()
              result = inserting_data.insert_agama(data_agama_2)
              
              #result = 'Calling insert method successed'

          except:
              result = 'Calling Error'
          
      elif operator == 'DEL':
          try:
              result = 'Callinf insert method'
          except:
              result = 'Calling error'

      else:
          try:
              result = 'Calling update method'
          except:
              result = 'Calling error'

      return result

