---
title: "HTTP API V2 (part 4/4)"
source: https://distribution.github.io/distribution/spec/api/
domain: container-registry
license: CC-BY-SA-4.0
tags: container registry, container image registry, oci image, image distribution
fetched: 2026-07-02
part: 4/4
---

# HTTP API V2

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

##### Chunked upload

```none
PATCH /v2/<name>/blobs/uploads/<uuid>
Host: <registry host>
Authorization: <scheme> <token>
Content-Range: <start of range>-<end of range, inclusive>
Content-Length: <length of chunk>
Content-Type: application/octet-stream

<binary chunk>
```

Upload a chunk of data to specified upload without completing the upload. The data will be uploaded to the specified Content Range. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `Content-Range` | header | Range of bytes identifying the desired block of content represented by the body. Start must the end offset retrieved via status check plus one. Note that this is a non-standard use of the `Content-Range` header. |
| `Content-Length` | header | Length of the chunk being uploaded, corresponding the length of the request body. |
| `name` | path | Name of the target repository. |
| `uuid` | path | A uuid identifying the upload. This field can accept characters that match `[a-zA-Z0-9-_.=]+`. |

###### On Success: Chunk Accepted

```none
202 Accepted
Location: /v2/<name>/blobs/uploads/<uuid>
Range: 0-<offset>
Content-Length: 0
Docker-Upload-UUID: <uuid>
```

The chunk of data has been accepted and the current progress is available in the range header. The updated upload location is available in the `Location` header.

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

###### On Failure: Requested Range Not Satisfiable

```none
416 Requested Range Not Satisfiable
```

The `Content-Range` specification cannot be accepted, either because it does not overlap with the current progress or it is invalid.

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

#### PUT Blob Upload

Complete the upload specified by `uuid`, optionally appending the body as the final chunk.

```none
PUT /v2/<name>/blobs/uploads/<uuid>?digest=<digest>
Host: <registry host>
Authorization: <scheme> <token>
Content-Length: <length of data>
Content-Type: application/octet-stream

<binary data>
```

Complete the upload, providing all the data in the body, if necessary. A request without a body will just complete the upload with previously uploaded content. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `Content-Length` | header | Length of the data being uploaded, corresponding to the length of the request body. May be zero if no data is provided. |
| `name` | path | Name of the target repository. |
| `uuid` | path | A uuid identifying the upload. This field can accept characters that match `[a-zA-Z0-9-_.=]+`. |
| `digest` | query | Digest of uploaded blob. |

###### On Success: Upload Complete

```none
201 Created
Location: <blob location>
Content-Range: <start of range>-<end of range, inclusive>
Content-Length: 0
Docker-Content-Digest: <digest>
```

The upload has been completed and accepted by the registry. The canonical location will be available in the `Location` header.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Location` | The canonical location of the blob for retrieval |
| `Content-Range` | Range of bytes identifying the desired block of content represented by the body. Start must match the end of offset retrieved via status check. Note that this is a non-standard use of the `Content-Range` header. |
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |
| `Docker-Content-Digest` | Digest of the targeted content for the request. |

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
| `UNSUPPORTED` | The operation is unsupported. | The operation was unsupported due to a missing implementation or invalid set of parameters. |

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

#### DELETE Blob Upload

Cancel outstanding upload processes, releasing associated resources. If this is not called, the unfinished uploads will eventually timeout.

```none
DELETE /v2/<name>/blobs/uploads/<uuid>
Host: <registry host>
Authorization: <scheme> <token>
Content-Length: 0
```

Cancel the upload specified by `uuid`. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `Content-Length` | header | The `Content-Length` header must be zero and the body must be empty. |
| `name` | path | Name of the target repository. |
| `uuid` | path | A uuid identifying the upload. This field can accept characters that match `[a-zA-Z0-9-_.=]+`. |

###### On Success: Upload Deleted

```none
204 No Content
Content-Length: 0
```

The upload has been successfully deleted.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |

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

An error was encountered processing the delete. The client may ignore this error.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
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

The upload is unknown to the registry. The client may ignore this error and assume the upload has been deleted.

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

### Catalog

List a set of available repositories in the local registry cluster. Does not provide any indication of what may be available upstream. Applications can only determine if a repository is available but not if it is not available.

#### GET Catalog

Retrieve a sorted, json list of repositories available in the registry.

##### Catalog Fetch

```none
GET /v2/_catalog
```

Request an unabridged list of repositories available. The implementation may impose a maximum limit and return a partial set with pagination links.

###### On Success: OK

```none
200 OK
Content-Length: <length>
Content-Type: application/json

{
	"repositories": [
		<name>,
		...
	],
}
```

Returns the unabridged list of repositories as a json response.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

##### Catalog Fetch Paginated

```none
GET /v2/_catalog?n=<integer>&last=<integer>
```

Return the specified portion of repositories. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `n` | query | Limit the number of entries in each response. It not present, 100 entries will be returned. |
| `last` | query | Result set will include values lexically after last. |

###### On Success: OK

```none
200 OK
Content-Length: <length>
Link: <<url>?n=<last n value>&last=<last entry from response>>; rel="next"
Content-Type: application/json

{
	"repositories": [
		<name>,
		...
	],
	"next": "<url>?last=<name>&n=<last value of n>"
}
```

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |
| `Link` | RFC5988 compliant rel=‘next’ with URL to next result set, if available |

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

The received parameter n was invalid in some way, as described by the error code. The client should resolve the issue and retry the request.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `PAGINATION_NUMBER_INVALID` | invalid number of results requested | Returned when the “n” parameter (number of results to return) is not an integer, “n” is negative or “n” is bigger than the maximum allowed. |
