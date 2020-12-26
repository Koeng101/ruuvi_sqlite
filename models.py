from peewee import *
import datetime

db = SqliteDatabase("/home/pi/sensor_data.db")

class Reading(Model):
    data_format = SmallIntegerField()
    humidity = FloatField()
    temperature = FloatField()
    pressure = FloatField()
    acceleration = FloatField()
    acceleration_x = IntegerField()
    acceleration_y = IntegerField()
    acceleration_z = IntegerField()
    tx_power = IntegerField()
    battery = IntegerField()
    movement_counter = IntegerField()
    measurement_sequence_number = IntegerField()
    mac = TextField()
    
    time_created = IntegerField(default=int(datetime.now().strftime('%s')))

    class Meta:
        database = db

models = [Reading]

if __name__ == "__main__":
    db.create_tables([Reading])
