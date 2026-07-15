### SYSTEM ARCHITECTURE: OPTIMIZED INTERMEDIATE COUPLING FOR STM32 BLACK PILL
To mitigate computational bloat and maintain a compact hardware footprint, the intermediate communication stack between the Host Application (User Space) and the Physical Medium (CAN_H/CAN_L) is streamlined into discrete hardware/software boundaries:

1. SPI HOST INTERFACE (Logical Boundary):
   * SCK / CS / MOSI / MISO (5V Tolerant on STM32F411)
   * Direct register-mapping via optimized SPI commands to eliminate multi-layer driver latency.

2. LOGICAL MAC/LLC LAYER (Silicon Boundary):
   * Handled by external hardware (MCP2515) to offload Bit Stuffing, Arbitration, and Hardware Acceptance Filtering from the main MCU core.

3. ANALOG TRANSCEIVER (Physical Border):
   * TJA1050 / MCP2551 mapping Logical TTL (TXD/RXD) to 3-Pin Differential Media (CAN_H, CAN_L, Common Ground Reference).
   * Impedance matching secured via exactly two 120-Ohm parallel termination resistors (60-Ohm equivalent line load) to prevent echo reflection.
