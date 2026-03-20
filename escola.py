import pytest


def verificador_media(media:int|float) -> str:
            
            if not isinstance(media, (int,float)):
                  raise TypeError("Tipo inválido, entrada deve ser numérica")
            
            if media >= 7: 
                  return "Aprovado"
            elif media <= 4:
                  return "Reprovado"
            else:
                  return "Recuperação"
            



if __name__ == "__main__":
      print(verificador_media(media=7))