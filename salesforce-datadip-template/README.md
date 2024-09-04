# Webex Contact Center - IVR HTTP Connector for Salesforce

## Name
Salesforce HTTP(S) Data Dip

## Labels 
Intermediate, Voice, Inbound, Data dip, CRM

## Description

This template demonstrates how to use the HTTP connector in Webex Contact Center to interact with Salesforce, allowing for dynamic routing decisions and information extraction. This is especially useful for querying, updating, and managing cases or other objects in Salesforce using all supported HTTP verbs.

This specific flow looks up customer information from Salesforce using their phone number (ANI) and routes the call based on the data retrieved. It also allows Webex Contact Center to post updates to Salesforce cases post-call.


## Details

This flow uses Webex Contact Center's HTTP connector to retrieve customer information from Salesforce using an ANI lookup. The flow fetches the customer's account, contact, and case information from Salesforce and routes the call accordingly.


> Note: The Flow uses Cisco Text-to-speech (TTS) for any prompts, and uses `defaultmusic_on_hold.wav` for hold music.

> Important: For all organization-specific configurations such as queues, entry points, connectors, and outdial ANI, these need to be manually configured by the user before the template is published.

### Use Case

1. A customer calls into Webex Contact Center, and their phone number is captured.
2. The system performs an ANI lookup in Salesforce to find matching account and contact information.
3. Based on the data retrieved, the customer is greeted with a personalized IVR message.
4. If there is an open case associated with the customer, the agent receives this information on their desktop.
5. After the call, Webex Contact Center posts call details and comments back to the Salesforce case.

This flow ensures seamless customer service by integrating Salesforce with Webex Contact Center, ensuring that relevant information is readily available to both customers and agents.

## Pre-Requisites

- Configure the Salesforce connector using OAuth2. Refer to the [official guide](https://help.webex.com/en-us/article/n26v7heb/Configure-Connected-App-for-Webex-Contact-Center-Salesforce-Connector) for detailed steps.
- Import the attached flow `Salesforce_HTTP_Connector.json` into the Webex Contact Center Flow Designer.
- Use the [Salesforce API collection](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm) to explore the REST APIs.
- To manually generate the OAuth access token, use the following command:

```sh
curl --location --request POST 'https://abcde-dev-ed.my.salesforce.com/services/oauth2/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=clientId' \
--data-urlencode 'client_secret=clientSecret' \
--data-urlencode 'username=yourLogin@salesforce.com' \
--data-urlencode 'password=yourPassword'

```


## Flow Breakdown

1. **ANI Lookup and Routing**: 
   - The flow begins by capturing the customer's phone number.
   - The phone number is formatted, and a Salesforce API call retrieves the account and contact associated with the ANI.
   - If the customer is found, they are routed based on the associated Salesforce case.

2. **Post-Call Updates**:
   - Once the agent completes the call, Webex Contact Center posts information such as call comments and call IDs to the relevant Salesforce case.

## Activities Used in Flow

**Start (NewPhoneContact)**
- Captures the incoming call details and begins the flow.

**Set Phone Number (SetPhoneNumber)**
- Formats the captured phone number for Salesforce API lookup.

**Account Lookup (AccountByANI)**
- Performs an HTTP GET request to Salesforce, retrieving the customer’s account details based on the phone number.

**Contact Lookup (ContactByANI)**
- Fetches the contact associated with the phone number via a Salesforce SOQL query.

**Case Lookup (CasebyContactId)**
- Retrieves the open cases linked to the contact, fetching case details including case number and ID.

**Queue Contact (QueueContact)**
- Routes the call to the appropriate agent based on the retrieved Salesforce information and customer priority.

**Play Music (Music)**
- Plays hold music while the customer waits to be connected to an agent.

**Screen Pop (ScreenPopAccount)**
- Opens the customer’s Salesforce account page on the agent's desktop when the call is answered.

**Post Comment (PostComment)**
- Posts the call details to the relevant Salesforce case once the interaction is complete.

**End Flow (EndFlow)**
- Ends the flow after completing all tasks.


## Additional Details

For more information on configuring Salesforce with Webex Contact Center, visit:

- [Salesforce REST API Introduction](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee)

For a comprehensive Video Configuration Walkthrough Watch the 2 Part series below

#### [Part 1 of 2: Configure Salesforce HTTP Connector](https://app.vidcast.io/share/51d8f1c7-f1ae-4963-97c2-73102a85fbf3)

#### [Part 2 of 2: Configure Salesforce HTTP Connector](https://app.vidcast.io/share/82e9adf5-cd50-43ce-9ac4-3a34d7a23e03)
