# Business Rules Engine (BRE) ANI/Area Code Template

## Name
Business Rules Engine (BRE) ANI or DNIS or Area Code Lookups

## Labels 
Basic, Voice, Inbound, BRE, Lookup, Datadip

## Description

This flow template is designed for use in contact centers to demonstrate how to perform ANI (Automatic Number Identification) and Area Code lookups using the Business Rules Engine (BRE). The template showcases how to set up different lookups based on ANI, DNIS (Dialed Number Identification Service), and Area Code, providing routing or further actions based on the returned lookup values. In this template, we dynamically assign the Queue using the Queue ID which is stored in BRE.

## Details

This sample flow is tailored for lookups within Webex Contact Center's Flow Designer. It demonstrates how to retrieve and use key information from an external system using the BRE to enhance customer interaction, providing better routing or information-based decision-making.

**Key Features:**
- Lookups for ANI, DNIS, and Area Code through a Business Rules Engine (BRE) request.
- Handling of various cases for when lookups are successful or fail.
- Support for dynamic routing based on the lookup results, enhancing customer experiences.
- Extra logging for the Flow Debugger and viewing the results on the Agent Desktop.

### Pre-requisites

1. **Business Rules Engine (BRE) Setup**: The necessary tables and keys (e.g., `ANILookup`, `DNISLookup`, `AreaCodeLookup`) should be set up and configured on the Webex Contact Center Business Rules Engine.
2. **Audio Files**: Prepare and upload audio files or utilize Cisco Text-to-Speech (TTS) for prompts used in the flow.
3. **Queues and Teams**: Ensure proper configuration of dynamic queues or agent teams in the Webex Control Hub.

### Flow Breakdown

1. **Call Received**: The flow starts when a call is received by Webex Contact Center.
2. **ANI/DNIS/Area Code Menu**: The system asks the caller to select the type of lookup they want—based on ANI, DNIS, or Area Code.
3. **Set Lookup Key**: The lookup key is set based on the selected option (ANI, DNIS, or Area Code).
4. **Set Table**: The appropriate lookup table is selected (ANILookup, DNISLookup, or AreaCodeLookup).
5. **BRE Request**: A BRE request is made using the selected lookup key and table.
6. **Check Lookup Result**: The result of the lookup is checked.
   - If found, the appropriate routing or next action is taken.
   - If not found, a message is played, and the caller is routed to an agent.
7. **Routing**: The flow dynamically queues the caller based on the lookup result.

### Activities Used

**Start (NewPhoneContact)**
- This activity triggers when a new phone contact is initiated.

**Menu (EnterLookup)**
- The system prompts the customer to select the type of lookup: ANI, DNIS, or Area Code.

**Set Variable (SetLookupKey1, SetLookupKey2, SetLookupKey3)**
- Based on the selected lookup type, the corresponding variable is set for the lookup key.

**Set Variable (SetTable, SetTable2, SetTable3)**
- Sets the appropriate lookup table for BRE: ANILookup, DNISLookup, or AreaCodeLookup.

**BRE Request (BRERequest_6vy)**
- Sends the request to the BRE with the selected lookup key and table.

**Set Variable (SetVariable_03p, SetVariable_b9h)**
- Logs the BRE response body and code for further handling.

**Condition Check (Condition_yvw)**
- Evaluates whether the lookup was successful.

**Play Message (PlayMessage_c24, PlayMessage_kzj, PlayMessage_owy)**
- Plays messages based on the result of the lookup (e.g., "Information found" or "Information not found").

**Queue Contact (Queue)**
- Dynamically queues the caller to an agent based on the lookup result.

**Hold Music (Music)**
- Plays music while the caller waits in the queue.

**Disconnect Contact (DisconnectContact)**
- Ends the call if necessary.

### Additional Details

For more information on configuring BRE tables and lookups, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).