# Help and guidance for this device

A dashboard and data logger for the **Caterham 420R**, built on a single 7-inch touch screen. The screen is the computer: the same board reads the engine, draws the dashboards and records the data. There is no separate logger or computer in the car.

## What it does

- **Live engine values** from the ECU, on four dashboards chosen from the MENU: STANDARD, RACE, SPORT and ENGINE VALUES. The choice is remembered.
- **Logging:** every value, 10 times a second, to the microSD card. Turn it on with the LOGGING switch on the MENU. LOGS lists the sessions with their dates and sizes, and deletes one.
- **A clock** in UK time, set from the internet when Wi-Fi connects, or by hand in SETUP.
- **Colours:** the button outlines, box outlines and text, tuned in SETUP with a colour dial. RESET returns to the standard colours.
- **Help pages,** these ones, read from the internet when Wi-Fi is connected.

## Values shown on the 420R

| Value | Units |
|---|---|
| Engine speed | RPM |
| Coolant temperature | °C |
| Air temperature | °C |
| Battery | volts |
| Throttle | sensor volts, and the ECU's throttle site |
| Lambda | 1.00 = the ideal mixture |
| Ignition advance | degrees |
| Injection time | milliseconds |

The 420R has no gear sensor, so there is no gear display. Oil pressure isn't shown yet.

## How it reads the engine

- It connects to the car's **CAN bus** through the diagnostic (OBD) port.
- It asks the **MBE 9A4 ECU** for values the same way MBE's Easimap software does: the main values 20 times a second, the rest 5 times a second.
- **It only reads.** It never writes to the ECU or changes the engine's settings.
- If Easimap is connected at the same time, the dash pauses its own requests.
- A value more than a quarter of a second old is blanked rather than shown out of date.

## Good to know

- **DEMO** at the top right means the values come from a simulated engine, for demonstrations. Real values never show DEMO.
- **It is a display, not a safety system.** It has no alarms yet: keep watching the car's own gauges and warning lights.
- **Status (November 2026):** tested on the bench and with recorded 420R data, not yet in a car.
- **Sunlight:** the screen isn't bright enough to read easily in direct sun.
- **Wi-Fi is optional.** Set it up with WI-FI on the MENU and the on-screen keyboard. Without it the dash works normally; only the internet clock, HELP and updates over Wi-Fi need it.
- **Updates** install over USB or Wi-Fi. A new version that fails to start is rolled back automatically.
- **The firmware version** is shown under BUILD on the MENU.
- **Logs on a computer:** the card is FAT32, with one file per session in the `LOGS` folder, such as `S00042_20261117-1805Z.clog`. The project's `clog` tool checks them and converts them to CSV.

## The hardware

| Part | Detail |
|---|---|
| Board | Waveshare ESP32-S3-Touch-LCD-7 |
| Screen | 7-inch IPS, 800 x 480, capacitive touch |
| Processor | ESP32-S3, two cores at 240 MHz, with Wi-Fi |
| Memory | 8 MB PSRAM, 16 MB flash |
| Storage | microSD card |
| Car connection | CAN bus, through the OBD port |

## These help pages

- They come from the public repository **ctrmint/Caterham-CAN-Logger-Display--Help** on GitHub.
- Any markdown file added there appears in this list, titled by its first heading, a few minutes after it is pushed. Press REFRESH to fetch the list again.
- Headings, **bold**, *italic*, `code`, lists, quotes and tables are shown formatted. Pictures and links are shown as text only.

## Credits

- An independent project, not made or endorsed by Caterham Cars or MBE Systems.
- Built with ESP-IDF (Apache-2.0) and LVGL (MIT). The text is set in Barlow Condensed (SIL Open Font License 1.1).
