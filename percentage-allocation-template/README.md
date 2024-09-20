# Percentage Allocation & A/B Distribution - Template

## Name
Percentage Allocation & A/B Distribution

## Labels 
Intermediate, Voice, Inbound, Percentages


## Description

This template demonstrates a flow for distributing customer interactions based on percentage allocation in a Webex Contact Center. It is designed to handle inbound phone contacts and distribute them dynamically across different queues.

## Details

This flow distributes incoming calls based on a percentage-based allocation. Specifically, 90% of contacts are routed to the Main Queue, 0% to Overflow Support (inactive), and 10% to an Offsite Queue. After allocation, callers are played a message indicating their queue assignment, followed by music on hold until an agent is available.

Modify the flow to suit your organization’s needs, ensuring seamless operation during high call volumes and minimizing contact drop-offs.

> Note: The Flow utilizes Cisco Text-to-Speech (TTS) for all message prompts.
> 
> For music, the flow uses the `defaultmusic_on_hold.wav` file provided out-of-the-box.
> 
> For custom configurations (e.g., Queue, Entry Points, Connectors, etc.), these must be configured manually in the Webex Contact Center before deploying the template.

### Pre-requisites

- Set up the Entry Point, Queue, Teams, and Entry Point Mapping in the Control Hub settings page for Webex Contact Center.
- Cisco TTS is used for audio prompts by default. Ensure you upload any required static audio files if using custom prompts.

### Flow Breakdown

1. **Call Receipt**: The call enters the flow at the "NewPhoneContact" point.
2. **Percentage Allocation**: 
   - 90% of calls are routed to the Main Queue.
   - 10% of calls are routed to the Offsite Queue.
3. **Play Queue Message**: After the percentage allocation, the caller hears a message indicating their allocation path.
4. **Queue Contact**: The caller is placed in the assigned queue.
5. **Hold Music**: While waiting in the queue, callers hear hold music.
6. **Agent Assignment**: Calls are routed to the available agent in their assigned queue.

### Activities Used in Flow

**NewPhoneContact**:  
- This is the starting point when a new phone contact is received.

**PercentAllocation**:  
- Allocates the incoming contact based on the percentage distribution:
  - 90% directed to the Main Queue.
  - 10% directed to the Offsite Queue.
  
**SetVariable**:  
- Captures the percentage allocated (e.g., 90%, 10%) into a variable called `PercentageAllocated`.

**SetVariable**:  
- Captures the exit path (MainQueue, Offsite) the call took into a variable called `PercentageExitPath`.

**PlayMessage**:  
- Plays a message using Cisco TTS informing the caller of their allocation, such as "You’ve reached 90% allocation! Branch 1 MainQueue."

**QueueContact**:  
- Queues the contact based on the allocated path (either Main Queue or Offsite).

**PlayMusic**:  
- Plays hold music (`defaultmusic_on_hold.wav`) while the caller waits in the queue.

## Additional Details

For more information on configuring this flow, refer to the [Webex Contact Center Setup and Administration Guide](https://help.webex.com/en-us/article/n5595zd/Webex-Contact-Center-Setup-and-Administration-Guide).

---

This tailored template now reflects the percentage-based allocation, ensuring that the structure fits within a specific context of handling and queuing customer interactions in a Webex Contact Center.