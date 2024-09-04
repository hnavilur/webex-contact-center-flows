# HTTP Connector for ServiceNow - Template

## Name
ServiceNow HTTP(S) Data Dip

## Labels 
Intermediate, Voice, Inbound, Data dip, CRM

## Description

This flow integrates Webex Contact Center with ServiceNow using an HTTP connector for routing decisions and extracting incident details via ServiceNow's REST APIs. It demonstrates how to securely retrieve and update incidents and other object types in ServiceNow through Webex Contact Center.

## Details

The flow handles an inbound voice call in a contact center and integrates it with ServiceNow to perform an ANI lookup, fetch relevant information, and provide personalized services. Below is the process flow:

1. A call is received by Webex Contact Center.
2. A welcome message is played to the caller, mentioning their incident details.
3. The system performs a lookup in ServiceNow using the ANI to fetch the caller's `sys_id` to get the caller's Object identifier on Service Now.
4. Based on the `sys_id`, the system looks up the active incident for the caller.
5. The incident number is played back to the caller.
6. The call is queued for the next available agent, prioritized based on incident severity.
7. Hold music is played while the caller waits in the queue.
8. Once the call is connected to an agent, the incident information is displayed on the agent's desktop.
9. Post-call, Webex Contact Center posts call information back to the relevant incident in ServiceNow.

### Pre-Requisites

Before configuring this flow, ensure the following:

- **OAuth2 Setup**: Configure OAuth2 in ServiceNow and Webex Contact Center, following the [video tutorial](https://app.vidcast.io/share/22e511b2-cb81-474d-a6c6-982214d0e473).
- **Admin Setup in Webex**: Log into [admin.webex.com](https://admin.webex.com) and configure the connector:
  - Go to: `Contact Center > Connectors > Custom Connector > OAuth2`
  - Enter the necessary credentials as outlined in the tutorial.

### Use Case

The integration demonstrates how Webex Contact Center can enhance customer experience through personalized interactions, while leveraging ServiceNow for ANI lookups and incident management:

1. **Inbound call**: Customer calls into Webex Contact Center.
2. **ANI Lookup**: Webex performs an ANI lookup in ServiceNow to identify the caller.
3. **Incident Lookup**: ServiceNow retrieves the associated Incident ID based on the caller's details.
4. **Personalized Greeting**: Customer is greeted with a personalized message, referencing their active incident.
5. **Routing and Prioritization**: Calls are routed based on the incident's severity, ensuring critical issues are addressed first.
6. **Agent Assignment**: The call is routed to an available agent, with incident details displayed on the agent's desktop.
7. **Post-Call Updates**: Webex Contact Center posts relevant call information, including call identifiers, to ServiceNow using event flows.


### Activities Used in Flow

Below is a list of activities used in the flow along with a description of their role in the integration:

**Start (New Phone Contact):**
- The flow begins when an inbound call is received.

**Play Message (Greeting):**
- Plays a welcome message using Cisco Cloud Text-to-Speech, such as: 
  "Welcome to ServiceNow demo. Your incident number is: {{incidentNum}}"

**Set Variable (Digit Strip ANI):**
- Strips the international code (+1) from the ANI for exact matching.

**Set Variable (Format ANI):**
- Formats the ANI into ServiceNow's required format for queries: `(123) 456-7890`.

**HTTP Request (Lookup User):**
- Looks up the user’s `sys_id` in ServiceNow using their ANI.

**HTTP Request (Lookup Incident):**
- Uses the `sys_id` to retrieve the caller's active incident from ServiceNow.

**Play Message (Incident Number):**
- Announces the incident number to the caller using Text-to-Speech.

**Queue Contact (Queue to Agent):**
- Places the caller in the queue for the next available agent, based on incident severity.

**Play Music (Hold Music):**
- Plays hold music while the caller is in the queue.

**Post Call (Post Comments to ServiceNow):**
- Posts the call information, including the incident number, back to ServiceNow once the call ends.

### Additional Details

To explore and test the REST APIs, you can import the ServiceNow API Postman collection (`ServiceNow API Collection.postman_collection.json`) into Postman. This helps in understanding which APIs are available and how they interact with Webex Contact Center.

- **ServiceNow REST API Documentation**: [REST API Docs](https://docs.servicenow.com/bundle/paris-application-development/page/integrate/inbound-rest/concept/c_RESTAPI.html)
- **ServiceNow Table API Documentation**: [Table API Docs](https://developer.servicenow.com/dev.do#!/reference/api/sandiego/rest/c_TableAPI)

For more information on Webex Contact Center Flows, refer to the detailed documentation on help.webex.com.

[Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee)
