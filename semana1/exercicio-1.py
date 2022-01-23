temperatura_graus_fahrenheit = float(input("Informe a Temperatura em °F : "))

### Formula de Conversão
##  C        F - 32
## ____  =  --------
##  5          9
## ( (C * 9) / 5) + 32 = F
## ( (F - 32) * 5 ) / 9 = C

temperatura_graus_celsius = (5.0 * (temperatura_graus_fahrenheit - 32.0)) / 9.0

print("Temperatura em °C é", temperatura_graus_celsius, "°C")
