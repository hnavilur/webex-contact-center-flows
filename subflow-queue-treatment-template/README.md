# Queue Treatment Subflow - Template

## Description

This subflow template automates queue treatment in the Webex Contact Center environment. It is designed to engage callers by playing music, delivering messages, and looping until a predefined condition is met. Specifically, the subflow repeats music and message prompts based on a counter, helping to improve the customer experience while waiting in a queue.

## Details

This subflow provides an efficient way to keep callers engaged while they are waiting in a queue. It plays queue music followed by a message, looping through this sequence until a set number of repetitions (default: three) is reached. The flow is structured to ensure seamless handling of queue wait times, providing an engaging experience for the caller.

The subflow can be customized by altering variables such as the type of music played, message content, and the number of loops.

> Note: The Subflow uses Cisco Text-to-speech (TTS) for all audio activities that require prompts.
> 
> Music defaults to the `defaultmusic_on_hold.wav` file.
> 
> For specific configurations like Queue, Entry Points, Connectors, etc., these need to be manually set up before the template is published.

### Pre-requisites

- Configure Entry Points, Queue, Teams, and Entry Point Mapping in the Webex Contact Center Management Portal.
- Ensure proper queue treatment logic and error-handling configurations.
- Set up any required static audio files if using custom audio for music or prompts.

### Subflow Inputs

1. `queueMessage` - STRING: The message to be played between music tracks (default: "Please wait").
2. `queueMusic1` - STRING: The first music file to be played while the caller waits (default: `defaultmusic_on_hold.wav`).
3. `queueMusic2` - STRING: The second music file to be played between messages (default: `defaultmusic_on_hold.wav`).
4. `counter` - INTEGER: A counter to track the number of loops (default: 0).
5. `musicDuration` - INTEGER: The duration for which each music track is played (default: 10 seconds).

### Subflow Outputs

None

### Subflow Breakdown

1. **Start Subflow:** The subflow begins.
2. **Condition Check:** The subflow checks if the counter is less than 2. If true, the flow continues to the music and message sequence. If false, the subflow ends.
3. **Play Music 1:** The first music file (`queueMusic1`) is played for the duration defined by `musicDuration`.
4. **Play Message:** After the first music file, a message is played using Cisco Cloud TTS, with the content defined by `queueMessage`.
5. **Play Music 2:** After the message, the second music file (`queueMusic2`) is played for the defined duration.
6. **Increment Counter:** The `counter` variable is incremented by 1 after the second music file is played.
7. **Re-check Condition:** After the counter is incremented, the flow rechecks if the counter is still less than 2. If true, the loop repeats; otherwise, the subflow ends.
8. **End Subflow:** Once the counter reaches 2, the subflow ends.

### Activities Used

**Start Subflow**
- Initializes the subflow process.

**Condition Check**
- A condition is checked to ensure the counter is less than 2, allowing the loop to continue.

**Play Music 1**
- Plays the first music file for the duration specified by `musicDuration`.

**Play Message**
- Plays a message using Cisco TTS with content provided by `queueMessage`.

**Play Music 2**
- Plays the second music file for the duration specified by `musicDuration`.

**Increment Counter**
- Increments the `counter` variable by 1 to control the loop.

**End Subflow**
- Ends the subflow once the counter reaches the predefined limit.

### Additional Details

For more information on configuring subflows, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).
