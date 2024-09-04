# Hello World - Template

## Description

Use this template to create a simple inbound voice flow where callers are greeted with a message and then disconnected. Often used during closed hours.

## Details

This flow provides a simple flow that plays an announcement to the caller.

Modify the flow to ensure a smooth caller experience by handling any errors or unknown conditions.

> Note: The Flow uses Cisco Text-to-speech for all the audio activities that require prompts (if any). 
> 
> For music, it defaults to the `defaultmusic_on_hold.wav` file available out of box.
> 
> For all organization specific configuration activities such as Queue, Entry Points, Connectors, Outdial ANI, etc. those need to be manually configured by the user before the template is published.
>

### Pre-requisites

- Create Entry Point, Queue, Teams and Entry Point Mapping from the Webex Contact Center Management Portal. Refer to the Webex Contact Center Setup and Administration Guide.
- This flow uses Cisco TTS(Text-to-speech). Upload required static audio files if using your own audio for the prompts.


### Flow Breakdown

1. Call is received and enters the flow.
2. A welcome message is played to the caller.
3. The caller is placed in a queue.
4. Hold music is played while the caller waits.

### Activities Used

**Start**

- The flow begins when a call is received

**Play Message**

- The call is directed to the "WelcomeMessage" activity, which plays a welcome message to the caller.
- This uses TTS (Text to speech) but can be a pre-recorded message, greeting the caller or providing some information.

**Disconnect**

- After the welcome message, the call is directed to the disconnect activity.
- This activity disconnects the call, ending the interaction after the message has been played.


## Additional Details

For more information, refer to the detailed documentation on help.webex.com.

[Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee)
