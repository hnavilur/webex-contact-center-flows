# Business Hours - Template

## Name
Business Hours Usage

## Labels 
Basic, Voice, Inbound, Business Hours

## Description

This flow template is designed to help contact centers manage their business hours efficiently by showcasing an example of using Business Hours in Flows. Callers are greeted with a message, and their calls are routed based on the business hours, holidays, and emergency conditions set for the organization. If the contact center is closed, the caller is notified of the closure.

## Details

This sample flow is tailored for business hours management in Webex Contact Center. The flow routes calls based on the contact center's working hours, holiday lists, and emergency overrides, ensuring an optimal caller experience and efficient handling of non-working hours.

**Key Features:**
- Centralized management of working hours, holidays, and emergency overrides.
- Automatic routing based on business hours configuration.
- Cisco Text-to-Speech (TTS) is used for all audio prompts, though custom audio files can be uploaded.
- Default music on hold is provided by `defaultmusic_on_hold.wav`, but this can be customized.

### Pre-requisites

1. **Business Hours Setup**: Create working hours, holiday lists, and overrides in the Webex Control Hub under Contact Center Setup.
2. **Audio Files**: Upload the required audio files for prompts such as the "BusinessHoursOpen.wav" or use Cisco’s TTS feature.
3. **Queue, Teams, and Entry Point Mapping**: Configure these elements in the Webex Contact Center Management Portal.

### Flow Breakdown

1. **Call Received**: A call is initiated and enters the flow.
2. **Business Hours Evaluation**: The system checks if the current time falls within working hours, holidays, or an override condition.
3. **Handling Open Hours**: If the contact center is open, a welcome message is played, and the call is routed to the agent queue.
4. **After Hours**: If the contact center is closed, a closed hours message is played, and the call is disconnected.
5. **Emergency Overrides**: If an emergency override is active, the emergency message is played, and the call is disconnected.

### Activities Used

**Start (NewPhoneContact)**
- The flow begins when a new phone contact is received.

**Business Hours Check (BusinessHours)**
- The system checks whether the contact center is within regular working hours, a holiday, or an emergency override.

**Working Hours Prompt (WorkingHours_Prompt)**
- During working hours, a message is played to inform the caller that the contact center is open (file: `BusinessHoursOpen.wav`).

**Queue Contact (Agent_Queue)**
- The caller is placed in the queue to be routed to an available agent.

**Hold Music (HoldMusic)**
- Music is played while the caller waits in the queue (default file: `defaultmusic_on_hold.wav`).

**Holiday Closed Message (Holiday_Closed)**
- If it’s a holiday, a message is played informing the caller that the office is closed.

**After Hours Prompt (AfterHours_Prompt)**
- If it’s after business hours, a message is played to inform the caller that the office is closed.

**Emergency Override (Override_Emergency)**
- In the case of an emergency override, an emergency message is played.

**Disconnect Contact (DisconnectContact)**
- After the message is played (whether it’s after hours, a holiday, or an emergency), the call is disconnected.

### Additional Details

For more information on configuring business hours, holiday lists, and overrides, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).
