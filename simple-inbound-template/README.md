

## Description

A simple inbound voice flow where callers are greeted, and queued to an agent, along with hold music while waiting for an agent.

## Details

This flow provides a straightforward process for handling inbound calls in a contact center:

1. A call is received and enters the flow through the entry point.
2. A welcome message is played to the caller.
3. The caller is placed in a queue for the next available agent.
4. While waiting in the queue, hold music is played to the caller.
5. The call flow handles error conditions gracefully and can redirect the caller if any unexpected issues arise.

### Pre-requisites

- Create Entry Point, Queue, Teams, and Entry Point Mapping from the Webex Contact Center Management Portal. Refer to the [Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee).
- This flow uses Cisco Text-to-Speech (TTS) for the welcome message. If required, upload static audio files for custom greetings.

This flow ensures a smooth experience by placing error-handling mechanisms and allowing fallback scenarios in case agents are not available.

### Activities Used in the Flow

Here are the activities used in the flow:

**Start (New Phone Contact):**
- The flow begins when a call is received via the entry point.
- The call is accepted into the flow and proceeds to the next step.

**Play Message (Welcome Prompt):**
- A message is played to welcome the caller. In this flow, the message says: "Welcome to Webex Contact Center!"
- This message is configured using Cisco TTS, but can be replaced with custom recordings.

**Queue (Direct Contact):**
- After the welcome message, the call is placed into a queue. 
- The queue is set to direct the call to the "Q_arubhatt" queue, which routes the caller to the longest available agent.

**Play Music (Music on Hold):**
- While waiting in the queue, the flow plays hold music. In this case, the default file "defaultmusic_on_hold.wav" is used, and it plays for 30 seconds before looping.

**Play Message (Hold Message):**
- A secondary message is played while the caller is waiting: "Thank you for your patience. Please wait while we find you an expert."
- This message is also handled using Cisco TTS.

**End Flow:**
- The flow terminates upon agent connection or if an error occurs.
- It ensures the caller is smoothly handled, whether they are connected to an agent or if the flow needs to end due to an error.

### Error Handling

- The flow has been designed to handle unexpected issues by terminating gracefully, with fallback routes available.

## Additional Details 

For more information on Webex Contact Center Flows, refer to the detailed documentation on help.webex.com.

[Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee)
