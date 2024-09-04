# Webex Instant Connect Video Escalation - Template

## Name
Webex Instant Connect Video Meeting Integration

## Labels 
Advanced, Voice, Video, SMS, Inbound, Integration, Webex

## Description

This template demonstrates how to set up a simple inbound voice flow that escalates the voice call to a video interaction using Webex Instant Connect's Instant Meeting API. The flow allows customers to connect to agents via Webex Contact Center, and enables video sharing through a voice-to-video escalation via an SMS link, while agents are able to launch the meetin controls via a Screenpop widget. This approach is beneficial in scenarios such as product support or healthcare consultations where real-time video enhances the problem resolution process.

## Details

The flow provides a seamless integration that allows both voice and video communication between customers and agents. Once the customer calls the contact center, they receive an SMS link that opens a video feed for the agent to view the customer's issue, improving support quality.

> Note: The Flow uses Cisco Text-to-speech for all audio activities.  
> 
> For music, it defaults to the `defaultmusic_on_hold.wav` file provided out of the box.  
> 
> Organization-specific configuration activities, such as Queue, Entry Points, Connectors, Outdial ANI, etc., need to be manually configured before publishing the flow.

### Pre-requisites

**Webex Instant Connect must be setup on the Organization**

- Ensure Webex Contact Center is already configured for the organization.
- Enable Instant Connect meeting and SMS features.
- Create a bot account on [developer.webex.com](https://developer.webex.com) to obtain an access token for API calls.
- Entry Point and Queue Configurations for routing, and other telephony configurations should be set up in Webex Contact Center.
- Upload any required static audio files if using custom prompts for the flow - the flow uses Cisco TTS for the templates.

### Flow Breakdown

1. A call is received and enters the flow.
2. The caller is greeted with a welcome message (using Cisco TTS or a pre-recorded message).
3. The caller is placed in a queue and the agent receives an SMS link for video consultation.
4. Hold music is played while the caller waits.
5. The agent joins the video meeting, and the customer receives an SMS with the meeting link.
6. The video meeting occurs while the voice call is maintained.

### Activities Used

**Start**

- The flow starts when a call is received.

**HTTPRequest (Generate Meeting Link)**

- This node creates a meeting link for the agent and customer. It generates the meeting URL via an HTTP POST request using the bot token.

**HTTP Request (Send SMS API)**

- This node sends the SMS link to the customer using the Webex Instant Connect API. The customer can click the link to join the video meeting.

**Play Music**

- The caller hears hold music while waiting for the agent.

**Queue Contact**

- The call is routed to an available agent using the longest available agent algorithm.

**Screen Pop (Open Host Meeting Link)**

- The agent's desktop displays a pop-up with the video meeting link, allowing the agent to join the meeting directly from the desktop.

**End Flow**

- After completing the process, the flow ends.

### Configuration

- **Org ID**: Replace with your organization's Org ID.
- **Token**: Replace with the bot token created from the developer portal.
- **GuestKey**: URL for the guest to join the meeting.
- **HostKey**: URL for the agent to join the meeting.

## Additional Details

For more information on configuration and flow design, refer to the detailed documentation at [Webex Contact Center Setup Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).

View the supporting vidcast on: **[Voice to Video Escalation with Instant Connect](https://app.vidcast.io/share/168c7b94-6fd9-48d1-9457-69d6dc643cc3)**
