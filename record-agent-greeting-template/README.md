# Recording Template

## Name
Record Agent Greeting Template

## Labels 
Voice, Inbound, Recording, Voicemail, Consent, Audio

## Description

This flow template is designed to showcase how to configure consent based call recording and record audio files within Webex Contact Center using the Record activity. The flow demonstrates call recording consent, audio recording for various use cases such as voicemail or allowing the post-call audio recordings using an HTTP request externally storing the audio file. The flow enables customers to record messages that are can be stored or uploaded externally or sent as a voicemail externally, as well as complete a post-call actions like recording an audio snippet of the customer's experience with the call for quality assessment.

## Details

This sample flow demonstrates Webex Contact Center’s capabilities to capture a customer's audio recording. It showcases the following features:
1. **Call Recording Consent**: A feature that provides customers with the option to allow or deny recording.
2. **Voicemail Recording**: Allows customers to record a message, which is then uploaded via an HTTP request for further processing externally.
3. **Post-call Recording**: Automatically initiates an audio recording once the agent ends the call.

**Key Features:**
- Offers customers call recording consent options.
- Provides audio recording capabilities within the Webex Contact Center flow.
- Uses HTTP requests to send customer recordings or audio survey responses to external systems.
- Custom messages and prompts using Cisco Cloud Text-to-Speech.
- Handles customer inputs with options to confirm recordings or re-record messages.

### Pre-requisites

1. **API Setup**: Ensure that an API endpoint is available to accept HTTP POST requests for uploading recordings and survey results.
2. **Audio Files**: Utilize Cisco TTS or if required upload custom audio prompts for the prompts in the flow.
3. **Queue Configuration**: Ensure queues are properly configured for routing calls within Webex Contact Center to agents.

### Flow Breakdown

1. **New Phone Contact (NewPhoneContact)**: The flow begins when a phone call is received by Webex Contact Center.
2. **Call Recording Consent (Menu_62n)**: The system asks if the customer consents to call recording. Customers can select:
   - Press 1 to allow recording.
   - Press 2 to deny recording.
3. **Recording Control (RecordingControl_upx)**: Enables or disables call recording based on the customer’s choice. This is the recording control activity.
4. **Voicemail Option (Menu_9qx)**: The system offers the customer to leave a voicemail or stay in the queue:
   - Press 1 to be placed in the queue.
   - Press 2 to leave a voicemail message.
5. **Voicemail Recording (Record_zfp)**: If the customer selects voicemail, the system records their message, which can be sent using an HTTP request.
6. **HTTP Request (HTTPRequest_dd3)**: Sends the recorded voicemail to an external API for processing.
7. **Post-call Survey (RecordSurvey)**: The flow captures customer feedback post-call.
8. **Call Termination (DisconnectContact)**: Ends the call after completing the survey or recording actions.

### Activities Used

**Start (NewPhoneContact)**  
- Initiates the flow when a new phone contact is received.

**Play Message (PlayMessage_b6d, PlayMessage_jd0)**  
- Plays messages to the customer during the flow. Prompts are generated using Google TTS or Cisco Cloud TTS.

**Menu (Menu_62n, Menu_9qx, Menu_3bk)**  
- Presents menu options to customers for call recording consent, voicemail options, and confirming voicemail recordings.

**Set Variable (SetVariable_qax, SetVariable_q0a)**  
- Sets variables for recording consent and survey opt-in.

**Recording Control (RecordingControl_upx)**  
- Controls the recording of the call based on customer consent.

**Record (Record_zfp)**  
- Records the customer’s message (used for voicemail).

**HTTP Request (HTTPRequest_dd3)**  
- Sends the recorded message to an external API endpoint.

**Disconnect Contact (DisconnectContact)**  
- Ends the call once all flow actions are completed.

### Additional Details

For more information on using the Record Activity, HTTP requests and Recording controls within Webex Contact Center, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).