# Agent Greeting Recording Template

## Name
Record Agent Greeting Template

## Labels 
Voice, Outbound, Agent Greeting Recording

## Description

This flow template provides agents to record their personal greeting, listen to it and choose to save or reject via a Telephony User Interface (TUI). This template improves customer experience and operational efficiency.


## Details

This flow template enables administrators to allow agents to record their personal greetings, listen to them, and decide whether to save or discard the recording directly through a phone interface. This functionality complements the manual greeting management available in Control Hub. It is particularly useful for large organizations that want to empower each agent to create personal greetings aligned with the greeting purposes defined by the organization's administrators.


### Pre-requisites

1. **OutDialEP**: System Generated OutDial EP for making outbound calls.
2.  <check if any other prerequisites>.

### Flow Breakdown

1. **New Phone Contact (NewPhoneContact)**: The flow begins when an outbound phone call is received by Webex Contact Center.
2. **Play Message (Menu_62n)**: An instructional messsage on how to record the Agent Greeting is played to the Agent.
3. **Record Message**: The message is recorded 
3. **Recording Processing Menu (Menu_62n)**: The system asks if the agent the  wants. Agents can select:
   - Press 1 to listen to the recording.
   - Press 2 to re-record.
   - Press 3 to upload and save the recording.
   - Press 2 to reject the recording.
4. **Call Termination (DisconnectContact)**: The call will automatically drop after agent makes his choice and the action is executed ,or when the retry limit is exhausted in case of erred input or when the flow runs into a error it cannot recover from.


### Activities Used

**Start (NewPhoneContact)**  
- Initiates the flow when a new phone contact is received.

**Play Message (PlayMessage_xan, PlayMessage_nvk, PlayMessage_3qt,PlayMessage_zgt,PlayMessage_pyt,PlayMessage_j0n,PlayMessage_cjf,PlayMessage_6f5,PlayMessage_v6m,PlayMessage_zr2,PlayMessage_cjf_eyn)**  
- Plays instructional messages to the agent during the flow to help process the recording. Prompts are generated using Cisco Cloud TTS.

**Menu (Menu_ozf)**  
- Presents menu options to agents for agent greeting recording processing.

**Set Variable (SetVariable_1q7, SetVariable_9l0,SetVariable_u61)**  
- Sets variables for to maintain variables to track retry exhaustion.

**Condition (Condition_6a1, Condition_775,Condition_czm)**
- To check for retry exhaustion.

**Upload Audio(UploadAudio_9ax)**  
- Uploads the saves the recoding.

**Record (Record_o10)**  
- Records the agent’s greeting message.

**Disconnect Contact (DisconnectContact)**  
- Ends the call once all flow actions are completed.

### Additional Details

This is a system generated flow and is to be used internally within the system.It is not intended for direct use by customers.