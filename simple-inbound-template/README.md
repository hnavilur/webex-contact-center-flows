# Description

A simple inbound voice flow where callers are greeted, and queued to an agent, along with hold music while waiting for an agent.

# Details

This flow provides a straightforward process for handling inbound calls in a contact center:

1. Call is received and enters the flow.
2. A welcome message is played to the caller.
3. The caller is placed in a queue.
4. Hold music is played while the caller waits.

Modify the flow to ensure a smooth caller experience by handling any errors or unknown conditions.

Here are the activities used in the flow:

**Start(New Phone Contact):**

- The flow begins when a call is received.

- This is via the entry point where the call is initially accepted into the flow.

**Play Message:**

- The call is directed to play a welcome message to the caller. This might be a greeting or an informational message.

**Queue (Direct Contact) Node:**

- After the welcome message, the call is directed to the "Queue" node.
- Here, the call is placed in a queue, with a potential to wait for the next available agent.

**Play Music Node:**

- While the caller is in the queue, the Play Music activity named "MusicOnHold" plays hold music to the caller.

### Pre-requisites

- Create Entry Point, Queue, Teams and Entry Point Mapping from the Webex Contact Center Management Portal. Refer Setup-and-Administration-Guide.
- This flow uses Cisco TTS(Text-to-speech). Upload required static audio files if using your own.
