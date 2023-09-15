# Guide: Setting up Raspberry Pi with SSH, Multiple Wi-Fi Networks, and Boot Service

## Step 1: Setting up the Raspberry Pi

1. **Get the Required Hardware:**
   - Raspberry Pi board (e.g., Raspberry Pi 4)
   - MicroSD card (at least 16GB)
   - Power supply

2. **Download Raspberry Pi OS:**
   - Visit the [Raspberry Pi Foundation's website](https://www.raspberrypi.org/software/) and download the latest version of Raspberry Pi OS.

3. **Flash the OS to MicroSD Card:**
   - Use a tool like [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to flash the OS image to your MicroSD card.

4. **Enable SSH During OS Flashing:**
   - In Raspberry Pi Imager, select your OS image and SD card.
   - Click on "Change" in the "Raspberry Pi Configuration" section.
   - In the "Advanced Options," check the box for "SSH" to enable SSH during the OS installation.
   - Click "Write" to flash the OS with SSH enabled.

5. **Insert the MicroSD Card:**
   - Insert the MicroSD card into your Raspberry Pi.

6. **Boot and Connect:**
   - Connect the power supply to your Raspberry Pi to boot it up.

## Step 2: Connecting to Raspberry Pi via SSH

1. **Find the Raspberry Pi's IP Address:**
   - You can use your router's admin interface or a network scanning tool like [Advanced IP Scanner](https://www.advanced-ip-scanner.com/) to find the Raspberry Pi's IP address on your local network.

2. **Connect via SSH:**
   - Use an SSH client (e.g., PuTTY on Windows, Terminal on macOS and Linux) to connect to your Raspberry Pi using its IP address:
     ```bash
     ssh pi@your_pi_ip_address
     ```
     (Replace `your_pi_ip_address` with the actual IP address of your Raspberry Pi.)

3. **Log In:**
   - Log in with the default username and password:
     - Username: `pi`
     - Password: `raspberry` (You should change this password for security.)

## Step 3: Enabling VNC (Virtual Network Computing)

1. **Enable VNC:**
   - While connected via SSH, run the following command to enable VNC:
     ```bash
     sudo raspi-config
     ```
   - Navigate to "Interfacing Options" > "VNC" and enable VNC.

2. **Connect via VNC:**
   - Use a VNC client like Real VNC Viewer on another computer to connect to your Raspberry Pi using its IP address and the VNC password you set during configuration.

## Step 4: Updating wpa_supplicant.conf for Multiple Wi-Fi Networks

1. **Connect via VNC Viewer**
   - Use VNC Viewer to connect to your Raspberry Pi via its IP address. 

2. **Edit wpa_supplicant.conf:**
   - Use a text editor like Nano to edit the `wpa_supplicant.conf` file:
     ```bash
     sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
     ```

3. **Add Network Information:**
   - Add network configurations for each Wi-Fi network you want to connect to:
     ```plaintext
     network={
         ssid="Your_SSID_1"
         psk="Your_Password_1"
     }
     network={
         ssid="Your_SSID_2"
         psk="Your_Password_
     }
     ```

4. **Save and Exit:**
   - Save your changes and exit Nano (Ctrl+O, Enter, Ctrl+X).

## Step 5: Copy the send_data.py and run_scripts.sh file in the home directory

## Step 6: Creating a Service on Boot

1. **Create a Service Script:**
   - Create a script (e.g., `myservice.sh`) for your desired service and save it in a directory of your choice.

2. **Make the Script Executable:**
   - Make the script executable:
     ```bash
     chmod +x /path/to/myservice.sh
     ```

3. **Create a systemd Service Unit:**
   - Copy the ```data_service.service``` file

4. **Enable and Start the Service:**
   - Enable and start your service:
     ```bash
     sudo systemctl enable myservice.service
     sudo systemctl start myservice.service
     ```

Now, your Raspberry Pi should be set up with SSH for the initial configuration, configured to connect to multiple Wi-Fi networks, and running your custom service on boot.

Please replace "Your_SSID_1," "Your_Password_1," and "Your_SSID_2," "Your_Password_2" with your actual Wi-Fi network names and passwords, and replace "/path/to/myservice.sh" with the actual path to your custom service script.