# Examples for *Explorer Hat Tricks*

## Warning

The examples in this repository rely on the Pimoroni library for the Explorer Hat.
I believe that the library will need to be updated for the Raspberry Pi 5
and the latest version of the Operating SYstem.

As soon as I have any information about the timescale for the update I will share it here and on X.

If you're using an earlier model of the Pi,
and are not using the latest version of the Operating system, everything here should work.

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K61CLW1)


**Disclaimer**: I have been a follower and customer of Pimoroni for years, but I have no official connection with them.

Please don't ask them for support in relation to this code!

## What this repository contains

These are projects from *Explorer Hat Tricks*, an ebook about the Pimoroni Explorer Hat Pro which you can buy on [Leanpub](https://leanpub.com/explorerhattricks/). That means you get a 40-day no-quibble **money back guarantee**).

![Traffic Lights Example](docs/images/traffic-lights.jpg)

### Wiring diagram

![Traffic Lights](docs/images/traffic-lights-01_bb.png)


## What you will need

1. A [Raspberry Pi](https://www.raspberrypi.org/) model zero/zero W (with headers), 2B+, 3B, 3B+ or 4B
running Raspberry Pi OS.
1. A [Pimoroni Explorer HAT Pro](https://shop.pimoroni.com/products/explorer-hat). You can run some of the
projects with the original Explorer HAT or the Explorer pHAT.

1. The parts from a Pimoroni Explorer Hat Parts kit
1. Optionally, an LDR (Light dependent resistor)

I'll add wiring diagrams and README files to this repository as time permits.

## Installation

This code has been tested using python3.

1. Install Pimoroni's Explorer Hat Library using [these instructions](https://github.com/pimoroni/explorer-hat)
1. Clone this repository or download and unzip into a directory of your choice.

## Using the examples

1. Navigate to the example or project you want to run
1. Wire up the example. 
1. Run the relevant script. 

For instance, to run the traffic light project once you have wired it up, open a terminal window, 
change to the relevant directory and run `python3 traffic-lights-01.py`

Use `Ctrl-C` to quit the example.

The console should look like this:

![Terminal session](docs/images/traffic-lights-term.png)

## Index to examples

*A work in progress*.

The code for all the examples is here, but not all have README files/wiring diagrams yet.

1. [On-board LEDs](projects/leds/README.md)
1. [Traffic Lights](projects/traffic-lights/README.md)
1. [Touch sensors](projects/touch/README.md)
1. [Using the HAT outputs](projects/touch/README.md)
1. [Morse Code Sender](projects/morse/README.md)
1. [What's the buzz?](projects/buzzer/README.md)
1. [Analogue Projects](projects/analog/README.md)





