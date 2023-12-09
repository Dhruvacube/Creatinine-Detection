# Creatinine Detection Kit

This repository contains the circuits diagrams and codes for the creatinine detection kit.

#### File structure

* *arduinocode*: It contains the codewhcih is to be uploaded to the ESP32 via the [Arduino IDE](https://www.arduino.cc/en/software "Arduino IDE download link")
* *Circuit Diagram and BOM*: It contains the schematic files for the kit and its BOM (Bill of Materials)
* *pythoncode*: It contains the python files for the ``Creatinine Detection.exe``

#### Usage

* First download these [CP210x](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers "CP210x USB to UART Bridge VCP Drivers") and [FTDI](https://ftdichip.com/drivers/vcp-drivers/ "FTDI Virtual COM Port Drivers")
* Then check how the check the ``device COM port`` from [here](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html#check-port-on-windows "Check Port on Windows")
* Then run ``Creatinine Detection.exe`` it would ask for the COM port, enter it viola, the data is being shown

**Note**: Its patent has also been publish under the id ``202311075715``
