import re

nums = """(123) 456-7890
1234567890
123-456-7890
123-45-8302
123-456-789
123 456 7890
123.456.7890""".split('\n')

tele_pattern = r"""
\(?\d{3}\)?   # area code
[ -.]?        # sep
\d{3}         # exchange
[ .-]?        # sep
\d{4}         # number
"""

rx_tele = re.compile(tele_pattern, re.X)

for num in nums:
    print(num, "MATCHED" if rx_tele.fullmatch(num) else "NO MATCH")

