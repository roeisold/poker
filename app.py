# app.py
from flask import Flask, render_template, request, jsonify, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Default chip values
DEFAULT_CHIP_VALUES = {
    "white": 0.25,
    "red": 0.5,
    "green": 1,
    "blue": 2,
    "black": 4,
    "purple": 8,
    "brown": 16,
    "grey": 32,
    "pink": 64,
    "yellow": 128,
    "orange": 256,
    "burgundy": 512,
    "light-blue": 1024
}

# Default selected chips
DEFAULT_SELECTED_CHIPS = ["white", "red", "green", "blue", "black"]

@app.route('/', methods=['GET'])
def index():
    # Initialize chip values and selections in session if not already set
    if 'chip_values' not in session:
        session['chip_values'] = DEFAULT_CHIP_VALUES
    if 'selected_chips' not in session:
        session['selected_chips'] = DEFAULT_SELECTED_CHIPS
        
    return render_template('index.html', 
                          chip_values=session['chip_values'],
                          selected_chips=session['selected_chips'])

@app.route('/chip-setup', methods=['GET'])
def chip_setup():
    # Use session values or defaults
    chip_values = session.get('chip_values', DEFAULT_CHIP_VALUES)
    selected_chips = session.get('selected_chips', DEFAULT_SELECTED_CHIPS)
    return render_template('chip_setup.html', 
                          chip_values=chip_values,
                          selected_chips=selected_chips,
                          all_chips=list(DEFAULT_CHIP_VALUES.keys()))

@app.route('/save-chip-values', methods=['POST'])
def save_chip_values():
    try:
        data = request.json
        chip_values = data.get('chip_values', {})
        selected_chips = data.get('selected_chips', [])
        
        # Validate values
        for color, value in chip_values.items():
            if not isinstance(value, (int, float)) or value <= 0:
                return jsonify({"error": f"Invalid value for {color} chip"}), 400
        
        # Validate that at least one chip is selected
        if not selected_chips:
            return jsonify({"error": "Please select at least one chip color"}), 400
            
        # Save to session
        session['chip_values'] = chip_values
        session['selected_chips'] = selected_chips
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        import logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        data = request.json
        friends = data.get('friends', [])
        
        # Get chip values and selected chips from session, NOT default values
        chip_values = session.get('chip_values', DEFAULT_CHIP_VALUES)
        selected_chips = session.get('selected_chips', DEFAULT_SELECTED_CHIPS)
        
        logger.info(f"Initial data: friends={friends}, chip_values={chip_values}, selected_chips={selected_chips}")
        
        # Find the lowest chip value to use as increment for adjustments
        lowest_chip_value = min([chip_values.get(color, float('inf')) 
                              for color in selected_chips if color in chip_values]) if selected_chips else 1
        logger.info(f"Lowest chip value: {lowest_chip_value}")
        
        # Store original balances before any adjustments
        original_balances = {}
        
        # Process chip counts and calculate actual balances
        for i, friend in enumerate(friends):
            name, reported_balance = friend
            buy_in = data.get('buy_ins', {}).get(name, 0)
            chip_counts = data.get('chip_counts', {}).get(name, {})
            
            # Calculate chip total using only selected chips
            chip_total = sum(chip_counts.get(color, 0) * chip_values.get(color, 0) 
                          for color in selected_chips if color in chip_values)
            
            # Calculate actual balance (chips - buy_in = profit/loss)
            actual_balance = chip_total - buy_in
            
            # Store original balance
            original_balances[name] = actual_balance
            
            # Update friend data with calculated balance
            friends[i] = (name, actual_balance)
            logger.info(f"Friend {name}: buy_in={buy_in}, chip_total={chip_total}, actual_balance={actual_balance}")
        
        # Calculate total imbalance
        total_imbalance = sum(amt for _, amt in friends)
        logger.info(f"Total imbalance before adjustment: {total_imbalance}")
        original_imbalance = total_imbalance
        
        # Distribute imbalance if it exists (but keep track of original values)
        adjusted_balances = {}
        if abs(total_imbalance) > lowest_chip_value:  # If there's a non-trivial imbalance
            logger.info(f"Non-trivial imbalance detected: {total_imbalance}, attempting to distribute")
            
            # Simple approach: just divide the imbalance equally among all friends
            adjustment_per_friend = -total_imbalance / len(friends)
            logger.info(f"Adjustment per friend: {adjustment_per_friend}")
            
            # Apply adjustment to each friend
            adjusted_friends = []
            for name, balance in friends:
                new_balance = balance + adjustment_per_friend
                adjusted_balances[name] = new_balance
                adjusted_friends.append((name, new_balance))
                logger.info(f"Adjusted {name}: {balance} → {new_balance}")
            
            # Update friends list with adjusted balances
            friends = adjusted_friends
            
            # Check if imbalance is now resolved
            new_total_imbalance = sum(amt for _, amt in friends)
            logger.info(f"Total imbalance after adjustment: {new_total_imbalance}")
            
            # Log comparison to verify adjustments were applied correctly
            for (orig_name, orig_balance), (adj_name, adj_balance) in zip([(name, original_balances[name]) for name, _ in friends], friends):
                logger.info(f"Friend {orig_name}: Original={orig_balance}, Adjusted={adj_balance}, Difference={adj_balance-orig_balance}")
        else:
            # If no adjustment was made, set adjusted balances same as original
            for name, balance in friends:
                adjusted_balances[name] = balance
        
        # Separate creditors and debtors (using adjusted balances)
        creditors = [(name, amt) for name, amt in friends if amt > 0]
        debtors = [(name, -amt) for name, amt in friends if amt < 0]  # Flip to positive for easier math
        
        logger.info(f"Creditors: {creditors}")
        logger.info(f"Debtors: {debtors}")
        
        i, j = 0, 0
        transactions = []
        
        # Generate suggested transactions
        logger.info("Generating transactions...")
        while i < len(debtors) and j < len(creditors):
            debtor_name, debt = debtors[i]
            creditor_name, credit = creditors[j]
            
            amount = min(debt, credit)
            logger.info(f"Transaction candidate: {debtor_name} pays {amount} to {creditor_name}")
            
            if amount > 0.01:  # Only add transactions for non-negligible amounts
                transactions.append({
                    "payer": debtor_name, 
                    "receiver": creditor_name, 
                    "amount": round(amount, 2)
                })
                logger.info(f"Added transaction: {debtor_name} pays {round(amount, 2)} to {creditor_name}")
            
            # Update balances
            debtors[i] = (debtor_name, debt - amount)
            creditors[j] = (creditor_name, credit - amount)
            logger.info(f"Updated balances: {debtor_name}={debtors[i][1]}, {creditor_name}={creditors[j][1]}")
            
            if abs(debtors[i][1]) < 0.01:  # Check with a small epsilon for floating point errors
                logger.info(f"Debtor {debtor_name} has settled their debt, moving to next debtor")
                i += 1
            if abs(creditors[j][1]) < 0.01:
                logger.info(f"Creditor {creditor_name} has received full credit, moving to next creditor")
                j += 1
        
        # Return friends data with their profit/loss
        friends_summary = []
        for name, _ in data.get('friends', []):
            buy_in = data.get('buy_ins', {}).get(name, 0)
            chip_counts = data.get('chip_counts', {}).get(name, {})
            
            # Calculate chip total using only selected chips
            chip_total = sum(chip_counts.get(color, 0) * chip_values.get(color, 0) 
                         for color in selected_chips if color in chip_values)
            
            # Get both original and adjusted balances
            original_balance = original_balances.get(name, 0)
            adjusted_balance = adjusted_balances.get(name, 0)
            
            friends_summary.append({
                "name": name,
                "buy_in": buy_in,
                "chip_total": chip_total,  # Always use original chip total
                "profit_loss": adjusted_balance,  # Use adjusted balance for calculations
                "original_profit_loss": original_balance  # Store original balance for display
            })
            logger.info(f"Friend summary for {name}: buy_in={buy_in}, chip_total={chip_total}, " 
                        f"original_profit_loss={original_balance}, adjusted_profit_loss={adjusted_balance}")
        
        # Final balance check (should be very close to zero now)
        final_imbalance = sum(friend["profit_loss"] for friend in friends_summary)
        logger.info(f"Final imbalance: {final_imbalance}")
        
        # Final verification
        total_debts = sum(amount for _, amount in debtors)
        total_credits = sum(amount for _, amount in creditors)
        total_transactions = sum(t["amount"] for t in transactions)
        logger.info(f"Verification: total_debts={total_debts}, total_credits={total_credits}, transactions_total={total_transactions}")
        
        return jsonify({
            "transactions": transactions,
            "original_imbalance": round(original_imbalance, 2),
            "imbalance": round(final_imbalance, 2),
            "hasImbalance": abs(original_imbalance) > 0.01,
            "friends_summary": friends_summary,
            "lowest_chip_value": lowest_chip_value
        })
        
    except Exception as e:
        import traceback
        logger.error(f"Error in calculate function: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"error": str(e)}), 400
    
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    app.run(debug=True)