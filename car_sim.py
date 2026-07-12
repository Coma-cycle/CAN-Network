import os
import time
import random

print("")

while True:
	# engine rpm is a reandom number between 2000 and 2500
	rpm = random.randint(2000, 2500)
	# convert int to hex string
	rpm_hex = f"{rpm:04X}"
	os.system(f"cansend vcan0 1A3#{rpm_hex[:2]}{rpm_hex[2:]}000000000000")

	# vehicle speed is a random number between 75 and 85
	speed = random.randint(75, 85)
	speed_hex = f"{speed:02X}"
	os.system(f"cansend vcan0 2B4#{speed_hex}000000000000")

	time.sleep(0.5)
