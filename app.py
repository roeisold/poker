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
    "black": 4
}

@app.route('/', methods=['GET'])
def index():
    # Initialize chip values in session if not already set
    if 'chip_values' not in session:
        session['chip_values'] = DEFAULT_CHIP_VALUES
    return render_template('index.html', chip_values=session['chip_values'])

@app.route('/chip-setup', methods=['GET'])
def chip_setup():
    # Use session values or defaults
    chip_values = session.get('chip_values', DEFAULT_CHIP_VALUES)
    return render_template('chip_setup.html', chip_values=chip_values)

@app.route('/save-chip-values', methods=['POST'])
def save_chip_values():
    try:
        chip_values = request.json
        # Validate values
        for color, value in chip_values.items():
            if not isinstance(value, (int, float)) or value <= 0:
                return jsonify({"error": f"Invalid value for {color} chip"}), 400
        
        # Save to session
        session['chip_values'] = chip_values
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        friends = data.get('friends', [])
        chip_values = session.get('chip_values', DEFAULT_CHIP_VALUES)
        
        # Process chip counts and calculate actual balances
        for i, friend in enumerate(friends):
            name, reported_balance = friend
            buy_in = data.get('buy_ins', {}).get(name, 0)
            chip_counts = data.get('chip_counts', {}).get(name, {})
            
            # Calculate chip total
            chip_total = sum(chip_counts.get(color, 0) * value for color, value in chip_values.items())
            
            # Calculate actual balance (chips - buy_in = profit/loss)
            actual_balance = chip_total - buy_in
            
            # Update friend data with calculated balance
            friends[i] = (name, actual_balance)
        
        # Separate creditors and debtors
        creditors = [(name, amt) for name, amt in friends if amt > 0]
        debtors = [(name, -amt) for name, amt in friends if amt < 0]  # Flip to positive for easier math
        
        total = sum(amt for _, amt in friends)
        
        i, j = 0, 0
        transactions = []
        
        # Generate suggested transactions
        while i < len(debtors) and j < len(creditors):
            debtor_name, debt = debtors[i]
            creditor_name, credit = creditors[j]
            
            amount = min(debt, credit)
            transactions.append({
                "payer": debtor_name, 
                "receiver": creditor_name, 
                "amount": round(amount, 2)
            })
            
            # Update balances
            debtors[i] = (debtor_name, debt - amount)
            creditors[j] = (creditor_name, credit - amount)
            
            if abs(debtors[i][1]) < 0.01:  # Check with a small epsilon for floating point errors
                i += 1
            if abs(creditors[j][1]) < 0.01:
                j += 1
        
        # Return friends data with their profit/loss
        friends_summary = []
        for name, balance in data.get('friends', []):
            buy_in = data.get('buy_ins', {}).get(name, 0)
            chip_counts = data.get('chip_counts', {}).get(name, {})
            chip_total = sum(chip_counts.get(color, 0) * value for color, value in chip_values.items())
            profit_loss = chip_total - buy_in
            
            friends_summary.append({
                "name": name,
                "buy_in": buy_in,
                "chip_total": chip_total,
                "profit_loss": profit_loss
            })
        
        imbalance = round(total, 2)
        return jsonify({
            "transactions": transactions,
            "imbalance": imbalance,
            "hasImbalance": abs(imbalance) > 0.01,
            "friends_summary": friends_summary
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    app.run(debug=True)