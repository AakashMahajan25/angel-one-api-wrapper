from wrapper import AngelAPIWrapper
import asyncio

async def main():
    # Create an instance of the wrapper
    api = AngelAPIWrapper()
    
    try:
        # Call the get_profile method
        profile = await api.get_profile()
        print("Profile:", profile)
    except Exception as e:
        print(f"Error occurred: {e}")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())