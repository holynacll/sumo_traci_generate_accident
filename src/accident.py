from random import choice
from src.config import traci, settings


def create_accident():
    road_ids: list[str] = get_road_ids_except_internals()
    road_id: str = choice(road_ids)

    vehicle_ids: list[str] = traci.edge.getLastStepVehicleIDs(edgeID=road_id)
    for vehicle_id in vehicle_ids:
        if not vehicle_is_in_a_valid_position_lane(vehicle_id):
            continue

        create_vehicle_accidented(vehicle_id, road_id)
        return

def vehicle_is_in_a_valid_position_lane(vehicle_id: str):
    position = traci.vehicle.getLanePosition(vehicle_id)
    return 0.2 * settings.lane_length < position > 0.4 * settings.lane_length


def create_vehicle_accidented(vehicle_id: str, road_id: str):
    speed_road_accidented: float = settings.speed_road_accidented
    traci.edge.setMaxSpeed(road_id, speed_road_accidented)
    traci.vehicle.slowDown(
        vehicle_id,
        slow_down_vehicle_speed(vehicle_id),
        settings.timing_to_slow_down_vehicle,
    )
    try:
        traci.vehicle.setStop(
            vehicle_id,
            edgeID=road_id,
            pos=get_position_vehicle_will_stop(vehicle_id),
            laneIndex=traci.vehicle.getLaneIndex(vehicle_id),
            duration=settings.accident_duration_timeout,
        )
    except:
        return
    set_highlight_accident(vehicle_id)
    print(
        f"{traci.simulation.getTime()} - Vehicle {vehicle_id} has been accidented in road {road_id}"
    )


def get_road_ids_except_internals():
    road_ids: list[str] = traci.edge.getIDList()
    return [road_id for road_id in road_ids if not road_id.startswith(':')]

def slow_down_vehicle_speed(vehicle_id: str):
    return 0.2 * traci.vehicle.getAllowedSpeed(vehicle_id)


def get_position_vehicle_will_stop(vehicle_id: str):
    return traci.vehicle.getLanePosition(vehicle_id) + (0.1 * settings.lane_length)


def set_highlight_accident(vehicle_id: str):
    traci.vehicle.highlight(vehicle_id, settings.color_accident)
