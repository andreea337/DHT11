# DHT11
IoT sensor data collection and MQTT transmission, using Docker and Node-RED for local data visualization.

# 🚀 IoT Project: Raspberry Pi Zero 2W + MQTT + Node-RED + Docker

A complete IoT system that collects temperature and humidity data from DHT11/DHT22 sensors using Raspberry Pi Zero 2W, transmits data via MQTT, and displays real-time dashboard using Node-RED in Docker containers.

## 📋 Project Overview

### 🎯 Objectives
- **Purpose**: Learn IoT sensor data collection and MQTT transmission with Docker + Node-RED for local data visualization
- **Timeline**: Completed by 2025/07/30
- **Learning Focus**:
  - Python sensor reading and MQTT publishing
  - Node-RED basics and dashboard creation
  - Docker and docker-compose architecture management

### 🏗️ System Architecture

```
┌─────────────────┐    MQTT     ┌──────────────────┐
│ Raspberry Pi    │ ──────────► │ Docker Server    │
│ Zero 2W         │             │                  │
│ ├─ DHT11/22     │             │ ├─ Mosquitto     │
│ ├─ Python       │             │ └─ Node-RED      │
│ └─ MQTT Client  │             │   └─ Dashboard   │
└─────────────────┘             └──────────────────┘
```
![image](https://github.com/andreea337/DHT11/blob/main/generated-svg-image_(3).svg)

## ✨ Features

- **Real-time Data Collection**: DHT11/DHT22 temperature and humidity sensing every minute
- **MQTT Communication**: Reliable data transmission using MQTT protocol
- **Docker Containerization**: Easy deployment and management with Docker Compose
- **Web Dashboard**: Real-time visualization with Node-RED dashboard
- **Data Persistence**: Mosquitto MQTT broker with data persistence

## 🛠️ Hardware Requirements

### Raspberry Pi Zero 2W Setup
- Raspberry Pi Zero 2W
- DHT11 or DHT22 temperature/humidity sensor
- 10kΩ pull-up resistor (if using bare sensor)
- Breadboard and jumper wires

### Wiring Diagram
```
DHT11/DHT22 → Raspberry Pi Zero 2W
VCC         → 3.3V (Pin 1)
GND         → Ground (Pin 6)  
DATA        → GPIO 4 (Pin 7)
```

**Note**: If using a breakout board, the pull-up resistor is already included.

## 📦 Software Requirements

### Docker Server
- Ubuntu Server (or similar Linux distribution)
- Docker and Docker Compose
- Network connectivity to Raspberry Pi

### Raspberry Pi
- Raspberry Pi OS
- Python 3
- Required Python packages (see installation section)

## 🚀 Installation & Setup

### 1. Raspberry Pi Setup

#### Hardware Connection
Connect the DHT sensor to your Raspberry Pi according to the wiring diagram above.

#### Software Installation
```bash
# Update system
sudo apt update

# Install Python packages
pip3 install adafruit-circuitpython-dht paho-mqtt

# Enable SSH (if needed)
sudo systemctl enable ssh
sudo systemctl start ssh
```

#### Create MQTT Publisher Script
Create `mqtt_publisher.py`:

### 2. Docker Server Setup

#### Create Directory Structure
```bash
# Create mosquitto directories
sudo mkdir -p /mosquitto/config
sudo mkdir -p /mosquitto/data
sudo mkdir -p /mosquitto/log

# Create project directory
mkdir -p ~/docker-configs/mqtt5
cd ~/docker-configs/mqtt5
```

#### Create Mosquitto Configuration
Create `/mosquitto/config/mosquitto.conf`:

#### Create Docker Compose File
Create `docker-compose.yml`:

#### Start Services
```bash
# Start containers
sudo docker-compose up -d

# Check status
sudo docker-compose ps

# View logs
sudo docker-compose logs
```

### 3. Node-RED Dashboard Setup

#### Access Node-RED
Open your browser and navigate to `http://your-docker-host:1880`

#### Import Dashboard Flow
1. Install dashboard: Menu → Manage palette → Install → node-red-dashboard
2. Import the NodeRed.json and then "Deploy"

#### Access Dashboard
Navigate to `http://your-docker-host:1880/ui` to view the live dashboard.

## 🔧 Usage
![image](https://github.com/andreea337/DHT11/blob/main/result.png)

### Starting the System
1. Start Docker containers on your server:
   ```bash
   sudo docker-compose up -d
   ```

2. Run the MQTT publisher on Raspberry Pi:
   ```bash
   python3 mqtt_publisher.py
   ```

3. Access the dashboard at `http://your-docker-host:1880/ui`

### Testing MQTT Communication
```bash
# Subscribe to MQTT topic to test data flow
mosquitto_sub -h localhost -t sensor/dht
```

### Stopping the System
```bash
# Stop Docker containers
sudo docker-compose down

# Stop Python script on Raspberry Pi
Ctrl+C
```

## 🛠️ Troubleshooting

### Common Issues

**1. DHT Sensor Reading Errors**
- Check wiring connections
- Chek whether your DHT11 is on breakout board or not

**2. MQTT Connection Issues**
- Verify IP addresses in configuration
- Check network connectivity between Pi and Docker host
- Ensure MQTT broker is running: `sudo docker-compose ps`

**3. Node-RED Dashboard Not Loading**
- Restart the container

**4. Docker Volume Issues**
- Use `--remove-orphans` flag: `sudo docker-compose down --remove-orphans`
- Check volume permissions for mosquitto directories

## 📚 Resources

- [DHT11/DHT22 Raspberry Pi Tutorial](https://randomnerdtutorials.com/raspberry-pi-dht11-dht22-python/)
- [Docker Installation Guide](https://docs.docker.com/engine/install/ubuntu/)
- [Node-RED Documentation](https://nodered.org/docs/)
- [Eclipse Mosquitto Documentation](https://mosquitto.org/documentation/)
- [MQTT Broker on Raspberry Pi Zero 2 W — YouTube](https://www.youtube.com/watch?v=k_GAuSONCqo) — 教學影片，示範如何在 Pi Zero 2 W 上安裝與設定 MQTT Broker（Mosquitto）
- [RPI Zero 2W GPIO pinout](https://yhhuang1966.blogspot.com/2021/01/gpio.html)
- [DHT11 Temperature and Humidity Sensor - Raspberry Pi](https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/)
- [GPIO 相關資源](https://yhhuang1966.blogspot.com/2021/01/gpio.html)
- [MQTT Mosquitto Docker 設定教學](https://weirenxue.github.io/2021/07/01/mqtt_mosquitto_docker/)
- [Setup Mosquitto with Docker - GitHub](https://github.com/sukesh-ak/setup-mosquitto-with-docker)

## 📝 Project Timeline

- **2025/07/13**: Hardware setup and DHT sensor testing
- **2025/07/14**: Docker installation and SSH configuration  
- **2025/07/15**: MQTT publisher implementation and testing
- **2025/07/17**: Docker Compose setup with Node-RED integration
- **2025/07/18**: Dashboard completion and documentation

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available under the MIT License.