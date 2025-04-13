# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        friends = data.get('friends', [])
        
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
        
        imbalance = round(total, 2)
        return jsonify({
            "transactions": transactions,
            "imbalance": imbalance,
            "hasImbalance": abs(imbalance) > 0.01
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
