---
title: "MediaRecorder - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder
domain: media-recorder
license: CC-BY-SA-4.0
tags: mediarecorder api, record media stream, recorded data blob, recording mime type
fetched: 2026-07-02
---

# MediaRecorder

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`MediaRecorder`** interface of the MediaStream Recording API provides functionality to easily record media. It is created using the `MediaRecorder()` constructor.

## Constructor

**`MediaRecorder()`**

Creates a new `MediaRecorder` object, given a `MediaStream` to record. Options are available to do things like set the container's MIME type (such as `"video/webm"` or `"video/mp4"`) and the bit rates of the audio and video tracks or a single overall bit rate.

## Instance properties

**`MediaRecorder.mimeType` Read only**

Returns the MIME type that was selected as the recording container for the `MediaRecorder` object when it was created.

**`MediaRecorder.state` Read only**

Returns the current state of the `MediaRecorder` object (`inactive`, `recording`, or `paused`.)

**`MediaRecorder.stream` Read only**

Returns the stream that was passed into the constructor when the `MediaRecorder` was created.

**`MediaRecorder.videoBitsPerSecond` Read only**

Returns the video encoding bit rate in use. This may differ from the bit rate specified in the constructor (if it was provided).

**`MediaRecorder.audioBitsPerSecond` Read only**

Returns the audio encoding bit rate in use. This may differ from the bit rate specified in the constructor (if it was provided).

**`MediaRecorder.audioBitrateMode` Read only**

Returns the bitrate mode used to encode audio tracks.

## Static methods

**`MediaRecorder.isTypeSupported()`**

A static method which returns a `true` or `false` value indicating if the given MIME media type is supported by the current user agent.

## Instance methods

**`MediaRecorder.pause()`**

Pauses the recording of media.

**`MediaRecorder.requestData()`**

Requests a `Blob` containing the saved data received thus far (or since the last time `requestData()` was called. After calling this method, recording continues, but in a new `Blob`.

**`MediaRecorder.resume()`**

Resumes recording of media after having been paused.

**`MediaRecorder.start()`**

Begins recording media; this method can optionally be passed a `timeslice` argument with a value in milliseconds. If this is specified, the media will be captured in separate chunks of that duration, rather than the default behavior of recording the media in a single large chunk.

**`MediaRecorder.stop()`**

Stops recording, at which point a `dataavailable` event containing the final `Blob` of saved data is fired. No more recording occurs.

## Events

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

**`dataavailable`**

Fires periodically each time `timeslice` milliseconds of media have been recorded (or when the entire media has been recorded, if `timeslice` wasn't specified). The event, of type `BlobEvent`, contains the recorded media in its `data` property.

**`error`**

Fired when there are fatal errors that stop recording. The received event is based on the `MediaRecorderErrorEvent` interface, whose `error` property contains a `DOMException` that describes the actual error that occurred.

**`pause`**

Fired when media recording is paused.

**`resume`**

Fired when media recording resumes after being paused.

**`start`**

Fired when media recording starts.

**`stop`**

Fired when media recording ends, either when the `MediaStream` ends, or after the `MediaRecorder.stop()` method is called.

## Example

```js
if (navigator.mediaDevices) {
  console.log("getUserMedia supported.");

  const constraints = { audio: true };
  let chunks = [];

  navigator.mediaDevices
    .getUserMedia(constraints)
    .then((stream) => {
      const mediaRecorder = new MediaRecorder(stream);

      record.onclick = () => {
        mediaRecorder.start();
        console.log(mediaRecorder.state);
        console.log("recorder started");
        record.style.background = "red";
        record.style.color = "black";
      };

      stop.onclick = () => {
        mediaRecorder.stop();
        console.log(mediaRecorder.state);
        console.log("recorder stopped");
        record.style.background = "";
        record.style.color = "";
      };

      mediaRecorder.onstop = (e) => {
        console.log("data available after MediaRecorder.stop() called.");

        const clipName = prompt("Enter a name for your sound clip");

        const clipContainer = document.createElement("article");
        const clipLabel = document.createElement("p");
        const audio = document.createElement("audio");
        const deleteButton = document.createElement("button");
        const mainContainer = document.querySelector("body");

        clipContainer.classList.add("clip");
        audio.setAttribute("controls", "");
        deleteButton.textContent = "Delete";
        clipLabel.textContent = clipName;

        clipContainer.appendChild(audio);
        clipContainer.appendChild(clipLabel);
        clipContainer.appendChild(deleteButton);
        mainContainer.appendChild(clipContainer);

        audio.controls = true;
        const blob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
        chunks = [];
        const audioURL = URL.createObjectURL(blob);
        audio.src = audioURL;
        console.log("recorder stopped");

        deleteButton.onclick = (e) => {
          const evtTgt = e.target;
          evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
        };
      };

      mediaRecorder.ondataavailable = (e) => {
        chunks.push(e.data);
      };
    })
    .catch((err) => {
      console.error(`The following error occurred: ${err}`);
    });
}
```

**Note:** This code sample is inspired by the Web Dictaphone demo. Some lines have been omitted for brevity; refer to the source for the complete code.

## Specifications

| Specification |
|---|
| MediaStream Recording # mediarecorder-api |

## Browser compatibility
