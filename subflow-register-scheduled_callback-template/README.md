# Register Scheduled Callback Subflow - Template

## Description

Use this template to create a callback scheduling subflow where callers can schedule a callback by selecting the date, time range, and timezone. This subflow is ideal for organizations wanting to offer callers flexibility in choosing when they wish to be called back, reducing wait times and improving the caller experience. 

## Details

The subflow guides the caller through a series of prompts to collect:

•	The preferred callback date (YYYYMMDD).

•	A start and end time for the callback window (HHMM).

•	The timezone (IST, Central, or Eastern).

•	The callback number (provided as an input variable).

The subflow includes input validation, error handling for invalid or timeout inputs, and maps all collected information to variables for downstream use.


> Note: The Subflow uses Cisco Text-to-speech (TTS) for all the audio activities that require prompts.
> 
> For music, it defaults to the `defaultmusic_on_hold.wav` file available out of box.
> 
> For organization-specific configuration activities such as Queue, Entry Points, Connectors, Outdial ANI, etc., these need to be manually configured by the user before the template is published.

### Pre-requisites

- Create Entry Point, Queue, Teams, and Entry Point Mapping from the Control Hub settings page for Webex Contact Center. Refer to the Webex Contact Center Setup and Administration Guide.
- This Subflow uses Cisco TTS (Text-to-speech). Upload required static audio files if using your own audio for the prompts.
- Ensure that the callback variables (e.g., `callbackNumber`, `CustomerName`, `callbackQueue`,`CallbackScheduleDate`,`CallbackScheduleTimezone`,`CallbackScheduleStartTime`,`CallbackScheduleEndTime`) are mapped correctly to your system to capture the appropriate data.

### Subflow Inputs

1. `callbackNumber` - STRING: The number to use for the callback (either the one the caller is calling from or a new number).
2. `CustomerName` - STRING: Name of the customer.
3. `callbackQueue` - STRING: Queue for routing the callback

### Subflow Outputs

1. `CallbackScheduleDate`-	STRING	Scheduled callback date (yyyy-MM-dd)
2. `CallbackScheduleTimezone`- STRING	Timezone in IANA format
3. `CallbackScheduleStartTime`- STRING	Callback window start (HH:mm:ss)
4. `CallbackScheduleEndTime` - STRING	Callback window end (HH:mm:ss)


### Subflow Breakdown


1.	**Start Subflow:** The subflow begins execution when invoked.
2.	**Prompt for Callback Date:** Caller is prompted (via TTS): "Please enter your preferred date in YYYYMMDD format" 
      -	Input is validated to ensure a valid date.
3.	**Prompt for Start Time:** If date is valid, prompt: "Please enter the start time for your callback in HHMM format" 
      -  Input is validated for correct time format.
4.	**Prompt for End Time:** If start time is valid, prompt: "Please enter the end time for your callback in HHMM format" 
      -	Input is validated for correct time format.
5.	**Prompt for Timezone:** Caller is prompted to select: 
6.	**Please choose your timezone**
7.	Press 1 for IST,
8.	2 for Central Time,
9.	3 for Eastern Time
   - 	Maps to IANA timezone strings (Asia/Kolkata, America/Chicago, America/Montreal).
10.	**Set Variables**
	Date is converted to yyyy-MM-dd.
  a.	Start and end times are formatted as HH:mm:ss.
  b. 	Selected timezone is mapped to the corresponding IANA identifier.
11.	**Schedule Callback:** The subflow schedules the callback using the collected values, including customer name, callback number, queue, date, time window, and timezone.
12.	**End Subflow** The flow ends after scheduling the callback.
13.	**Error/Timeout Handling** 
   -	Each step handles timeouts/invalid input by re-prompting or returning to the appropriate step.



### Activities Used

**Start Subflow**
- The subflow begins when invoked.

**Collect Digits (Date/Time):**
- TTS prompts for date and time (with format validation).

**Menu (Timezone)**
- Presents a menu for timezone selection.

**Set Variable**
- Converts/assigns date and time to proper formats.

**Condition Activities**
- Validate date/time entries.

**Schedule Callback**
- Schedules the callback with all collected data.

**End Subflow**
- The flow concludes after handling the caller's choices and collecting the necessary information.

**Error/Timeout Handling**
- Loops back on invalid/timeout responses.

### Additional Details
**Example Variable Mapping**

**Input Example:**

{
  "CallbackNumber": "+1234567890",
  "CustomerName": "John Doe",
  "CallbackQueue": "SalesQueue"
}


**Output Example:**
{
  "CallbackScheduleDate": "2025-07-30",
  "CallbackScheduleTimezone": "America/Chicago",
  "CallbackScheduleStartTime": "14:00:00",
  "CallbackScheduleEndTime": "16:00:00"
}

**Edge Cases & Considerations**

  a.	All digit entries are validated; invalid/timeout responses re-prompt the user.

  b.	Timezone selection is limited to IST, Central, and Eastern; extend as needed.

  c.	CustomerName is marked as secure for privacy.

  d.	Modify prompt wording to match organization policy or caller demographics.


For more information on configuring subflows, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).
