class Simulation:

    def __init__(
        self,
        transformer,
        daily_report,
        temp_sensor,
        load_sensor,
        time_engine
    ):
        self.transformer = transformer
        self.daily_report = daily_report
        self.temp_sensor = temp_sensor
        self.load_sensor = load_sensor
        self.time_engine = time_engine

        self.record_number = 1

    # -------------------------
    # Private Methods
    # -------------------------

    def __read_sensors(self,season,hour):
        return {
            "temperature" : self.temp_sensor.read_temperature(season,hour),
            "load" : self.load_sensor.read_load(season,hour)
        }



    def __simulate_transformer(self,season, hour):

        sens = self.__read_sensors(season,hour)

        self.transformer.update_status(
            sens["temperature"],
            sens["load"]
        )

        return self.transformer.get_status()

    # -------------------------
    # Simulation Methods
    # -------------------------

    def simulate_hour(self):

        time = self.time_engine.get_time()

        status = {

            "Record Number": self.record_number,

            "Hour": time["Hour"],
            "Day": time["Day"],
            "Month": time["Month"],
            "Year": time["Year"],
            "Season": time["Season"],

            **self.__simulate_transformer(
                time["Season"],
                time["Hour"]
            )
        }

        self.daily_report.add_record(status)

        self.record_number += 1

    def simulate_day(self):

        for _ in range(self.time_engine.get_hours_in_day()):

            self.simulate_hour()

            self.time_engine.next_time()

    def simulate_month(self):

        for _ in range(self.time_engine.get_days_in_month()):

            self.simulate_day()

    def simulate_year(self):

        for _ in range(self.time_engine.get_month_in_year()):

            self.simulate_month()

    def simulate(self):

        self.simulate_year()