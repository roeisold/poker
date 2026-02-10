from flask import Flask, render_template, request, jsonify, session
import os

app = Flask(__name__)

# Static key prevents the app from 'forgetting' chip values on restart
app.secret_key = 'poker_night_settler_secure_key_123' 

DEFAULT_CHIP_VALUES = {
    "white": 0.25, "red": 0.5, "green": 1, "blue": 2, "black": 4,
    "purple": 8, "brown": 16, "grey": 32, "pink": 64, "yellow": 128,
    "orange": 256, "burgundy": 512, "light-blue": 1024
}
DEFAULT_SELECTED_CHIPS = ["white", "red", "green", "blue", "black"]

@app.route('/', methods=['GET'])
def index():
    if 'chip_values' not in session:
        session['chip_values'] = DEFAULT_CHIP_VALUES
    if 'selected_chips' not in session:
        session['selected_chips'] = DEFAULT_SELECTED_CHIPS
    return render_template('index.html', 
                          chip_values=session['chip_values'],
                          selected_chips=session['selected_chips'])

@app.route('/chip-setup', methods=['GET'])
def chip_setup():
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
        session['chip_values'] = data.get('chip_values', {})
        session['selected_chips'] = data.get('selected_chips', [])
        session.modified = True
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        friends = data.get('friends', [])
        chip_values = session.get('chip_values', DEFAULT_CHIP_VALUES)
        selected_chips = session.get('selected_chips', DEFAULT_SELECTED_CHIPS)
        
        lowest_chip_value = min([chip_values.get(color, float('inf')) 
                              for color in selected_chips if color in chip_values]) if selected_chips else 1
        
        original_balances = {}
        for i, friend in enumerate(friends):
            name, _ = friend
            buy_in = data.get('buy_ins', {}).get(name, 0)
            chip_counts = data.get('chip_counts', {}).get(name, {})
            chip_total = sum(chip_counts.get(color, 0) * chip_values.get(color, 0) 
                          for color in selected_chips if color in chip_values)
            actual_balance = chip_total - buy_in
            original_balances[name] = actual_balance
            friends[i] = (name, actual_balance)
        
        total_imbalance = sum(amt for _, amt in friends)
        original_imbalance = total_imbalance
        
        adjusted_balances = {}
        if abs(total_imbalance) > 0.01:
            adjustment_per_friend = -total_imbalance / len(friends)
            for name, balance in friends:
                adjusted_balances[name] = balance + adjustment_per_friend
        else:
            for name, balance in friends:
                adjusted_balances[name] = balance

        # Transaction logic
        creditors = [(n, b) for n, b in adjusted_balances.items() if b > 0]
        debtors = [(n, -b) for n, b in adjusted_balances.items() if b < 0]
        transactions = []
        i, j = 0, 0
        while i < len(debtors) and j < len(creditors):
            amount = min(debtors[i][1], creditors[j][1])
            if amount > 0.01:
                transactions.append({"payer": debtors[i][0], "receiver": creditors[j][0], "amount": round(amount, 2)})
            debtors[i] = (debtors[i][0], debtors[i][1] - amount)
            creditors[j] = (creditors[j][0], creditors[j][1] - amount)
            if debtors[i][1] < 0.01: i += 1
            if creditors[j][1] < 0.01: j += 1

        friends_summary = []
        for name, _ in data.get('friends', []):
            friends_summary.append({
                "name": name,
                "buy_in": data.get('buy_ins', {}).get(name, 0),
                "chip_total": sum(data.get('chip_counts', {}).get(name, {}).get(c, 0) * chip_values.get(c, 0) for c in selected_chips),
                "profit_loss": adjusted_balances.get(name, 0),
                "original_profit_loss": original_balances.get(name, 0)
            })

        return jsonify({
            "transactions": transactions,
            "original_imbalance": round(original_imbalance, 2),
            "hasImbalance": abs(original_imbalance) > 0.01,
            "friends_summary": friends_summary
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)