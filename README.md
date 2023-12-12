# Cache 4 Trash

### Dataset Usage

### Data Augmentation

### Model Training

### Model Deployment and Hardware Setup

To deploy our already-trained model to Arduino Nicla Vision, first clone this repository, then simply connect the Nicla to the computer and open OpenMV IDE. Open the 

`./cache-4-trash/cache4trash/final_nicla_cache4trash.py` 

script from the cache-4-trash repository. 

Within OpenMV IDE, go to -> Tools -> Run Bootloader (Load Firmware) to load our firmware into the Nicla. select the pathway on your local computer that leads to

`./cache-4-trash/open_mv_firmware/edge_impulse_firmware_arduino_nicla_vision.bin`. 

Select "Erase internal file system" and click "Run". 

After the light flashes and the upload is completed, press the green start button, and the feedback loop should start working. Use the Nicla to capture images of common objects and in the Serial terminal, the probability of whether that item is recyclable or not recyclable will be printed.


For the full hardware setup, please see the circuit diagram below. 
![Full circuit diagram of the hardware setup](https://github.com/AditiR-42/cache-4-trash/diagrams/circuit.png)

### Running Cache 4 Trash

Following model deployment through firmware installation and OpenMV IDE, click the green button while Nicla is connected to your machine and you are currently on the 

`./cache-4-trash/cache4trash/final_nicla_cache4trash.py` script. This should start the inference feedback loop. Please open the Serial monitor to see the inference results of past snapshots. 
