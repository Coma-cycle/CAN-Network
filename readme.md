# Day 1 CAN Bus Research & Virtual Emulation Pipeline

## 1. Electrical & Physical Topology
* **Differential Signaling Standards:** High-speed automotive CAN utilizes 5V differential voltage lines to handle noise immunity. An industrial transceiver (e.g., ISO1050) steps down signals to match an MCU's 3.3V digital logic rails (TX/RX lines).
* **Recessive State (Logical '1'):** Passive bus state. Both `CAN_H` and `CAN_L` sit at a baseline voltage of ~2.5V ($\Delta V = 0V$). Any node on the loop can overwrite this state.
* **Dominant State (Logical '0'):** Active bus state. `CAN_H` is driven up to ~3.5V and `CAN_L` is pulled down to ~1.5V ($\Delta V \approx 2V$). The dominant bit physically overrides recessive bits.

## 2. Low-Level Hardware State Machines
* ** bxCAN Processing Core:** Integrated peripherals (like the STM32F405/407 bxCAN block) run on independent hardware Finite State Machines. They manage bit-stuffing, automatic packet retransmissions, and cyclic redundancy checksums (CRC) without CPU calculation overhead.
* **Hardware Frame Filtering:** Minimizes application latency by handling network filtering in hardware registers, ensuring the main MCU execution loop only processes relevant target message IDs.

## 3. Communication Frame Architecture
* **SOF (Start of Frame):** A single dominant bit that breaks an idle bus stream (`1111...`) to trigger hardware clock synchronization across nodes.
* **11-Bit Standard Identifier:** Sets the priority and description of the data packet, rather than a physical node address. numerical priority allows non-destructive bitwise arbitration during simultaneous wire collisions.
* **Control Metadata:**
  * **IDE (Identifier Extension):** 1-bit flag denoting standard 11-bit (`0`) or extended 29-bit (`1`) payloads.
  * **r0:** Reserved configuration bit (transmitted as dominant `0`).
  * **DLC (Data Length Code):** 4-bit array defining the payload volume (0 to 8 bytes).

## 4. Hardware Acknowledgment (ACK)
* **Bus Handshaking:** The transmitting node drops the line to a floating Recessive `1` during the ACK time slot. Every receiving peripheral that confirms a valid CRC actively drives the wire to a Dominant `0`. A dominant state confirms a successful bus transmission.

## 5. Linux SocketCAN Emulation Environment
A virtual vehicle bus loopback interface (`vcan0`) was deployed to simulate network layers and validate packet parsing structures prior to deploying raw SPI-to-CAN standalone transceiver hardware modules (e.g., MCP2515):

```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

### Automotive Dataset Capture (`candump vcan0`)
Validated live data logs from simulated Electronic Control Units (ECUs):
* **ID 0x2B4 (Vehicle Speed):** Real-time tracking fluctuating within a 75-85 km/h driving baseline.
* **ID 0x1A3 (Engine RPM):** Dual-byte tracking monitoring performance fluctuations within a 2000-2500 RPM envelope.


Defining an objective... simulating CAN in terminal

install CAN utilities
```
dnf install can-utils -y 
```

initialize

```
modprobe vcan
ip link add dev vcan0 type vcan
ip link set up vcan0
```

simulate using CAN0

Monotor BUS TRAFFIC::
```
candump vcan0
```

```
cansend vcan0 <can_id>#<hex_data_payload>
```
using a python script to generate radom rpm for the engie and random speed numbers for the vehicle, and sending it through a simulated CAN.

since CAN is a protocol for electronic devices to talk to each other, 
In a real car the random speed data is generated using a speed sensor in car , and rpm could be calculated using sensors as well all going through an ECU unit via CAN to be controlled.

the simulated result are ready now, i could use reall sensors to calculate an attribute , 
and then use a spi to CAN controller to send it to an ECU or a simple black pill. 
readyly I can send the simulated data to a black pill, but to use CAN i need spi to CAN converter.
