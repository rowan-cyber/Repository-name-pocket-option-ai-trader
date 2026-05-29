-- Initial database migrations

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(255) PRIMARY KEY,
    telegram_id INTEGER UNIQUE NOT NULL,
    username VARCHAR(255),
    email VARCHAR(255),
    position_size FLOAT DEFAULT 0.02,
    daily_loss_limit FLOAT DEFAULT 0.05,
    max_consecutive_losses INTEGER DEFAULT 3,
    auto_trading_enabled BOOLEAN DEFAULT FALSE,
    selected_market VARCHAR(50),
    selected_asset VARCHAR(50),
    selected_strategy VARCHAR(50) DEFAULT 'rsi_macd_strategy',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create trades table
CREATE TABLE IF NOT EXISTS trades (
    id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    asset VARCHAR(50) NOT NULL,
    market VARCHAR(50),
    direction VARCHAR(10),
    entry_price FLOAT,
    exit_price FLOAT,
    amount FLOAT,
    profit_loss FLOAT,
    status VARCHAR(50),
    rsi FLOAT,
    macd FLOAT,
    signal FLOAT,
    entry_time TIMESTAMP,
    exit_time TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_user_id (user_id),
    INDEX idx_asset (asset),
    INDEX idx_created_at (created_at)
);

-- Create assets table
CREATE TABLE IF NOT EXISTS assets (
    id VARCHAR(255) PRIMARY KEY,
    symbol VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255),
    market VARCHAR(50),
    asset_type VARCHAR(50),
    min_investment FLOAT,
    max_investment FLOAT,
    is_active BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_symbol (symbol),
    INDEX idx_market (market)
);

-- Create signals table
CREATE TABLE IF NOT EXISTS signals (
    id VARCHAR(255) PRIMARY KEY,
    asset VARCHAR(50) NOT NULL,
    market VARCHAR(50),
    direction VARCHAR(10),
    strength FLOAT,
    rsi FLOAT,
    macd FLOAT,
    bb_upper FLOAT,
    bb_lower FLOAT,
    ema_fast FLOAT,
    ema_slow FLOAT,
    executed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_asset (asset),
    INDEX idx_created_at (created_at)
);
