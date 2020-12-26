from peewee import *
import datetime
import peeweedbevolve

db = SqliteDatabase("/home/pi/sensor_data.db")

class BaseModel(Model):
    time_created = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db

class Sensor(BaseModel):
    mac = TextField(primary_key=True)

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
    sensor = ForeignKeyField(Sensor)

models = [Sensor, Reading]

if __name__ == "__main__":
    db.evolve(models)
