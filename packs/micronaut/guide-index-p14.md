---
title: "Micronaut Core (part 14/27)"
source: https://docs.micronaut.io/latest/guide/index.html
domain: micronaut
license: CC-BY-SA-4.0
tags: micronaut framework, micronaut jvm, compile-time injection, microservices framework
fetched: 2026-07-02
part: 14/27
---

## Route Arguments

Method argument types determine how files are received. Data can be received a chunk at a time or when an upload is completed.

|   | If the route argument name cannot or should not match the name of the part in the request, add the Part annotation to the argument and specify the expected name in the request. |
|---|---|

### Chunk Data Types

PartData represents a chunk of data received in a multipart request. PartData interface methods convert the data to a `byte[]`, InputStream, or a ByteBuffer.

|   | Data can only be retrieved from a PartData once. The underlying buffer is released, causing further attempts to fail. |
|---|---|

Route arguments of type Publisher are treated as intended to receive a single file, and each chunk of the received file will be sent downstream. If the generic type is other than PartData, conversion will be attempted using Micronaut’s conversion service. Conversions to `String` and `byte[]` are supported by default.

If you need knowledge about the metadata of an uploaded file, the StreamingFileUpload class is a Publisher that also has file information such as the content type and file name.

Streaming file upload

```java
import io.micronaut.core.async.annotation.SingleResult;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.multipart.StreamingFileUpload;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;

import static io.micronaut.http.HttpStatus.CONFLICT;
import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA;
import static io.micronaut.http.MediaType.TEXT_PLAIN;

@Controller("/upload")
public class UploadController {

    @Post(value = "/", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    @SingleResult
    public Publisher<HttpResponse<String>> upload(StreamingFileUpload file) { // (2)

        File tempFile;
        try {
            tempFile = File.createTempFile(file.getFilename(), "temp");
        } catch (IOException e) {
            return Mono.error(e);
        }
        Publisher<?> uploadPublisher = file.transferTo(tempFile); // (3)

        return Mono.from(uploadPublisher)  // (4)
            .<HttpResponse<String>>thenReturn(HttpResponse.ok("Uploaded"))
            .onErrorReturn(HttpResponse.<String>status(CONFLICT).body("Upload Failed"));
    }

}
```

Streaming file upload

```kotlin
import io.micronaut.core.async.annotation.SingleResult
import io.micronaut.http.HttpResponse
import io.micronaut.http.HttpStatus.CONFLICT
import io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import io.micronaut.http.MediaType.TEXT_PLAIN
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.StreamingFileUpload
import reactor.core.publisher.Mono
import java.io.ByteArrayOutputStream
import java.io.File

@Controller("/upload")
class UploadController {

    @Post(value = "/", consumes = [MULTIPART_FORM_DATA], produces = [TEXT_PLAIN]) // (1)
    fun upload(file: StreamingFileUpload): Mono<HttpResponse<String>> { // (2)

        val tempFile = File.createTempFile(file.filename, "temp")
        val uploadPublisher = file.transferTo(tempFile) // (3)

        return Mono.from(uploadPublisher)  // (4)
            .thenReturn<HttpResponse<String>>(HttpResponse.ok("Uploaded"))
            .onErrorReturn(HttpResponse.status<String>(CONFLICT)
                .body("Upload Failed"))
    }

}
// end::endclass]
```

Streaming file upload

```groovy
import io.micronaut.core.async.annotation.SingleResult
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.StreamingFileUpload
import org.reactivestreams.Publisher
import reactor.core.publisher.Mono

import static io.micronaut.http.HttpStatus.CONFLICT
import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import static io.micronaut.http.MediaType.TEXT_PLAIN

@Controller("/upload")
class UploadController {

    @Post(value = "/", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    Mono<HttpResponse<String>> upload(StreamingFileUpload file) { // (2)

        File tempFile = File.createTempFile(file.filename, "temp")
        Publisher<Boolean> uploadPublisher = file.transferTo(tempFile) // (3)

        Mono.from(uploadPublisher)  // (4)
            .thenReturn(HttpResponse.ok("Uploaded"))
            .onErrorReturn(HttpResponse.<String>status(CONFLICT)
                    .body("Upload Failed"))
    }

}
```

| **1** | The method consumes MULTIPART_FORM_DATA |
|---|---|
| **2** | The method parameters match form attribute names. In this case `file` will match for example an `<input type="file" name="file">` |
| **3** | The StreamingFileUpload.transferTo(File) method transfers the file to the server. The method returns a Publisher |
| **4** | The returned Mono subscribes to the Publisher and outputs a response once the upload is complete, without blocking. |

It is also possible to pass an output stream with the `transferTo` method.

|   | The reading of the file or stream will be offloaded to the IO thread pool to prevent the possibility of blocking the event loop. |
|---|---|

Streaming file upload

```java
import io.micronaut.core.async.annotation.SingleResult;
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.multipart.StreamingFileUpload;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;

import static io.micronaut.http.HttpStatus.CONFLICT;
import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA;
import static io.micronaut.http.MediaType.TEXT_PLAIN;

@Controller("/upload")
public class UploadController {

    @Post(value = "/outputStream", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    @SingleResult
    public Mono<HttpResponse<String>> uploadOutputStream(StreamingFileUpload file) { // (2)

        OutputStream outputStream = new ByteArrayOutputStream(); // (3)

        Publisher<?> uploadPublisher = file.transferTo(outputStream); // (4)

        return Mono.from(uploadPublisher)  // (5)
            .<HttpResponse<String>>thenReturn(HttpResponse.ok("Uploaded"))
            .onErrorReturn(HttpResponse.<String>status(CONFLICT).body("Upload Failed"));
    }

}
```

Streaming file upload

```kotlin
import io.micronaut.core.async.annotation.SingleResult
import io.micronaut.http.HttpResponse
import io.micronaut.http.HttpStatus.CONFLICT
import io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import io.micronaut.http.MediaType.TEXT_PLAIN
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.StreamingFileUpload
import reactor.core.publisher.Mono
import java.io.ByteArrayOutputStream
import java.io.File

@Controller("/upload")
class UploadController {

    @Post(value = "/outputStream", consumes = [MULTIPART_FORM_DATA], produces = [TEXT_PLAIN]) // (1)
    @SingleResult
    fun uploadOutputStream(file: StreamingFileUpload): Mono<HttpResponse<String>> { // (2)
        val outputStream  = ByteArrayOutputStream() // (3)
        val uploadPublisher = file.transferTo(outputStream) // (4)

        return Mono.from(uploadPublisher) // (5)
            .thenReturn<HttpResponse<String>>(HttpResponse.ok("Uploaded"))
            .onErrorReturn(HttpResponse.status<String>(CONFLICT)
                .body("Upload Failed"))
    }

}
// end::endclass]
```

Streaming file upload

```groovy
import io.micronaut.core.async.annotation.SingleResult
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.StreamingFileUpload
import org.reactivestreams.Publisher
import reactor.core.publisher.Mono

import static io.micronaut.http.HttpStatus.CONFLICT
import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import static io.micronaut.http.MediaType.TEXT_PLAIN

@Controller("/upload")
class UploadController {

    @Post(value = "/outputStream", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    @SingleResult
    Mono<HttpResponse<String>> uploadOutputStream(StreamingFileUpload file) { // (2)

        OutputStream outputStream = new ByteArrayOutputStream() // (3)

        Publisher<Boolean> uploadPublisher = file.transferTo(outputStream) // (4)

        Mono.from(uploadPublisher)  // (5)
                .thenReturn(HttpResponse.ok("Uploaded"))
                .onErrorReturn(HttpResponse.<String>status(CONFLICT)
                        .body("Upload Failed"))
    }

}
```

| **1** | The method consumes MULTIPART_FORM_DATA |
|---|---|
| **2** | The method parameters match form attribute names. In this case `file` will match for example an `<input type="file" name="file">` |
| **3** | A stream is created to output the data to. In real world scenarios this would come from some other source. |
| **4** | The StreamingFileUpload.transferTo(OutputStream) method transfers the file to the server. The method returns a Publisher |
| **5** | The returned Mono subscribes to the Publisher and outputs a response once the upload is complete, without blocking. |

### Whole Data Types

Route arguments that are not publishers cause route execution to be delayed until the upload has finished. The received data will attempt to be converted to the requested type. Conversions to a `String` or `byte[]` are supported by default. In addition, the file can be converted to a POJO if a media type codec is registered that supports the media type of the file. A media type codec is included by default that allows conversion of JSON files to POJOs.

Receiving a byte array

```java
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA;
import static io.micronaut.http.MediaType.TEXT_PLAIN;

@Controller("/upload")
public class BytesUploadController {

    @Post(value = "/bytes", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    public HttpResponse<String> uploadBytes(byte[] file, String fileName) { // (2)
        try {
            File tempFile = File.createTempFile(fileName, "temp");
            Path path = Paths.get(tempFile.getAbsolutePath());
            Files.write(path, file); // (3)
            return HttpResponse.ok("Uploaded");
        } catch (IOException e) {
            return HttpResponse.badRequest("Upload Failed");
        }
    }
}
```

Receiving a byte array

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import io.micronaut.http.MediaType.TEXT_PLAIN
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import java.io.File
import java.io.IOException
import java.nio.file.Files
import java.nio.file.Paths

@Controller("/upload")
class BytesUploadController {

    @Post(value = "/bytes", consumes = [MULTIPART_FORM_DATA], produces = [TEXT_PLAIN]) // (1)
    fun uploadBytes(file: ByteArray, fileName: String): HttpResponse<String> { // (2)
        return try {
            val tempFile = File.createTempFile(fileName, "temp")
            val path = Paths.get(tempFile.absolutePath)
            Files.write(path, file) // (3)
            HttpResponse.ok("Uploaded")
        } catch (e: IOException) {
            HttpResponse.badRequest("Upload Failed")
        }
    }
}
```

Receiving a byte array

```groovy
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post

import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import static io.micronaut.http.MediaType.TEXT_PLAIN

@Controller("/upload")
class BytesUploadController {

    @Post(value = "/bytes", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    HttpResponse<String> uploadBytes(byte[] file, String fileName) { // (2)
        try {
            File tempFile = File.createTempFile(fileName, "temp")
            Path path = Paths.get(tempFile.absolutePath)
            Files.write(path, file) // (3)
            HttpResponse.ok("Uploaded")
        } catch (IOException e) {
            HttpResponse.badRequest("Upload Failed")
        }
    }
}
```

If you need knowledge about the metadata of an uploaded file, the CompletedFileUpload class has methods to retrieve the data of the file, and also file information such as the content type and file name.

File upload with metadata

```java
import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.multipart.CompletedFileUpload;
import io.micronaut.scheduling.TaskExecutors;
import io.micronaut.scheduling.annotation.ExecuteOn;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA;
import static io.micronaut.http.MediaType.TEXT_PLAIN;

@Controller("/upload")
public class CompletedUploadController {

    @Post(value = "/completed", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    @ExecuteOn(TaskExecutors.BLOCKING)
    public HttpResponse<String> uploadCompleted(CompletedFileUpload file) throws IOException { // (2)
        try {
            File tempFile = File.createTempFile(file.getFilename(), "temp"); //(3)
            Path path = Paths.get(tempFile.getAbsolutePath());
            Files.write(path, file.getBytes()); //(3)
            return HttpResponse.ok("Uploaded");
        } catch (IOException e) {
            return HttpResponse.badRequest("Upload Failed");
        } finally {
            file.close();
        }
    }
}
```

File upload with metadata

```kotlin
import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import io.micronaut.http.MediaType.TEXT_PLAIN
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.CompletedFileUpload
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn
import java.io.File
import java.io.IOException
import java.nio.file.Files
import java.nio.file.Paths

@Controller("/upload")
class CompletedUploadController {

    @Post(value = "/completed", consumes = [MULTIPART_FORM_DATA], produces = [TEXT_PLAIN]) // (1)
    @ExecuteOn(TaskExecutors.BLOCKING)
    fun uploadCompleted(file: CompletedFileUpload): HttpResponse<String> { // (2)
        return try {
            val tempFile = File.createTempFile(file.filename, "temp") //(3)
            val path = Paths.get(tempFile.absolutePath)
            Files.write(path, file.bytes) //(3)
            HttpResponse.ok("Uploaded")
        } catch (e: IOException) {
            HttpResponse.badRequest("Upload Failed")
        } finally {
            file.close()
        }
    }
}
```

File upload with metadata

```groovy
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.CompletedFileUpload
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn

import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import static io.micronaut.http.MediaType.TEXT_PLAIN

@Controller("/upload")
class CompletedUploadController {

    @Post(value = "/completed", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    @ExecuteOn(TaskExecutors.BLOCKING)
    HttpResponse<String> uploadCompleted(CompletedFileUpload file) { // (2)
        try {
            File tempFile = File.createTempFile(file.filename, "temp") //(3)
            Path path = Paths.get(tempFile.absolutePath)
            Files.write(path, file.bytes) //(3)
            HttpResponse.ok("Uploaded")
        } catch (IOException e) {
            HttpResponse.badRequest("Upload Failed")
        } finally {
            file.close()
        }
    }
}
```

| **1** | The method consumes MULTIPART_FORM_DATA |
|---|---|
| **2** | The method parameters match form attribute names. In this case the `file` will match for example an `<input type="file" name="file">` |
| **3** | The `CompletedFileUpload` instance gives access to metadata about the upload as well as access to the file contents. |

|   | If a file will not be read, the `discard` method on the file object **must** be called to prevent memory leaks. |
|---|---|


## Multiple Uploads

### Different Names

If a multipart request has multiple uploads that have different part names, create an argument to your route that receives each part. For example:

```java
HttpResponse upload(String title, String name)
```

A route method signature like the above expects two different parts, one named "title" and the other "name".

### Same Name

To receive multiple parts with the same part name, the argument must be a Publisher. When used in one of the following ways, the publisher emits one item per part found with the specified name. The publisher must accept one of the following types:

- StreamingFileUpload
- CompletedFileUpload
- CompletedPart for attributes
- Any POJO, assuming a media codec that supports the content type exists
- Another Publisher that accepts one of the chunked data types described above

For example:

```java
HttpResponse upload(Publisher<StreamingFileUpload> files)
HttpResponse upload(Publisher<CompletedFileUpload> files)
HttpResponse upload(Publisher<MyObject> files)
HttpResponse upload(Publisher<Publisher<PartData>> files)
HttpResponse upload(Publisher<CompletedPart> attributes)
```


## Whole Body Binding

When request part names aren’t known ahead of time, or to read the entire body, a special type can be used to indicate the entire body is desired.

If a route has an argument of type MultipartBody (not to be confused with the class for the client) annotated with @Body, each part of the request will be emitted through the argument. A MultipartBody is a publisher of CompletedPart instances.

For example:

Binding to the entire multipart body

```java
import io.micronaut.core.async.annotation.SingleResult;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.multipart.CompletedFileUpload;
import io.micronaut.http.multipart.CompletedPart;
import io.micronaut.http.server.multipart.MultipartBody;
import org.reactivestreams.Publisher;
import org.reactivestreams.Subscriber;
import org.reactivestreams.Subscription;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;
import reactor.core.scheduler.Schedulers;

import java.io.IOException;

import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA;
import static io.micronaut.http.MediaType.TEXT_PLAIN;

@Controller("/upload")
public class WholeBodyUploadController {

    @Post(value = "/whole-body", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    @SingleResult
    public Publisher<String> uploadBytes(@Body MultipartBody body) { // (2)

        return Mono.create(emitter -> {
            Flux.from(body).publishOn(Schedulers.boundedElastic()).subscribe(new Subscriber<>() {
                private Subscription s;

                @Override
                public void onSubscribe(Subscription s) {
                    this.s = s;
                    s.request(1);
                }

                @Override
                public void onNext(CompletedPart completedPart) {
                    String partName = completedPart.getName();
                    if (completedPart instanceof CompletedFileUpload upload) {
                        String originalFileName = upload.getFilename();
                    }
                    try {
                        completedPart.close();
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                }

                @Override
                public void onError(Throwable t) {
                    emitter.error(t);
                }

                @Override
                public void onComplete() {
                    emitter.success("Uploaded");
                }
            });
        });
    }
}
```

Binding to the entire multipart body

```kotlin
import io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import io.micronaut.http.MediaType.TEXT_PLAIN
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.CompletedFileUpload
import io.micronaut.http.multipart.CompletedPart
import io.micronaut.http.server.multipart.MultipartBody
import org.reactivestreams.Subscriber
import org.reactivestreams.Subscription
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono
import reactor.core.scheduler.Schedulers

@Controller("/upload")
class WholeBodyUploadController {

    @Post(value = "/whole-body", consumes = [MULTIPART_FORM_DATA], produces = [TEXT_PLAIN]) // (1)
    fun uploadBytes(@Body body: MultipartBody): Mono<String> { // (2)
        return Mono.create { emitter ->
            Flux.from(body).publishOn(Schedulers.boundedElastic()).subscribe(object : Subscriber<CompletedPart> {
                private var s: Subscription? = null

                override fun onSubscribe(s: Subscription) {
                    this.s = s
                    s.request(1)
                }

                override fun onNext(completedPart: CompletedPart) {
                    val partName = completedPart.name
                    if (completedPart is CompletedFileUpload) {
                        val originalFileName = completedPart.filename
                    }
                    completedPart.close()
                }

                override fun onError(t: Throwable) {
                    emitter.error(t)
                }

                override fun onComplete() {
                    emitter.success("Uploaded")
                }
            })
        }
    }
}
```

Binding to the entire multipart body

```groovy
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.http.multipart.CompletedFileUpload
import io.micronaut.http.multipart.CompletedPart
import io.micronaut.http.server.multipart.MultipartBody
import org.reactivestreams.Subscriber
import org.reactivestreams.Subscription
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono
import reactor.core.scheduler.Schedulers

import static io.micronaut.http.MediaType.MULTIPART_FORM_DATA
import static io.micronaut.http.MediaType.TEXT_PLAIN

@Controller("/upload")
class WholeBodyUploadController {

    @Post(value = "/whole-body", consumes = MULTIPART_FORM_DATA, produces = TEXT_PLAIN) // (1)
    Mono<String> uploadBytes(@Body MultipartBody body) { // (2)

        Mono.<String>create({ emitter ->
            Flux.from(body).publishOn(Schedulers.boundedElastic()).subscribe(new Subscriber<CompletedPart>() {
                private Subscription s

                @Override
                void onSubscribe(Subscription s) {
                    this.s = s
                    s.request(1)
                }

                @Override
                void onNext(CompletedPart completedPart) {
                    String partName = completedPart.name
                    if (completedPart instanceof CompletedFileUpload) {
                        String originalFileName = completedPart.filename
                    }
                    completedPart.close()
                }

                @Override
                void onError(Throwable t) {
                    emitter.error(t)
                }

                @Override
                void onComplete() {
                    emitter.success("Uploaded")
                }
            })
        })
    }
}
```


## 6.24 File Transfers

The Micronaut framework supports sending files to the client in a couple of easy ways.


## Sending File Objects

It is possible to return a File object from your controller method, and the data will be returned to the client. The `Content-Type` header of file responses is calculated based on the name of the file.

To control either the media type of the file being sent, or to set the file to be downloaded (i.e. using the `Content-Disposition` header), instead construct a SystemFile with the file to use. For example:

Sending a SystemFile

```java
@Get
public SystemFile download() {
    File file = ...
    return new SystemFile(file).attach("myfile.txt");
    // or new SystemFile(file, MediaType.TEXT_HTML_TYPE)
}
```


## Sending an InputStream

For cases where a reference to a `File` object is not possible (for example resources in JAR files), the Micronaut framework supports transferring input streams. To return a stream of data from the controller method, construct a StreamedFile.

|   | The constructor for `StreamedFile` also accepts a `java.net.URL` for your convenience. |
|---|---|

Sending a StreamedFile

```java
@Get
public StreamedFile download() {
    InputStream inputStream = ...
    return new StreamedFile(inputStream, MediaType.TEXT_PLAIN_TYPE)
    // An attach(String filename) method is also available to set the Content-Disposition
}
```

The server supports returning `304` (Not Modified) responses if the files being transferred have not changed, and the request contains the appropriate header. In addition, if the client accepts encoded responses, the Micronaut framework encodes the file if appropriate. Encoding happens if the file is text-based and larger than 1KB by default. The threshold at which data is encoded is configurable. See the server configuration reference for details.

|   | To use a custom data source to send data through an input stream, construct a PipedInputStream and PipedOutputStream to write data from the output stream to the input. Make sure to do the work on a separate thread so the file can be returned immediately. |
|---|---|


## Sending Reactive Streams as File Downloads

Micronaut also supports returning **reactive streams** (e.g., `Flux`, `Flowable`, or any `Publisher`) without buffering the entire response in memory. If you want to force the client browser to download the streamed data (for example, CSV lines), you can set the `Content-Disposition: attachment` header.

Sending Reactive Stream

```java
@Get("/csv")
public HttpResponse<Flux<String>> downloadCsv() {
    Flux<String> data = Flux.just(
        "data1,data2",
        "data3,data4"
    );
    return HttpResponse.ok(data)
        .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"data.csv\"")
        .contentType(MediaType.TEXT_PLAIN_TYPE);
}
```

Sending Reactive Stream

```groovy
@Get("/csv")
 HttpResponse<Flux<String>> downloadCsv() {
    Flux<String> data = Flux.just(
            "data1,data2",
            "data3,data4"
    )
    return HttpResponse.ok(data)
            .header(HttpHeaders.CONTENT_DISPOSITION, 'attachment; filename="data.csv"')
            .contentType(MediaType.TEXT_PLAIN_TYPE)
}
```

|   | Wrapping your stream in `HttpResponse<Flux<String>>` does not cause the entire CSV to be loaded into memory. Micronaut will still **stream** the data as it is produced. Returning `HttpResponse<T>` simply allows you to set any headers or custom status codes. |
|---|---|


## Cache Configuration

By default, file responses include caching headers. The following options determine how the `Cache-Control` header is built.

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.server.netty.responses.file.cache-seconds` | int | Cache Seconds. Default value (60). |   |

🔗

| Property | Type | Description | Default value |
|---|---|---|---|
| `micronaut.server.netty.responses.file.cache-control.public` | boolean | Sets whether the cache control is public. Default value (false) |   |


## 6.25 HTTP Filters

The Micronaut HTTP server supports applying filters to request/response processing in a similar (but reactive) way to Servlet filters in traditional Java applications.

Filters support the following use cases:

- Decoration of the incoming HttpRequest
- Modification of the outgoing HttpResponse
- Implementation of cross-cutting concerns such as security, tracing, etc.

There are two ways to implement a filter:

- Annotating class with Filter and implementing HttpServerFilter or HttpClientFilter.
- By using Filter methods.

|   | We recommend Micronaut developers use Filter methods introduced in Micronaut Framework 4.0 to implement filters. |
|---|---|


## 6.25.1 Filter Patterns

Filter patterns can be defined on the filter class (in Filter, the ServerFilter or ClientFilter annotation), or on the filter method (in the RequestFilter or ResponseFilter annotation).

You can use different styles of pattern for path matching by setting `patternStyle`. By default, AntPathMatcher is used for path matching. When using Ant, the mapping matches URLs using the following rules:

- ? matches one character
- * matches zero or more characters
- ** matches zero or more subdirectories in a path

| Pattern | Example Matched Paths |
|---|---|
| `/**` | any path |
| `customer/j?y` | customer/joy, customer/jay |
| `customer/*/id` | customer/adam/id, customer/amy/id |
| `customer/**` | customer/adam, customer/adam/id, customer/adam/name |
| `customer/***/**.html` | customer/index.html, customer/adam/profile.html, customer/adam/job/description.html |

The other option is regular expression based matching. To use regular expressions, set `patternStyle = FilterPatternStyle.REGEX`. The `pattern` attribute is expected to contain a regular expression which will be expected to match the provided URLs exactly (using Matcher#matches).

|   | Using `FilterPatternStyle.ANT` is preferred as the pattern matching is more performant than using regular expressions. `FilterPatternStyle.REGEX` should be used when your pattern cannot be written properly using Ant. |
|---|---|


## 6.25.2 Filter Methods

A filter method must be declared in a bean annotated with ServerFilter, or ClientFilter if it should instead intercept requests made by the HTTP client. Each filter method must also be annotated with RequestFilter, to run before the request is processed, or ResponseFilter, to run after the request has completed to process the response.

|   | Request filters can be executed before the route is matched if annotated with PreMatching` |
|---|---|

A filter method can take various parameters, such as the HttpRequest and the HttpResponse (only for response filters). The return type can be `void` or `null` to continue execution as normal, or an updated HttpRequest (only for request filters) or HttpResponse. The different supported parameter and return types are described in the documentation of RequestFilter and ResponseFilter.

Request filters can bind the full request body using the Body annotation. This is useful e.g. to verify a signed request body.

|   | Accessing the full body should be done with care. It forces the body to be fully buffered, even if the controller supports streaming (e.g. `@Body InputStream` parameter), leading to potential negative performance impact. |
|---|---|

|   | Body binding is supported by the netty-based HTTP server, but may not be supported by all other HTTP server backends. |
|---|---|

To write asynchronous filters, you can return a reactive publisher.

To put these concepts into practice lets look at an example.

|   | Filter methods execute in the event loop by default. If you need to perform blocking operations, you can annotate the filter with ExecuteOn. |
|---|---|


## 6.25.2.1 Server Filter with Filter Methods

Suppose you wish to trace each request to the "Hello World" example using some external system. This system could be a database or a distributed tracing service, and may require I/O operations.

You should not block the underlying Netty event loop in your filter; instead the filter should proceed with execution once any I/O is complete.

As an example, consider this `TraceService` that performs an I/O operation:

A TraceService Example using Reactive Streams

```java
import io.micronaut.http.HttpRequest;
import jakarta.inject.Singleton;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Singleton
public class TraceService {

    private static final Logger LOG = LoggerFactory.getLogger(TraceService.class);

    public void trace(HttpRequest<?> request) {
        LOG.debug("Tracing request: {}", request.getUri());
        // trace logic here, potentially performing I/O (1)
    }
}
```

A TraceService Example using Reactive Streams

```groovy
import io.micronaut.http.HttpRequest
import org.slf4j.Logger
import org.slf4j.LoggerFactory

import jakarta.inject.Singleton
import reactor.core.publisher.Flux
import reactor.core.publisher.Mono
import reactor.core.scheduler.Schedulers

@Singleton
class TraceService {
    private static final Logger LOG = LoggerFactory.getLogger(TraceService.class)

    void trace(HttpRequest<?> request) {
        LOG.debug('Tracing request: {}', request.uri)
        // trace logic here, potentially performing I/O (2)
    }
}
```

| **1** | Since this is just an example, the logic does nothing yet |
|---|---|

The following code sample shows how to write a filter using filter methods:

An Example ServerFilter

```java
import io.micronaut.context.annotation.Requires;
import io.micronaut.http.HttpRequest;
import io.micronaut.http.MutableHttpResponse;
import io.micronaut.http.annotation.RequestFilter;
import io.micronaut.http.annotation.ResponseFilter;
import io.micronaut.http.annotation.ServerFilter;
import io.micronaut.scheduling.TaskExecutors;
import io.micronaut.scheduling.annotation.ExecuteOn;

@ServerFilter("/hello/**") // (1)
public class TraceFilter {

    private final TraceService traceService;

    public TraceFilter(TraceService traceService) { // (2)
        this.traceService = traceService;
    }

    @RequestFilter
    @ExecuteOn(TaskExecutors.BLOCKING) // (3)
    public void filterRequest(HttpRequest<?> request) {
        traceService.trace(request); // (4)
    }

    @ResponseFilter // (5)
    public void filterResponse(MutableHttpResponse<?> res) {
        res.getHeaders().add("X-Trace-Enabled", "true");
    }
}
```

An Example ServerFilter

```groovy
import io.micronaut.http.HttpRequest
import io.micronaut.context.annotation.Requires
import io.micronaut.http.MutableHttpResponse
import io.micronaut.http.annotation.RequestFilter
import io.micronaut.http.annotation.ResponseFilter
import io.micronaut.http.annotation.ServerFilter
import io.micronaut.scheduling.TaskExecutors
import io.micronaut.scheduling.annotation.ExecuteOn

@ServerFilter("/hello/**") // (1)
class TraceFilter {

    private final TraceService traceService

    TraceFilter(TraceService traceService) { // (2)
        this.traceService = traceService
    }

    @RequestFilter
    @ExecuteOn(TaskExecutors.BLOCKING) // (3)
    void filterRequest(HttpRequest<?> request) {
        traceService.trace(request) // (4)
    }

    @ResponseFilter // (5)
    void filterResponse(MutableHttpResponse<?> res) {
        res.headers.add("X-Trace-Enabled", "true")
    }
}
```

| **1** | The ServerFilter annotation defines the URI pattern(s) the filter matches |
|---|---|
| **2** | The previously defined `TraceService` is injected via constructor |
| **3** | The request filter is marked to execute on a separate thread so that the blocking code in `TraceService` does not cause problems |
| **4** | `TraceService` is invoked to trace the request |
| **5** | Finally, a separate response filter method adds a `X-Trace-Enabled` header to the response. |

The previous example demonstrates some key concepts such as executing blocking logic in a worker thread before proceeding with the request and modifying the outgoing response.


## 6.25.2.2 Proceeding with Filter Methods

If you need to write a filter, e.g., security-related, which needs to proceed with requests in some scenarios or stop the request execution and return an HTTP Response directly in the filter; you can use, for example, a `CompletableFuture` as the filter method’s response type.

```java
@ServerFilter(ServerFilter.MATCH_ALL_PATTERN)
class FooBarFilter {
    @RequestFilter
    CompletableFuture<@Nullable HttpResponse<?>> filter(HttpRequest<?> request) {
        if (request.getHeaders().contains("X-FOOBAR")) {
            // proceed
            return CompletableFuture.completedFuture(null);
        } else {
            return CompletableFuture.completedFuture(HttpResponse.unauthorized());
        }
    }
}
```


## 6.25.2.3 Error States

In principle, downstream filters and controllers can produce exceptions, and response filters should be prepared to handle them. For a response filter to be called when there is an exception, it must declare the exception type as a parameter.

| Declaration | Called when? |
|---|---|
| `void responseFilter(HttpResponse<?> response)` | Only called on non-exception response |
| `void responseFilter(Throwable failure)` | Only called on exception response |
| `void responseFilter(IOException failure)` | Only called on exception response, if the exception is an `IOException` |
| `void responseFilter(HttpResponse<?> response, @Nullable Throwable failure)` | Always called. `failure` will be `null` if there was no error. If there was an error, `response` will be `null`. |

Whether errors appear as exceptions depends on the context of the filter. For the Micronaut HTTP server, any exception is mapped to a non-exceptional HttpResponse with an error status code. This mapping happens before each filter, so a server filter will never actually see an exception. If you still want to access the original cause of the response, it is stored as the attribute EXCEPTION.


## 6.25.2.4 Continuations

Request filters can define a special FilterContinuation parameter to get more control of the downstream execution, and to be run further actions after it completes. For example, the above `TraceFilter` can be expressed using a single request filter:

Single request filter

```java
@RequestFilter
@ExecuteOn(TaskExecutors.BLOCKING) // (4)
public void filterRequest(HttpRequest<?> request, FilterContinuation<MutableHttpResponse<?>> continuation) { // (1)
    traceService.trace(request);
    MutableHttpResponse<?> res = continuation.proceed(); // (2)
    res.getHeaders().add("X-Trace-Enabled", "true"); // (3)
}
```

Single request filter

```groovy
@RequestFilter
@ExecuteOn(TaskExecutors.BLOCKING) // (4)
void filterRequest(HttpRequest<?> request, FilterContinuation<MutableHttpResponse<?>> continuation) { // (1)
    traceService.trace(request)
    MutableHttpResponse<?> res = continuation.proceed(); // (2)
    res.headers.add("X-Trace-Enabled", "true") // (3)
}
```

| **1** | The request filter declares a FilterContinuation parameter. The continuation will return a MutableHttpResponse |
|---|---|
| **2** | After the request processing is done, the filter calls the blocking `proceed` to run downstream filters and the controller |
| **3** | When downstream processing completes, the filter adds a `X-Trace-Enabled` header to the response returned by the continuation |
| **4** | The whole filter is executed on a worker thread to avoid blocking the event loop in the `proceed` call |

|   | The call to `FilterContinuation.proceed` is blocking by default, so it should never be done on the event loop. Such filters should be run on a worker thread as described above. Alternatively, the continuation can also be declared to return a reactive type (`Publisher<HttpResponse<?>>`) to proceed in an asynchronous manner, similar to the old FilterChain API. |
|---|---|


## 6.25.2.5 Filter Order

Filters can be ordered by annotating the filter method or filter class with Order or jakarta.annotation.Priority, or by implementing Ordered in the filter class.

1. An Order or @Priority annotation on the filter method
2. An Order or @Priority annotation on the filter class
3. Implementing Ordered in the filter class

Request filters are executed in order from the highest precedence (the smallest integer value, as defined by `Ordered.HIGHEST_PRECEDENCE`) to the lowest precedence (the biggest integer value, as defined by `Ordered.LOWEST_PRECEDENCE`). Response filters are executed in reverse order.

Micronaut applies the same numeric precedence rule to jakarta.annotation.Priority because @Priority is mapped to @Order during annotation processing.

Request filter A is executed first, because it has the higher precedence (-100), followed by request filter B with the lower precedence (100). Then the controller is executed. Response filter C is executed first, because it has the lower precedence (100), and finally response filter D with the higher precedence (-100) is executed last.


## 6.25.3 HttpServerFilter

|   | We recommend Micronaut developers use Filter methods instead of `HttpServerFilter` introduced in Micronaut Framework 4.0 to implement filters. |
|---|---|

For a server application, the HttpServerFilter interface `doFilter` method can be implemented.

The `doFilter` method accepts the HttpRequest and an instance of ServerFilterChain.

The `ServerFilterChain` interface contains a resolved chain of filters where the final entry in the chain is the matched route. The ServerFilterChain.proceed(io.micronaut.http.HttpRequest) method resumes processing of the request.

The `proceed(..)` method returns a Reactive Streams Publisher that emits the response to be returned to the client. Implementors of filters can subscribe to the Publisher and mutate the emitted MutableHttpResponse to modify the response prior to returning the response to the client.

To put these concepts into practice lets look at an example.

|   | Filters execute in the event loop, so blocking operations must be offloaded to another thread pool. |
|---|---|
