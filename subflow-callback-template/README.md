# Collect Callback Info Subflow - Template

## Description

Use this template to create a callback info collection subflow where callers can choose to stay in the queue or opt for a callback. This subflow is useful when callers need flexibility in receiving service, allowing them to remain in the queue or enter a callback request. 

## Details

This subflow provides a menu that allows callers to opt for a callback or remain in the queue. If the callback option is chosen, it will collect the necessary information for a callback, either using the caller's current number or an alternate number.

Modify the subflow to ensure smooth caller experience by handling errors or unknown conditions, such as timeouts and invalid inputs.

> Note: The Subflow uses Cisco Text-to-speech (TTS) for all the audio activities that require prompts.
> 
> For music, it defaults to the `defaultmusic_on_hold.wav` file available out of box.
> 
> For organization-specific configuration activities such as Queue, Entry Points, Connectors, Outdial ANI, etc., these need to be manually configured by the user before the template is published.

### Pre-requisites

- Create Entry Point, Queue, Teams, and Entry Point Mapping from the Webex Contact Center Management Portal. Refer to the Webex Contact Center Setup and Administration Guide.
- This Subflow uses Cisco TTS (Text-to-speech). Upload required static audio files if using your own audio for the prompts.
- Ensure that the callback variables (e.g., `callbackNumber`, `callbackNumberEntered`, `stayInQueue`) are mapped correctly to your system to capture the appropriate data.

### Subflow Inputs

1. `callbackNumber` - STRING: The number to use for the callback (either the one the caller is calling from or a new number).
2. `stayInQueue` - BOOLEAN: Indicates whether the caller chose to remain in the queue (True) or request a callback (False).

### Subflow Outputs

1. `callbackNumberEntered` - STRING: The number that the caller entered for the callback, if they chose to provide an alternate number.
2. `stayInQueue` - BOOLEAN: Whether the caller opted to stay in the queue or receive a callback.

### Subflow Breakdown

1. **Start Subflow:** The call enters the subflow.
2. **Opt-Out Menu:** The caller is presented with an option to either stay in the queue or receive a callback.
   - Press 1 for callback.
   - Press 2 to stay in the queue.
3. **Number Menu:** If the caller chooses to receive a callback, they are presented with the option to:
   - Press 1 to use the number they are calling from.
   - Press 2 to enter a new callback number.
4. **Collect Digits:** If the caller chooses to enter a new callback number, they are prompted to input their 10-digit number followed by the pound key (#).
5. **Set Variable:** The collected callback number is stored in the `callbackNumberEntered` variable.
6. **End Subflow:** The subflow ends after collecting the callback information or handling any errors.

### Activities Used

**Start Subflow**
- The subflow begins when invoked.

**Opt-Out Menu**
- This presents an option to the caller to either stay in the queue or receive a callback.
- This uses TTS to ask the caller to press 1 for a callback or 2 to stay in the queue.

**Number Menu**
- If the caller chooses a callback, they are prompted to either use their current number or enter a new one.

**Collect Digits**
- If the caller chooses to enter a new number, this activity collects their 10-digit number followed by the pound sign (#).

**Set Variable**
- The collected number is stored in the `callbackNumberEntered` variable for further use.

**End Subflow**
- The flow concludes after handling the caller's choices and collecting the necessary information.

### Additional Details

For more information on configuring subflows, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).
