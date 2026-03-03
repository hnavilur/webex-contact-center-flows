***

# PIN-Authorized Emergency Management Flow - Template

## Name
PIN_Authorized_Emergency_Management_Flow

## Labels 
Admin, Security, API, Emergency, Global Variables, Supervisor

## Description
This flow is an administrative tool designed to provide supervisors with secure, real-time control over the organization's emergency routing status. It utilizes PIN-based authentication and Webex APIs to toggle a global "Emergency" flag, allowing all production flows to instantly react to critical events or service disruptions.

## Details
This flow provides a secure framework for managing organization-wide emergency routing without requiring access to the Flow Designer UI. Authorized users can dial a dedicated number, verify their identity, and update the system state.

> **Note:** This flow uses **Cisco Cloud Text-to-Speech (TTS)** with enhanced **SSML** for all audio prompts to ensure natural-sounding delivery and clear instructions.
>
> **API Integration:** This flow requires a pre-configured HTTP Connector to communicate with the Webex Contact Center APIs.
>
> **Global Variable:** The logic relies on a Global Variable named `Emergency` (Boolean) which must be created in the Management Portal before the flow can function correctly.

### Pre-requisites
- **Global Variable:** Create a Global Variable named `Emergency` (Type: Boolean) in the Control Hub.
- **API Connector:** Set up a connector named `WxCC_API` in the Control Hub with permissions to modify CAD variables. Refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee).
- **Authentication:** The default PIN is hardcoded as `1111` in the `PIN_Check` activity. This should be updated to a secure value before deployment.
- **Placeholders:** Update the `orgId` and `variableId` within the **HTTP_GET**, **Update_True_ON**, and **HTTP_Turn_Off_Emer** activities to match your specific organization.

### Flow Breakdown

1. **Call Entry:**
   - The supervisor dials into the flow, starting at the **NewPhoneContact** activity.

2. **Authentication:**
   - The **CollectPIN** activity prompts the user for a 4-digit code.
   - The **PIN_Check** activity validates the input. If the PIN is incorrect, the call is routed to an error message and disconnected.

3. **Retrieve Current Status:**
   - The **HTTP_GET** activity queries the Webex API to check the current default value of the `Emergency` global variable.
   - The **Case_0bd** activity branches the flow based on the result (`True` or `False`).

4. **Toggle Logic (State 1: Emergency is ON):**
   - If the flag is already `True`, the **CollectDigits_y83** activity informs the supervisor and asks them to **Press 1** to disable it.
   - If confirmed, the **HTTP_Turn_Off_Emer** activity sends a `PUT` request to set the variable to `False`.

5. **Toggle Logic (State 2: Emergency is OFF):**
   - If the flag is `False`, the **CollectDigits_y83_o6y** activity asks the supervisor to **Press 1** to activate the emergency status.
   - If confirmed, the **Update_True_ON** activity sends a `PUT` request to set the variable to `True`.

6. **Confirmation & Success:**
   - Upon a successful API response (HTTP 200), the flow plays a specific success message (**PlayMessage_c4n** or **PlayMessage_Emer_Off**) using natural SSML pacing.

7. **Error Handling:**
   - If an API error occurs or the user provides invalid input, the flow directs the caller to the **PlayMessage_j4c** activity ("Something went wrong. Please reach out to your administrator") before disconnecting.

### Activities Used

**Start**
- **NewPhoneContact:** Triggers the flow when the supervisor dials the entry point.

**Authentication**
- **CollectPIN:** Captures the 4-digit supervisor PIN.
- **PIN_Check:** Validates the entered digits against the authorized PIN.

**API Integration (Webex API)**
- **HTTP_GET:** Retrieves the current state of the Global Variable.
- **Update_True_ON:** Updates the Global Variable to `True`.
- **HTTP_Turn_Off_Emer:** Updates the Global Variable to `False`.

**Decision & Branching**
- **Case_0bd:** Determines the flow path based on the current Boolean value of the emergency flag.
- **HTTPStatusCode / HTTPStatusCode_ujp:** Verifies that the API updates were successful (Response 200).

**User Interaction (IVR)**
- **CollectDigits_y83 / CollectDigits_y83_o6y:** Confirmation menus for toggling the status.
- **PlayMessage (Various):** Success and error announcements using SSML.

**Disconnection**
- **DisconnectContact:** Ends the call after a successful update, an authentication failure, or a system error.

### Additional Details

For more information on managing Global Variables and API Connectors, refer to the detailed documentation on the Webex Contact Center help portal.

[Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee)  
 
