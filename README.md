# Cache 4 Trash

### Dataset Usage

### Data Augmentation

### Model Training

### Hardware Setup

To deploy our already-trained model to Arduino Nicla Vision, first clone this repository, then simply connect the Nicla to the computer and open OpenMV IDE. Open the `final_nicla_cache4trash.py` script from the cache-4-trash repository. 

Within OpenMV IDE, go to -> Tools -> Run Bootloader (Load Firmware) to load our firmware into the Nicla. select the pathway on your local computer that leads to `./cache-4-trash/open_mv_firmware/edge_impulse_firmware_arduino_nicla_vision.bin`. Select "Erase internal file system" and click "Run". 

After the light flashes and the upload is completed, press the green start button, and the feedback loop should start working. Use the Nicla to capture images of common objects and in the Serial terminal, the probability of whether that item is recyclable or not recyclable will be printed.

### Model Deployment

### Running Cache 4 Trash
