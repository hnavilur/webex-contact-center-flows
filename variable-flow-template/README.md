# Variable Flow Template

## Name
Dynamic Variable Support

## Labels 
Intermediate, Voice, Inbound

## Description

This template provides an advanced, dynamic inbound voice flow that retrieves external settings, setting the flow variables with those settings and routes calls based on the variable configurations. This is often used for scenarios requiring flexibility in call handling based on real-time business conditions like working hours or holidays - where a single flow can be reused across different use cases using dynamic variable based routing.

## Details

The flow dynamically fetches flow settings via an HTTP request and sets variables that guide the rest of the flow. These variables manage routing decisions, queue handling, prompts, and error management.

The flow ensures a smooth and efficient caller experience by playing appropriate messages, handling working hours or error cases, and providing routing based on the organization's specific requirements.

> Note: The flow uses Cisco Text-to-Speech for all the audio activities requiring prompts. Custom music on hold or messages can be configured by updating the flow variables. Additionally, organization-specific configurations like Queue, Entry Points, Outdial ANI, and others need to be set up before publishing this flow.

### Pre-requisites

- Configure Entry Point, Queue, and other necessary settings in Webex Contact Center Management Portal. Refer to the Webex Contact Center Setup and Administration Guide.
- Ensure that any required static audio files or custom TTS prompts are uploaded to the system.
- Have a valid API endpoint to fetch the flow settings.

### Flow Breakdown

1. **New Phone Contact:** The flow begins when a call is received at the entry point.
2. **HTTP Request:** The flow makes an HTTP request to fetch flow settings dynamically based on the call’s DNIS.
3. **Business Hours Check:** Depending on the flow settings, the flow checks business hours, holidays, and overrides to route the call appropriately.
4. **Play Message (Welcome):** Based on the fetched settings, a welcome message is played using TTS or a pre-recorded prompt.
5. **Queue Activity:** If necessary, the call is placed in a queue based on dynamic variables.
6. **Play Music (Queue Management & Music in Queue):** While the caller waits in the queue, hold music is played, which can be dynamically set.
7. **Error Handling:** If any error occurs, the call is redirected to an error handling flow or a different entry point using the GoTo enabled by dynamic variables.

### Activities Used

**Start:**

- The flow starts when a call is received through the `NewPhoneContact` activity.

**HTTP Request:**

- The `FetchFlowSettings` activity makes an HTTP request to retrieve all necessary flow settings, such as business hours, prompts, and queue configurations.

**Set Variables:**

- The `SetVariable` activity stores the data retrieved from the HTTP request and assigns values to flow-related variables like `businessHours`, `queue`, `welcomePrompt`, and `holdMusic`.

**Business Hours:**

- The `BusinessHours` activity checks the working schedule, holidays, and overrides, directing the flow based on the current time.

**Play Message:**

- The `PlayMessage` activity plays a welcome message to the caller. This can be set dynamically or pre-configured.

**Queue Contact:**

- The `QueueContact` activity places the caller in the appropriate queue, utilizing dynamic variables for queue management and fallback handling.

**Play Music:**

- The `PlayMusic` activity plays hold music to callers waiting in the queue, configured based on the `holdMusic` variable.

**Go To:**

- Multiple `Go To` activities are used to navigate between different parts of the flow or handle specific conditions like holidays or errors.

**Disconnect:**

- After all necessary steps are completed, the flow ends with the appropriate disconnect or redirection.

### Additional Details

For more information, refer to the detailed documentation on [Webex Contact Center Flow Designer - Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide#Cisco_Generic_Topic.dita_e338e055-64b0-4973-bd52-8a5581dcb0ee).
