from pprint import pprint


list_numeric_systems = [{'bin':bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(16)]
pprint(list_numeric_systems)