# Rotary-Encoder
This project uses a Raspberry Pi Pico W board to control a rotary encoder with 2 outputs and 1 switch, and then sends data to a broker using an MQTT connection.
## Hardware Requirements
+ Raspberry Pi Pico W board
+ Rotary encoder with 2 outputs and 1 switch
+ Breadboard and jumper wires
+ Micro USB cable
+ Computer with a USB port
## Software Requirements
+ Thonny
+ Raspberry Pi Pico Python SDK
+ Umqtt-client library
## Installation
1. Install the Raspberry Pi Pico Python SDK by following the instructions in the official [documentation](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf).
2. Install the Umqtt-client library on pico w.
3. Connect the rotary encoder to the Raspberry Pi Pico W board.
4. Clone this repository to your computer.
 ```
git clone https://github.com/phuong-ta/Rotary-Encoder.git
```
5. Open the project in Thonny and modify the main.py file according to your MQTT broker configuration.
6. Run the main.py script using the following command:
```
python main.py
```
## Usage
1. Turn the rotary encoder to generate events, and press the switch to toggle between the two output modes. The firmware will publish the events to the MQTT broker according to the configuration in the main.py file.
2. Use an MQTT client to subscribe to the topics published by the firmware and process the data as desired.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
