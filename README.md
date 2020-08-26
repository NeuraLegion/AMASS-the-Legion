# AMASS The Legion
Script used for enumerating hosts and domains via OWASP AMASS, than starting a scan with NexPloit on targets.

![alt text](https://user-images.githubusercontent.com/1631073/91214992-85e99600-e71c-11ea-9ffe-a9249296065b.jpg)

## Prerequisite
* Python3.x
* [OWASP AMASS](https://github.com/OWASP/Amass)
* [NexPloit-CLI](https://github.com/NeuraLegion/nexploit-cli/tree/06fcd5f41bd1d721acf60b95d3f5313c761a8185#%F0%9F%93%9A-full-documentation)

## Installation
* Install nexploit-cli via `npm i @neuralegion/nexploit-cli` (you can see more details [here](https://www.npmjs.com/package/@neuralegion/nexploit-cli)
* Install OWASP AMASS via `sudo snap install amass` (you can see more details [here](https://github.com/OWASP/Amass#installation---)

## Usage
Once all of the prerequisite are ready and installed, it's as easy as running:

`python amass_the_legion.py -t TARGET --token API-TOKEN -n SCAN-NAME`

example: 

`python amass_the_legion.py -t example.com --token 0r2prxw.nexa.qyn9gffrgnbbl6plwl3j2fm7jrf2nu4g -n example.com-scan-amass`
