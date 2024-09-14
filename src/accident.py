import random
from config import (
    traci,
    settings
)
from random import sample


def create_accident():
    road_ids: list[str] = traci.edge.getIDList()
    road_id: str = sample(road_ids)
    
    vehicle_ids: list[str] = traci.edge.getLastStepVehicleIDs(edgeID=road_id)
    for vehicle_id in vehicle_ids:
        if not vehicle_is_in_a_valid_position_lane(vehicle_id)
            continue
        
        create_vehicle_accidented(vehicle_id, road_id)

def vehicle_is_in_a_valid_position_lane(vehicle_id: str):
    position = traci.vehicle.getLanePosition(vehicle_id)
    return 0.2 * settings.lane_length < position > 0.4 * settings.lane_length


def create_vehicle_accidented(vehicle_id: str, road_id: str):
    speed_road_accidented: float = settings.speed_road_accidented
    traci.edge.setMaxSpeed(road_id, speed_road_accidented)
    traci.vehicle.slowDown(
        vehicle_id,
        slow_down_vehicle_speed(vehicle_id),
        settings.timing_to_slow_down_vehicle
    )
    


def slow_down_vehicle_speed(vehicle_id: str):
    return 0.2 * traci.vehicle.getAllowedSpeed(vehicle_id)
