# ScreBay (for OpenFaaS)

ScreBay is a personal OpenFaaS (via faasd) Python scraper microservice which scans for good eBay prices on a schedule.

## Installation

Install an OpenFaaS server, then run

```bash
faas-cli up -y screbay.yml
```

## Usage

If not using microservices, it can be run manually and takes user input.
```bash
$ python3 scrape.py
```

## Contributing
Open to making this more generic over time.

## License
[MIT](https://choosealicense.com/licenses/mit/)