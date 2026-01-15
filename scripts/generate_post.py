python
from datetime import datetime

This script just prints the current time
def generate_post():
    now = datetime.now()
    print(f"Blog post generated at {now.strftime('%Y-%m-%d %H:%M:%S')}")

if _name_ == "_main_":
    generate_post()
