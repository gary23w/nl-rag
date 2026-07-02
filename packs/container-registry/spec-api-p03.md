---
title: "HTTP API V2 (part 3/4)"
source: https://distribution.github.io/distribution/spec/api/
domain: container-registry
license: CC-BY-SA-4.0
tags: container registry, container image registry, oci image, image distribution
fetched: 2026-07-02
part: 3/4
---

# HTTP API V2

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DENIED` | requested access to the resource is denied | The access controller denied access for the operation on a resource. |

###### On Failure: Too Many Requests

```none
429 Too Many Requests
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client made too many requests within a time interval.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `TOOMANYREQUESTS` | too many requests | Returned when a client attempts to contact a service too many times |

### Initiate Blob Upload

Initiate a blob upload. This endpoint can be used to create resumable uploads or monolithic uploads.

#### POST Initiate Blob Upload

Initiate a resumable blob upload. If successful, an upload location will be provided to complete the upload. Optionally, if the `digest` parameter is present, the request body will be used to complete the upload in a single request.

##### Initiate Monolithic Blob Upload

```none
POST /v2/<name>/blobs/uploads/?digest=<digest>
Host: <registry host>
Authorization: <scheme> <token>
Content-Length: <length of blob>
Content-Type: application/octet-stream

<binary data>
```

Upload a blob identified by the `digest` parameter in single request. This upload will not be resumable unless a recoverable error is returned. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `Content-Length` | header |   |
| `name` | path | Name of the target repository. |
| `digest` | query | Digest of uploaded blob. If present, the upload will be completed, in a single request, with contents of the request body as the resulting blob. |

###### On Success: Created

```none
201 Created
Location: <blob location>
Content-Length: 0
Docker-Upload-UUID: <uuid>
```

The blob has been created in the registry and is available at the provided location.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Location` |   |
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |
| `Docker-Upload-UUID` | Identifies the docker upload uuid for the current request. |

###### On Failure: Invalid Name or Digest

```none
400 Bad Request
```

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |

###### On Failure: Not allowed

```none
405 Method Not Allowed
```

Blob upload is not allowed because the registry is configured as a pull-through cache or for some other reason

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNSUPPORTED` | The operation is unsupported. | The operation was unsupported due to a missing implementation or invalid set of parameters. |

###### On Failure: Authentication Required

```none
401 Unauthorized
WWW-Authenticate: <scheme> realm="<realm>", ..."
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client is not authenticated.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `WWW-Authenticate` | An RFC7235 compliant authentication challenge header. |
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNAUTHORIZED` | authentication required | The access controller was unable to authenticate the client. Often this will be accompanied by a Www-Authenticate HTTP response header indicating how to authenticate. |

###### On Failure: No Such Repository Error

```none
404 Not Found
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The repository is not known to the registry.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |

###### On Failure: Access Denied

```none
403 Forbidden
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client does not have required access to the repository.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DENIED` | requested access to the resource is denied | The access controller denied access for the operation on a resource. |

###### On Failure: Too Many Requests

```none
429 Too Many Requests
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client made too many requests within a time interval.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `TOOMANYREQUESTS` | too many requests | Returned when a client attempts to contact a service too many times |

##### Initiate Resumable Blob Upload

```none
POST /v2/<name>/blobs/uploads/
Host: <registry host>
Authorization: <scheme> <token>
Content-Length: 0
```

Initiate a resumable blob upload with an empty request body. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `Content-Length` | header | The `Content-Length` header must be zero and the body must be empty. |
| `name` | path | Name of the target repository. |

###### On Success: Accepted

```none
202 Accepted
Location: /v2/<name>/blobs/uploads/<uuid>
Range: 0-<offset>
Content-Length: 0
Docker-Upload-UUID: <uuid>
```

The upload has been created. The `Location` header must be used to complete the upload. The response should be identical to a `GET` request on the contents of the returned `Location` header.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Location` | The location of the created upload. Clients should use the contents verbatim to complete the upload, adding parameters where required. |
| `Range` | Range header indicating the progress of the upload. When starting an upload, it will return an empty range, since no content has been received. |
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |
| `Docker-Upload-UUID` | Identifies the docker upload uuid for the current request. |

###### On Failure: Invalid Name or Digest

```none
400 Bad Request
```

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |

###### On Failure: Authentication Required

```none
401 Unauthorized
WWW-Authenticate: <scheme> realm="<realm>", ..."
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client is not authenticated.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `WWW-Authenticate` | An RFC7235 compliant authentication challenge header. |
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNAUTHORIZED` | authentication required | The access controller was unable to authenticate the client. Often this will be accompanied by a Www-Authenticate HTTP response header indicating how to authenticate. |

###### On Failure: No Such Repository Error

```none
404 Not Found
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The repository is not known to the registry.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |

###### On Failure: Access Denied

```none
403 Forbidden
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client does not have required access to the repository.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DENIED` | requested access to the resource is denied | The access controller denied access for the operation on a resource. |

###### On Failure: Too Many Requests

```none
429 Too Many Requests
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client made too many requests within a time interval.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `TOOMANYREQUESTS` | too many requests | Returned when a client attempts to contact a service too many times |

##### Mount Blob

```none
POST /v2/<name>/blobs/uploads/?mount=<digest>&from=<repository name>
Host: <registry host>
Authorization: <scheme> <token>
Content-Length: 0
```

Mount a blob identified by the `mount` parameter from another repository. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `Content-Length` | header | The `Content-Length` header must be zero and the body must be empty. |
| `name` | path | Name of the target repository. |
| `mount` | query | Digest of blob to mount from the source repository. |
| `from` | query | Name of the source repository. |

###### On Success: Created

```none
201 Created
Location: <blob location>
Content-Length: 0
Docker-Upload-UUID: <uuid>
```

The blob has been mounted in the repository and is available at the provided location.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Location` |   |
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |
| `Docker-Upload-UUID` | Identifies the docker upload uuid for the current request. |

###### On Failure: Invalid Name or Digest

```none
400 Bad Request
```

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |

###### On Failure: Not allowed

```none
405 Method Not Allowed
```

Blob mount is not allowed because the registry is configured as a pull-through cache or for some other reason

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNSUPPORTED` | The operation is unsupported. | The operation was unsupported due to a missing implementation or invalid set of parameters. |

###### On Failure: Authentication Required

```none
401 Unauthorized
WWW-Authenticate: <scheme> realm="<realm>", ..."
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client is not authenticated.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `WWW-Authenticate` | An RFC7235 compliant authentication challenge header. |
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNAUTHORIZED` | authentication required | The access controller was unable to authenticate the client. Often this will be accompanied by a Www-Authenticate HTTP response header indicating how to authenticate. |

###### On Failure: No Such Repository Error

```none
404 Not Found
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The repository is not known to the registry.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |

###### On Failure: Access Denied

```none
403 Forbidden
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client does not have required access to the repository.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DENIED` | requested access to the resource is denied | The access controller denied access for the operation on a resource. |

###### On Failure: Too Many Requests

```none
429 Too Many Requests
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client made too many requests within a time interval.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `TOOMANYREQUESTS` | too many requests | Returned when a client attempts to contact a service too many times |

### Blob Upload

Interact with blob uploads. Clients should never assemble URLs for this endpoint and should only take it through the `Location` header on related API requests. The `Location` header and its parameters should be preserved by clients, using the latest value returned via upload related API calls.

#### GET Blob Upload

Retrieve status of upload identified by `uuid`. The primary purpose of this endpoint is to resolve the current status of a resumable upload.

```none
GET /v2/<name>/blobs/uploads/<uuid>
Host: <registry host>
Authorization: <scheme> <token>
```

Retrieve the progress of the current upload, as reported by the `Range` header. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |
| `uuid` | path | A uuid identifying the upload. This field can accept characters that match `[a-zA-Z0-9-_.=]+`. |

###### On Success: Upload Progress

```none
204 No Content
Range: 0-<offset>
Content-Length: 0
Docker-Upload-UUID: <uuid>
```

The upload is known and in progress. The last received offset is available in the `Range` header.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Range` | Range indicating the current progress of the upload. |
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |
| `Docker-Upload-UUID` | Identifies the docker upload uuid for the current request. |

###### On Failure: Bad Request

```none
400 Bad Request
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

There was an error processing the upload and it must be restarted.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |
| `BLOB_UPLOAD_INVALID` | blob upload invalid | The blob upload encountered an error and can no longer proceed. |

###### On Failure: Not Found

```none
404 Not Found
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The upload is unknown to the registry. The upload must be restarted.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `BLOB_UPLOAD_UNKNOWN` | blob upload unknown to registry | If a blob upload has been cancelled or was never started, this error code may be returned. |

###### On Failure: Authentication Required

```none
401 Unauthorized
WWW-Authenticate: <scheme> realm="<realm>", ..."
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client is not authenticated.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `WWW-Authenticate` | An RFC7235 compliant authentication challenge header. |
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNAUTHORIZED` | authentication required | The access controller was unable to authenticate the client. Often this will be accompanied by a Www-Authenticate HTTP response header indicating how to authenticate. |

###### On Failure: No Such Repository Error

```none
404 Not Found
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The repository is not known to the registry.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |

###### On Failure: Access Denied

```none
403 Forbidden
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client does not have required access to the repository.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DENIED` | requested access to the resource is denied | The access controller denied access for the operation on a resource. |

###### On Failure: Too Many Requests

```none
429 Too Many Requests
Content-Length: <length>
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

The client made too many requests within a time interval.

The following headers will be returned on the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `TOOMANYREQUESTS` | too many requests | Returned when a client attempts to contact a service too many times |

#### PATCH Blob Upload

Upload a chunk of data for the specified upload.

##### Stream upload

```none
PATCH /v2/<name>/blobs/uploads/<uuid>
Host: <registry host>
Authorization: <scheme> <token>
Content-Type: application/octet-stream

<binary data>
```

Upload a stream of data to upload without completing the upload. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |
| `uuid` | path | A uuid identifying the upload. This field can accept characters that match `[a-zA-Z0-9-_.=]+`. |

###### On Success: Data Accepted

```none
202 Accepted
Location: /v2/<name>/blobs/uploads/<uuid>
Range: 0-<offset>
Content-Length: 0
Docker-Upload-UUID: <uuid>
```

The stream of data has been accepted and the current progress is available in the range header. The updated upload location is available in the `Location` header.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Location` | The location of the upload. Clients should assume this changes after each request. Clients should use the contents verbatim to complete the upload, adding parameters where required. |
| `Range` | Range indicating the current progress of the upload. |
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |
| `Docker-Upload-UUID` | Identifies the docker upload uuid for the current request. |

###### On Failure: Bad Request

```none
400 Bad Request
Content-Type: application/json

{
	"errors": [
	    {
            "code": <error code>,
            "message": "<error message>",
            "detail": ...
        },
        ...
    ]
}
```

There was an error processing the upload and it must be restarted.
