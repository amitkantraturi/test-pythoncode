import boto3
import requests

# Initialize a Boto3 client for S3
def connect_to_s3():
    try:
        s3_client = boto3.client('s3')
        print("Successfully connected to S3.")
        return s3_client
    except Exception as e:
        print(f"Error connecting to S3: {e}")
        return None

# Function to fetch data from a fake API
def fetch_fake_api_data():
    url = "https://jsonplaceholder.typicode.com/todos"
    try:
        response = requests.get(url)
        if response.ok:
            print("Successfully fetched data from the fake API.")
            return response.json()  # Return the JSON data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data from the API: {e}")
        return None

# Main function
if __name__ == "__main__":
    # Connect to AWS S3 using Boto3
    s3_client = connect_to_s3()

    # Fetch data from the fake API
    api_data = fetch_fake_api_data()

    # Print the fetched data (if any)
    if api_data:
        print("API Data:")
        for item in api_data[:5]:  # Print first 5 items for brevity
            print(item)
