def alarm(hour,minutes):
    hora = hour + 6 + (minutes + 51)//60
    minutes = (minutes + 51) % 60
    if hora > 24:
        hora = hora - 24
    if len(str(hora)) < 2:
        hora = '0' + str(hora)
    if len(str(minutes)) < 2:
        minutes = '0' + str(minutes)
    alarme = str(hora) + ':' + str(minutes)
    return alarme