import re
import os

def audit_file(filepath):
    print(f"Auditing {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()

    # Check for escapeHTML definition with robust check
    if 'if (str === undefined || str === null) return \'\';' not in content:
        print(f"  FAILED: improved escapeHTML function NOT found in {filepath}")
        return False

    # Check for innerHTML assignments
    if 'index.html' in filepath:
        if 'escapedBuyIn = escapeHTML(playerData?.buyIn || \'\')' not in content:
            print(f"  FAILED: playerData?.buyIn not escaped in {filepath}")
            return False

        if 'escapedChipCount = escapeHTML(chipCount)' not in content:
            print(f"  FAILED: chipCount not escaped in {filepath}")
            return False

    if 'chip_setup.html' in filepath:
        if 'escapedChipValue = escapeHTML(chipValues[chip])' not in content:
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
