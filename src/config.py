from pathlib import Path
from os import environ
from sys import path, exit

environ['SUMO_HOME'] = Path(environ['VIRTUAL_ENV']) / 'lib' / 'python3.11' / 'site-packages' / 'sumo'

if 'SUMO_HOME' in environ:
    tools = Path(environ.get('SUMO_HOME')) / 'tools'
    path.append(tools)
    print(f"Pasta tools adicionada ao sys.path: {tools}")
else:
    exit("please declare environment variable 'SUMO_HOME'")

try:
    import traci
    from sumolib import checkBinary  # noqa
    print("traci importado com sucesso.")
except ModuleNotFoundError as e:
    print(f"Erro ao importar módulo: {e}")
    exit("Certifique-se de que o SUMO e o Traci estão instalados corretamente e o caminho do SUMO_HOME está correto.")


class Config:
    def __init__(self):
        self.lane_length: int = 300 # meters
        self.speed_road_accidented: float = 1.0 # meters/seconds
        self.timing_to_slow_down_vehicle: int = 10 # seconds

settings = Config()