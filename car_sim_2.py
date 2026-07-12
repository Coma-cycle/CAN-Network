# Decoding the hex values from the candump trace to find the simulated values

# ID 0x2B4 (Vehicle Speed) - First byte contains the speed in hex
# Let's extract the distinct hex values found in the dump for 2B4: 4E, 51, 4D, 53, 4C, 55
speeds_hex = ["4E", "51", f"4D", "53", "4C", "55"]
speeds_dec = [int(x, 16) for x in speeds_hex]

# ID 0x1A3 (Engine RPM) - First two bytes contain the RPM in hex
# Let's extract the pairs found in the dump for 1A3: 0922, 09B5, 0848, 083A, 07D2, 085A, 0921, 0965, 0822, 08C6, 091D
rpm_hex = ["0922", "09B5", "0848", "083A", "07D2", "085A", "0921", "0965", "0822", "08C6", "091D"]
rpm_dec = [int(x, 16) for x in rpm_hex]

print(f"Speeds (km/h): {speeds_dec}")
print(f"RPM values: {rpm_dec}")
