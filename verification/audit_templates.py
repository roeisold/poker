import re
import os

def audit_file(filepath):
    print(f"Auditing {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()

    # Check for escapeHTML definition
    if 'function escapeHTML' not in content:
        print(f"  FAILED: escapeHTML function NOT defined in {filepath}")
        return False

    # Check for innerHTML assignments
    # We want to make sure variables inside innerHTML templates are wrapped in escapeHTML()
    # This is a bit tricky with regex, but let's look for common patterns

    # 1. Look for selectedChips.map in index.html
    if 'index.html' in filepath:
        if 'selectedChips.map(chip => {' not in content or 'escapeHTML(chip)' not in content:
            print(f"  FAILED: selectedChips.map not properly secured in {filepath}")
            return False

        if 'p.name' in content and 'escapeHTML(p.name)' not in content:
            print(f"  FAILED: p.name not escaped in {filepath}")
            return False

        if 'p.buy_in.toFixed(2)' in content and 'escapeHTML(p.buy_in.toFixed(2))' not in content:
            print(f"  FAILED: p.buy_in not escaped in {filepath}")
            return False

        if 'p.chip_total.toFixed(2)' in content and 'escapeHTML(p.chip_total.toFixed(2))' not in content:
            print(f"  FAILED: p.chip_total not escaped in {filepath}")
            return False

        if 'p.profit_loss_original.toFixed(2)' in content and 'escapeHTML(p.profit_loss_original.toFixed(2))' not in content:
            print(f"  FAILED: p.profit_loss_original not escaped in {filepath}")
            return False

        if 'p.profit_loss_balanced.toFixed(2)' in content and 'escapeHTML(p.profit_loss_balanced.toFixed(2))' not in content:
            print(f"  FAILED: p.profit_loss_balanced not escaped in {filepath}")
            return False

        if 'data.total_imbalance.toFixed(2)' in content and 'escapeHTML(data.total_imbalance.toFixed(2))' not in content:
            print(f"  FAILED: data.total_imbalance not escaped in {filepath}")
            return False

        if 't.amount.toFixed(2)' in content and 'escapeHTML(t.amount.toFixed(2))' not in content:
            print(f"  FAILED: t.amount not escaped in {filepath}")
            return False

        if 't.payer' in content and 'escapeHTML(t.payer)' not in content:
            print(f"  FAILED: t.payer not escaped in {filepath}")
            return False

        if 't.receiver' in content and 'escapeHTML(t.receiver)' not in content:
            print(f"  FAILED: t.receiver not escaped in {filepath}")
            return False

        if 'playerData?.name' in content and 'escapeHTML(playerData?.name || \'\')' not in content:
            print(f"  FAILED: playerData.name not escaped in {filepath}")
            return False

        if 'playerData?.buyIn' in content and 'escapeHTML(playerData?.buyIn || \'\')' not in content:
            print(f"  FAILED: playerData.buyIn not escaped in {filepath}")
            return False

        if 'value="${chipCount}"' in content and 'value="${escapeHTML(chipCount)}"' not in content:
            print(f"  FAILED: chipCount not escaped in {filepath}")
            return False

    # 2. Look for ALL_CHIPS.map in chip_setup.html
    if 'chip_setup.html' in filepath:
        if 'ALL_CHIPS.map(chip => {' not in content or 'escapeHTML(chip)' not in content:
            print(f"  FAILED: ALL_CHIPS.map not properly secured in {filepath}")
            return False

        if 'value="${chipValues[chip]}"' in content and 'value="${escapeHTML(chipValues[chip])}"' not in content:
            print(f"  FAILED: chipValues[chip] not escaped in {filepath}")
            return False

    print(f"  PASSED audit for {filepath}")
    return True

if __name__ == "__main__":
    success = True
    success &= audit_file('templates/index.html')
    success &= audit_file('templates/chip_setup.html')
    if not success:
        exit(1)
