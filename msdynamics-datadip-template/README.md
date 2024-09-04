# Webex Contact Center - IVR HTTP Connector for MS Dynamics

## Name
Microsoft Dynamics HTTP(S) Data Dip

## Labels 
Intermediate, Voice, Inbound, Data dip, CRM

## Description

This template is designed to create an IVR flow in Webex Contact Center that connects with MS Dynamics using an HTTP connector. The flow fetches customer and case details based on the ANI (Automatic Number Identification) from the CRM and makes routing decisions accordingly. The caller is greeted with a personalized message based on the CRM data, and if no case is found, the call is transferred to an agent. The agent is provided with the customer or case details in real time via a screen pop.

## Details

The flow interacts with MS Dynamics through two HTTP requests: 
1. Fetches customer details by performing an ANI lookup. 
2. Retrieves the most recent case details based on the customer ID.

In case no customer or case information is found, the call will be routed to an agent, and the appropriate message will be played to the caller. The agent receives a screen pop showing either a "New Case" form or the details of the last created case for the customer.

### Integrations 
- The flow integrates MS Dynamics CRM via secure HTTP requests.
- All the necessary configurations for OAuth 2.0 and connector setup in the Webex Control Hub are prerequisites.
- Screen pops are enabled to ensure agents are equipped with the necessary information when answering calls.

> **Note:** The flow uses Cisco Text-to-speech for dynamic prompts. If static audio is required, users can upload audio files. Default hold music is used from the Webex repository.

## Pre-requisites

1. Application registered in Azure for MS Dynamics CRM.
2. Webex Control Hub set up with the HTTP connector using OAuth 2.0.
3. Import the template into Flow Designer.
4. Adjust the flow variables, queues, and any specific configurations based on your organizational needs.

## Flow Breakdown

1. **Call Received:** The caller's ANI is captured.
2. **Strip ANI:** The "+" country code is removed from the ANI.
3. **Fetch Customer Info:** An HTTP request is made to MS Dynamics CRM to look up customer details using the stripped ANI.
4. **Condition Check - Customer Exists:** 
   - If the customer exists, another HTTP request is made to fetch their case details.
   - If the customer doesn't exist, a "No Case Found" message is played.
5. **Play Personalized Case Info:** If a case is found, the caller is greeted with details of their last case.
6. **Route to Agent or Disconnect:** The caller is then offered the option to speak to an agent or disconnect.
7. **Screen Pop for Agent:** When the agent answers, the case details or new case form is presented in a new browser tab.

## Activities Used in Flow

**Start**

- Initiates the flow when the call is received.

**Strip ANI**

- Strips the "+" country code from the ANI to prepare for the MS Dynamics lookup.

**Get Customer Info**

- An HTTP GET request is sent to retrieve the customer’s full name and contact ID based on the ANI.

**Condition Check - Customer Exists**

- Checks if the customer exists in MS Dynamics. 
   - If true, fetches the case details.
   - If false, plays a message informing the caller that no case was found.

**Get Case Info**

- Retrieves the case title and case number using the customer’s ID from the previous step.

**Play Personalized Message**

- Greets the caller by name and provides case details using TTS (Text-to-Speech).

**Play No Case Found**

- Plays a message if no case is found for the caller and informs them they will be transferred to an agent.

**Main Menu**

- Offers the caller the choice to connect with an agent or disconnect the call.

**Queue Contact**

- Routes the caller to an available agent based on predefined queue settings.

**Play Music**

- Plays hold music while the caller waits in the queue.

**Disconnect Contact**

- Ends the call if the caller chooses to disconnect.

**Screen Pop**

- Pops up the case information or new case form for the agent when the call is answered.

### Additional Details

For step-by-step guidance, refer to the [Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).

For MS Dynamics integration tutorials, visit:
- [How to Configure MS Dynamics HTTP Connector on Webex Contact Center Flow Designer](https://app.vidcast.io/share/17b06533-8391-4327-b51f-0716076b8ea3)
- [MS Dynamics REST API Documentation](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/use-postman-perform-operations)