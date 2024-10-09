# Bridged Transfer Flow - Updated Template

## Name
Bridged and Blind Transfer Flow

## Labels 
Voice, Inbound, Transfer, IVR

## Description

This flow template is designed to showcase two types of external transfers using Webex Contact Center. It includes both a **Bridged Transfer**, where the call control is maintained and the call is eventually queued back to the Webex Contact Center, and a **Blind Transfer**, where the call control is handed over to a third party, and Webex Contact Center loses further control over the call. 

This template highlights the configuration of external transfer flows, which are useful when routing calls to outside systems or agents.

## Details

This sample flow demonstrates external call transfers using **Webex Contact Center**. It supports two transfer types:
1. **Bridged Transfer**: Connects to an external IVR while maintaining call control, then transfers back to the Webex Contact Center.
2. **Blind Transfer**: Transfers the call to an external system where call control is lost, completing the process without Webex Contact Center involvement.

**Key Features:**
- Transfer between Webex Contact Center and external IVR systems using Bridged Transfer and further processing of the call by Queueing to a WebexCC Agent using the Queue Activity.
- An Option for a complete handover of the call using Blind Transfer.
- Cisco Text-to-Speech (TTS) is used for the prompts, though these can be replaced with audio files.
- Music-on-hold during queue time (using default file `defaultmusic_on_hold.wav`).

### Pre-requisites

1. **Transfer DN Setup**: Ensure that external transfer destination numbers (DN) are configured. Both bridged and blind transfer DNs need to be correctly specified. A sample value is provided.
2. **Audio Files**: Uses Cisco TTS by default with text input. If using custom audio, upload appropriate audio prompts (e.g., transfer and hold prompts) to the Webex Contact Center.
3. **Queue Configuration**: Ensure proper setup of queues and agents in Webex Contact Center for the Queue Activity.

### Flow Breakdown

1. **New Phone Contact (NewPhoneContact)**: The flow begins when a phone call is received.
2. **Play Welcome Message (WelcomePrompt)**: A welcome message is played to the customer, using TTS.
3. **Choose Transfer Type (ChooseTransferType)**: The customer is asked to choose between a **Bridged Transfer** or a **Blind Transfer**.
   - Press 1 for a **Bridged Transfer**: Transfers the call to an external DN and routes it back to the Webex Contact Center queue.
   - Press 2 for a **Blind Transfer**: Transfers the call to an external DN with no return to Webex Contact Center.
4. **Bridged Transfer (BridgedTransfer_5vu)**: For a bridged transfer, the call is connected to the external target and eventually returned to a WebexCC queue once the call is ended by the remote party.
5. **Blind Transfer (BlindTransfer_uk4)**: For a blind transfer, the call is passed to the external party, ending WebexCC's control of the call.
6. **Queue Contact (Queue)**: After the bridged transfer, the call is queued to a Webex Contact Center agent.
7. **Play Music (Music)**: Plays hold music while the customer waits in the queue.
8. **End Flow**: The call ends when the flow completes, either after a successful transfer or queueing process.

### Activities Used

**Start (NewPhoneContact)**  
- The flow starts when a phone call is received.

**Play Message (WelcomePrompt)**  
- Plays a welcome message using TTS or an uploaded audio file.

**Menu (ChooseTransferType)**  
- Prompts the caller to choose between a bridged or blind transfer.  

**Bridged Transfer (BridgedTransfer_5vu)**  
- Transfers the call to an external DN while maintaining call control, and returns to Webex Contact Center.

**Blind Transfer (BlindTransfer_uk4)**  
- Transfers the call to an external DN, handing over full control to the third party.

**Queue Contact (Queue)**  
- After the bridged transfer, the call is queued to a Webex Contact Center agent.

**Music on Hold (Music)**  
- Plays hold music while the caller is waiting in the queue.

**End Flow (EndFlow)**  
- Terminates the call once the flow is completed.

### Additional Details

For more information on configuring the Bridged Transfer activity in Flow Designer, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).