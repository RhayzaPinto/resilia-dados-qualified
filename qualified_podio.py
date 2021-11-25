def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
# Implemente aqui a lógica da função 
  if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
    if tempo_chegada2 < tempo_chegada3:
      return f"1 - {tempo_chegada1} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada3} minutos\n"
    else:
      return f"1 - {tempo_chegada1} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada2} minutos\n"
  elif tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
    if tempo_chegada1 < tempo_chegada3:
      return  f"1 - {tempo_chegada2} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada3} minutos\n"
    else:
      return f"1 - {tempo_chegada2} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada1} minutos\n"
  elif tempo_chegada3 < tempo_chegada1 and tempo_chegada3 < tempo_chegada2:
    if tempo_chegada1 < tempo_chegada2:
      return f"1 - {tempo_chegada3} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada2} minutos\n"
    else:
      return f"1 - {tempo_chegada3} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada1} minutos\n"
  
  
def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3,):
    # Implemente aqui a lógica da função
    if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
        if tempo_chegada2 < tempo_chegada3:
            return (
                f'1 - {nome_corredor1} - {tempo_chegada1} minutos\n'+
                f'2 - {nome_corredor2} - {tempo_chegada2} minutos\n'+
                f'3 - {nome_corredor3} - {tempo_chegada3} minutos\n'
            )
        else:
            return (
                f'1 - {nome_corredor1} - {tempo_chegada1} minutos\n'+
                f'2 - {nome_corredor3} - {tempo_chegada3} minutos\n'+
                f'3 - {nome_corredor2} - {tempo_chegada2} minutos\n'
            )
    if tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
        if tempo_chegada1 < tempo_chegada3:
            return (
                f'1 - {nome_corredor2} - {tempo_chegada2} minutos\n'+
                f'2 - {nome_corredor1} - {tempo_chegada1} minutos\n'+
                f'3 - {nome_corredor3} - {tempo_chegada3} minutos\n'
            )
        else:
            return (
                f'1 - {nome_corredor2} - {tempo_chegada2} minutos\n'+
                f'2 - {nome_corredor3} - {tempo_chegada3} minutos\n'+
                f'3 - {nome_corredor1} - {tempo_chegada1} minutos\n'
            )
    if tempo_chegada3 < tempo_chegada1 and tempo_chegada3 < tempo_chegada2:
        if tempo_chegada1 < tempo_chegada2:
            return (
                    f'1 - {nome_corredor3} - {tempo_chegada3} minutos\n'+
                    f'2 - {nome_corredor1} - {tempo_chegada1} minutos\n'+
                    f'3 - {nome_corredor2} - {tempo_chegada2} minutos\n'
                )
        else:
            return (
                    f'1 - {nome_corredor3} - {tempo_chegada3} minutos\n'+
                    f'2 - {nome_corredor2} - {tempo_chegada2} minutos\n'+
                    f'3 - {nome_corredor1} - {tempo_chegada1} minutos\n'
                )