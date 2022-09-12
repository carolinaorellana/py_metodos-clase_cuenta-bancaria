from cuenta import CuentaBancaria 

#INSTRUCCIONES
#Crea 2 cuentas
#Para la primera cuenta, haz 3 depósitos y 1 retiro, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)
#Para la segunda cuenta, haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)

cuentaCarolina = CuentaBancaria(500)
#cuentaCarolina.mostrar_info_cuenta() #comprobar que todo esta OK
cuentaCarolina.deposito(200).deposito(100).deposito(400).retiro(600).generar_intereses().mostrar_info_cuenta()

cuentaAndrea = CuentaBancaria()
#cuentaAndrea.mostrar_info_cuenta()#comprobar que todo esta OK

cuentaAndrea.deposito(1000).deposito(500).retiro(50).retiro(100).retiro(250).retiro(200).generar_intereses().mostrar_info_cuenta()

"""
print(CuentaBancaria.imprimir_todas_las_cuentas()) #imprime las impresiones dentro del metodo y NECESUTO TENER el retorno
"""
CuentaBancaria.imprimir_todas_las_cuentas()#solo imprime los print dentro del metodo, no necita tener retorno
print(CuentaBancaria.suma_todos_los_balances())#enecista tener retorno porque imprime el retorno al usar print.

#CuentaBancaria.suma_todos_los_balances()#esto no imprime nada ya que no hay impresiones dentro del metodo.