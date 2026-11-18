# Setting the throttle stop on a Caterham 420 / 420R

*Duratec 2.0, MBE 9A4 ECU, read with a data logger. Compiled 18 November 2026.*

> **Read this first.** This guide is a synthesis of owner write-ups and club forum threads (listed at the end). It is **not** Caterham documentation. The voltages quoted by different owners disagree with each other by a wide margin, so treat every number here as a starting point and your own car's readings as the truth. If the car is under warranty, the dealer or Caterham can do this adjustment for you, and forum posters often suggest that route.

---

## 1. What the throttle stop does

- The standard 420R setup has no separate idle air control. Forum threads describe the car as relying on the mechanical **throttle stop** (an idle screw with a locking nut) to decide how far the throttles rest open at idle. The cable should hold no tension at idle, so the spring pulls the throttle back onto the stop.
- The ECU reads the throttle position sensor (TPS) and turns it into a **Throttle Site** value. The TPS reading *at the stop* is the idle reference for the map.
- The TPS itself has little or no adjustment on the standard Duratec throttle body, so the stop is where nearly all the adjusting is done.
- The adjustments are tiny. One forum poster says about 0.05 mm of butterfly movement makes a big difference to idle, and that half a degree of TPS rotation is only about 0.02 V.
- The ECU is **permanently powered**, so it does not notice a new stop position until you cut its power (step 7).

## 2. Symptoms that point to the stop

- Stalls at traffic lights or junctions, or fires after a restart but won't hold idle without blipping.
- Won't idle from cold, or stalls once warm.
- Hunting: for example 950 to 1300 rpm when hot, or a slow "breathing" swing between 1000 and 1500 rpm.
- A high idle that won't come down (1800 to 2000 rpm).
- Sometimes part-throttle hesitation or "kangarooing", because the TPS and stop relationship feeds the map.

## 3. Rule out other causes first

| Check | Why |
|---|---|
| **Cable slack.** The throttle quadrant must be resting on the stop at idle, hot or cold. | A cable that is too tight holds the throttles open or moves the effective idle. Adjusting the cable adjuster can mask a stop that has actually moved. |
| **Stop screw and locking nut tightness.** | The screw can back out and the nut can come loose. Some owners put a little blue threadlock on it after setting. |
| **Lambda (O2) sensor.** Check it is not blocked or failing. | One owner found tape over the back of the sensor, which can block its reference air. Another cured a hot-idle hunt by replacing the sensor. The ECU goes closed-loop at around 60 °C coolant, so hunting that only appears hot is worth checking here. |
| **Coolant temperature sensor.** | Reported as a first thing to check on a 420R that won't idle cold. |
| **TPS condition.** | Several owners cured part-throttle problems or drifting readings by replacing the TPS with a genuine part. Non-genuine sensors are reported as troublesome. |
| **Throttle body balance** (synchrometer). | A badly balanced set affects idle. Balance is separate from the stop. |
| **Injectors and vacuum leaks.** | One US 420R kit that wouldn't idle was fixed by swapping the injectors to the type the tune expects. |

## 4. Tools

- **A data logger that reads the ECU's throttle channels.** Strongly recommended. Several people say this job is difficult to do properly without seeing TPS and lambda values live. As a minimum you need Throttle Site 1 and the TPS voltage (the source write-ups call that channel "Throttle Angle Increasing"; your logger may label it differently). One owner warned that moving the stop without a logger made the fault harder to diagnose.
- Screwdriver (or the key your stop screw takes) to turn the screw, and a small spanner or socket for the locking nut.
- Feeler gauges (for the static test in step 4).
- Marker or paint pen to mark the starting position.
- A spanner for the battery terminal, or use the master switch if you have one.
- A voltmeter, if you have no data logger (see section 6 for the caveat).
- Optional: blue threadlock.

## 5. Targets

| Reading | Target | Notes |
|---|---|---|
| **Throttle Site 1 at idle** | **0.0**, with the slightest throttle lifting it just above 0. At worst, below 0.5. | The most consistent target across sources. One thread says the ECU is still applying idle conditions below site 0.5. Another says to stay in 0 to 0.4. Some owners report around 1.0 at idle on cars that run fine, and one 420R SV owner needed 6.2 for a stable cold start, so this is a target, not a law. |
| **TPS voltage** (called "Throttle Angle Increasing" in the source write-ups) | **Car-specific.** Record your own. | Published values range from about 0.3 V to 4.7 V, probably because sensors and wiring differ (section 7). |
| **Idle speed** | Roughly **950 to 1100 rpm**. | One owner's stable result was about 950. Another says about 1100 is typical for a roller-barrel 420R. One owner found a lower idle made the ECU hunt badly, and thought a 500 rpm idle is unrealistic on a 420 cam. |

**A note on resolution.** In the 9A4 definition file, `RT_THROTTLESITE1` is an 8-bit value, so the logged value moves in steps of about 0.06. A reading of "0.1" is probably one step above "0.0". This comes from the definition file, not yet from a log of your own car.

## 6. Procedure

> Make **very small** changes, one at a time. After every change, reset the ECU (step 7) before judging the result. If you work on a hot engine, keep hands clear of the exhaust and the cooling fans.

### Step 1: Record the baseline

1. Connect the data logger and show **Throttle Site 1** and the TPS voltage (**Throttle Angle Increasing**).
2. With the engine off and the throttle resting on the stop, note both values. Note the idle rpm hot and cold if you can.
3. **Mark the current position of the stop screw and the cable adjuster** with a pen so you can get back to where you started.

### Step 2: Make sure the cable is slack

1. Check the quadrant touches the throttle stop at idle and that there is a small amount of slack in the cable.
2. If the cable is tight, back the adjuster off a few turns from your mark. Then recheck the idle position.
3. Check the cable returns freely. A binding cable can stop the throttles returning to rest and gives a high idle.

### Step 3 (optional): Check the stop hasn't been moved

1. Slacken the stop off a touch and check that the butterflies close fully. The TPS voltage should drop by roughly 0.05 V.
2. Return the stop to your mark. This tells you whether the stop was holding them open.

### Step 4 (optional): Static feeler test

This is a way to learn how much the stop needs to move before you touch it.

1. With the engine off and the data logger connected, note the Throttle Site (probably 0.0).
2. Slide a feeler gauge between the stop screw and the throttle body, opening the throttle very slightly until the Throttle Site just flicks above zero. Note how much the voltage rose.
3. Start the engine. If the idle is fixed, that is roughly how far the screw needs to move.
4. Remove the feeler gauge and make the real adjustment in step 5.

### Step 5: Adjust the stop

1. With the data logger still connected, loosen the locking nut under the TPS housing.
2. Hold the screw with the screwdriver and turn it a **very small** amount. Per the Duratec Assembly Guide (as quoted on the club forum), **turning the screw anticlockwise raises idle** and clockwise lowers it. Confirm this on your own car by watching the logged reading.
3. Hold the screw still while you tighten the nut, because tightening can move it. Expect some trial and error.
4. Aim for **Throttle Site 0.0** and the voltage that gives a stable idle on your car.

### Step 6: Check it and lock it

- Re-read Throttle Site and the voltage after tightening the nut, to confirm the screw didn't move as the nut went down.
- A little blue threadlock is a common suggestion, because a loose stop is a known cause of idle problems.

### Step 7: Reset the ECU

- Disconnect the battery (or use the master switch) for about **10 seconds**, then reconnect. This is what makes the ECU learn the new resting position.
- On a stubborn Caterham 310S, one owner left the battery disconnected for half an hour and the car came back to normal.
- An older forum post suggests cycling the ignition on and off. The battery disconnect is the method most sources use.

### Step 8: Verify

1. Reconnect, start the car and read Throttle Site and the voltage again. They should match what you set.
2. Check the cold start and idle. Then let it reach operating temperature and check for hunting.
3. Repeat steps 5 to 8 with a further tiny change if needed.
4. Final trim is best done hot. One forum poster advises setting the screw when hot so the site is 0 at idle and the slightest touch lifts it above 0. Then confirm the cold start.

### Voltmeter alternative

If you have no data logger, you can read the TPS voltage with a voltmeter and compare it with a known-good value for your car. This is much cruder. One 420R forum post says to read the voltage at the back of the TPS plug, but the exact wire is not given in the source. Don't rely on voltage values from other cars.

## 7. Reported settings (other people's cars)

These show how much values vary. **Do not copy a voltage from this table.**

| Source | Car / setup | TPS voltage at idle | Throttle Site | Result |
|---|---|---|---|---|
| Caterham7Diaries (final setting) | 420R | 1.21 V (Throttle Angle Increasing) | 0.0 | Starts and idles cold, about 950 rpm, stable hot. |
| Caterham7Diaries (first attempt, advice from Blatchat) | 420R | 1.25 to 1.3 V | 0.1 | Idled cold but hunted between about 950 and 1300 rpm hot. Rejected. |
| Caterham7Diaries comment | 420R SV | 1.40 V | 6.2 | Lowest stable cold-start setting. Lower stalled. |
| Club forum (ChrisC) | 360R | 1.21 V | not stated | Steady. Hunted at 1.06 V. |
| 420 build blog | 420R | not stated | 0.0 | Set the stop for 0.0 at idle. |
| USA7s forum | 420R, roller barrels | about 4.62 V | not stated | Voltage falls as the throttle opens on that setup. A drop to 4.55 V raised the idle. |
| Club forum (aerobod) | Jenvey with Colvern TPS | about 0.30 V (4.70 V if wired reversed) | not stated | Standard Jenvey figure quoted as a reference. |

**Why the voltages differ.** The sensor voltage can rise or fall as the throttle opens, depending on the sensor and wiring. SBD Motorsport notes that older Cosworth Caterhams had throttle sensors wired backwards, and that MBE wrote software to invert the input. Sensor type and wiring direction are likely reasons the published idle voltages differ, but I couldn't find a source that explains the gap between a 1.2 V and a 4.6 V 420R specifically. So the *direction* of "more open" in volts can differ from car to car. Use the **Throttle Site** as your primary target, and record the voltage that gives a good idle on *your* car.

## 8. Related check: full throttle

The idle stop is half of the throttle calibration. The other half is whether the pedal and cable reach wide open.

- On the Caterham7Diaries 420R, the pedal at full travel gave a Throttle Site of **14.2**, but moving the throttle by hand gave **15.2**. The author read this as about 90 % throttle at full pedal.
- The fix there was lowering the pedal stop by removing its inner height-adjustment nut and spring washer (about 8 mm of extra travel), then using the cable adjuster so the pedal stop is reached before the cable bottoms out.
- **Changing the cable adjuster alters the slack at idle.** If you adjust for full throttle, go back to step 2 and recheck the idle position and the ECU reset.

## 9. Troubleshooting

| Symptom | Likely cause | What to try |
|---|---|---|
| Idle came back after tightening the cable adjuster, but it's lumpy until warm | The stop has probably backed out, and the cable is compensating | Restore cable slack, then reset the stop properly. Add threadlock. |
| Throttle Site won't reach 0.0, or goes back to 1.0 after the ECU reset | ECU still holding the old reference, or the TPS position | Cut ECU power fully (battery off and wait). If it still won't go, some owners reposition the TPS within its mounting holes. Note the original position first, because moving the TPS changes the mapping. |
| Idle fine cold, hunts hot | Stop slightly too open, or lambda sensor | Close the stop a touch. On the Caterham7Diaries car, going from 1.25 to 1.3 V down to 1.21 V cured a hot hunt, but which way is "closed" in volts depends on your sensor. Also check the O2 sensor. |
| Won't idle cold, stalls | Possibly too little air at the stop | One forum poster says that if the site isn't yet at its idle value, the engine is short of air. Open the stop a small amount and recheck. Also check the coolant temperature sensor. |
| Hunts at a very low idle | Stop too closed | One report started hunting at 1.06 V and was steady at 1.21 V. |
| High idle (1800 to 2000 rpm) | Cable holding the throttles open, binding cable, moved stop or poor balance | Restore slack, check the return, check the stop position against your mark, check the balance. |
| Idle OK but hesitation or kangarooing at part throttle | TPS fault or drift, or poor stop/TPS relationship | Check TPS voltage stability on the data logger. Replace a suspect sensor with a genuine part. |
| No change after several attempts | Engine tolerances | One poster says stop adjustment alone may not get close enough on some engines without a remap. Get a specialist to look. |

## 10. Quick do and don't

**Do**

- Use a data logger and watch both Throttle Site and the voltage.
- Mark positions before you change anything.
- Make tiny changes and reset the ECU after each.
- Keep slack in the cable.
- Record your final working values.

**Don't**

- Don't adjust the stop blind and then adjust the cable to compensate.
- Don't copy another car's voltage.
- Don't forget the ECU reset. Without it the readings are meaningless.
- Don't move the TPS unless you have noted where it started.

## Sources

- Correcting the idle via the throttle stop, Caterham7Diaries
- Throttle pedal, stop and cable equals max power, Caterham7Diaries
- Engine start, Caterham 420 detailed build blog
- Query re throttle cable and TPS, Caterham and Lotus Seven Club
- Throttle response Duratec, Caterham and Lotus Seven Club
- 2000rpm idle 420s, Caterham and Lotus Seven Club
- Request for advice, car won't idle, Caterham and Lotus Seven Club
- R400D won't idle when cold and now stalling at junctions, Caterham and Lotus Seven Club
- 420R won't idle when cold, Caterham and Lotus Seven Club
- Is it normal for a new engine to stall when it is first started, Caterham and Lotus Seven Club
- Request for advice, car won't idle (page 3), Caterham and Lotus Seven Club
- New 420R kit won't idle, running rich, USA7s
- TPS drifting voltage, USA7s
- Throttle position sensors on Cosworth Caterhams, SBD Motorsport
- Erratic tickover, Caterham and Lotus Seven Club
