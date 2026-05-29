# Pocket Option Telegram Binary Bot

A powerful Telegram bot for automated binary options trading on Pocket Option platform. Supports both real and OTC markets without asset name limitations.

## Features

- ✅ Real-time market data from Pocket Option
- ✅ Support for Real Markets
- ✅ Support for OTC Markets
- ✅ Unlimited asset names (Crypto, Forex, Commodities, Indices)
- ✅ Telegram integration with inline keyboards
- ✅ Automated trading signals
- ✅ Account balance management
- ✅ Trade history tracking
- ✅ Risk management features
- ✅ Multi-user support
- ✅ Logging and error handling

## Project Structure

```
pocket-option-telegram-bot/
├── src/
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── handlers/
│   │   │   ├── __init__.py
│   │   │   ├── start.py
│   │   │   ├── markets.py
│   │   │   ├── trading.py
│   │   │   ├── account.py
│   │   │   └── settings.py
│   │   ├── keyboards/
│   │   │   ├── __init__.py
│   │   │   ├── main_keyboard.py
│   │   │   └── market_keyboard.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── validators.py
│   │       └── formatters.py
│   ├── pocket_option/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── asset.py
│   │   │   ├── market.py
│   │   │   └── trade.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── real_markets.py
│   │   │   └── otc_markets.py
│   │   └── exceptions.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── models.py
│   │   └── migrations/
│   │       └── initial.sql
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── constants.py
│   └── logger/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   ├── test_pocket_option.py
│   └── test_database.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   ├── SETUP.md
│   ├── API_REFERENCE.md
│   ├── USER_GUIDE.md
│   └── TROUBLESHOOTING.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup.py
└── LICENSE
```

## Requirements

- Python 3.8+
- Telegram Bot Token
- Pocket Option Account
- Docker (optional)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rowan-cyber/Repository-name-pocket-option-ai-trader.git
cd Repository-name-pocket-option-ai-trader
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your Telegram bot token and Pocket Option credentials
```

### 5. Run the Bot

```bash
python -m src.bot.main
```

## Quick Start

1. Create a Telegram bot with [@BotFather](https://t.me/botfather)
2. Get your bot token
3. Set up your `.env` file
4. Run the bot
5. Start trading!

## Configuration

See [SETUP.md](docs/SETUP.md) for detailed configuration instructions.

## Supported Assets

- **Crypto**: BTC, ETH, XRP, LTC, BCH, ADA, DOT, LINK
- **Forex**: EUR/USD, GBP/USD, USD/JPY, EUR/GBP, AUD/USD
- **Commodities**: Gold, Silver, Oil, Natural Gas
- **Indices**: SPX500, DAXINDX, FTSE100

## Usage

See [USER_GUIDE.md](docs/USER_GUIDE.md) for detailed usage instructions.

## API Reference

See [API_REFERENCE.md](docs/API_REFERENCE.md) for API documentation.

## Troubleshooting

See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for common issues and solutions.

## Docker Setup

```bash
docker-compose up -d
```

## Contributing

Contributions are welcome! Please follow the guidelines in CONTRIBUTING.md

## License

This project is licensed under the MIT License - see LICENSE file for details

## Disclaimer

This bot is for educational purposes only. Trading binary options involves risk. Always use proper risk management and trade with capital you can afford to lose.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Author

Created by [rowan-cyber](https://github.com/rowan-cyber)
