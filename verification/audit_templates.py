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

        if 't.payer' in content and 'escapeHTML(t.payer)' not in content:
            print(f"  FAILED: t.payer not escaped in {filepath}")
            return False

        if 't.receiver' in content and 'escapeHTML(t.receiver)' not in content:
            print(f"  FAILED: t.receiver not escaped in {filepath}")
            return False

        if 'playerData?.name' in content and 'escapeHTML(playerData?.name || \'\')' not in content:
            print(f"  FAILED: playerData.name not escaped in {filepath}")
            return False

        if 'chipCount' in content and 'escapeHTML(chipCount)' not in content:
            print(f"  FAILED: chipCount not escaped in {filepath}")
            return False

    # 2. Look for ALL_CHIPS.map in chip_setup.html
    if 'chip_setup.html' in filepath:
        if 'ALL_CHIPS.map(chip => {' not in content or 'escapeHTML(chip)' not in content:
            print(f"  FAILED: ALL_CHIPS.map not properly secured in {filepath}")
            return False

        if 'chipValues[chip]' in content and 'escapeHTML(chipValues[chip])' not in content:
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
