def hello_world():
    return "Hello, GitHub Actions with Python 3.10!"

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print("✅ Application running successfully!")