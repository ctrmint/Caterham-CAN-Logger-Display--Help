# Connecting, Device to Caterham

How to wire the dash to the 420R's OBD-II diagnostic port, and how to test it in the car, one stage at a time.

## What the connection does

- **For the first tests, three wires** come from the OBD-II port: ground, CAN-H and CAN-L.
- **Power:** the board runs on **5 V only**, through its USB-C port.
  - For the first tests it runs from a **USB power bank**, not the car: power from the car waits until a 12 V to 5 V supply has been tested.
  - Later, the car's 12 V will go through a fused converter with a USB-C output.
- **Data:** CAN-H and CAN-L go to the board's 2-pin CAN connector, at 500 kbit/s.
  - **It only listens at first.**
  - Once the stages below have passed, it reads the ECU by sending **read requests**, the way Easimap does.
  - **It never writes to the ECU** or changes its settings.
- On the 420R the ECU is the only device on this CAN bus: the standard dash isn't on it.

## What you need

| Item | Notes |
|---|---|
| OBD-II (J1962) plug with flying leads | Or an OBD-II breakout board or cable |
| USB-C power bank | For the first tests. One that keeps supplying about 0.5 A at 5 V |
| HY2.0 2-pin lead | One comes with the board, for its CAN connector |
| Twisted pair wire | For CAN-H and CAN-L, a metre or less |
| A ground wire | The board's CAN connector has no ground pin |
| Multimeter | For the checks in step 1 |
| Phone hotspot and a laptop | Once CAN is on, the dash is reached over Wi-Fi: settings between stages, and records |
| Easimap and its interface | The reference for stages 1, 4 and 7 |
| Later: 12 V to 5 V converter, USB-C output | At least 2 A, once tested. With an inline fuse holder and a 1 A fuse on the +12 V wire, close to the OBD plug |

## The OBD-II port

The port is under the dash, near the ignition switch. Reports on the 420R say it carries just four signals: 12 V, ground, CAN-H and CAN-L. The pin numbers below are the **standard OBD-II positions**; they haven't been confirmed on this car, so check them with the meter in step 1 before connecting anything. Most connectors have the numbers moulded beside the pins.

| OBD pin | Signal | Goes to |
|---|---|---|
| 16 | +12 V | **Nothing for the first tests.** Later: the 1 A fuse, then the converter's + input |
| 4 or 5 | Ground | The board's GND (later the converter's - input too) |
| 6 | CAN-H | The board's CAN connector, **pin 2 (CAN-H)** |
| 14 | CAN-L | The board's CAN connector, **pin 1 (CAN-L)** |

Pin 4 is chassis ground and pin 5 signal ground; use whichever is fitted. If both are, use pin 5 for the board's GND.

## Step 1: Check the port with a meter

Do this with **nothing plugged in**. If you use an OBD breakout board with its own terminator switch, switch it off while you measure, or it adds to the readings.

1. **Is the 12 V permanent?** With the ignition **off**, measure between pin 16 and ground. This matters once the dash takes its power from the car.
   - **About 12 V:** the port is permanently live. Powered from it, the dash would stay on with the car parked and flatten the battery: about 0.2 A at 12 V, or about 5 Ah a day.
   - **0 V:** the port is switched with the ignition, which is what you want.
2. **How is the bus terminated?** With the ignition **off**, measure the **resistance** between pin 6 and pin 14.

| Reading | What it means | Board jumper J5 |
|---|---|---|
| About 60 ohms | The bus already has a terminator at each end | Make sure the board's resistor is **off** (J5 on NC) |
| About 120 ohms | One terminator, probably in the ECU | Turn the board's resistor **on** (J5 on 120R): the dash becomes the bus's second end |
| Far above 120 ohms, or open | No terminator found | **Stop.** Recheck the pins before going further |

3. **Are the CAN pins right?** With the ignition **on** and the engine off, measure the **voltage** from pin 6 to ground and from pin 14 to ground. Each should read between about 2 and 3 V, CAN-H a little higher than CAN-L. **If either reads near 12 V or 0 V, stop:** that's the wrong pin.

## Step 2: Set the termination jumper

- The CAN termination jumper (**J5**) is a three-pin header marked **CAN 120R NC**, beside the battery LEDs. The RS485 port has one that looks the same beside it: make sure you use the CAN one.
- Its cap joins the middle pin to one side, as marked:
  - **120R:** a 120 ohm resistor is connected across CAN-H and CAN-L;
  - **NC**, or with the cap removed: it's out.
- **Check which side yours is on.** Waveshare's documentation says the board is delivered on 120R, but the project's board arrived on NC.
- Set it as the table in step 1 says.
- **Then check it with the meter.** With the board unpowered and connected to nothing else, measure across the two pins of its CAN connector:
  - **about 120 ohms:** the resistor is on;
  - **open:** it's off.
  - A breakout board or adapter on the same wires with its own terminator adds to the reading, so disconnect it first.
- **Count every terminator on the bus,** including one on an OBD breakout board if you wire the dash through it.
- A CAN bus needs exactly two terminators, one at each end. Never three.

## Step 3: Make the leads

- **CAN:**
  - Twist CAN-H and CAN-L together, about one twist every 2 to 3 cm, and keep the run short: a metre or less.
  - On the HY2.0 lead, **pin 2 is CAN-H and pin 1 is CAN-L**. Wire colours vary between leads, so check which wire goes to which pin with the meter.
  - OBD pin 6 goes to CAN-H, and pin 14 to CAN-L.
- **Ground:** run a wire from OBD pin 5 (or 4) to a **GND pin on one of the board's expansion headers** (the UART or I2C header), alongside the CAN pair.
  - The CAN connector has no ground pin, and the CAN signals need the board and the ECU to share a ground.
  - **On a power bank, this wire is the board's only connection to the car's ground,** so it's essential.
- **Power, for the first tests:** the power bank to the board's USB-C port. Nothing from pin 16.
- **Finishing:** insulate every joint, and secure the leads so they can't reach the pedals, the steering column or anything hot.

## Step 4: Get the dash ready (on the bench)

Once CAN is on, the board's USB data lines carry CAN instead, so **the USB console stops working**. The CAN switch is on **SETUP > CAN** in firmware **0.4 or later**: check BUILD on the MENU, and update first if it's older.

1. **Set up the Wi-Fi console,** so the laptop can reach the dash once CAN is on: settings between stages, and records.
   - Wi-Fi with **WI-FI** on the MENU, on the phone's hotspot;
   - the console secret over USB (`netsecret`).
2. **Listen only, to start:** send `can source stream` and `can ack off` over USB.
   - SETUP > CAN should show SOURCE as **BROADCAST - LISTEN-ONLY**.
   - In this mode the dash sends nothing at all.
3. **Leave CAN off** until you're at the car.

## Step 5: Test in the car, one stage at a time

Do the stages **in order**, parked, and don't skip one: each checks something the next relies on.

### Rules for every stage

- **Only with the ignition off:**
  - switch CAN on or off;
  - plug or unplug the dash, or restart it;
  - change its settings.
- **Keep SETUP > CAN open.** Its message list shows frames only while it is showing:
  - **RX** frames come from the bus;
  - **TX** frames are the dash's own.
- **Changing settings between stages:** over the Wi-Fi console from the laptop, or over USB after turning CAN off.
- **Keep a record of each stage:** a screenshot of SETUP > CAN, the `can` line, and Easimap's log if it was used. It's your car's data, so keep it private.
- **To stop:** turn CAN off on SETUP > CAN, or unplug the CAN lead. The dash runs from the power bank, so unplugging disconnects it completely.

### The stages

| Stage | What to do | What you should see |
|---|---|---|
| 1. Listen only | Ignition off: plug in, then turn CAN on (SETUP > CAN). Ignition on, engine off. Then again with Easimap connected through the breakout | **SEARCHING · LISTEN**, then BUS SPEED 500 KBIT/S, the same as Easimap uses. **No TX in the list, ever.** Without Easimap, nothing acknowledges the ECU's frames: it may resend one frame (WAITING · LISTEN) and the bus errors may count, which is expected here. With Easimap connected: **LIVE · LISTEN**, values matching Easimap's, and the bus errors stop rising |
| 2. Acknowledge | Ignition off: `can ack on`. Ignition on, without Easimap | **LIVE · ACK**: the dash now acknowledges the ECU's frames, so the broadcast flows. Still no TX. The bus errors stop rising |
| 3. Read requests | Ignition off: `can source poll`. Ignition on, engine off, without Easimap | The bus speed found again **before any TX**. Then **LIVE · POLL**, about 30 replies a second. TX only on **0CBE1101**, each followed by an RX reply. Battery, coolant and air temperature plausible; the throttle follows the pedal. Nothing changes in the car |
| 4. With Easimap | Start Easimap reading the ECU while the dash polls | **PAUSED**, and the TX stop. Easimap works normally. When Easimap stops, the dash carries on about 3 s later |
| 5. Ignition off | While polling, turn the ignition off | The TX stop after 20 unanswered requests, and it goes back to **SEARCHING · LISTEN**. The bus errors rise until then. Ignition on: it finds the bus speed, then polls again |
| 6. Restart | Ignition off: restart the dash (unplug the power bank and plug it back in, or `reboot` over Wi-Fi). Ignition on | The bus speed found before polling, as in stage 3 |
| 7. Engine running | Parked, in neutral, outdoors | The values, lambda included, compared with Easimap's one after the other: the dash pauses while Easimap reads. Then the same with LOGGING on, and the log read on a computer |

### Stop at once if

- **an unexpected TX:** any TX in stage 1 or 2, a TX on any ID other than 0CBE1101, or a TX before the bus speed is found;
- **errors:** dropped frames, or bus errors still rising while something acknowledges the ECU's frames (Easimap's interface in stage 1, the dash from stage 2 on). Stage 5 is the exception, while the ignition is off;
- **the car or Easimap behaves differently:** Easimap reports a communication error, a warning lamp comes on, or the engine behaves differently;
- **values:** one doesn't match Easimap's.

Turn CAN off or unplug the lead, then go back to the previous stage.

After stage 7 the dash stays on read requests, the default. Road and track tests come later.

## What the top row shows

| Shows | Meaning |
|---|---|
| SEARCHING · LISTEN | Checking the bus speed, listen-only. Normal with the ignition off |
| WAITING · LISTEN or · ACK | Listening to the broadcast: the bus speed is found, but the broadcast isn't recognised yet |
| LIVE · LISTEN | Reading the ECU's broadcast without acknowledging it (stage 1) |
| LIVE · ACK | Reading the broadcast and acknowledging it (stage 2) |
| DATA LOST | The broadcast was found, then stopped |
| WAITING · POLL | Bus speed found and read requests sent, but no replies yet |
| LIVE · POLL | Reading the ECU with read requests (stage 3 on) |
| PAUSED | Another tool, such as Easimap, is reading the ECU. The dash waits |
| STARTING | New firmware: CAN starts once it confirms itself, about 20 s after an update |
| SERVICE BOOT | The screen was touched in the first 3 s after power-up: USB is kept, and CAN stays off until the next start |
| CAN OFF | CAN is switched off (on SETUP > CAN, or with `can off`) |
| DEMO | The simulated engine. It stops by itself when CAN is on, unless it was forced on with `dash demo on`; `dash demo auto` sets it back |

## If something's wrong

- **SEARCHING with the ignition on:** the dash sees no traffic. Check that CAN-H and CAN-L aren't swapped, the ground wire, and the pins.
- **WAITING · LISTEN in stage 1 without Easimap:** expected, because nothing acknowledges the ECU. Connect Easimap, or go on to stage 2.
- **WAITING · POLL for more than a few seconds:** the ECU isn't answering. Check the termination (step 1 and step 2), and that CAN-H and CAN-L aren't swapped. After 20 unanswered requests the dash goes back to listening.
- **Values look wrong:** note what the dash and Easimap each show, and report it.
- **To get USB back:**
  - turn CAN off on **SETUP > CAN**, or send `can off` over the Wi-Fi console: USB returns in about 1 s;
  - or touch the screen within 3 s of power-up. That gives a SERVICE BOOT, for that start only.

## Safety

- **The dash only reads:**
  - in stage 1 it sends nothing at all;
  - in stage 2 only the acknowledge bit of the ECU's frames;
  - from stage 3, ECU read requests as well.
  - It never writes ECU memory or calibration, and it stops while another tool reads the ECU.
- **It is a display, not a safety system.** It has no alarms yet: keep watching the car's own gauges and warning lights.
- **With the ignition off only:** make and break connections, switch CAN, and restart the dash.
- **Route the wiring** away from the pedals, the steering column and hot parts.

## Powering the dash from the car (later)

Once a 12 V to 5 V supply has been tested:
- **Wiring:** OBD pin 16, then the **1 A fuse** close to the plug, then the converter's + input. The converter's - input goes to OBD pin 4 (or 5), and its USB-C output to the board. The ground wire and the CAN pair stay as they are.
- **If pin 16 is permanently live** (step 1) and you want to leave the dash fitted: feed the converter from an ignition-switched 12 V circuit instead, still through a fuse.
- **Logging:** turn LOGGING off before switching off. A session cut short by a power loss can usually be recovered on a computer (`clog to-csv --recover`), but cutting power while recording hasn't been tested on the hardware yet.
