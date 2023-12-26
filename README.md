# loopring-python-SDK
Unofficial Python SDK for Loopring v3 API

## Loopring API Session Setup Guide
This guide outlines the necessary steps to set up a secure and functional environment for integrating with the Loopring API in Python. It includes instructions for creating a .env file, which will safely store your API credentials.

Step 1: Navigate to Your Project Directory: Open the root directory of your Python project.
Create a New File: Name this file .env. Add Your Credentials: Edit the .env file with your text editor, including the following lines:

### .env Contents
API_KEY=your_api_key_here \
ACCOUNT_ID=your_account_id_here \

### Security and Best Practices
Confidentiality: Keep your .env file confidential. It contains sensitive data. \
Deployment: In deployment environments, ensure these variables are set securely. \
With the .env file in place, the Session class in your Python code will automatically load and use these variables for Loopring API authentication.

### Further Information
For detailed API usage and capabilities, refer to the [Loopring API documentation](https://docs-protocol.loopring.io/).