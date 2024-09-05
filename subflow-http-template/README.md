# HTTP Data Dip Subflow - Template

## Description

This template creates a subflow that fetches customer account information through an HTTP request. The subflow handles successful responses, allowing callers to confirm their account ID or manually enter it if the request fails. It also includes error-handling mechanisms for timeouts, invalid inputs, and critical failures. This subflow can be used for automated customer account lookups in contact center scenarios.

## Details

This subflow provides a dynamic experience where customer account information is fetched using an HTTP request. If the lookup is successful, the customer is asked to confirm the account ID. If it fails or the caller prefers, they can enter their account number manually. The flow gracefully handles errors such as invalid inputs, timeouts, and critical failures, with appropriate prompts.

Modify the subflow as needed to match your specific requirements for HTTP requests and error handling.

> Note: The Subflow uses Cisco Text-to-speech (TTS) for all audio activities that require prompts.
> 
> The HTTP request URL can be modified based on your API endpoint.
> 
> For any organization-specific configuration activities such as Queue, Entry Points, Connectors, etc., these need to be manually configured by the user before the template is published.

### Pre-requisites

- Create Entry Point, Queue, Teams, and Entry Point Mapping from the Webex Contact Center Management Portal. Refer to the Webex Contact Center Setup and Administration Guide.
- Ensure that the HTTP request URL and parameters are correctly set based on your organization's needs.
- Upload required static audio files if using your own audio for the prompts.

### Subflow Inputs

1. `errorMessage` - STRING: A message that will be played in case of an error during the subflow.

### Subflow Outputs

1. `outputVariable` - STRING: Stores the confirmed or manually entered account number.

### Subflow Breakdown

1. **Start Subflow (Initialization):** The subflow starts the process of fetching customer data.
2. **Please Wait (Comfort Message):** The caller is informed that the system is retrieving their information using a TTS prompt: “Please wait while we look up your information.”
3. **HTTPRequest (Fetch Customer Info):** The system sends an HTTP GET request to retrieve customer information from a specified API endpoint. If successful, the response contains the customer ID.
4. **Check HTTP Status (Evaluate Response):** The HTTP response is evaluated based on the status code. If the request was successful, the process moves to the next step.
5. **Confirmation Menu (Request Confirmation or Manual Entry):** The caller is prompted to confirm the fetched account ID or manually enter their account number if it’s incorrect.
6. **Set Variable (Store Account ID):** If the caller confirms the account ID, the value is stored in the `outputVariable`.
7. **Collect Digits (Manual Account Entry):** If the request fails or the caller chooses to re-enter their account number, they are prompted to input a 6-digit account number followed by the pound key (#).
8. **Error Handling (StillThere, Invalid, Critical):** The subflow handles timeouts, invalid inputs, and critical errors with respective prompts:
   - StillThere: Asks, “Are you still there?” in case of a timeout.
   - Invalid: Notifies the caller of invalid input and asks them to try again.
   - Error: A critical error prompt informing, “Something went wrong.”
9. **End Subflow (Conclusion):** The subflow ends either after confirming the account number or handling an error.

### Activities Used

**Start Subflow**
- The subflow begins when invoked.

**Please Wait**
- Plays a message using TTS, asking the caller to wait while their information is retrieved.

**HTTPRequest**
- Sends an HTTP GET request to retrieve the customer's account information.

**Check HTTP Status**
- Evaluates the HTTP response to determine if the request was successful.

**Confirmation Menu**
- Prompts the caller to confirm the retrieved account ID or re-enter it if incorrect.

**Set Variable**
- Stores the confirmed or manually entered account number.

**Collect Digits**
- Collects a 6-digit account number from the caller if the HTTP request fails or they opt to enter a new account number.

**Error Handling**
- Several prompts handle timeouts, invalid inputs, and critical errors during the subflow.

**End Subflow**
- The flow concludes after the account number is confirmed or an error occurs.

### Additional Details

For more information on configuring subflows, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).
