#!/usr/bin/python3

'''
    Analizar los datos provisorios de las Elecciones PASO 2017 Legilativas en la Provincia 
    de Córdoba.

    Muestra de los datos

    sub_proCodigoProvincia,sub_depCodigoDepartamento,sub_munCodigoMunicipio,sub_mesCodigoCircuito,
        sub_mesCodigoMesa,sub_mesCodSexo,sub_votparCodigo,sub_parCodigo,ordenPartidos,subVotosPartido
    "04","001","666","0001 ","0001","X","0022","3017",1,0
    "04","001","666","0001 ","0001","X","0069","3037",1,3

'''
import csv
import sys

campos = ['sub_proCodigoProvincia','sub_depCodigoDepartamento',
            'sub_munCodigoMunicipio','sub_mesCodigoCircuito',
            'sub_mesCodigoMesa','sub_mesCodSexo','sub_votparCodigo',
            'sub_parCodigo','ordenPartidos','subVotosPartido']

data_file = 'datos/MesasSublemasCordobaProvincia.csv'

circuitos = {}
agrupaciones = []

with open(data_file) as csvfile:
    reader = csv.DictReader(csvfile)
    headers = next(reader)

    for row in reader:
        circuito = row['sub_mesCodigoCircuito'].strip().lstrip('0')
        votos = int(row['subVotosPartido'].strip())
        # agrupacion sobre las internas
        agrupacion = row['sub_votparCodigo'].strip().lstrip('0')
        if agrupacion not in agrupaciones:
            agrupaciones.append(agrupacion)
            print('agrupacion nueva {}'.format(agrupacion))
        
        if circuito not in circuitos.keys():
            circuitos[circuito] = {}
            print('circuito nuevo {}'.format(circuito))
        if agrupacion not in circuitos[circuito].keys():
            circuitos[circuito][agrupacion] = 0
        
        circuitos[circuito][agrupacion] += votos

file_dest = 'datos/resultados-por-circuitos-por-agrupacion.csv'
headers = ['circuito'] + agrupaciones

print(headers)

with open(file_dest, 'w') as csvfile:
    w = csv.DictWriter(csvfile, headers)
    w.writeheader()
    for circuito in circuitos.keys():
        row = {'circuito': circuito}
        for agrupacion in circuitos[circuito].keys():
            row[agrupacion] = circuitos[circuito][agrupacion]

        w.writerow(row)
        