# AI Agent Scripted (Doctor's Appointment Booking)

## Name
AI Agent Scripted (Doctor's Appointment Booking)

## Labels 
Advanced, Voice, AI Agent Studio, Virtual Assistant

## Description

This template demonstrates the data flow between Webex Contact Center and Webex AI Agent Studio for an interaction that leverages a scripted agent. The flow contains several integrations with external systems. These are invoked based on custom events sent by AI Agent and the fulfilment data is passed back to the agent.

## Details

This flow showcases how data is passed between Webex Contact Center and Webex AI Agent Studio using custom events. This flow facilitates automated scheduling and management of doctor's appointments through a scripted AI agent. It integrates with external systems to check availability, create appointments, look up existing appointments, and cancel appointments. The flow ensures seamless communication between the caller and the AI agent, with escalation options to human agents when necessary.
### Pre-requisites

To use this flow, ensure the following are set up:

- A scripted AI Agent configured with relevant intents to handle appointment booking and cancellation. This can be imported from templates while creating a new scripted agent in the AI Agent Studio platform.
- Entry Point, Queue, Teams, and Entry Point Mapping configured in the Control Hub settings page for Webex Contact Center.
- APIs to interface with the external appointment management system.
- Cisco Text-to-Speech (TTS) is enabled for generating dynamic audio messages.
- Upload static audio files if you are not using Cisco’s default audio.

### Integration Breakdown

1. **Caller initiates contact**: The call is received by Webex Contact Center and directed to the AI agent.
2. **Interaction with AI agent**: The AI agent processes customer input and responds based on configured intents.
3. **Switching of control between AI agent and flow**: The control of the conversation is exchanged between the AI Agent and the flow at various steps. AI agent hands the control to the flow via custom events, the flow carries out appropriate fulfilment based on the event name and hands the control back to the AI Agent along with fulfilment data via State Event in the Virtual Agent V2 Activity.
4. **Queue to Agent**: If escalation is required, the caller is placed in a queue for a human agent.
5. **Disconnect**: The interaction ends once the task is completed or the caller is transferred to an agent.

### Activities Used in the Flow

**Start**

- This activity marks the beginning of the flow, triggered by a new call.

**Virtual Agent V2 (VAV2)**

- The activity responsible for AI Agent interaction. The same activity is used to initiate the conversation and to send state events to the AI agent.

**Parse**

- Used to parse event payload from the VAV2 activity.

**Case**

- Used to check the event name sent by the VAV2 activity and branch to appropriate HTTP request activities.

**HTTP Request**

- Interacts with external systems to perform operations like checking availability, creating, looking up, or cancelling appointments using HTTP requests based on the event name sent by the VAV2 activity. The activity also parses the response for the HTTP request.

**Condition**

- Evaluates the outcome of HTTP requests, directing the flow based on success or error conditions.

**Set Variable**

- Used to configure variables like event name and event data, which are essential for re-invoking the VAV2 activity with appropriate state event parameters.

**Play Message**

- Provides system messages using Cisco Text-to-Speech. Used to play an error message before escalation to human agent in case of VAV2 activity errors.

**Queue to Agent**

- Manages queueing logic for escalation to human agents.

**Play Music**

- Hold music played during queueing when the caller awaits agent connection.

**Disconnect Contact**

- Ends the interaction after completion of tasks or if escalated to a human agent.

### Flow Specifics

The flow JSON used in this example contains variables and activities essential for interaction handling, error processing, and communication between Webex Contact Center and DialogFlow. The key variables used include:

- `event_name`: Name of the event sent to the AI Agent.
- `event_data`: Event payload sent to the AI Agent.
- `event_data_string`: String version of event_data since the VAV2 activity accepts string only.
- `http_input`: Request body for the HTTP activity based on VAV2 metadata.
- `Global_VoiceName`: Determines the voice used for text-to-speech.

### Error Handling

The flow includes error management strategies to handle unexpected issues gracefully, ensuring the caller is informed and redirected appropriately.

### Additional Resources

For deeper insights into setting up your AI Agents on Webex AI Agent Studio and using them with Webex Contact Center, refer to [Webex AI Agent Studio Administration Guide](https://help.webex.com/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide)

## Developer Support

For any support regarding this integration, open a ticket with the Webex Contact Center Developer Support team via the [Webex Developer Portal](https://developer.webex-cx.com/support).

For further discussions, visit the [Webex Contact Center APIs Developer Community](https://community.cisco.com/t5/contact-center/bd-p/j-disc-dev-contact-center).
