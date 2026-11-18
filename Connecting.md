# Connecting, Device to Caterham

How to wire the dash to the 420R's OBD-II diagnostic port: power, ground and the CAN bus.

## What the connection does

- **Four wires** come from the OBD-II port: +12 V, ground, CAN-H and CAN-L.
- **Power:** the board runs on **5 V only**, through its USB-C port. The car's 12 V goes through a fused 12 V to 5 V converter with a USB-C output.
- **Data:** CAN-H and CAN-L go to the board's 2-pin CAN connector. The dash reads the ECU at 500 kbit/s by sending **read requests**, the way Easimap does. **It never writes to the ECU** or changes its settings.
- On the 420R the ECU is the only device on this CAN bus: the standard dash isn't on it.

## What you need

| Item | Notes |
|---|---|
| OBD-II (J1962) plug with flying leads | Or an OBD-II breakout cable |
| 12 V to 5 V converter, USB-C output | At least 2 A. The dash takes about 0.5 A at 5 V |
| Inline fuse holder and a 1 A fuse | On the +12 V wire, close to the OBD plug |
| HY2.0 2-pin lead | One comes with the board, for its CAN connector |
| Twisted pair wire | For CAN-H and CAN-L, a metre or less |
| A ground wire | The board's CAN connector has no ground pin |
| Multimeter | For the checks in step 1 |
| Phone hotspot | Once CAN is on, the dash is serviced over Wi-Fi (step 4) |

## The OBD-II port

The port is under the dash, near the ignition switch. Reports on the 420R say it carries just four signals: 12 V, ground, CAN-H and CAN-L. The pin numbers below are the **standard OBD-II positions**; they haven't been confirmed on this car, so check them with the meter in step 1 before connecting anything. Most connectors have the numbers moulded beside the pins.

| OBD pin | Signal | Goes to |
|---|---|---|
| 16 | +12 V | The 1 A fuse, then the converter's + input |
| 4 or 5 | Ground | The converter's - input, and the board's GND |
| 6 | CAN-H | The board's CAN connector, **pin 2 (CAN-H)** |
| 14 | CAN-L | The board's CAN connector, **pin 1 (CAN-L)** |

Pin 4 is chassis ground and pin 5 signal ground; use whichever is fitted. If both are, use pin 5 for the board's GND.

## Step 1: Check the port with a meter

Do this with **nothing plugged in**.

1. **Is the 12 V permanent?** With the ignition **off**, measure between pin 16 and ground.
   - **About 12 V:** the port is permanently live. The dash would stay on with the car parked and flatten the battery: about 0.2 A at 12 V, or about 5 Ah a day. Unplug it after each drive, or power it from an ignition-switched circuit (see the end of this page).
   - **0 V:** the port is switched with the ignition, which is what you want.
2. **How is the bus terminated?** With the ignition **off**, measure the **resistance** between pin 6 and pin 14.

| Reading | What it means | Board jumper J5 |
|---|---|---|
| About 60 ohms | The bus already has a terminator at each end | Leave J5 **out** |
| About 120 ohms | One terminator, probably in the ECU | Fit J5 on **COM-B**: the dash becomes the bus's second end |
| Far above 120 ohms, or open | No terminator found | **Stop.** Recheck the pins before going further |

3. **Are the CAN pins right?** With the ignition **on** and the engine off, measure the **voltage** from pin 6 to ground and from pin 14 to ground. Each should read between about 2 and 3 V, CAN-H a little higher than CAN-L. **If either reads near 12 V or 0 V, stop:** that's the wrong pin.

## Step 2: Set the termination jumper

- Jumper **J5** on the board puts a 120 ohm resistor across CAN-H and CAN-L when it's on **COM-B**. In its other position, or removed, the resistor is out.
- Set it as the table in step 1 says.
- **Check it:** with the board unpowered, measure across the two pins of its CAN connector. It should read about 120 ohms with J5 on COM-B, and open without.
- A CAN bus needs exactly two terminators, one at each end. Never three.

## Step 3: Make the leads

- **CAN:**
  - Twist CAN-H and CAN-L together, about one twist every 2 to 3 cm, and keep the run short: a metre or less.
  - On the HY2.0 lead, **pin 2 is CAN-H and pin 1 is CAN-L**. Wire colours vary between leads, so check which wire goes to which pin with the meter.
  - OBD pin 6 goes to CAN-H, and pin 14 to CAN-L.
- **Ground:** run a wire from OBD pin 5 (or 4) to a **GND pin on one of the board's expansion headers** (the UART or I2C header), alongside the CAN pair.
  - The CAN connector has no ground pin, and the CAN signals need the board and the ECU to share a ground.
  - Fit it even if the converter already shares the car's ground: it gives the CAN signals a short, direct reference.
- **Power:** OBD pin 16, then the **1 A fuse** close to the plug, then the converter's + input. The converter's - input goes to OBD pin 4 (or 5), and its USB-C output to the board.
- **Finishing:** insulate every joint, and secure the leads so they can't reach the pedals, the steering column or anything hot.

## Step 4: Get the dash ready (on the bench)

Once CAN is on, the board's USB data lines carry CAN instead, so **the USB console stops working**. Set up the way back in first:

1. **Wi-Fi:** set it up with **WI-FI** on the MENU, on a network the car will have, such as your phone's hotspot.
2. **The console secret:** set it over USB (`netsecret`). The Wi-Fi console needs it.
3. **Switch CAN on:** send `can on` over USB. It refuses until the Wi-Fi console is set up. USB disconnects at once: that's expected. The setting is remembered.
4. **Leave the source on polling** (`can source poll`, the default).

## Step 5: The first connection

1. **Ignition off.** Plug the lead into the OBD port. If the port is permanently live, the dash starts and shows **SEARCHING · LISTEN**. It is only listening: it sends nothing on a silent bus.
2. **Ignition on, engine off.** Within a few seconds the top row should show **LIVE · POLL**. On the MENU the data source reads POLLING - 500 KBIT/S, with the number of replies a second.
3. **Check the values:**
   - battery close to the car's voltage;
   - coolant and air temperature close to the air temperature on a cold engine;
   - the throttle moves with the pedal.
4. **Start the engine,** parked, in neutral, outdoors. The RPM should match the car's rev counter.
5. **If you have Easimap,** connect it as well. The dash shows **PAUSED** while Easimap reads the ECU, and carries on about 3 s after Easimap stops. Compare the two.

## What the top row shows

| Shows | Meaning |
|---|---|
| SEARCHING · LISTEN | Checking the bus speed, listen-only. Normal with the ignition off |
| WAITING · POLL | Bus speed found and read requests sent, but no replies yet |
| LIVE · POLL | Reading the ECU |
| PAUSED | Another tool, such as Easimap, is reading the ECU. The dash waits |
| STARTING | New firmware: CAN starts once it confirms itself, about 20 s after an update |
| SERVICE BOOT | The screen was touched in the first 3 s after power-up: USB is kept, and CAN stays off until the next start |
| CAN OFF | CAN is switched off (`can off`) |
| DEMO | The simulated engine. It stops by itself when CAN is on, unless it was forced on with `dash demo on`; `dash demo auto` sets it back |

## If something's wrong

- **SEARCHING with the ignition on:** the dash sees no traffic. Check that CAN-H and CAN-L aren't swapped, the ground wire, and the pins.
- **WAITING for more than a few seconds:** the ECU isn't answering. Check the termination (step 1 and step 2), and that CAN-H and CAN-L aren't swapped. After 20 unanswered requests the dash goes back to listening.
- **Values look wrong:** note what the dash and Easimap each show, and report it.
- **To get USB back:**
  - send `can off` over the Wi-Fi console: USB returns in about 1 s;
  - or touch the screen within 3 s of power-up. That gives a SERVICE BOOT, for that start only.

## Safety

- **The dash only reads.** It sends only ECU read requests, never writes ECU memory or calibration, and stops while another tool reads the ECU.
- **It is a display, not a safety system.** It has no alarms yet: keep watching the car's own gauges and warning lights.
- **Make and break connections with the ignition off.**
- **Fuse the 12 V feed,** close to where it's taken from.
- **Route the wiring** away from the pedals, the steering column and hot parts.

## Powering from an ignition-switched circuit (optional)

- **When to use it:** if pin 16 is permanently live and you want to leave the dash fitted.
- **How:** feed the converter from an ignition-switched 12 V circuit instead, still through a fuse. The CAN pair and the ground wire still go to the OBD port.
- **Logging:** turn LOGGING off before switching off. A session cut short by a power loss can usually be recovered on a computer (`clog to-csv --recover`), but cutting power while recording hasn't been tested on the hardware yet.
