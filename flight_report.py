def flight_report(estimated_time, scheduled_time):
		if estimated_time > scheduled_time:
			time_diff = estimated_time - scheduled_time
			time_diff = time_diff * 60
			print("Flight will arrive", int(time_diff), "min early!")

def flight_report(estimated_time, scheduled_time):
		if estimated_time < scheduled_time:
			time_diff = scheduled_time - estimated_time
			time_diff = time_diff * 60
			print("Flight will be delayed", int(time_diff), "min")

def flight_report(estimated_time, scheduled_time):
		if estimated_time == scheduled_time:
			print("Flight will be there on time, No delayed!")
