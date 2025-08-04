
# Sample Python script with intentional issues for SonarQube testing

# Hardcoded credentials (Security Vulnerability)
USERNAME = "admin"
PASSWORD = "password123"

# Function with code smell: too many responsibilities
def process_data(data):
    print("Processing data...")
    cleaned_data = [d.strip().lower() for d in data if d]
    print("Data cleaned.")
    result = []
    for item in cleaned_data:
        if item.startswith("error"):
            print(f"Error found: {item}")
        else:
            result.append(item)
    print("Data processed.")
    return result

# Function with a bug: division by zero
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count  # Bug if count is zero

# Function with code smell: unused variable
def greet_user(name):
    greeting = "Hello, " + name
    unused_variable = 42
    print(greeting)

# Function with code smell: duplicate code
def log_error(message):
    print("ERROR: " + message)

def log_warning(message):
    print("WARNING: " + message)
