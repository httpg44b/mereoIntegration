from zeep import Client
from zeep.wsse.username import UsernameToken
from getToken import getToken
from connectSqlServer import setup
from getHistoryPosition import querySQL

#headers
wsdl = 'https://hml-engeform.mereo.com/services/JobPositionHistoryService.svc?wsdl'
user = 'service.mereo'
client = Client(wsdl=wsdl, wsse=UsernameToken(user, getToken(user), use_digest=False))

#Variáveis para consulta ao banco:
conn = setup()
res = querySQL(conn)


JobPositionCode = [tupla[0] for tupla in res]
Salary = [float(tupla[1]) for tupla in res]
StartDate = [tupla[3] for tupla in res]
UserLogin = [tupla[2] for tupla in res]
x = len(JobPositionCode)

#Variavel contador
n = 0

try:
   for code in JobPositionCode:
     job_position_history_list = {
      'JobPositionHistoryImportData': {
          'JobPositionCode': JobPositionCode[n],
          'Salary': Salary[n],
          'StartDate': StartDate[n],
          'UserLogin': UserLogin[n]
      }
     }
     #print(job_position_history_list)

     try:
      response = client.service.ImportJobPositionHistory(jobPositionHistoryList=job_position_history_list)
      
      if response == '':
       print(f'Usuario {UserLogin[n]} não cadastrado no Mereo, {type(response)}')
      else:
        print(f'Atualizado o cargo do {UserLogin[n]} com sucesso, {response}')
     except Exception as e:
       f'Error: ${e.message}'
     n+=1
except(ValueError):
   f'Error: ${ValueError}'