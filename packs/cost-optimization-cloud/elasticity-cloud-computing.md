---
title: "Elasticity (computing)"
source: https://en.wikipedia.org/wiki/Elasticity_(cloud_computing)
domain: cost-optimization-cloud
license: CC-BY-SA-4.0
tags: cloud cost optimization, rightsizing spend reduction, reserved capacity commitment, idle resource cleanup
fetched: 2026-07-02
---

# Elasticity (computing)

(Redirected from

Elasticity (cloud computing)

)

In computing, **elasticity** is defined as "the degree to which a system is able to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that at each point in time the available resources match the current demand as closely as possible". Elasticity is a defining characteristic that differentiates cloud computing from previously proposed distributed computing paradigms, such as grid computing. The dynamic adaptation of capacity, e.g., by altering the use of computing resources, to meet a varying workload is called "elastic computing".

In the world of distributed systems, there are several definitions according to the authors; some consider the concepts of scalability a sub-part of elasticity, others as being distinct.

## Purpose

Elasticity aims to match the amount of resources allocated to a service with the amount of resources it actually requires, avoiding over- or under-provisioning. **Over-provisioning**, i.e., allocating more resources than required, should be avoided as it may incur extra costs (monetary, energy, operational, etc.) for unused or underutilized resources. For example, if a website is over-provisioned with two cloud computing resources to handle current demand that only requires one resource, the costs of maintaining the second resource would effectively be wasted.

**Under-provisioning**, i.e., allocating fewer resources than required, must be avoided; otherwise, the service cannot serve its users with a good service. For example, under-provisioning a website may make it seem slow or unreachable, because not enough resources have been allocated to meet current demand.

## Example

Elasticity can be illustrated through an example of a service provider who wants to run a website on the cloud. At moment $t_{0}$ , the website is unpopular and a single machine is sufficient to serve all users. At moment $t_{1}$ , the website suddenly becomes popular, and a single machine is no longer sufficient to serve all users. Based on the number of web users simultaneously accessing the website and the resource requirements of the web server, ten machines are needed. An elastic system should immediately detect this condition and provision nine additional machines from the cloud to serve all users responsively.

At time $t_{2}$ , the website becomes unpopular again. The ten machines currently allocated to the website are mostly idle and a single machine would be sufficient to serve the few users who are accessing the website. An elastic system should immediately detect this condition and deprovision nine machines, releasing them to the cloud.

## Problems

### Resource provisioning time

Resource provisioning takes time. A cloud virtual machine (VM) can be acquired at any time by the user; however, it may take up to several minutes for the acquired VM to be ready to use. The VM startup time is dependent on factors such as image size, VM type, data center location, number of VMs, etc. Cloud providers have different VM startup performance. This implies that any control mechanism designed for elastic applications must consider the time needed for the resource provisioning actions to take effect.

### Monitoring elastic applications

Elastic applications can allocate and deallocate resources on demand for specific application components. This makes cloud resources volatile, and traditional monitoring tools which associate monitoring data with a particular resource, such as Ganglia or Nagios, are no longer suitable for monitoring the *behavior* of elastic applications. For example, during its lifetime, a data storage tier of an elastic application might add and remove data storage VMs due to cost and performance requirements, varying the number of used VMs. Thus, additional information is needed in monitoring elastic applications, such as associating the logical application structure over the underlying virtual infrastructure. This in turn generates other problems, such as data aggregation from multiple VMs towards extracting the behavior of the application component running on top of those VMs, as different metrics may need to be aggregated differently (e.g., CPU usage could be averaged, network transfer might be summed up).

### Stakeholder requirements

When deploying applications in cloud infrastructures (IaaS/PaaS), stakeholder requirements need to be considered in order to ensure that elastic behavior meets stakeholder needs. Traditionally, the optimal trade-off between cost and quality or performance is considered; however, for real world cloud users, requirements regarding elastic behavior are more complex and target multiple dimensions of elasticity (e.g., SYBL).

### Multiple levels of control

Cloud applications vary in type and complexity, with multiple levels of artifacts deployed in layers. Controlling such structures must take into consideration a variety of issues. For multi-level control, control systems need to consider the impact lower level control has upon higher level ones, and vice versa (e.g., controlling virtual machines, web containers, or web services in the same time), as well as conflicts that may appear between various control strategies from various levels. Elastic strategies on in cloud computing can take advantage of control-theoretic methods (e.g., predictive control has been experimented in cloud computing scenarios by showing considerable advantages with respect to reactive methods). One approach to multi-level elastic clouc control is rSYBL.
