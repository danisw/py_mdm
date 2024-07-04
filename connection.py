import pyodbc
class Connection:
  def __init__(self):
      pass

  def greetings(self):
      return "================ Started ==============="

  def pdt_connection(self):
      pdt_conn = pyodbc.connect('Driver={SQL Server};''Server=10.199.16.69;''Database=PDT;''Trusted_Connection=no;''UID=sa;''PWD=xxx;')
      cursor_pdt = pdt_conn.cursor()
      return cursor_pdt

  def siakad_connection(self):
      siakad_conn = pyodbc.connect('Driver={SQL Server};''Server=10.199.16.69;''Database=SIAKAD;''Trusted_Connection=no;''UID=sa;''PWD=xxx;')
      cursor_siakad = siakad_conn.cursor()
      return cursor_siakad

  def sipmaba_connection(self):
      sipmaba_conn = pyodbc.connect('Driver={SQL Server};''Server=10.199.16.69;''Database=SIPMABA;''Trusted_Connection=no;''UID=sa;''PWD=xxx;')
      cursor_sipmaba = sipmaba_conn.cursor()
      return cursor_sipmaba
