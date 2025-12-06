from calculator import calculate
from utils import fetch_data, process_data

def main():
    """Main application."""
    data = fetch_data()
    processed = process_data(data)
    result = calculate('divide', 10, 2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()