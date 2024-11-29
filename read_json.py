
import json

el_inpute = input()

try:
    with open(el_inpute, encoding="utf8") as el_data:
        el_armazem = json.load(el_data)
    print(el_armazem)

except:
    print("Ocorreu um erro!")

finally:
    print("Processo concluído!")