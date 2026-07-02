---
title: "Secrets Management (part 2/2)"
source: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
domain: secrets-management
license: CC-BY-SA-4.0
tags: secrets management, key management, hardware security module, secret sharing, password manager
fetched: 2026-07-02
part: 2/2
---

## 6 Implementation Guidance

In this section, we will discuss implementation. Note that it is always best to refer to the official documentation of the secrets management system of choice for the actual implementation as it will be more up to date than any secondary document such as this cheat sheet.

### 6.1 Key Material Management Policies

Key material management is discussed in the Key Management Cheat Sheet

### 6.2 Dynamic vs Static Use Cases

We see the following use cases for dynamic secrets, among others:

- short-lived secrets (e.g., credentials or API keys) for a secondary service that expresses the intent for connecting the primary service (e.g., consumer) to the service.
- short-lived integrity and encryption controls for guarding and securing in-memory and runtime communication processes. Think of encryption keys that only need to live for a single session or a single deployment lifetime.
- short-lived credentials for building a stack during the deployment of a service for interacting with the deployers and supporting infrastructure.

Note that these dynamic secrets often need to be created with the service we need to connect to. To create these types of dynamic secrets, we usually require long-term static secrets to create the dynamic secrets themselves. Other static use cases:

- key material that needs to live longer than a single deployment due to the nature of its usage in the interaction with other instances of the same service (e.g., storage encryption keys, TLS PKI keys)
- key material or credentials to connect to services that do not support creating temporal roles or credentials.

### 6.3 Ensure limitations are in place

Secrets should never be retrievable by everyone and everything. Always make sure that you put guardrails in place:

- Do you have the opportunity to create access policies? Ensure that there are policies in place to limit the number of entities that can read or write the secret. At the same time, write the policies so that you can easily extend them, and they are not too complicated to understand.
- Is there no way to reduce access to certain secrets within a secrets management solution? Consider separating the production and development secrets by having separate secret management solutions. Then, reduce access to the production secrets management solution.

### 6.4 Security Event Monitoring is Key

Continually monitor who/what, from which IP, and what methodology accesses the secret. There are various patterns to look out for, such as, but not limited to:

- Monitor who accesses the secret at the secret management system: is this normal behavior? If the CI/CD credentials are used to access the secret management solution from a different IP than where the CI/CD system is running, provide a security alert and assume the secret is compromised.
- Monitor the service requiring the secret (if possible), e.g., whether the user of the secret is coming from an expected IP, with an expected user agent. If not, alert and assume the secret is compromised.

### 6.5 Usability and Ease of Onboarding

For a secrets management solution to be effective, it must be easy for developers to adopt and use. If the process is too complex, developers may resort to insecure practices. A focus on usability and a smooth onboarding experience is critical.

- **Clear and Comprehensive Documentation:**
  - Provide clear, concise, and easy-to-find documentation. This should include tutorials for common use cases, detailed API references, and practical examples.
  - Maintain a "getting started" guide that walks new users through the process of obtaining their first secret.
- **Developer-Friendly Tooling and SDKs:**
  - Offer well-maintained SDKs for various programming languages to simplify integration.
  - Provide a command-line interface (CLI) that allows developers to manage secrets from their local development environment.
  - Develop plugins for common IDEs, CI/CD systems, and infrastructure-as-code (IaC) tools like Terraform and Pulumi.
- **Streamlined Workflows:**
  - Implement self-service workflows that enable developers to request and receive secrets with minimal manual intervention.
  - Use GitOps principles to manage secrets as code, allowing developers to define secret needs in a declarative manner alongside their application code.
  - Automate the approval process for low-risk secrets while maintaining appropriate controls for more sensitive ones.
- **Actionable Feedback and Support:**
  - Provide clear error messages that help developers troubleshoot issues independently.
  - Establish dedicated support channels (e.g., a Slack channel, a ticketing system) where developers can get help from the security or platform team.
- **Easy Integration:**
  - Ensure the secrets management solution can be easily integrated with existing applications. Sidecar containers, such as the Vault Agent Sidecar Injector or the Conjur Secrets Provider, can help decouple applications from the secrets management system.


## 7 Encryption

Secrets Management goes hand in hand with encryption. After all, secrets must be stored encrypted somewhere to protect their confidentiality and integrity.

### 7.1 Encryption Types to Use

You can use various encryption types to secure a secret as long as they provide sufficient security, including adequate resistance against quantum computing-based attacks. Given that this is a moving field, it is best to take a look at sources like keylength.com, which enumerate up-to-date recommendations on the usage of encryption types and key lengths for existing standards, as well as the NSA's Commercial National Security Algorithm Suite 2.0 which enumerates quantum resistant algorithms.

Please note that in all cases, we need to preferably select an algorithm that provides encryption and confidentiality at the same time, such as AES-256 using GCM (Galois Counter Mode), or a mixture of ChaCha20 and Poly1305 according to the best practices in the field.

### 7.2 Convergent Encryption

Convergent Encryption ensures that a given plaintext and its key results in the same ciphertext. This can help detect possible reuse of secrets, resulting in the same ciphertext. The challenge with enabling convergent encryption is that it allows attackers to use the system to generate a set of cryptographic strings that might end up in the same secret, allowing the attacker to derive the plaintext secret. Given the algorithm and key, you can mitigate this risk if the convergent crypto system you use has sufficient resource challenges during encryption. Another factor that can help reduce the risk is ensuring that a secret is of adequate length, further hampering the possible guess-iteration time required.

### 7.3 Where to store the Encryption Keys?

You should not store keys next to the secrets they encrypt, except if those keys are encrypted themselves (see envelope encryption). Start by consulting the Key Management Cheat Sheet on where and how to store the encryption and possible HMAC keys.

### 7.4 Encryption as a Service (EaaS)

EaaS is a model in which users subscribe to a cloud-based encryption service without having to install encryption on their own systems. Using EaaS, you can get the following benefits:

- Encryption at rest
- Encryption in transit (TLS)
- Key handling and cryptographic implementations are taken care of by Encryption Service, not by developers
- The provider could add more services to interact with the sensitive data


## 8 Detection

There are many approaches to secrets detection and some very useful open-source projects to help with this. The Yelp Detect Secrets project is mature and has signature matching for around 20 secrets. For more information on other tools to help you in the detection space, check out the Secrets Detection topic on GitHub.

### 8.1 General detection approaches

Shift-left and DevSecOps principles apply to secrets detection as well. These general approaches below aim to consider secrets earlier and evolve the practice over time.

- Create standard test secrets and use them universally across the organization. This allows for reducing false positives by only needing to track a single test secret for each secret type.
- Consider enabling secrets detection at the developer level to avoid checking secrets into code before commit/PR either in the IDE, as part of test-driven development, or via pre-commit hook.
- Make secrets detection part of the threat model. Consider secrets as part of the attack surface during threat modeling exercises.
- Evaluate detection utilities and related signatures often to ensure they meet expectations.
- Consider having more than one detection utility and correlating/de-duping results to identify potential areas of detection weakness.
- Explore a balance between entropy and ease of detection. Secrets with consistent formats are easier to detect with lower false-positive rates, but you also don't want to miss a human-created password simply because it doesn't match your detection rules.

### 8.2 Types of secrets to be detected

Many types of secrets exist, and you should consider signatures for each to ensure accurate detection for all. Among the more common types are:

- High availability secrets (Tokens that are difficult to rotate)
- Application configuration files
- Connection strings
- API keys
- Credentials
- Passwords
- 2FA keys
- Private keys (e.g., SSH keys)
- Session tokens
- Platform-specific secret types (e.g., Amazon Web Services, Google Cloud)

For more fun learning about secrets and practice rooting them out, check out the Wrong Secrets project.

### 8.3 Detection lifecycle

Secrets are like any other authorization token. They should:

- Exist only for as long as necessary (rotate often)
- Have a method for automatic rotation
- Only be visible to those who need them (least privilege)
- Be revocable (including the logging of attempt to use a revoked secret)
- Never be logged (must implement either an encryption or masking approach in place to avoid logging plaintext secrets)

Create detection rules for each of the stages of the secret lifecycle.

### 8.4 Documentation for how to detect secrets

Create documentation and update it regularly to inform the developer community on procedures and systems available at your organization and what types of secrets management you expect, how to test for secrets, and what to do in the event of detected secrets.

Documentation should:

- Exist and be updated often, especially in response to an incident
- Include the following information:
  - Who has access to the secret
  - How it gets rotated
  - Any upstream or downstream dependencies that could potentially be broken during secret rotation
  - Who is the point of contact during an incident
  - Security impact of exposure
- Identify when secrets may be handled differently depending on the threat risk, data classification, etc.


## 9 Incident Response

Quick response in the event of a secret exposure is perhaps one of the most critical considerations for secrets management.

### 9.1 Documentation

Incident response in the event of secret exposure should ensure that everyone in the chain of custody is aware and understands how to respond. This includes application creators (every member of a development team), information security, and technology leadership.

Documentation must include:

- How to test for secrets and secrets handling, especially during business continuity reviews.
- Whom to alert when a secret is detected.
- Steps to take for containment
- Information to log during the event

### 9.2 Remediation

The primary goal of incident response is rapid response and containment.

Containment should follow these procedures:

1. Revocation: Keys that were exposed should undergo immediate revocation. The secret must be able to be de-authorized quickly, and systems must be in place to identify the revocation status.
2. Rotation: A new secret must be able to be quickly created and implemented, preferably via an automated process to ensure repeatability, low rate of implementation error, and least-privilege (not directly human-readable).
3. Deletion: Secrets revoked/rotated must be removed from the exposed system immediately, including secrets discovered in code or logs. Secrets in code could have commit history for the exposure squashed to before the introduction of the secret, however, this may introduce other problems as it rewrites git history and will break any other links to a given commit. If you decide to do this be aware of the consequences and plan accordingly. Secrets in logs must have a process for removing the secret while maintaining log integrity.
4. Logging: Incident response teams must have access to information about the lifecycle of a secret to aid in containment and remediation, including:
  - Who had access?
  - When did they use it?
  - When was it previously rotated?

### 9.3 Logging

Additional considerations for logging of secrets usage should include:

- Logging for incident response should be to a single location accessible by incident response (IR) teams
- Ensure fidelity of logging information during purple team exercises such as:
  - What should have been logged?
  - What was actually logged?
  - Do we have adequate alerts in place to ensure this?

Consider using a standardized logging format and vocabulary such as the Logging Vocabulary Cheat Sheet to ensure that all necessary information is logged.


## 10 Secrets Management in a Multi-Cloud Environment

### 10.1 Introduction

Managing secrets in a multi-cloud environment presents unique challenges due to the diversity of cloud providers and their respective services. This section discusses the challenges and best practices for managing secrets across multiple cloud providers.

### 10.2 Challenges

1. **Diverse APIs and Interfaces**: Each cloud provider has its own API and interface for managing secrets, which can lead to complexity in integrating and managing secrets across multiple providers.
2. **Inconsistent Security Policies**: Different cloud providers may have varying security policies and practices, making it challenging to enforce consistent security standards across all environments.
3. **Key Rotation**: Ensuring that keys are rotated consistently and securely across multiple cloud providers can be difficult, especially if each provider has different mechanisms for key rotation.
4. **Access Control**: Managing access control for secrets across multiple cloud providers can be complex, as each provider may have different access control mechanisms and policies.
5. **Auditing and Monitoring**: Ensuring comprehensive auditing and monitoring of secret access and usage across multiple cloud providers can be challenging due to the differences in logging and monitoring capabilities.

### 10.3 Best Practices

1. **Use a Centralized Secrets Management Solution**: Implement a centralized secrets management solution that can integrate with multiple cloud providers. This can help standardize the management of secrets and enforce consistent security policies across all environments. Examples include HashiCorp Vault and CyberArk Conjur.
2. **Standardize Security Policies**: Define and enforce standardized security policies for managing secrets across all cloud providers. This includes policies for key rotation, access control, and auditing.
3. **Automate Key Rotation**: Implement automated key rotation processes to ensure that keys are rotated consistently and securely across all cloud providers. Use tools and scripts to automate the rotation process and reduce the risk of human error.
4. **Implement Fine-Grained Access Control**: Use fine-grained access control mechanisms to restrict access to secrets based on the principle of least privilege. Ensure that access control policies are consistently enforced across all cloud providers.
5. **Enable Comprehensive Auditing and Monitoring**: Implement comprehensive auditing and monitoring of secret access and usage across all cloud providers. Use centralized logging and monitoring solutions to aggregate and analyze logs from multiple providers.

### 10.4 References

- HashiCorp Vault
- CyberArk Conjur
- AWS Secrets Manager
- Azure Key Vault
- Google Cloud Secret Manager

- Key Management Cheat Sheet
- Logging Cheat Sheet
- Password Storage Cheat Sheet
- Cryptographic Storage Cheat Sheet
- OWASP WrongSecrets project
- Blog: 10 Pointers on Secrets Management
- Blog: From build to run: pointers on secure deployment
- GitHub listing on secrets detection tools
- NIST SP 800-57 Recommendation for Key Management
- OpenCRE References to secrets
