import json


def lambda_handler(event, context):
    try:
        # Obtener datos de entrada
        material_id = event['material_id']
        gramaje = event['gramaje']

        # Creating a dictionary
        material_dict = {
            "1": {"name": "Oro puro 24k", "price": 1500.00},
            "2": {"name": "Oro alto 18k", "price": 1000.00},
            "3": {"name": "Oro medio 14k", "price": 800.00},
            "4": {"name": "Oro bajo 10k", "price": 500.00},
            "5": {"name": "Plata ley .925", "price": 300.00},
            "6": {"name": "Titanio", "price": 200.00},
            "7": {"name": "Rodio", "price": 100.00}

        }

        material = material_dict[material_id]
        print(material)

        # Calculo del avaluo
        avaluo = material["price"] * float(gramaje)
        print("El monto del avaluo es: " + str(avaluo))

        # Calculo del prestamo
        monto_prestamo = avaluo * 0.8
        print("El monto del prestamo es: " + str(monto_prestamo))

        response = {
            'statusCode': 200,
            'body': json.dumps({'metal': material["name"], 'gramaje': gramaje, 'prestamo': monto_prestamo})
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response
