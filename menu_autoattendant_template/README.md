# Menu Auto Attendant - Template

## Name
Menu Auto Attendant

## Labels 
Basic,Voice,Inbound,Menu,Auto Attendant

## Description

This Auto Attendant template leverages the capabilities of a menu-driven interaction to automate call routing and handle inbound contact actions efficiently. It is powered by Cisco Text-to-speech, and includes dynamic options for callers, such as routing based on menu selection, error handling, and music on hold for queued interactions.

## Details

The flow automates the initial interaction with the caller, allowing them to navigate through various menu options. This allows for efficient call routing to appropriate teams or services, all while ensuring a smooth caller experience. It includes dynamic error handling, multilingual support, and a polite disconnection process in case of errors or unrecognized inputs.

> Note: This flow utilizes Cisco Text-to-Speech for all the audio activities that require prompts (if any). 
> 
> For music, it defaults to the `defaultmusic_on_hold.wav` file available out-of-the-box.
> 
> For all organization-specific configuration activities such as Queue, Entry Points, Connectors, and Outdial ANI, these need to be manually configured by the user before the template is published.

### Pre-requisites

- Create Entry Point, Queue, Teams, and Entry Point Mapping from the Webex Contact Center Management Portal. Refer to the Webex Contact Center Setup and Administration Guide.
- This flow uses Cisco Text-to-Speech (TTS). Upload required static audio files if using your own audio for the prompts.

### Flow Breakdown

1. **Call Received (NewPhoneContact):** The flow is triggered when a new phone contact is initiated by an inbound call.
2. **Welcome Message (WelcomePrompt):** A greeting message is played: "Welcome to the Webex Contact Center!"
3. **Main Menu (IVR Menu):** The caller is presented with a set of menu options. The menu is read aloud using TTS, guiding the caller through different service options:
    - Press 1 for Services Team
    - Press 2 for Sales Team
    - Press 3 for Overseas Team
    - Press 4 for Hours of Operation
    - Press 5 for Frequently Asked Questions
    - Press 6 for Prerequisites
    - Press 7 for Billing Issues
    - Press 8 for a Representative
    - Press 9 for general information
    - Press # to repeat the menu
    - Press * to hang up
4. **Routing Based on Selection:** 
   - Based on the selected option, the caller is either transferred to a specific team (blind transfer) or placed in a queue to wait for the next available agent.
5. **Error Handling:** Invalid inputs are addressed with an error message, and the caller is prompted to try again.
6. **Music on Hold (PlayMusic):** While waiting in a queue, the default hold music (`defaultmusic_on_hold.wav`) is played.
7. **Disconnect:** The flow concludes by disconnecting the call.

### Flow Activities Used

**NewPhoneContact (Start)**

- This is the starting point of the flow when a new phone contact is initiated by an inbound call.

**Play Message (WelcomePrompt)**

- The customer is greeted with a message: "Welcome to the Webex Contact Center!" This step uses Cisco Cloud Text-to-Speech to generate the message.

**Main Menu (IVR Menu)**

- A menu is presented to the caller with various options:
    - Press 1 for Services Team
    - Press 2 for Sales Team
    - Press 3 for Overseas Team
    - Press 4 for Hours of Operation
    - Press 5 for Frequently Asked Questions
    - Press 6 for Prerequisites
    - Press 7 for Billing Issues
    - Press 8 for a Representative
    - Press 9 to speak to the Services team again
    - Press # to repeat the menu
    - Press * to hang up

**Routing Based on Selection (Conditions)**

- Based on the caller's selection, the flow transfers the call to the appropriate team or places it in a queue. Depending on the chosen option, different routes are executed:
    - Blind transfer to the Services or Sales teams.
    - Queue the caller for a representative, with **Music on Hold** playing during the wait.

**PlayMusic (Music on Hold)**

- For queued calls, the system plays hold music while the caller waits for the next available agent.

**Error Handling**

- If an invalid option is selected or the input times out, the system plays a message prompting the caller to try again.

**Disconnect**

- After the interaction is complete or an error occurs, the flow disconnects the call using the **DisconnectContact** activity.

### Additional Use Cases

- **Sub-Menus:** There is a language selection menu, where users can choose their preferred language by pressing 1 for English or 2 for Spanish. The menu repeats if the caller presses #.
- **Error Messages:** When invalid input is received, an error message is played. For critical errors, the system apologizes and disconnects the caller.

## Additional Details

For more information, refer to the detailed documentation on help.webex.com.

[Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee)