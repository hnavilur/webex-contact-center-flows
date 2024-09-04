# Zendesk HTTP Connector for Webex Contact Center

## Name
Zendesk HTTP(S) Data Dip

## Labels 
Intermediate, Voice, Inbound, Data dip, CRM

## Description

This template outlines a flow designed to interact with Zendesk via the Webex Contact Center's HTTP connector. The flow enables extracting customer data from Zendesk based on ANI (Automatic Number Identification) and fetching corresponding ticket details. Once the information is retrieved, the call is handled accordingly, with routing decisions made based on the severity of the incident or the availability of agents.

The template can be used to perform customer data lookups, manage tickets in Zendesk, and route calls efficiently within Webex Contact Center using data from Zendesk.

## Details

This flow illustrates how to integrate Zendesk’s APIs to enhance customer interactions within Webex Contact Center by using the HTTP connector. The system can perform several actions:
- Lookup a Zendesk user based on ANI (the caller's number).
- Retrieve the user’s most recent unresolved ticket.
- Present relevant ticket details to the customer via IVR.
- Route the call to an agent based on predefined criteria or let the customer opt to disconnect.

This template uses Cisco Text-to-Speech (TTS) for all prompt activities. For custom music, it defaults to the `defaultmusic_on_hold.wav` file provided out of the box. Custom settings for entry points, queues, and audio prompts must be manually configured before publishing the flow.

> **Note:** All organization-specific configurations, such as Queues, Entry Points, and Audio Prompts, need to be customized based on the system setup before deploying the flow.

### Pre-requisites

- Ensure API authentication is enabled in the Zendesk instance via the Admin portal. Follow the steps: **Admin** → **Apps and Integrations** → **APIs** → **Enable API authentication**.
- The Zendesk HTTP connector must be configured using BasicAuth within the Webex Contact Center admin portal.
- Upload any custom audio files if required for prompts.
- Ensure proper configuration of Entry Points, Queues, and Teams in the Webex Contact Center Management Portal.

### Use Case

A customer calls into the Webex Contact Center, and the following flow occurs:
1. An ANI lookup is performed to fetch the customer details from Zendesk.
2. The most recent ticket associated with the customer is retrieved.
3. The customer is greeted via an IVR and informed of the status of their ticket.
4. The customer can either:
   - Connect to an agent.
   - Disconnect if they choose not to speak to an agent.

Post-call, the system can update the Zendesk ticket with relevant call information.

### Flow Breakdown

1. **Call Received**: The call enters the system and the Zendesk connector starts.
2. **Lookup User in Zendesk**: The system performs a lookup in Zendesk using the caller's number.
3. **Fetch Ticket Details**: The system retrieves the most recent unresolved ticket for the user.
4. **Present Ticket Details**: The customer is informed of the ticket status via an IVR message.
5. **Menu Options**: The customer can choose to speak to an agent or disconnect.

### Activities Used

**Start**

- The flow begins when a call is received.

**Lookup User (Zendesk)**

- This activity performs an HTTP request to Zendesk, searching for the user based on their ANI.

**Fetch Ticket Details**

- Another HTTP request is made to Zendesk to retrieve the most recent ticket for the user.

**Present Ticket Details**

- A message is played to the caller via TTS, providing information about their ticket's status.

**Confirmation Menu**

- The system presents a menu to the customer, allowing them to either connect to an agent or disconnect.

**Queue Contact**

- If the customer chooses to connect to an agent, they are placed in a queue.

**Play Music**

- Hold music is played while the customer waits for an agent.

**Post Comments (Zendesk)**

- After the call, the system posts a comment on the Zendesk ticket summarizing the interaction.

**Disconnect**

- The system disconnects the call if the customer opts to disconnect or after the call is completed.

### Additional Details

This flow leverages Webex Contact Center's HTTP connector to interact with Zendesk’s APIs. For further details, refer to:
- [Zendesk API Documentation](https://developer.zendesk.com/documentation/developer-tools/working-with-the-zendesk-apis/exploring-zendesk-apis-with-postman/)
- [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide)