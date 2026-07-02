"""Deep web platform: browser APIs, rendering/JS-engine internals, and web standards."""
from .common import CC_BY_SA, CC_BY_SA_25, mdn, wiki

DOMAINS = {
    "web-workers": {
        "tags": ["web workers", "background threads browser", "worker global scope", "dedicated worker thread"],
        "license": CC_BY_SA,
        "pages": wiki("Web_worker", "JavaScript")
        + [mdn("Web/API/Web_Workers_API"),
           mdn("Web/API/Worker"),
           mdn("Web/API/SharedWorker"),
           mdn("Web/API/Web_Workers_API/Using_web_workers"),
           mdn("Web/API/WorkerGlobalScope")],
    },
    "shared-array-buffer": {
        "tags": ["shared array buffer", "shared memory multithreading", "atomics operations", "cross-origin isolation"],
        "license": CC_BY_SA,
        "pages": wiki("Memory_barrier", "Linearizability")
        + [mdn("Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer"),
           mdn("Web/JavaScript/Reference/Global_Objects/Atomics"),
           mdn("Web/JavaScript/Reference/Global_Objects/ArrayBuffer"),
           mdn("Web/API/Window/crossOriginIsolated")],
    },
    "web-assembly-js-api": {
        "tags": ["webassembly javascript api", "wasm module instantiation", "wasm linear memory", "compiled web bytecode"],
        "license": CC_BY_SA,
        "pages": wiki("WebAssembly")
        + [mdn("WebAssembly"),
           mdn("WebAssembly/Guides/Concepts"),
           mdn("Web/JavaScript/Reference/Global_Objects/WebAssembly"),
           mdn("Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate"),
           mdn("Web/JavaScript/Reference/Global_Objects/WebAssembly/Memory")],
    },
    "broadcast-channel": {
        "tags": ["broadcast channel api", "same-origin messaging bus", "cross-tab communication", "message event dispatch"],
        "license": CC_BY_SA,
        "pages": wiki("Inter-process_communication", "Publish–subscribe_pattern")
        + [mdn("Web/API/Broadcast_Channel_API"),
           mdn("Web/API/BroadcastChannel"),
           mdn("Web/API/BroadcastChannel/postMessage"),
           mdn("Web/API/BroadcastChannel/message_event")],
    },
    "message-channel": {
        "tags": ["message channel api", "message port pair", "channel messaging", "transferable object handoff"],
        "license": CC_BY_SA,
        "pages": wiki("Channel_(programming)", "Message_passing")
        + [mdn("Web/API/Channel_Messaging_API"),
           mdn("Web/API/MessageChannel"),
           mdn("Web/API/MessagePort"),
           mdn("Web/API/Channel_Messaging_API/Using_channel_messaging")],
    },
    "structured-clone": {
        "tags": ["structured clone algorithm", "deep copy serialization", "transferable objects", "postmessage data copy"],
        "license": CC_BY_SA,
        "pages": wiki("Serialization", "Object_copying")
        + [mdn("Web/API/Web_Workers_API/Structured_clone_algorithm"),
           mdn("Web/API/structuredClone"),
           mdn("Web/API/Window/structuredClone"),
           mdn("Glossary/Transferable_objects")],
    },
    "web-locks-api": {
        "tags": ["web locks api", "mutual exclusion resource", "cross-tab lock coordination", "exclusive shared lock mode"],
        "license": CC_BY_SA,
        "pages": wiki("Lock_(computer_science)", "Mutual_exclusion")
        + [mdn("Web/API/Web_Locks_API"),
           mdn("Web/API/LockManager"),
           mdn("Web/API/Lock"),
           mdn("Web/API/LockManager/request")],
    },
    "web-crypto-api": {
        "tags": ["web crypto api", "subtle crypto operations", "cryptographic key generation", "secure random values"],
        "license": CC_BY_SA,
        "pages": wiki("Cryptography", "Public-key_cryptography")
        + [mdn("Web/API/Web_Crypto_API"),
           mdn("Web/API/Crypto"),
           mdn("Web/API/SubtleCrypto"),
           mdn("Web/API/Crypto/getRandomValues"),
           mdn("Web/API/SubtleCrypto/encrypt")],
    },
    "credential-management": {
        "tags": ["credential management api", "browser credential store", "federated credential login", "automatic sign-in"],
        "license": CC_BY_SA,
        "pages": wiki("Password_manager", "Federated_identity")
        + [mdn("Web/API/Credential_Management_API"),
           mdn("Web/API/CredentialsContainer"),
           mdn("Web/API/Credential"),
           mdn("Web/API/PasswordCredential"),
           mdn("Web/API/FederatedCredential")],
    },
    "web-authentication-deep": {
        "tags": ["web authentication ceremony", "public key credential", "authenticator attestation", "assertion signature verify"],
        "license": CC_BY_SA,
        "pages": wiki("WebAuthn", "FIDO_Alliance")
        + [mdn("Web/API/PublicKeyCredential"),
           mdn("Web/API/CredentialsContainer/create"),
           mdn("Web/API/CredentialsContainer/get"),
           mdn("Web/API/AuthenticatorAttestationResponse"),
           mdn("Web/API/AuthenticatorAssertionResponse")],
    },
    "payment-request-api": {
        "tags": ["payment request api", "browser checkout flow", "payment method data", "merchant payment sheet"],
        "license": CC_BY_SA,
        "pages": wiki("Payment_service_provider", "Electronic_funds_transfer")
        + [mdn("Web/API/Payment_Request_API"),
           mdn("Web/API/PaymentRequest"),
           mdn("Web/API/PaymentResponse"),
           mdn("Web/API/PaymentRequest/show"),
           mdn("Web/API/Payment_Request_API/Using_the_Payment_Request_API")],
    },
    "web-share-api": {
        "tags": ["web share api", "native share sheet", "share target registration", "shared file payload"],
        "license": CC_BY_SA,
        "pages": wiki("Sharing", "Hyperlink")
        + [mdn("Web/API/Web_Share_API"),
           mdn("Web/API/Navigator/share"),
           mdn("Web/API/Navigator/canShare"),
           mdn("Web/Progressive_web_apps/How_to/Share_data_between_apps")],
    },
    "notifications-api": {
        "tags": ["notifications api", "desktop notification permission", "notification event handling", "system notification banner"],
        "license": CC_BY_SA,
        "pages": wiki("Notification_system", "Pop-up_notification")
        + [mdn("Web/API/Notifications_API"),
           mdn("Web/API/Notification"),
           mdn("Web/API/Notification/permission_static"),
           mdn("Web/API/Notifications_API/Using_the_Notifications_API")],
    },
    "push-api": {
        "tags": ["push api", "push subscription endpoint", "push message delivery", "web push protocol"],
        "license": CC_BY_SA,
        "pages": wiki("Push_technology", "WebSocket")
        + [mdn("Web/API/Push_API"),
           mdn("Web/API/PushManager"),
           mdn("Web/API/PushSubscription"),
           mdn("Web/API/PushEvent"),
           mdn("Web/API/ServiceWorkerRegistration/pushManager")],
    },
    "background-sync": {
        "tags": ["background sync api", "deferred network request", "sync event retry", "offline action queue"],
        "license": CC_BY_SA,
        "pages": wiki("Data_synchronization", "Offline")
        + [mdn("Web/API/Background_Synchronization_API"),
           mdn("Web/API/SyncManager"),
           mdn("Web/API/SyncEvent"),
           mdn("Web/API/ServiceWorkerRegistration/sync")],
    },
    "periodic-background-sync": {
        "tags": ["periodic background sync", "periodic sync registration", "scheduled content refresh", "minimum sync interval"],
        "license": CC_BY_SA,
        "pages": wiki("Scheduling_(computing)", "Polling_(computer_science)")
        + [mdn("Web/API/Web_Periodic_Background_Synchronization_API"),
           mdn("Web/API/PeriodicSyncManager"),
           mdn("Web/API/PeriodicSyncEvent"),
           mdn("Web/API/ServiceWorkerRegistration/periodicSync")],
    },
    "web-bluetooth": {
        "tags": ["web bluetooth api", "bluetooth low energy gatt", "gatt service characteristic", "bluetooth device pairing"],
        "license": CC_BY_SA,
        "pages": wiki("Bluetooth_Low_Energy", "Bluetooth")
        + [mdn("Web/API/Web_Bluetooth_API"),
           mdn("Web/API/Bluetooth"),
           mdn("Web/API/BluetoothDevice"),
           mdn("Web/API/BluetoothRemoteGATTServer")],
    },
    "web-usb": {
        "tags": ["web usb api", "usb device access", "usb interface endpoint", "usb transfer control"],
        "license": CC_BY_SA,
        "pages": wiki("USB", "Device_driver")
        + [mdn("Web/API/WebUSB_API"),
           mdn("Web/API/USB"),
           mdn("Web/API/USBDevice"),
           mdn("Web/API/USBConfiguration")],
    },
    "web-serial": {
        "tags": ["web serial api", "serial port communication", "readable writable stream port", "serial baud rate config"],
        "license": CC_BY_SA,
        "pages": wiki("Serial_port", "Serial_communication")
        + [mdn("Web/API/Web_Serial_API"),
           mdn("Web/API/Serial"),
           mdn("Web/API/SerialPort"),
           mdn("Web/API/SerialPort/open")],
    },
    "web-hid": {
        "tags": ["web hid api", "human interface device", "hid report descriptor", "raw input output device"],
        "license": CC_BY_SA,
        "pages": wiki("Human_interface_device", "USB_human_interface_device_class")
        + [mdn("Web/API/WebHID_API"),
           mdn("Web/API/HID"),
           mdn("Web/API/HIDDevice"),
           mdn("Web/API/HIDInputReportEvent")],
    },
    "web-nfc": {
        "tags": ["web nfc api", "near field communication", "ndef record message", "contactless tag reading"],
        "license": CC_BY_SA,
        "pages": wiki("Near-field_communication", "Radio-frequency_identification")
        + [mdn("Web/API/Web_NFC_API"),
           mdn("Web/API/NDEFReader"),
           mdn("Web/API/NDEFMessage"),
           mdn("Web/API/NDEFRecord")],
    },
    "geolocation-api": {
        "tags": ["geolocation api", "device position coordinates", "watch position updates", "location permission prompt"],
        "license": CC_BY_SA,
        "pages": wiki("Geolocation", "Global_Positioning_System")
        + [mdn("Web/API/Geolocation_API"),
           mdn("Web/API/Geolocation"),
           mdn("Web/API/GeolocationPosition"),
           mdn("Web/API/Geolocation/getCurrentPosition"),
           mdn("Web/API/Geolocation/watchPosition")],
    },
    "device-orientation": {
        "tags": ["device orientation events", "accelerometer motion data", "gyroscope rotation rate", "device motion sensing"],
        "license": CC_BY_SA,
        "pages": wiki("Accelerometer", "Gyroscope")
        + [mdn("Web/API/Device_orientation_events"),
           mdn("Web/API/DeviceOrientationEvent"),
           mdn("Web/API/DeviceMotionEvent"),
           mdn("Web/API/Window/deviceorientation_event")],
    },
    "screen-orientation": {
        "tags": ["screen orientation api", "orientation lock landscape", "portrait orientation type", "orientation change event"],
        "license": CC_BY_SA,
        "pages": wiki("Page_orientation", "Display_device")
        + [mdn("Web/API/Screen_Orientation_API"),
           mdn("Web/API/ScreenOrientation"),
           mdn("Web/API/ScreenOrientation/lock"),
           mdn("Web/API/ScreenOrientation/type")],
    },
    "fullscreen-api": {
        "tags": ["fullscreen api", "request fullscreen element", "fullscreen change event", "exit fullscreen mode"],
        "license": CC_BY_SA,
        "pages": wiki("Full-screen_writing_program", "Kiosk_software")
        + [mdn("Web/API/Fullscreen_API"),
           mdn("Web/API/Element/requestFullscreen"),
           mdn("Web/API/Document/fullscreenElement"),
           mdn("Web/API/Document/exitFullscreen"),
           mdn("Web/API/Element/fullscreenchange_event")],
    },
    "pointer-events": {
        "tags": ["pointer events model", "unified input pointer", "pointer capture target", "primary pointer detection"],
        "license": CC_BY_SA,
        "pages": wiki("Pointing_device", "Touchscreen")
        + [mdn("Web/API/Pointer_events"),
           mdn("Web/API/PointerEvent"),
           mdn("Web/API/Element/setPointerCapture"),
           mdn("Web/API/Element/pointerdown_event"),
           mdn("Web/CSS/touch-action")],
    },
    "pointer-lock": {
        "tags": ["pointer lock api", "mouse capture relative motion", "raw mouse movement", "pointer lock change event"],
        "license": CC_BY_SA,
        "pages": wiki("Mouse_(computing)", "Video_game")
        + [mdn("Web/API/Pointer_Lock_API"),
           mdn("Web/API/Element/requestPointerLock"),
           mdn("Web/API/Document/pointerlockchange_event"),
           mdn("Web/API/MouseEvent/movementX")],
    },
    "gamepad-api": {
        "tags": ["gamepad api", "game controller input", "gamepad button axes", "gamepad connected event"],
        "license": CC_BY_SA,
        "pages": wiki("Gamepad", "Game_controller")
        + [mdn("Web/API/Gamepad_API"),
           mdn("Web/API/Gamepad"),
           mdn("Web/API/Navigator/getGamepads"),
           mdn("Web/API/GamepadButton"),
           mdn("Web/API/Window/gamepadconnected_event")],
    },
    "web-midi": {
        "tags": ["web midi api", "midi message port", "midi input output", "musical instrument digital interface"],
        "license": CC_BY_SA,
        "pages": wiki("MIDI", "Musical_note")
        + [mdn("Web/API/Web_MIDI_API"),
           mdn("Web/API/MIDIAccess"),
           mdn("Web/API/MIDIInput"),
           mdn("Web/API/MIDIOutput"),
           mdn("Web/API/Navigator/requestMIDIAccess")],
    },
    "web-audio-api": {
        "tags": ["web audio api", "audio node graph", "audio context processing", "gain oscillator node"],
        "license": CC_BY_SA,
        "pages": wiki("Digital_audio", "Sound_synthesis")
        + [mdn("Web/API/Web_Audio_API"),
           mdn("Web/API/AudioContext"),
           mdn("Web/API/AudioNode"),
           mdn("Web/API/GainNode"),
           mdn("Web/API/OscillatorNode")],
    },
    "media-source-extensions": {
        "tags": ["media source extensions", "source buffer append", "adaptive streaming buffer", "segmented media playback"],
        "license": CC_BY_SA,
        "pages": wiki("Adaptive_bitrate_streaming", "Dynamic_Adaptive_Streaming_over_HTTP")
        + [mdn("Web/API/Media_Source_Extensions_API"),
           mdn("Web/API/MediaSource"),
           mdn("Web/API/SourceBuffer"),
           mdn("Web/API/MediaSource/addSourceBuffer")],
    },
    "encrypted-media": {
        "tags": ["encrypted media extensions", "content decryption module", "digital rights management", "media key session"],
        "license": CC_BY_SA,
        "pages": wiki("Encrypted_Media_Extensions", "Digital_rights_management")
        + [mdn("Web/API/Encrypted_Media_Extensions_API"),
           mdn("Web/API/MediaKeys"),
           mdn("Web/API/MediaKeySession"),
           mdn("Web/API/Navigator/requestMediaKeySystemAccess")],
    },
    "media-capabilities": {
        "tags": ["media capabilities api", "decoding playback ability", "media codec support query", "smooth power-efficient playback"],
        "license": CC_BY_SA,
        "pages": wiki("Video_codec", "Transcoding")
        + [mdn("Web/API/Media_Capabilities_API"),
           mdn("Web/API/MediaCapabilities"),
           mdn("Web/API/MediaCapabilities/decodingInfo"),
           mdn("Web/API/Navigator/mediaCapabilities")],
    },
    "webcodecs-api": {
        "tags": ["webcodecs api", "low-level frame encode", "video frame decode", "encoded audio chunk"],
        "license": CC_BY_SA,
        "pages": wiki("Data_compression", "Frame_(networking)")
        + [mdn("Web/API/WebCodecs_API"),
           mdn("Web/API/VideoEncoder"),
           mdn("Web/API/VideoDecoder"),
           mdn("Web/API/VideoFrame"),
           mdn("Web/API/AudioEncoder")],
    },
    "media-recorder": {
        "tags": ["mediarecorder api", "record media stream", "recorded data blob", "recording mime type"],
        "license": CC_BY_SA,
        "pages": wiki("Screencast", "Digital_recording")
        + [mdn("Web/API/MediaStream_Recording_API"),
           mdn("Web/API/MediaRecorder"),
           mdn("Web/API/MediaRecorder/start"),
           mdn("Web/API/MediaRecorder/dataavailable_event")],
    },
    "image-capture": {
        "tags": ["image capture api", "camera photo capture", "grab video frame", "camera track settings"],
        "license": CC_BY_SA,
        "pages": wiki("Digital_camera", "Photograph")
        + [mdn("Web/API/ImageCapture"),
           mdn("Web/API/ImageCapture/takePhoto"),
           mdn("Web/API/ImageCapture/grabFrame"),
           mdn("Web/API/MediaStreamTrack")],
    },
    "screen-capture": {
        "tags": ["screen capture api", "display media stream", "get display media", "screen sharing surface"],
        "license": CC_BY_SA,
        "pages": wiki("Screenshot", "Remote_desktop_software")
        + [mdn("Web/API/Screen_Capture_API"),
           mdn("Web/API/MediaDevices/getDisplayMedia"),
           mdn("Web/API/Screen_Capture_API/Using_Screen_Capture"),
           mdn("Web/API/CaptureController")],
    },
    "picture-in-picture": {
        "tags": ["picture in picture api", "floating video window", "detached video overlay", "enter pip mode"],
        "license": CC_BY_SA,
        "pages": wiki("Picture-in-picture", "Multiview_Video_Coding")
        + [mdn("Web/API/Picture-in-Picture_API"),
           mdn("Web/API/HTMLVideoElement/requestPictureInPicture"),
           mdn("Web/API/PictureInPictureWindow"),
           mdn("Web/API/Document/pictureInPictureElement")],
    },
    "resize-observer": {
        "tags": ["resize observer api", "element size change callback", "content box resize", "observe box dimensions"],
        "license": CC_BY_SA,
        "pages": wiki("Observer_pattern", "Callback_(computer_programming)")
        + [mdn("Web/API/ResizeObserver"),
           mdn("Web/API/ResizeObserver/observe"),
           mdn("Web/API/ResizeObserverEntry"),
           mdn("Web/API/ResizeObserver/ResizeObserver")],
    },
    "mutation-observer": {
        "tags": ["mutation observer api", "dom tree change watch", "mutation record list", "observe child list"],
        "license": CC_BY_SA,
        "pages": wiki("Document_Object_Model", "Reactive_programming")
        + [mdn("Web/API/MutationObserver"),
           mdn("Web/API/MutationObserver/observe"),
           mdn("Web/API/MutationRecord"),
           mdn("Web/API/MutationObserver/MutationObserver")],
    },
    "performance-observer": {
        "tags": ["performance observer api", "performance entry buffer", "observe entry types", "buffered performance records"],
        "license": CC_BY_SA,
        "pages": wiki("Profiling_(computer_programming)", "Latency_(engineering)")
        + [mdn("Web/API/PerformanceObserver"),
           mdn("Web/API/PerformanceObserver/observe"),
           mdn("Web/API/PerformanceObserverEntryList"),
           mdn("Web/API/PerformanceEntry")],
    },
    "navigation-timing": {
        "tags": ["navigation timing api", "page load milestones", "performance navigation entry", "dom content loaded timing"],
        "license": CC_BY_SA,
        "pages": wiki("Web_performance", "Round-trip_delay")
        + [mdn("Web/API/Navigation_timing_API"),
           mdn("Web/API/PerformanceNavigationTiming"),
           mdn("Web/API/Performance/timing"),
           mdn("Web/API/PerformanceTiming")],
    },
    "resource-timing": {
        "tags": ["resource timing api", "resource fetch timing", "network request phases", "transfer size metric"],
        "license": CC_BY_SA,
        "pages": wiki("Time_to_first_byte", "Network_performance")
        + [mdn("Web/API/Resource_Timing_API"),
           mdn("Web/API/PerformanceResourceTiming"),
           mdn("Web/API/PerformanceResourceTiming/transferSize"),
           mdn("Web/API/Resource_Timing_API/Using_the_Resource_Timing_API")],
    },
    "paint-timing": {
        "tags": ["paint timing api", "first contentful paint", "first paint metric", "render performance milestone"],
        "license": CC_BY_SA,
        "pages": wiki("Rendering_(computer_graphics)", "Frame_rate")
        + [mdn("Web/API/PerformancePaintTiming"),
           mdn("Web/API/PerformanceEntry/entryType"),
           mdn("Web/API/Performance_API"),
           mdn("Web/API/LargestContentfulPaint")],
    },
    "requestidlecallback": {
        "tags": ["request idle callback", "idle period scheduling", "background task deadline", "cooperative task chunking"],
        "license": CC_BY_SA,
        "pages": wiki("Cooperative_multitasking", "Idle_(CPU)")
        + [mdn("Web/API/Window/requestIdleCallback"),
           mdn("Web/API/Background_Tasks_API"),
           mdn("Web/API/IdleDeadline"),
           mdn("Web/API/Window/cancelIdleCallback")],
    },
    "requestanimationframe": {
        "tags": ["request animation frame", "frame-synced callback", "smooth animation loop", "repaint scheduling browser"],
        "license": CC_BY_SA,
        "pages": wiki("Refresh_rate", "Computer_animation")
        + [mdn("Web/API/Window/requestAnimationFrame"),
           mdn("Web/API/Window/cancelAnimationFrame"),
           mdn("Web/API/DedicatedWorkerGlobalScope/requestAnimationFrame"),
           mdn("Web/API/HTMLVideoElement/requestVideoFrameCallback")],
    },
    "intersection-observer-deep": {
        "tags": ["intersection observer internals", "root margin threshold", "intersection ratio callback", "viewport visibility tracking"],
        "license": CC_BY_SA,
        "pages": wiki("Viewport", "Hit-testing")
        + [mdn("Web/API/Intersection_Observer_API"),
           mdn("Web/API/IntersectionObserver"),
           mdn("Web/API/IntersectionObserverEntry"),
           mdn("Web/API/IntersectionObserver/thresholds"),
           mdn("Web/API/IntersectionObserver/rootMargin")],
    },
    "css-object-model": {
        "tags": ["css object model", "cssom style sheet", "computed style access", "cssstyledeclaration interface"],
        "license": CC_BY_SA,
        "pages": wiki("Cascading_Style_Sheets", "Document_Object_Model")
        + [mdn("Web/API/CSS_Object_Model"),
           mdn("Web/API/CSSStyleSheet"),
           mdn("Web/API/CSSStyleDeclaration"),
           mdn("Web/API/Window/getComputedStyle"),
           mdn("Web/API/CSSRule")],
    },
    "css-typed-om": {
        "tags": ["css typed object model", "typed cssom value", "css unit value", "attribute style map"],
        "license": CC_BY_SA,
        "pages": wiki("Cascading_Style_Sheets", "Type_system")
        + [mdn("Web/API/CSS_Typed_OM_API"),
           mdn("Web/API/CSSStyleValue"),
           mdn("Web/API/CSSUnitValue"),
           mdn("Web/API/StylePropertyMap"),
           mdn("Web/API/Element/computedStyleMap")],
    },
    "css-paint-api": {
        "tags": ["css painting api", "paint worklet registration", "programmatic css background", "custom paint function"],
        "license": CC_BY_SA,
        "pages": wiki("Rasterisation", "2D_computer_graphics")
        + [mdn("Web/API/CSS_Painting_API"),
           mdn("Web/API/PaintWorklet"),
           mdn("Web/API/CSS_Painting_API/Guide"),
           mdn("Web/API/PaintWorkletGlobalScope"),
           mdn("Web/CSS/paint")],
    },
    "css-layout-api": {
        "tags": ["css layout api", "layout worklet definition", "custom layout algorithm", "fragment layout children"],
        "license": CC_BY_SA,
        "pages": wiki("Page_layout", "Algorithm")
        + [mdn("Web/Guide/Houdini"),
           mdn("Web/CSS/CSS_containment"),
           mdn("Web/API/Houdini_APIs"),
           mdn("Web/API/Worklet")],
    },
    "houdini-worklets": {
        "tags": ["css houdini worklets", "worklet global scope", "add module worklet", "extensible styling engine"],
        "license": CC_BY_SA,
        "pages": wiki("Thread_(computing)", "Sandbox_(computer_security)")
        + [mdn("Web/API/Worklet"),
           mdn("Web/API/Worklet/addModule"),
           mdn("Web/API/WorkletGlobalScope"),
           mdn("Web/API/AudioWorklet"),
           mdn("Web/API/Houdini_APIs")],
    },
    "custom-elements-deep": {
        "tags": ["custom elements lifecycle", "connected callback reaction", "attribute changed callback", "element upgrade reaction"],
        "license": CC_BY_SA,
        "pages": wiki("Web_Components", "Reflection_(computer_programming)")
        + [mdn("Web/API/CustomElementRegistry"),
           mdn("Web/API/CustomElementRegistry/define"),
           mdn("Web/API/Web_components/Using_custom_elements"),
           mdn("Web/API/CustomElementRegistry/upgrade"),
           mdn("Web/API/HTMLElement/attachInternals")],
    },
    "shadow-dom-deep": {
        "tags": ["shadow dom internals", "shadow root attachment", "style encapsulation boundary", "slot content projection"],
        "license": CC_BY_SA,
        "pages": wiki("Web_Components", "Encapsulation_(computer_programming)")
        + [mdn("Web/API/ShadowRoot"),
           mdn("Web/API/Element/attachShadow"),
           mdn("Web/API/Web_components/Using_shadow_DOM"),
           mdn("Web/API/HTMLSlotElement"),
           mdn("Web/CSS/::part")],
    },
    "html-templates-slots": {
        "tags": ["html template slots", "slotted content distribution", "named slot assignment", "template instantiation clone"],
        "license": CC_BY_SA,
        "pages": wiki("Template_(word_processing)", "Placeholder")
        + [mdn("Web/HTML/Reference/Elements/template"),
           mdn("Web/HTML/Reference/Elements/slot"),
           mdn("Web/API/HTMLSlotElement"),
           mdn("Web/API/HTMLTemplateElement"),
           mdn("Web/API/Web_components/Using_templates_and_slots")],
    },
    "declarative-shadow-dom": {
        "tags": ["declarative shadow dom", "shadowrootmode attribute", "server rendered shadow tree", "template shadowroot parsing"],
        "license": CC_BY_SA,
        "pages": wiki("Web_Components", "Server-side_scripting")
        + [mdn("Web/HTML/Reference/Elements/template"),
           mdn("Web/API/ShadowRoot"),
           mdn("Web/API/ShadowRoot/mode"),
           mdn("Web/API/Element/attachShadow"),
           mdn("Web/API/HTMLTemplateElement/shadowRootMode")],
    },
    "dom-parsing-serialization": {
        "tags": ["dom parsing serialization", "domparser markup string", "xml serializer output", "inner html parsing"],
        "license": CC_BY_SA,
        "pages": wiki("Parsing", "Serialization")
        + [mdn("Web/API/DOMParser"),
           mdn("Web/API/XMLSerializer"),
           mdn("Web/API/DOMParser/parseFromString"),
           mdn("Web/API/Element/innerHTML"),
           mdn("Web/API/Document_Object_Model")],
    },
    "selection-api": {
        "tags": ["selection api", "text selection range", "user selected content", "caret anchor focus"],
        "license": CC_BY_SA,
        "pages": wiki("Selection_(user_interface)", "Cursor_(user_interface)")
        + [mdn("Web/API/Selection"),
           mdn("Web/API/Window/getSelection"),
           mdn("Web/API/Selection/getRangeAt"),
           mdn("Web/API/Range"),
           mdn("Web/API/Document/selectionchange_event")],
    },
    "clipboard-api": {
        "tags": ["clipboard api", "async clipboard read write", "clipboard item data", "programmatic copy paste"],
        "license": CC_BY_SA,
        "pages": wiki("Cut,_copy,_and_paste", "Clipboard_(computing)")
        + [mdn("Web/API/Clipboard_API"),
           mdn("Web/API/Clipboard"),
           mdn("Web/API/Clipboard/writeText"),
           mdn("Web/API/ClipboardItem"),
           mdn("Web/API/Navigator/clipboard")],
    },
    "drag-and-drop-api": {
        "tags": ["html drag and drop", "data transfer object", "draggable attribute element", "drop target zone"],
        "license": CC_BY_SA,
        "pages": wiki("Drag_and_drop", "Pointing_device_gesture")
        + [mdn("Web/API/HTML_Drag_and_Drop_API"),
           mdn("Web/API/DataTransfer"),
           mdn("Web/API/DragEvent"),
           mdn("Web/HTML/Global_attributes/draggable"),
           mdn("Web/API/HTML_Drag_and_Drop_API/Drag_operations")],
    },
    "history-api": {
        "tags": ["history api", "push state navigation", "session history entry", "popstate history traversal"],
        "license": CC_BY_SA,
        "pages": wiki("Web_navigation", "Web_browsing_history")
        + [mdn("Web/API/History_API"),
           mdn("Web/API/History"),
           mdn("Web/API/History/pushState"),
           mdn("Web/API/Window/popstate_event"),
           mdn("Web/API/History_API/Working_with_the_History_API")],
    },
    "url-pattern-api": {
        "tags": ["url pattern api", "url matching syntax", "route pattern parsing", "named path group"],
        "license": CC_BY_SA,
        "pages": wiki("URL", "Regular_expression")
        + [mdn("Web/API/URL_Pattern_API"),
           mdn("Web/API/URLPattern"),
           mdn("Web/API/URLPattern/test"),
           mdn("Web/API/URLPattern/exec")],
    },
}
