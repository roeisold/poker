from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DEFAULT_CHIP_VALUES = {
    "white": 0.25, "red": 0.5, "green": 1, "blue": 2, "black": 4,
    "purple": 8, "brown": 16, "grey": 32, "pink": 64, "yellow": 128,
    "orange": 256, "burgundy": 512, "light-blue": 1024
}
DEFAULT_SELECTED_CHIPS = ["white", "red", "green", "blue", "black"]

@app.route('/', methods=['GET'])
def index():
    # Defaults will be overridden by localStorage on the frontend
    return render_template('index.html', 
                          chip_values=DEFAULT_CHIP_VALUES,
                          selected_chips=DEFAULT_SELECTED_CHIPS)

@app.route('/chip-setup', methods=['GET'])
def chip_setup():
    # Defaults will be overridden by localStorage on the frontend
    return render_template('chip_setup.html', 
                          chip_values=DEFAULT_CHIP_VALUES,
                          selected_chips=DEFAULT_SELECTED_CHIPS,
                          all_chips=list(DEFAULT_CHIP_VALUES.keys()))

@app.route('/save-chip-values', methods=['POST'])
def save_chip_values():
    # Frontend handles persistence via localStorage
    try:
        data = request.json
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        friends = data.get('friends', [])
        
        # Get chip values from request (sent from frontend localStorage)
        chip_values = data.get('chip_values', DEFAULT_CHIP_VALUES)
        selected_chips = data.get('selected_chips', DEFAULT_SELECTED_CHIPS)
        
        # Calculation logic
        original_balances = {}
        chip_totals = {}
        buy_ins_dict = {}
        
        for i, friend in enumerate(friends):
            name, _ = friend
            buy_in = data.get('buy_ins', {}).get(name, 0)
            chip_counts = data.get('chip_counts', {}).get(name, {})
            chip_total = sum(chip_counts.get(color, 0) * chip_values.get(color, 0) 
                          for color in selected_chips if color in chip_values)
            
            actual_balance = chip_total - buy_in
            original_balances[name] = actual_balance
            chip_totals[name] = chip_total
            buy_ins_dict[name] = buy_in
            friends[i] = (name, actual_balance)
        
        total_imbalance = sum(amt for _, amt in friends)
        
        # Calculate adjusted balances (after balancing)
        adjusted_balances = {}
        if abs(total_imbalance) > 0.01:
            adj = -total_imbalance / len(friends)
            for name, balance in friends:
                adjusted_balances[name] = balance + adj
        else:
            for name, balance in friends:
                adjusted_balances[name] = balance

        # Generate transactions
        creditors = [(n, b) for n, b in adjusted_balances.items() if b > 0]
        debtors = [(n, -b) for n, b in adjusted_balances.items() if b < 0]
        transactions = []
        i, j = 0, 0
        while i < len(debtors) and j < len(creditors):
            amt = min(debtors[i][1], creditors[j][1])
            if amt > 0.01:
                transactions.append({
                    "payer": debtors[i][0], 
                    "receiver": creditors[j][0], 
                    "amount": round(amt, 2)
                })
            debtors[i] = (debtors[i][0], debtors[i][1] - amt)
            creditors[j] = (creditors[j][0], creditors[j][1] - amt)
            if debtors[i][1] < 0.01: i += 1
            if creditors[j][1] < 0.01: j += 1

        # Create detailed player summary
        players_summary = []
        for name, _ in friends:
            players_summary.append({
                "name": name,
                "buy_in": buy_ins_dict.get(name, 0),
                "chip_total": chip_totals.get(name, 0),
                "profit_loss_original": original_balances.get(name, 0),
                "profit_loss_balanced": adjusted_balances.get(name, 0)
            })

        return jsonify({
            "transactions": transactions,
            "players_summary": players_summary,
            "total_imbalance": round(total_imbalance, 2),
            "has_imbalance": abs(total_imbalance) > 0.01
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)