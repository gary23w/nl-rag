---
title: "HTTP API V2 (part 2/4)"
source: https://distribution.github.io/distribution/spec/api/
domain: container-registry
license: CC-BY-SA-4.0
tags: container registry, container image registry, oci image, image distribution
fetched: 2026-07-02
part: 2/4
---

## Detail

> This section is still under construction. For the purposes of implementation, if any details below differ from the described request flows above, the section below should be corrected. When they match, this note should be removed.

The behavior of the endpoints are covered in detail in this section, organized by route and entity. All aspects of the request and responses are covered, including headers, parameters and body formats. Examples of requests and their corresponding responses, with success and failure, are enumerated.

> The sections on endpoint detail are arranged with an example request, a description of the request, followed by information about that request.

A list of methods and URIs are covered in the table below:

| Method | Path | Entity | Description |
|---|---|---|---|
| GET | `/v2/` | Base | Check that the endpoint implements Docker Registry API V2. |
| GET | `/v2/<name>/tags/list` | Tags | Fetch the tags under the repository identified by `name`. |
| GET | `/v2/<name>/manifests/<reference>` | Manifest | Fetch the manifest identified by `name` and `reference` where `reference` can be a tag or digest. A `HEAD` request can also be issued to this endpoint to obtain resource information without receiving all data. |
| PUT | `/v2/<name>/manifests/<reference>` | Manifest | Put the manifest identified by `name` and `reference` where `reference` can be a tag or digest. |
| DELETE | `/v2/<name>/manifests/<reference>` | Manifest | Delete the manifest or tag identified by `name` and `reference` where `reference` can be a tag or digest. Note that a manifest can *only* be deleted by digest. |
| GET | `/v2/<name>/blobs/<digest>` | Blob | Retrieve the blob from the registry identified by `digest`. A `HEAD` request can also be issued to this endpoint to obtain resource information without receiving all data. |
| DELETE | `/v2/<name>/blobs/<digest>` | Blob | Delete the blob identified by `name` and `digest` |
| POST | `/v2/<name>/blobs/uploads/` | Initiate Blob Upload | Initiate a resumable blob upload. If successful, an upload location will be provided to complete the upload. Optionally, if the `digest` parameter is present, the request body will be used to complete the upload in a single request. |
| GET | `/v2/<name>/blobs/uploads/<uuid>` | Blob Upload | Retrieve status of upload identified by `uuid`. The primary purpose of this endpoint is to resolve the current status of a resumable upload. |
| PATCH | `/v2/<name>/blobs/uploads/<uuid>` | Blob Upload | Upload a chunk of data for the specified upload. |
| PUT | `/v2/<name>/blobs/uploads/<uuid>` | Blob Upload | Complete the upload specified by `uuid`, optionally appending the body as the final chunk. |
| DELETE | `/v2/<name>/blobs/uploads/<uuid>` | Blob Upload | Cancel outstanding upload processes, releasing associated resources. If this is not called, the unfinished uploads will eventually timeout. |
| GET | `/v2/_catalog` | Catalog | Retrieve a sorted, json list of repositories available in the registry. |

The detail for each endpoint is covered in the following sections.

### Errors

The error codes encountered via the API are enumerated in the following table:

| Code | Message | Description |
|---|---|---|
| `BLOB_UNKNOWN` | blob unknown to registry | This error may be returned when a blob is unknown to the registry in a specified repository. This can be returned with a standard get or if a manifest references an unknown layer during upload. |
| `BLOB_UPLOAD_INVALID` | blob upload invalid | The blob upload encountered an error and can no longer proceed. |
| `BLOB_UPLOAD_UNKNOWN` | blob upload unknown to registry | If a blob upload has been cancelled or was never started, this error code may be returned. |
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |
| `MANIFEST_BLOB_UNKNOWN` | blob unknown to registry | This error may be returned when a manifest blob is unknown to the registry. |
| `MANIFEST_INVALID` | manifest invalid | During upload, manifests undergo several checks ensuring validity. If those checks fail, this error may be returned, unless a more specific error is included. The detail will contain information the failed validation. |
| `MANIFEST_UNKNOWN` | manifest unknown | This error is returned when the manifest, identified by name and tag is unknown to the repository. |
| `MANIFEST_UNVERIFIED` | manifest failed signature verification | During manifest upload, if the manifest fails signature verification, this error will be returned. |
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |
| `PAGINATION_NUMBER_INVALID` | invalid number of results requested | Returned when the “n” parameter (number of results to return) is not an integer, “n” is negative or “n” is bigger than the maximum allowed. |
| `RANGE_INVALID` | invalid content range | When a layer is uploaded, the provided range is checked against the uploaded chunk. This error is returned if the range is out of order. |
| `SIZE_INVALID` | provided length did not match content length | When a layer is uploaded, the provided size will be checked against the uploaded content. If they do not match, this error will be returned. |
| `TAG_INVALID` | manifest tag did not match URI | During a manifest upload, if the tag in the manifest does not match the uri tag, this error will be returned. |
| `UNAUTHORIZED` | authentication required | The access controller was unable to authenticate the client. Often this will be accompanied by a Www-Authenticate HTTP response header indicating how to authenticate. |
| `DENIED` | requested access to the resource is denied | The access controller denied access for the operation on a resource. |
| `UNSUPPORTED` | The operation is unsupported. | The operation was unsupported due to a missing implementation or invalid set of parameters. |

### Base

Base V2 API route. Typically, this can be used for lightweight version checks and to validate registry authentication.

#### GET Base

Check that the endpoint implements Docker Registry API V2.

```none
GET /v2/
Host: <registry host>
Authorization: <scheme> <token>
```

The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |

###### On Success: OK

```none
200 OK
```

The API implements V2 protocol and is accessible.

###### On Failure: Not Found

```none
404 Not Found
```

The registry does not implement the V2 API.

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

### Tags

Retrieve information about tags.

#### GET Tags

Fetch the tags under the repository identified by `name`.

##### Tags

```none
GET /v2/<name>/tags/list
Host: <registry host>
Authorization: <scheme> <token>
```

Return all tags for the repository The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |

###### On Success: OK

```none
200 OK
Content-Length: <length>
Content-Type: application/json

{
    "name": <name>,
    "tags": [
        <tag>,
        ...
    ]
}
```

A list of tags for the named repository.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Content-Length` | Length of the JSON response body. |

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

##### Tags Paginated

```none
GET /v2/<name>/tags/list?n=<integer>&last=<integer>
```

Return a portion of the tags for the specified repository. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `name` | path | Name of the target repository. |
| `n` | query | Limit the number of entries in each response. It not present, 100 entries will be returned. |
| `last` | query | Result set will include values lexically after last. |

###### On Success: OK

```none
200 OK
Content-Length: <length>
Link: <<url>?n=<last n value>&last=<last entry from response>>; rel="next"
Content-Type: application/json

{
    "name": <name>,
    "tags": [
        <tag>,
        ...
    ],
}
```

A list of tags for the named repository.

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

### Manifest

Create, update, delete and retrieve manifests.

#### GET Manifest

Fetch the manifest identified by `name` and `reference` where `reference` can be a tag or digest. A `HEAD` request can also be issued to this endpoint to obtain resource information without receiving all data.

```none
GET /v2/<name>/manifests/<reference>
Host: <registry host>
Authorization: <scheme> <token>
```

The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |
| `reference` | path | Tag or digest of the target manifest. |

###### On Success: OK

```none
200 OK
Docker-Content-Digest: <digest>
Content-Type: <media type of manifest>

{
    "name": <name>,
    "tag": <tag>,
    "fsLayers": [
        {
            "blobSum": "<digest>"
        },
        ...
    ],
    "history": <v1 images>,
    "signature": <JWS>
}
```

The manifest identified by `name` and `reference`. The contents can be used to identify and resolve resources required to run the specified image.

The following headers will be returned with the response:

| Name | Description |
|---|---|
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

The name or reference was invalid.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |
| `TAG_INVALID` | manifest tag did not match URI | During a manifest upload, if the tag in the manifest does not match the uri tag, this error will be returned. |

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

#### PUT Manifest

Put the manifest identified by `name` and `reference` where `reference` can be a tag or digest.

```none
PUT /v2/<name>/manifests/<reference>
Host: <registry host>
Authorization: <scheme> <token>
Content-Type: <media type of manifest>

{
    "name": <name>,
    "tag": <tag>,
    "fsLayers": [
        {
            "blobSum": "<digest>"
        },
        ...
    ],
    "history": <v1 images>,
    "signature": <JWS>
}
```

The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |
| `reference` | path | Tag or digest of the target manifest. |

###### On Success: Created

```none
201 Created
Location: <url>
Content-Length: 0
Docker-Content-Digest: <digest>
```

The manifest has been accepted by the registry and is stored under the specified `name` and `tag`.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Location` | The canonical location url of the uploaded manifest. |
| `Content-Length` | The `Content-Length` header must be zero and the body must be empty. |
| `Docker-Content-Digest` | Digest of the targeted content for the request. |

###### On Failure: Invalid Manifest

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

The received manifest was invalid in some way, as described by the error codes. The client should resolve the issue and retry the request.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |
| `TAG_INVALID` | manifest tag did not match URI | During a manifest upload, if the tag in the manifest does not match the uri tag, this error will be returned. |
| `MANIFEST_INVALID` | manifest invalid | During upload, manifests undergo several checks ensuring validity. If those checks fail, this error may be returned, unless a more specific error is included. The detail will contain information the failed validation. |
| `MANIFEST_UNVERIFIED` | manifest failed signature verification | During manifest upload, if the manifest fails signature verification, this error will be returned. |
| `BLOB_UNKNOWN` | blob unknown to registry | This error may be returned when a blob is unknown to the registry in a specified repository. This can be returned with a standard get or if a manifest references an unknown layer during upload. |

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

###### On Failure: Missing Layer(s)

```none
400 Bad Request
Content-Type: application/json

{
    "errors": [
        {
            "code": "BLOB_UNKNOWN",
            "message": "blob unknown to registry",
            "detail": {
                "digest": "<digest>"
            }
        },
        ...
    ]
}
```

One or more layers may be missing during a manifest upload. If so, the missing layers will be enumerated in the error response.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `BLOB_UNKNOWN` | blob unknown to registry | This error may be returned when a blob is unknown to the registry in a specified repository. This can be returned with a standard get or if a manifest references an unknown layer during upload. |

###### On Failure: Not allowed

```none
405 Method Not Allowed
```

Manifest put is not allowed because the registry is configured as a pull-through cache or for some other reason

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNSUPPORTED` | The operation is unsupported. | The operation was unsupported due to a missing implementation or invalid set of parameters. |

#### DELETE Manifest

Delete the manifest or tag identified by `name` and `reference` where `reference` can be a tag or digest. Note that a manifest can *only* be deleted by digest.

```none
DELETE /v2/<name>/manifests/<reference>
Host: <registry host>
Authorization: <scheme> <token>
```

The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |
| `reference` | path | Tag or digest of the target manifest. |

###### On Success: Accepted

```none
202 Accepted
```

###### On Failure: Invalid Name or Reference

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

The specified `name` or `reference` were invalid and the delete was unable to proceed.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |
| `TAG_INVALID` | manifest tag did not match URI | During a manifest upload, if the tag in the manifest does not match the uri tag, this error will be returned. |

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

###### On Failure: Unknown Manifest

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

The specified `name` or `reference` are unknown to the registry and the delete was unable to proceed. Clients can assume the manifest or tag was already deleted if this response is returned.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |
| `MANIFEST_UNKNOWN` | manifest unknown | This error is returned when the manifest, identified by name and tag is unknown to the repository. |

###### On Failure: Not allowed

```none
405 Method Not Allowed
```

Manifest or tag delete is not allowed because the registry is configured as a pull-through cache or `delete` has been disabled.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `UNSUPPORTED` | The operation is unsupported. | The operation was unsupported due to a missing implementation or invalid set of parameters. |

### Blob

Operations on blobs identified by `name` and `digest`. Used to fetch or delete layers by digest.

#### GET Blob

Retrieve the blob from the registry identified by `digest`. A `HEAD` request can also be issued to this endpoint to obtain resource information without receiving all data.

##### Fetch Blob

```none
GET /v2/<name>/blobs/<digest>
Host: <registry host>
Authorization: <scheme> <token>
```

The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |
| `digest` | path | Digest of desired blob. |

###### On Success: OK

```none
200 OK
Content-Length: <length>
Docker-Content-Digest: <digest>
Content-Type: application/octet-stream

<blob binary data>
```

The blob identified by `digest` is available. The blob content will be present in the body of the request.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Content-Length` | The length of the requested blob content. |
| `Docker-Content-Digest` | Digest of the targeted content for the request. |

###### On Success: Temporary Redirect

```none
307 Temporary Redirect
Location: <blob location>
Docker-Content-Digest: <digest>
```

The blob identified by `digest` is available at the provided location.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Location` | The location where the layer should be accessible. |
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

There was a problem with the request that needs to be addressed by the client, such as an invalid `name` or `tag`.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |

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

The blob, identified by `name` and `digest`, is unknown to the registry.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |
| `BLOB_UNKNOWN` | blob unknown to registry | This error may be returned when a blob is unknown to the registry in a specified repository. This can be returned with a standard get or if a manifest references an unknown layer during upload. |

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

##### Fetch Blob Part

```none
GET /v2/<name>/blobs/<digest>
Host: <registry host>
Authorization: <scheme> <token>
Range: bytes=<start>-<end>
```

This endpoint may also support RFC7233 compliant range requests. Support can be detected by issuing a HEAD request. If the header `Accept-Range: bytes` is returned, range requests can be used to fetch partial content. The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `Range` | header | HTTP Range header specifying blob chunk. |
| `name` | path | Name of the target repository. |
| `digest` | path | Digest of desired blob. |

###### On Success: Partial Content

```none
206 Partial Content
Content-Length: <length>
Content-Range: bytes <start>-<end>/<size>
Content-Type: application/octet-stream

<blob binary data>
```

The blob identified by `digest` is available. The specified chunk of blob content will be present in the body of the request.

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Content-Length` | The length of the requested blob chunk. |
| `Content-Range` | Content range of blob chunk. |

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

There was a problem with the request that needs to be addressed by the client, such as an invalid `name` or `tag`.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |

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

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |
| `BLOB_UNKNOWN` | blob unknown to registry | This error may be returned when a blob is unknown to the registry in a specified repository. This can be returned with a standard get or if a manifest references an unknown layer during upload. |

###### On Failure: Requested Range Not Satisfiable

```none
416 Requested Range Not Satisfiable
```

The range specification cannot be satisfied for the requested content. This can happen when the range is not formatted correctly or if the range is outside of the valid size of the content.

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

#### DELETE Blob

Delete the blob identified by `name` and `digest`

```none
DELETE /v2/<name>/blobs/<digest>
Host: <registry host>
Authorization: <scheme> <token>
```

The following parameters should be specified on the request:

| Name | Kind | Description |
|---|---|---|
| `Host` | header | Standard HTTP Host Header. Should be set to the registry host. |
| `Authorization` | header | An RFC7235 compliant authorization header. |
| `name` | path | Name of the target repository. |
| `digest` | path | Digest of desired blob. |

###### On Success: Accepted

```none
202 Accepted
Content-Length: 0
Docker-Content-Digest: <digest>
```

The following headers will be returned with the response:

| Name | Description |
|---|---|
| `Content-Length` | 0 |
| `Docker-Content-Digest` | Digest of the targeted content for the request. |

###### On Failure: Invalid Name or Digest

```none
400 Bad Request
```

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `DIGEST_INVALID` | provided digest did not match uploaded content | When a blob is uploaded, the registry will check that the content matches the digest provided by the client. The error may include a detail structure with the key “digest”, including the invalid digest string. This error may also be returned when a manifest includes an invalid layer digest. |
| `NAME_INVALID` | invalid repository name | Invalid repository name encountered either during manifest validation or any API operation. |

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

The blob, identified by `name` and `digest`, is unknown to the registry.

The error codes that may be included in the response body are enumerated below:

| Code | Message | Description |
|---|---|---|
| `NAME_UNKNOWN` | repository name not known to registry | This is returned if the name used during an operation is unknown to the registry. |
| `BLOB_UNKNOWN` | blob unknown to registry | This error may be returned when a blob is unknown to the registry in a specified repository. This can be returned with a standard get or if a manifest references an unknown layer during upload. |

###### On Failure: Method Not Allowed

```none
405 Method Not Allowed
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

Blob delete is not allowed because the registry is configured as a pull-through cache or `delete` has been disabled

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
