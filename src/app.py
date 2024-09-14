from config import (
    traci,
    checkBinary,
    settings,
)
import traceback

def shouldContinueSim():
    """Checks that the simulation should continue running.
    Returns:
        bool: `True` if vehicles exist on network. `False` otherwise.
    """
    numVehicles = traci.simulation.getMinExpectedNumber()
    return True if numVehicles > 0 else False

def run():
    step = 0
    print('Running simulation...')
    try:
        while shouldContinueSim():
            actual_time = traci.simulation.getTime()
            traci.simulationStep()
            if actual_time % 10 == 0:
                create_accident()
            step += 1
    except Exception:
        print(traceback.format_exc())
    finally:
        traci.close()



def start():
    sumoBinary = checkBinary('sumo-gui')
    
    traci.start([
        sumoBinary,
        "-c", settings.sumocfg_filepath,
        "-S",
        "-Q"
    ])
    
    run()    
    