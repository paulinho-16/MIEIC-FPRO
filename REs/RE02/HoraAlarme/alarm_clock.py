import datetime
tempo_atual=datetime.datetime.now()
print('Hora atual:',tempo_atual.strftime('%H:%M'))
tempo_alarme=(tempo_atual+datetime.timedelta(0,8*3600+30*60))
print('Hora do alarme:',tempo_alarme.strftime('%H:%M'))