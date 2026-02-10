# app.py
from flask import Flask, render_template, request, jsonify, session
import os

app = Flask(__name__)

# --- CRITICAL FIX ---
# We use a static key so the session (and your chip settings) 
# aren't lost if the server restarts.
app.secret_key = 'poker_night_secret_static_key_12345' 
# --------------------

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
        
        # Mark session as modified to ensure it saves
        session.modified = True
        
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        friends = data.get('friends', [])
        
        # Get chip values and selected chips from session
        chip_values = session.get('chip_values', DEFAULT_CHIP_VALUES)
        selected_chips = session.get('selected_chips', DEFAULT_SELECTED_CHIPS)
        
        # Find the lowest chip value to use as increment for adjustments
        lowest_chip_value = min([chip_values.get(color, float('inf')) 
                              for color in selected_chips if color in chip_values]) if selected_chips else 1
        
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
        
        # Calculate total imbalance
        total_imbalance = sum(amt for _, amt in friends)
        original_imbalance = total_imbalance
        
        # Distribute imbalance if it exists
        adjusted_balances = {}
        if abs(total_imbalance) > lowest_chip_value / 2.0:  # Threshold relative to chip value
            adjustment_per_friend = -total_imbalance / len(friends)
            
            # Apply adjustment
            adjusted_friends = []
            for name, balance in friends:
                new_balance = balance + adjustment_per_friend
                adjusted_balances[name] = new_balance
                adjusted_friends.append((name, new_balance))
            
            friends = adjusted_friends
        else:
            for name, balance in friends:
                adjusted_balances[name] = balance
        
        # Separate creditors and debtors
        creditors = [(name, amt) for name, amt in friends if amt > 0]
        debtors = [(name, -amt) for name, amt in friends if amt < 0]
        
        i, j = 0, 0
        transactions = []
        
        while i < len(debtors) and j < len(creditors):
            debtor_name, debt = debtors[i]
            creditor_name, credit = creditors[j]
            
            amount = min(debt, credit)
            
            if amount > 0.01:
                transactions.append({
                    "payer": debtor_name, 
                    "receiver": creditor_name, 
                    "amount": round(amount, 2)
                })
            
            debtors[i] = (debtor_name, debt - amount)
            creditors[j] = (creditor_name, credit - amount)
            
            if abs(debtors[i][1]) < 0.01: i += 1
            if abs(creditors[j][1]) < 0.01: j += 1
        
        # Return friends data summary
        friends_summary = []
        for name, _ in data.get('friends', []):
            buy_in = data.get('buy_ins', {}).get(name, 0)
            chip_counts = data.get('chip_counts', {}).get(name, {})
            
            chip_total = sum(chip_counts.get(color, 0) * chip_values.get(color, 0) 
                         for color in selected_chips if color in chip_values)
            
            original_balance = original_balances.get(name, 0)
            adjusted_balance = adjusted_balances.get(name, 0)
            
            friends_summary.append({
                "name": name,
                "buy_in": buy_in,
                "chip_total": chip_total,
                "profit_loss": adjusted_balance,
                "original_profit_loss": original_balance
            })
        
        final_imbalance = sum(friend["profit_loss"] for friend in friends_summary)
        
        return jsonify({
            "transactions": transactions,
            "original_imbalance": round(original_imbalance, 2),
            "imbalance": round(final_imbalance, 2),
            "hasImbalance": abs(original_imbalance) > 0.01,
            "friends_summary": friends_summary,
            "lowest_chip_value": lowest_chip_value
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    app.run(debug=True)