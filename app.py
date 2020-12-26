from ruuvitag_sensor.ruuvi import RuuviTagSensor
from models import *

macs = [
    'F0:B6:9D:BA:22:65',
    'FC:08:E2:99:77:5F',
    'F9:CC:D3:40:0F:C9'
    ]

# Empirically, 10 seconds has approximately been the right amount of time to wait per measurement
timeout = 10 

while True:
    datas = RuuviTagSensor.get_data_for_sensors(macs, timeout)
    for key, json in datas.items():
        r = Reading.create(
                data_format = json["data_format"],
                humidity = json["humidity"],
                temperature = json["temperature"],
                pressure = json["pressure"],
                acceleration = json["acceleration"],
                acceleration_x = json["acceleration_x"],
                acceleration_y = json["acceleration_y"],
                acceleration_z = json["acceleration_z"],
                tx_power = json["tx_power"],
                battery = json["battery"],
                movement_counter = json["movement_counter"],
                measurement_sequence_number = json["measurement_sequence_number"],
                mac = json["mac"],
                )
        r.save()

