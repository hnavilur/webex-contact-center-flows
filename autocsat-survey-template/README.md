# Post Call Survey - Auto CSAT Template

## Name
Post Call AutoCSAT DTMF Survey Template

## Labels 
Survey, Voice, Inbound, Feedback

## Description

This flow template is designed to help contact centers efficiently gather customer feedback through a simple automated post-call survey using DTMF tones. Customers are prompted to rate their experience, and their responses are collected for analysis as the survey response in a global variable used for reporting. The survey captures customer satisfaction ratings on a scale of 1 to 5.

## Details

This flow contains the functionality for a IVR (Interactive Voice Response) powered Post Call Survey (PCS) system. The survey is designed to capture customer satisfaction ratings efficiently and effectively using a basic menu and touch tone IVR.

### Usage

> To use this flow effectively as a "Post call Survey" flow, use this flow by connecting a **GoTo Flow** from the **AgentDisconnected** Event Flow on your main flow. 
> This ensures that when the Agent disconnects the call, the caller is presented with the Post Call IVR Survey that captures CSAT data required to train the AutoCSAT model.

### Pre-Requisites

> Before using this template effectively, you will need to create the Global Variable: **Global_FeedbackSurveyResponse** of type Integer. 
> Please refer to the details below on the exact values.

### Variables

- **CounterSurvey**
  - **Type**: INTEGER
  - **Default Value**: 0
  - **Description**: Tracks the number of survey attempts and increments with each invalid or timeout response.

- **Global_FeedbackSurveyResponse**
  - **Type**: INTEGER
  - **Default Value**: 0
  - **Source**: GLOBAL VARIABLE
  - **Description**: Stores the customer's rating response or "NoResponse" in case of invalid/timeout scenarios. This is a Global Variable of Integer Type with default value 0.

### Activities Used

The process includes several activities arranged in a flowchart, ensuring smooth operation of the survey:

1. **NewPhoneContact**
   - **Purpose**: Starts the survey when a new phone contact is initiated.
   - **Event**: NewPhoneContact

2. **SurveyOptions (IVR Menu)**
   - **Description**: Prompts the user to select a rating (1-5).
   - **Options**: 1, 2, 3, 4, 5 (Corresponding to satisfaction levels)
   - **Handling**: Timeout or invalid response leads to a retry.

3. **SetResponse**
   - **Purpose**: Captures the user’s selection and stores it in SurveyResponse.

4. **SetCounterSurvey**
   - **Purpose**: Increments the CounterSurvey variable after a timeout or invalid response.

5. **CheckCounterSurvey**
   - **Purpose**: Validates if the number of retries exceeds 2.
   - **Condition**: CounterSurvey > 2
   - **Action**: Ends the survey if retries are exhausted.

6. **SetVariable_r3k**
   - **Purpose**: Assigns "NoResponse" to SurveyResponse if retries are exhausted.

7. **PlaySurveyRecorded**
   - **Purpose**: Plays a thank-you message after capturing the response.

8. **DisconnectContact**
   - **Purpose**: Ends the call gracefully.

## Flow Logic

1. **Prompt for Response**
   - The user is prompted with the message: "Please rate your experience on a scale of 1 to 5. Press the corresponding number on your keypad."

2. **Response Handling**
   - If the user selects 1-5, the choice is stored in SurveyResponse.
   - If the user fails to respond or selects an invalid option, CounterSurvey is incremented, and the prompt is replayed.

3. **Retry Limit**
   - After 2 invalid attempts, the survey ends, and "NoResponse" is recorded.

4. **Call Termination**
   - A thank-you message is played: "Thank you for your response."
   - The call is then disconnected.

### Variables and Prompts Mapping

| Variable        | Usage                                 | Default Value |
|-----------------|---------------------------------------|---------------|
| CounterSurvey   | Tracks retries for invalid responses. | 0             |
| Global_FeedbackSurveyResponse  | Stores the customer rating or timeout.| "NoResponse"  |

| Prompt                       | Description                      |
|------------------------------|----------------------------------|
| "Select 1 to 5"              | Played during rating prompt.     |
| "Thank you for your response." | Played at the end of the survey.|

### Error Handling

- **Global Error Handling**: Captures and logs any unexpected errors during the flow.
- **Invalid Input**: Prompts the user to re-enter a valid option.
- **Timeout**: Re-prompts after 3 seconds of inactivity.

## Customization

1. **Prompt Messages**: Modify the Prompt's TTS values for customized voice prompts.
2. **Timeout Duration**: Update the `entryTimeout` property under SurveyOptions to change the wait duration for a response.

### Additional Details

For more information on configuring surveys and managing responses, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).