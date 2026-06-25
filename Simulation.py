class Simulation:

    MONTHS_IN_YEAR = 12

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

    def __get_hour_temperature(self, season, hour):
        return self.temp_sensor.read_temperature(season, hour)

    def __get_hour_load(self, season, hour):
        return self.load_sensor.read_load(season, hour)

    def __simulate_transformer(self, season, hour):

        ambient_temp = self.__get_hour_temperature(season, hour)
        load = self.__get_hour_load(season, hour)

        self.transformer.update_status(
            ambient_temp,
            load
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

        for _ in range(self.time_engine.clock.HOURS_IN_DAY):

            self.simulate_hour()

            self.time_engine.next_time()

    def simulate_month(self):

        days = self.time_engine.calendar.get_days_in_month()

        for _ in range(days):

            self.simulate_day()

    def simulate_year(self):

        for _ in range(self.MONTHS_IN_YEAR):

            self.simulate_month()

    def simulate(self):

        self.simulate_year()