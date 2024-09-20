# Description

Use this template to create a simple inbound voice flow where callers are greeted with a message and then disconnected. Often used during closed hours.

# Details

This flow provides a simple flow that plays an announcement to the caller:

1. Call is received and enters the flow.
2. A welcome message is played to the caller.
3. The caller is placed in a queue.
4. Hold music is played while the caller waits.

Modify the flow to ensure a smooth caller experience by handling any errors or unknown conditions.

Here are the activities used in the flow:

**Start**

- The flow begins when a call is received

**Play Message**

- The call is directed to the "WelcomeMessage" activity, which plays a welcome message to the caller.
- This uses TTS (Text to speech) but can be a pre-recorded message, greeting the caller or providing some information.

**Disconnect**

- After the welcome message, the call is directed to the disconnect activity.
- This activity disconnects the call, ending the interaction after the message has been played.

### Pre-requisites

- Create Entry Point, Queue, Teams and Entry Point Mapping from the Control Hub settings page for Webex Contact Center. Refer to the Webex Contact Center Setup and Administration Guide.
- This flow uses Cisco TTS(Text-to-speech). Upload required static audio files if using your own audio for the prompts.

## Additional Details

For more information, refer to the detailed documentation on help.webex.com.

[Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee)
