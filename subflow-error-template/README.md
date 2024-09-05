# Error Handling Subflow - Template

## Description

This subflow handles error conditions that may arise during the contact center process, such as issues with queue handling or API requests. It can be attached to specific activities or configured as a global error handler, ensuring that the system continues operating smoothly and provides users with feedback on any issues. 

## Details

The error-handling subflow is triggered by errors in the contact center workflow. When an error occurs, the system plays an error message, informing the user of the technical difficulty. The subflow decides the next steps based on whether the error is resolved or escalated, allowing agents or the system to manage the situation.

This subflow provides the flexibility to handle various types of errors across workflows, ensuring consistent error management. Cisco Cloud Text-to-Speech (TTS) is used to deliver the error messages dynamically through the `errorMessage` variable, which can change based on the error context.

### Pre-requisites

- Ensure that Cisco TTS is enabled for the contact center to use Text-to-Speech for error prompts.
- Map the `errorMessage` variable to dynamically handle the appropriate error messages in your workflow.

### Subflow Inputs

1. `errorMessage` - STRING: The error message to play dynamically, indicating the issue encountered by the caller.

### Subflow Outputs

1. **N/A**: This subflow does not produce outputs as it is used to handle errors and provide feedback to the caller.

### Subflow Breakdown

1. **Start Subflow:** The subflow is triggered when an error occurs.
2. **Play Error Message:** The system plays a dynamic error message defined by the `errorMessage` variable using Cisco Cloud TTS. For example, the message might be “We are experiencing technical difficulties. Please try again later.”
3. **End Subflow (Normal End):** If the error is handled successfully, the subflow ends gracefully.
4. **End Subflow (Error End):** If further issues arise (e.g., the error message fails to play), the subflow ends in an escalation state to indicate a critical failure.

### Activities Used

**Start Subflow**
- The subflow starts when an error occurs, kicking off the error-handling sequence.

**Play Error Message**
- Plays the error message to the caller using Cisco Cloud TTS. The message content is defined dynamically by the `errorMessage` variable.

**End Subflow (Normal End)**
- Ends the subflow if the error is resolved without further issues.

**End Subflow (Error End)**
- Ends the subflow with an escalation if additional errors occur during the error-handling process.

### Additional Details

For more information on configuring subflows, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).
