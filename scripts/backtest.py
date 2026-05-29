"""
Backtesting Script

Test trading strategy on historical data.
"""

import sys
import argparse
from datetime import datetime, timedelta
from src.config.settings import settings
from src.strategy.rsi_macd_strategy import RSIMACDStrategy
from src.logger.logger import setup_logger

logger = setup_logger(__name__)

def run_backtest(asset, market, days, position_size=0.02):
    """
    Run backtest on historical data
    
    Args:
        asset: Asset symbol (e.g., 'EUR/USD')
        market: 'real' or 'otc'
        days: Number of days to backtest
        position_size: Position size as percentage
    """
    try:
        logger.info(f"🧪 Starting backtest for {asset} ({market}) - {days} days")
        
        # Initialize strategy
        strategy = RSIMACDStrategy(settings)
        
        # Mock data (in production, fetch from API)
        logger.info("📊 Generating mock price data...")
        prices = generate_mock_prices(100)  # 100 candles
        
        # Run analysis
        results = []
        wins = 0
        losses = 0
        
        for i in range(len(prices) - 1):
            current_prices = prices[:i+1]
            previous_prices = prices[:i] if i > 0 else None
            
            result = strategy.analyze(current_prices, previous_prices)
            
            if result['signal']:
                # Simulate trade execution
                entry_price = prices[i]
                exit_price = prices[i+1]
                
                if result['signal'] == 'buy':
                    pnl = exit_price - entry_price
                else:  # sell
                    pnl = entry_price - exit_price
                
                if pnl > 0:
                    wins += 1
                else:
                    losses += 1
                
                results.append({
                    'time': i,
                    'signal': result['signal'],
                    'entry': entry_price,
                    'exit': exit_price,
                    'pnl': pnl,
                    'strength': result['strength']
                })
        
        # Calculate statistics
        total_trades = wins + losses
        win_rate = (wins / total_trades * 100) if total_trades > 0 else 0
        total_pnl = sum(r['pnl'] for r in results)
        
        # Print results
        print("\n" + "="*60)
        print(f"📊 BACKTEST RESULTS - {asset} ({market})")
        print("="*60)
        print(f"Period: Last {days} days")
        print(f"Total Trades: {total_trades}")
        print(f"Winning Trades: {wins}")
        print(f"Losing Trades: {losses}")
        print(f"Win Rate: {win_rate:.2f}%")
        print(f"Total P&L: ${total_pnl:.2f}")
        print(f"Avg Win: ${sum(r['pnl'] for r in results if r['pnl'] > 0) / max(wins, 1):.2f}")
        print(f"Avg Loss: ${sum(r['pnl'] for r in results if r['pnl'] < 0) / max(losses, 1):.2f}")
        print("="*60 + "\n")
        
        logger.info(f"✅ Backtest complete. Win rate: {win_rate:.2f}%")
        
        return {
            'total_trades': total_trades,
            'wins': wins,
            'losses': losses,
            'win_rate': win_rate,
            'total_pnl': total_pnl,
            'results': results
        }
    
    except Exception as e:
        logger.error(f"❌ Backtest error: {e}", exc_info=True)
        return None

def generate_mock_prices(count):
    """Generate mock price data for testing"""
    import random
    prices = [1.0950]
    for _ in range(count - 1):
        change = random.uniform(-0.0010, 0.0010)
        prices.append(prices[-1] + change)
    return prices

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Backtest trading strategy')
    parser.add_argument('--asset', default='EUR/USD', help='Asset to backtest')
    parser.add_argument('--market', default='real', choices=['real', 'otc'], help='Market type')
    parser.add_argument('--days', type=int, default=30, help='Days to backtest')
    parser.add_argument('--position-size', type=float, default=0.02, help='Position size')
    
    args = parser.parse_args()
    
    run_backtest(args.asset, args.market, args.days, args.position_size)
