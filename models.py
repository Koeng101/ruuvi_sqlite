from peewee import *
import datetime

db = SqliteDatabase("/home/pi/sensor_data.db")

class BaseModel(Model):
    time_created = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db

class Reading(BaseModel):
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

models = [Reading]

if __name__ == "__main__":
    db.create_tables([Reading])
