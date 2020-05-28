def exchange_rate(value):
    # Las plataformas como Payoneer cobran un 2% por pasar de una moneda a otra
    return value * 0.98

def salary_usd_to_eur(salary, exchange_rate):
    return salary / exchange_rate

if __name__ == '__main__':
    print ('Ingresa tu salario en USD')
    salary = input ()

    print (
        'Ingresa el valor que sale en la siguiente URL https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD'
    )
    xe_value = input ()
    
    exchange_rate = exchange_rate(float(xe_value))
    
    print(
        'La tasa de cambio utilizada para este calculo es: {0}'.format(exchange_rate)
    )
    
    print (
        'Su Salario en Euros es: {0}'.format(salary_usd_to_eur( float(salary), exchange_rate ))
    )

