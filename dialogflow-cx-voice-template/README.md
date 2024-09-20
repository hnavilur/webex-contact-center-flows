# Virtual Agent with Google DialogFlow CX - Template

## Name
Dialogflow CX Virtual Agent

## Labels 
Intermediate, Voice, Inbound, Virtual Agent

## Description

This flow demonstrates the full potential of integrating Google DialogFlow CX with Webex Contact Center, providing enhanced customer interaction with flexible and dynamic data handling.

This template is designed to facilitate an inbound voice flow integrating Webex Contact Center with Google DialogFlow CX. The flow allows for data transfer between the two platforms, playing a welcome message, and directing the caller through interactions with a virtual agent. This flow showcases the integration's flexibility for handling customer inputs and dynamically passing information back and forth between Webex Contact Center and Google DialogFlow CX.

## Details

This flow demonstrates how to pass data from Webex Contact Center to Google DialogFlow CX, allowing you to leverage advanced virtual agent capabilities. It includes examples for handling caller inputs such as names, appointments, and call reasons, with a focus on transferring data seamlessly between both platforms.

You can customize this flow further by adding organization-specific configurations like queues, entry points, and connectors, while also integrating security best practices for production-grade environments.

> Note: 
> - This Flow uses Cisco Text-to-Speech (TTS) for the audio prompts (if any).
> - For any specific configurations such as Queue, Entry Points, Connectors, etc., those will need to be manually configured in Webex Contact Center before publishing the flow.
> - Ensure that any static audio files, if used, are uploaded to the Webex Contact Center system.

### Flow Breakdown

1. Call is received and enters the flow.
2. The caller is directed to an API that retrieves their name from a mock endpoint.
3. A welcome message is played to the caller, including their name, with the help of Google DialogFlow CX.
4. DialogFlow CX virtual agent interacts with the caller to gather inputs such as appointment dates and times.
5. The customer data is passed back to Webex Contact Center for potential further processing.
6. Based on the interaction, the call either escalates or ends.
7. If escalated, the caller is placed in a queue.
8. Hold music is played while the caller waits for an agent.

### Activities Used

**Start**

- The flow begins when a call is received, initiated through the `NewPhoneContact` activity.

**HTTP Request - GetCustomerName**

- The system makes an API request to retrieve the customer's name from an external system via HTTP request.
- The result is stored in a global variable (`DF_CustomerName`) that will be used for further interaction with Google DialogFlow CX.

**Virtual Agent**

- The flow invokes the `VirtualAgent` activity to pass the customer's name and interact with Google DialogFlow CX. 
- The virtual agent gathers information, including call reason, appointment details, etc.

**Parse**

- This activity parses the response received from DialogFlow CX and updates the flow variables (`Call_Reason`, `appointment_date`, `appointment_time`) accordingly.

**Set Variable - Appointment**

- The appointment date and time gathered from DialogFlow CX are formatted and stored in a global variable (`DF_Appointment`).

**Queue Contact**

- After the virtual agent interaction, the customer is placed into a queue to wait for the next available agent.

**Play Music**

- While the caller waits in the queue, the system plays default hold music (`defaultmusic_on_hold.wav`).

**Disconnect Contact**

- If no further action is required, the call is disconnected using the `DisconnectContact` activity.

### Pre-requisites

- Create Entry Point, Queue, Teams, and Entry Point Mapping from the Control Hub settings page for Webex Contact Center.
- Set up the Google DialogFlow CX virtual agent and configure necessary webhook integrations.
- Ensure that you have uploaded any static audio files required for the prompts.

### Additional Details

For further details on integrating Webex Contact Center with Google DialogFlow CX, refer to:

- [Google DialogFlow CX Developer Documentation](https://cloud.google.com/dialogflow/cx/docs)
- [Webex Contact Center Virtual Agent Voice Guide](https://help.webex.com/en-us/article/n6gaghu/Virtual-Agent-Voice-in-Webex-Contact-Center)

For support, visit the [Webex Contact Center Developer Support](https://developer.webex-cx.com/support) or join the [Webex Contact Center APIs Developer Community](https://community.cisco.com/t5/contact-center/bd-p/j-disc-dev-contact-center).
