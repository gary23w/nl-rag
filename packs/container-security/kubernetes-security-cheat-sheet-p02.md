---
title: "Kubernetes Security (part 2/2)"
source: https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html
domain: container-security
license: CC-BY-SA-4.0
tags: container security, docker security, kubernetes security, linux namespaces, hypervisor isolation
fetched: 2026-07-02
part: 2/2
---

## SECTION 5: Kubernetes Security Best Practices: Runtime Phase

When the Kubernetes infrastructure enters the runtime phase, containerized applications are exposed to a slew of new security challenges. You must gain visibility into your running environment so you can detect and respond to threats as they arise.

If you proactively secure your containers and Kubernetes deployments at the build and deploy phases, you can greatly reduce the likelihood of security incidents at runtime and the subsequent effort needed to respond to them.

First, monitor the most security-relevant container activities, including:

- Process activity
- Network communications among containerized services
- Network communications between containerized services and external clients and servers

Detecting anomalies by observing container behavior is generally easier in containers than in virtual machines because of the declarative nature of containers and Kubernetes. These attributes allow easier introspection into what you have deployed and its expected activity.

### Use Pod Security Admission to prevent risky containers/Pods from being deployed

The previously recommended Pod Security Policy is deprecated and replaced by Pod Security Admission, a new feature that allows you to enforce security policies on pods in a Kubernetes cluster.

It is recommended to use the `baseline` level as a minimum security requirement for all pods to ensure a standard level of security across the cluster. However, clusters should strive to apply the `restricted` level which follows pod hardening best practices.

For more information on configuring Pod Security Admission, refer to the documentation at https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/.

### Container Runtime Security

If containers are hardened containers at runtime, security teams have the ability to detect and respond to threats and anomalies while the containers or workloads are in a running state. Typically, this is carried out by intercepting the low-level system calls and looking for events that may indicate compromise. Some examples of events that should trigger an alert would include:

- A shell is run inside a container
- A container mounts a sensitive path from the host such as /proc
- A sensitive file is unexpectedly read in a running container such as /etc/shadow
- An outbound network connection is established

Open source tools such as Falco from Sysdig can help operators get up and running with container runtime security by providing defenders with a large number of out-of-the-box detections as well as the ability to create custom rules.

### Container Sandboxing

When container runtimes are permitted to make direct calls to the host kernel, the kernel often interacts with hardware and devices to respond to the request. Though Cgroups and namespaces give containers a certain amount of isolation, the kernel still presents a large attack surface. When defenders have to deal with multi-tenant and highly untrusted clusters, they often add additional layer of sandboxing to ensure that container breakout and kernel exploits are not present. Below, we will explore a few OSS technologies that help further isolate running containers from the host kernel:

- Kata Containers: Kata Containers is an OSS project that uses stripped-down VMs to keep the resource footprint minimal and maximize performance to ultimately isolate containers further.
- gVisor : gVisor is a more lightweight kernel than a VM (even stripped down). It is its own independent kernel written in Go and sits in the middle of a container and the host kernel. It is a strong sandbox--gVisor supports ~70% of the linux system calls from the container but ONLY uses about 20 system calls to the host kernel.
- Firecracker: It is a super lightweight VM that runs in user space. Since it is locked down by seccomp, cgroup, and namespace policies, the system calls are very limited. Firecracker is built with security in mind, however it may not support all Kubernetes or container runtime deployments.

### Preventing containers from loading unwanted kernel modules

Because Linux kernel automatically loads kernel modules from disk if needed in certain circumstances, such as when a piece of hardware is attached or a filesystem is mounted, this can be a significant attack surface. Of particular relevance to Kubernetes, even unprivileged processes can cause certain network-protocol-related kernel modules to be loaded, just by creating a socket of the appropriate type. This situation may allow attackers to exploit a security hole in kernel modules that the administrator assumed was not in use.

To prevent specific modules from being automatically loaded, you can uninstall them from the node, or add rules to block them. On most Linux distributions, you can do that by creating a file such as `/etc/modprobe.d/kubernetes-blacklist.conf` with contents like:

```
# DCCP is unlikely to be needed, has had multiple serious
# vulnerabilities, and is not well-maintained.
blacklist dccp

# SCTP is not used in most Kubernetes clusters, and has also had
# vulnerabilities in the past.
blacklist sctp
```

To block module loading more generically, you can use a Linux Security Module (such as SELinux) to completely deny the module_request permission to containers, preventing the kernel from loading modules for containers under any circumstances. (Pods would still be able to use modules that had been loaded manually, or modules that were loaded by the kernel on behalf of some more-privileged process).

### Compare and analyze different runtime activity in pods of the same deployments

When containerized applications are replicated for high availability, fault tolerance, or scale reasons, these replicas should behave nearly identically. If a replica has significant deviations from the others, defenders would want further investigation. Your Kubernetes security tool should be integrated with other external systems (email, PagerDuty, Slack, Google Cloud Security Command Center, SIEMs [security information and event management], etc.) and leverage deployment labels or annotations to alert the team responsible for a given application when a potential threat is detected. If you chose to use a commercial Kubernetes security vendor, they should support a wide array of integrations with external tools.

### Monitor network traffic to limit unnecessary or insecure communication

Containerized applications typically make extensive use of cluster networking, so observing active networking traffic is a good way to understand how applications interact with each other and identify unexpected communication. You should observe your active network traffic and compare that traffic to what is allowed based on your Kubernetes network policies.

At the same time, comparing the active traffic with what’s allowed gives you valuable information about what isn’t happening but is allowed. With that information, you can further tighten your allowed network policies so that it removes superfluous connections and decreases your overall attack surface.

Open source projects like https://github.com/kinvolk/inspektor-gadget or https://github.com/deepfence/PacketStreamer may help with this, and commercial security solutions provide varying degrees of container network traffic analysis.

### If breached, scale suspicious pods to zero

Contain a successful breach by using Kubernetes native controls to scale suspicious pods to zero or kill then restart instances of breached applications.

### Rotate infrastructure credentials frequently

The shorter the lifetime of a secret or credential, the harder it is for an attacker to make use of that credential. Set short lifetimes on certificates and automate their rotation. Use an authentication provider that can control how long issued tokens are available and use short lifetimes where possible. If you use service account tokens in external integrations, plan to rotate those tokens frequently. For example, once the bootstrap phase is complete, a bootstrap token used for setting up nodes should be revoked or its authorization removed.

### Logging

Kubernetes supplies cluster-based logging, which allows you to log container activity into a central log hub. When a cluster is created, the standard output and standard error output of each container can be ingested using a Fluentd agent running on each node (into either Google Stackdriver Logging or into Elasticsearch) and viewed with Kibana.

#### Enable audit logging

The audit logger is a beta feature that records actions taken by the API for later analysis in the event of a compromise. It is recommended to enable audit logging and archive the audit file on a secure server

Ensure logs that are monitoring for anomalous or unwanted API calls, especially any authorization failures (these log entries will have a status message “Forbidden”). Authorization failures could mean that an attacker is trying to abuse stolen credentials.

Managed Kubernetes providers, including GKE, provide access to this data in their cloud console and may allow you to set up alerts on authorization failures.

##### Audit logs

Audit logs can be useful for compliance as they should help you answer the questions of what happened, who did what and when. Kubernetes provides flexible auditing of kube-apiserver requests based on policies. These help you track all activities in chronological order.

Here is an example of an audit log:

```
{
  "kind":"Event",
  "apiVersion":"audit.k8s.io/v1beta1",
  "metadata":{ "creationTimestamp":"2019-08-22T12:00:00Z" },
  "level":"Metadata",
  "timestamp":"2019-08-22T12:00:00Z",
  "auditID":"23bc44ds-2452-242g-fsf2-4242fe3ggfes",
  "stage":"RequestReceived",
  "requestURI":"/api/v1/namespaces/default/persistentvolumeclaims",
  "verb":"list",
  "user": {
    "username":"[email protected]",
    "groups":[ "system:authenticated" ]
  },
  "sourceIPs":[ "172.12.56.1" ],
  "objectRef": {
    "resource":"persistentvolumeclaims",
    "namespace":"default",
    "apiVersion":"v1"
  },
  "requestReceivedTimestamp":"2019-08-22T12:00:00Z",
  "stageTimestamp":"2019-08-22T12:00:00Z"
}
```

#### Define Audit Policies

Audit policy sets rules which define what events should be recorded and what data is stored when an event includes. The audit policy object structure is defined in the audit.k8s.io API group. When an event is processed, it is compared against the list of rules in order. The first matching rule sets the "audit level" of the event.

The known audit levels are:

- None - don't log events that match this rule
- Metadata - log request metadata (requesting user, timestamp, resource, verb, etc.) but not request or response body
- Request - log event metadata and request body but not response body. This does not apply for non-resource requests
- RequestResponse - log event metadata, request and response bodies. This does not apply for non-resource requests

You can pass a file with the policy to kube-apiserver using the --audit-policy-file flag. If the flag is omitted, no events are logged. Note that the rules field must be provided in the audit policy file. A policy with no (0) rules is treated as illegal.

#### Understanding Logging

One main challenge with logging Kubernetes is understanding what logs are generated and how to use them. Let’s start by examining the overall picture of Kubernetes' logging architecture.

##### Container logging

The first layer of logs that can be collected from a Kubernetes cluster are those being generated by your containerized applications. The easiest method for logging containers is to write to the standard output (stdout) and standard error (stderr) streams.

Manifest is as follows.

```
apiVersion: v1
kind: Pod
metadata:
  name: example
spec:
  containers:
    - name: example
      image: busybox
      args: [/bin/sh, -c, 'while true; do echo $(date); sleep 1; done']
```

To apply the manifest, run:

```
kubectl apply -f example.yaml
```

To take a look the logs for this container, run:

```
kubectl log <container-name> command.
```

For persisting container logs, the common approach is to write logs to a log file and then use a sidecar container. As shown below in the pod configuration above, a sidecar container will run in the same pod along with the application container, mounting the same volume and processing the logs separately.

An example of a Pod Manifest is seen below:

```
apiVersion: v1
kind: Pod
metadata:
  name: example
spec:
  containers:
  - name: example
    image: busybox
    args:
    - /bin/sh
    - -c
    - >
      while true;
      do
        echo "$(date)\n" >> /var/log/example.log;
        sleep 1;
      done
    volumeMounts:
    - name: varlog
      mountPath: /var/log
  - name: sidecar
    image: busybox
    args: [/bin/sh, -c, 'tail -f /var/log/example.log']
    volumeMounts:
    - name: varlog
      mountPath: /var/log
  volumes:
  - name: varlog
    emptyDir: {}
```

##### Node logging

When a container running on Kubernetes writes its logs to stdout or stderr streams, the container engine streams them to the logging driver set by the Kubernetes configuration.

In most cases, these logs will end up in the /var/log/containers directory on your host. Docker supports multiple logging drivers but unfortunately, driver configuration is not supported via the Kubernetes API.

Once a container is terminated or restarted, kubelet stores logs on the node. To prevent these files from consuming all of the host’s storage, the Kubernetes node implements a log rotation mechanism. When a container is evicted from the node, all containers with corresponding log files are evicted.

Depending on what operating system and additional services you’re running on your host machine, you might need to take a look at additional logs.

For example, systemd logs can be retrieved using the following command:

```
journalctl -u
```

##### Cluster logging

In the Kubernetes cluster itself, there is a long list of cluster components that can be logged as well as additional data types that can be used (events, audit logs). Together, these different types of data can give you visibility into how Kubernetes is performing as a system.

Some of these components run in a container, and some of them run on the operating system level (in most cases, a systemd service). The systemd services write to journald, and components running in containers write logs to the /var/log directory, unless the container engine has been configured to stream logs differently.

#### Events

Kubernetes events can indicate any Kubernetes resource state changes and errors, such as exceeded resource quota or pending pods, as well as any informational messages.

The following command returns all events within a specific namespace:

```
kubectl get events -n <namespace>

NAMESPACE LAST SEEN TYPE   REASON OBJECT MESSAGE
kube-system  8m22s  Normal   Scheduled            pod/metrics-server-66dbbb67db-lh865                                       Successfully assigned kube-system/metrics-server-66dbbb67db-lh865 to aks-agentpool-42213468-1
kube-system     8m14s               Normal    Pulling                   pod/metrics-server-66dbbb67db-lh865                                       Pulling image "aksrepos.azurecr.io/mirror/metrics-server-amd64:v0.2.1"
kube-system     7m58s               Normal    Pulled                    pod/metrics-server-66dbbb67db-lh865                                       Successfully pulled image "aksrepos.azurecr.io/mirror/metrics-server-amd64:v0.2.1"
kube-system     7m57s               Normal     Created                   pod/metrics-server-66dbbb67db-lh865                                       Created container metrics-server
kube-system     7m57s               Normal    Started                   pod/metrics-server-66dbbb67db-lh865                                       Started container metrics-server
kube-system     8m23s               Normal    SuccessfulCreate          replicaset/metrics-server-66dbbb67db             Created pod: metrics-server-66dbbb67db-lh865
```

The following command will show the latest events for this specific Kubernetes resource:

```
kubectl describe pod <pod-name>

Events:
  Type    Reason     Age   From                               Message
  ----    ------     ----  ----                               -------
  Normal  Scheduled  14m   default-scheduler                  Successfully assigned kube-system/coredns-7b54b5b97c-dpll7 to aks-agentpool-42213468-1
  Normal  Pulled     13m   kubelet, aks-agentpool-42213468-1  Container image "aksrepos.azurecr.io/mirror/coredns:1.3.1" already present on machine
  Normal  Created    13m   kubelet, aks-agentpool-42213468-1  Created container coredns
  Normal  Started    13m   kubelet, aks-agentpool-42213468-1  Started container coredns
```


## SECTION 5: Securing a managed-service Kubernetes on Cloud Service Provider

### AWS

There are few open source tools that can help you on securing your managed-service Kubernetes on AWS (EKS)

- hardeneks
- MKAD (Managed Kubernetes Auditing Toolkit) from DataDog


## SECTION 6: Supply Chain Security

Container supply chain security is critical for preventing attacks that exploit vulnerabilities in the software delivery process. A compromised supply chain can lead to malicious code being deployed into production environments, potentially affecting thousands of containers and applications.

Supply chain attacks in Kubernetes environments typically target:

- Base images and dependencies
- Build processes and CI/CD pipelines
- Container registries
- Deployment manifests and Helm charts
- Third-party libraries and packages

Recent high-profile attacks (SolarWinds, Codecov, ua-parser-js) demonstrate the severe impact of supply chain compromises.

### Best practices for securing the container supply chain

1. Use trusted base images: Start with minimal, verified base images from reputable sources to reduce vulnerabilities.
2. Implement image scanning: Regularly scan container images for vulnerabilities using tools like Clair, Trivy, or Aqua Security.
3. Secure CI/CD pipelines: Ensure that build processes are secure, with proper access controls and monitoring.
4. Sign and verify images: Use image signing tools like Notary or Cosign to ensure the integrity of container images.
5. Use private registries: Store container images in private registries with access controls to prevent unauthorized access.
6. Monitor for vulnerabilities: Continuously monitor for new vulnerabilities in dependencies and base images.
7. Implement runtime security: Use tools to monitor container behavior at runtime and detect anomalies.


## SECTION 7: Final Thoughts

### Embed security into the container lifecycle as early as possible

You must integrate security earlier into the container lifecycle and ensure alignment and shared goals between security and DevOps teams. Security can (and should) be an enabler that allows your developers and DevOps teams to confidently build and deploy applications that are production-ready for scale, stability and security.

### Use Kubernetes-native security controls to reduce operational risk

Leverage the native controls built into Kubernetes whenever available in order to enforce security policies so that your security controls don’t collide with the orchestrator. Instead of using a third-party proxy or shim to enforce network segmentation, you could use Kubernetes network policies to ensure secure network communication.

### Leverage the context that Kubernetes provides to prioritize remediation efforts

Note that manually triaging security incidents and policy violations is time consuming in sprawling Kubernetes environments.

For example, a deployment containing a vulnerability with severity score of 7 or greater should be moved up in remediation priority if that deployment contains privileged containers and is open to the Internet but moved down if it’s in a test environment and supporting a non-critical app.

(Kubernetes Architecture)
