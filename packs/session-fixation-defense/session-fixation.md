---
title: "Session fixation"
source: https://en.wikipedia.org/wiki/Session_fixation
domain: session-fixation-defense
license: CC-BY-SA-4.0
tags: session fixation defense, session identifier rotation, session hijacking prevention, session lifecycle management
fetched: 2026-07-02
---

# Session fixation

In computer network security, **session fixation attacks** attempt to exploit the vulnerability of a system that allows one person to fixate (find or set) another person's session identifier. Most session fixation attacks are web based, and most rely on session identifiers being accepted from URLs (query string) or POST data.

## Attack scenarios

Alice has an account at the bank `http://unsafe.example.com/`

Mallory intends to target Alice's money from her bank.

Alice has a reasonable level of trust in Mallory, and will visit links Mallory sends her.

### A simple attack scenario

Straightforward scenario:

1. Mallory has determined that `http://unsafe.example.com/` accepts any session identifier, accepts session identifiers from query strings and has no security validation. `http://unsafe.example.com/` is thus not secure.
2. Mallory sends Alice an e-mail: "Hey, check this out, there is a cool new account summary feature on our bank, `http://unsafe.example.com/?SID=I_WILL_KNOW_THE_SID`". Mallory is trying to fixate the SID to `I_WILL_KNOW_THE_SID`.
3. Alice is interested and visits `http://unsafe.example.com/?SID=I_WILL_KNOW_THE_SID`. The usual log-on screen pops up, and Alice logs on.
4. Mallory visits `http://unsafe.example.com/?SID=I_WILL_KNOW_THE_SID` and now has unlimited access to Alice's account.

### Attack using server generated SID

A misconception is that if a server only accepts server-generated session identifiers, it is safe from fixation. This is **false**.

Scenario:

1. Mallory visits `http://vulnerable.example.com/` and checks which SID is returned. For example, the server may respond: `Set-Cookie: SID=0D6441FEA4496C2`.
2. Mallory is now able to send Alice an e-mail: "Check out this new cool feature on our bank, `http://vulnerable.example.com/?SID=0D6441FEA4496C2`."
3. Alice logs on, with fixated session identifier `SID=0D6441FEA4496C2`.
4. Mallory visits `http://vulnerable.example.com/?SID=0D6441FEA4496C2` and now has unlimited access to Alice's account.

This type of attack is similar to a cross-site cookie attack except that, it does not rely on the vulnerability of the user's browser. Rather, it relies on the fact that wildcard cookies can be set by a subdomain and, that those cookies may affect other subdomains.

Scenario:

1. A web site `www.example.com` hands out subdomains to untrusted third parties
2. One such party, Mallory, who now controls `evil.example.com`, lures Alice to his site
3. A visit to `evil.example.com` sets a session cookie with the domain `.example.com` on Alice's browser
4. When Alice visits `www.example.com` this cookie will be sent with the request and Alice will have the session specified by Mallory's cookie.
5. If Alice now logs on, Mallory can use her account.

When this attack is complete, Mallory can gain access to `www.example.com` as Alice.

It is not essential that a user login to exploit session fixation attacks and, although these unauthenticated attacks are not constrained to cross-sub-domain cookie attacks, the implications of sub-domain attacks are relevant to these unauthenticated scenarios. For example, Mallory may provide a URL from their evil site, fixating a session into an unauthenticated scenario, and use those techniques to exploit their target. This includes scenarios exploiting both the unauthenticated scenarios (e.g. forms or registration) as well as the ability to feed the user an established session to bypass the login completely.

Consider, for example, that Mallory may create a user *A1ice* on *www.example.com* and login that user to capture a current, valid session identifier. Mallory then entraps Alice with a URL from *evil.example.com* which fixates that session cookie in Alice's browser (as described above) and redirects to *www.example.com* for finalizing a particular transaction (or, in fact, broader use). Mallory is thus able to ghost the session from their original login, scraping data and executing operations as 'A1ice' on 'www.example.com'. If Alice was successfully duped and saved her credit card to the account, Mallory might then make purchases using that card.

## Countermeasures

### Do not accept session identifiers from GET / POST variables

Session identifiers in URL (query string, GET variables) or POST variables are not recommended as they simplify this attack – it is easy to make links or forms that set GET / POST variables.

- The SID is leaked to other people as users cut & paste "interesting links" from the address bar into chats, forums, communities, etc.
- The SID is stored in many places (browser history log, web server log, proxy logs, ...)

Note: Cookies are shared between tabs and popped up browser windows. If your system requires to be hit with the same domain (www.example.com/?code=site1 and www.example.com/?code=site2 ), cookies may conflict with one another between tabs.

It may be required to send the session identifier on the URL in order to overcome this limitation. If possible use site1.example.com or site2.example.com so there is no domain conflicts in the cookies. This may incur costs with extra SSL certificates.

This behavior can be seen on many sites by opening another tab and trying to do side by side search results. One of the sessions will become unusable.

Session identifiers in GET and POST were deprecated in PHP 8.4 and will be removed in PHP 9.0.

#### Best solution: Identity confirmation

This attack can be largely avoided by changing, regenerating the session ID when users log in. If every request specific to a user requires the user to be authenticated with ("logged into") the site, an attacker would need to know the id of the victim's log-in session. When the victim visits the link with the fixed session id, however, they will need to log into their account in order to do anything "important" as themselves. At this point, their session id will change, and the attacker will not be able to do anything "important" with the anonymous session ID.

A similar technique can be used to solve the phishing problem. If the user protects their account with two passwords, then it can be solved to a great extent.

This technique is also useful against cross-site request forgery attacks.

#### Solution: Store session identifiers in HTTP cookies

The session identifier on most modern systems is stored by default in an HTTP cookie, which has a moderate level of security as long as the session system disregards GET/POST values. However, this solution is vulnerable to cross-site request forgery, and it does not meet the statelessness requirement of REST.

#### Solution: Utilize SSL / TLS session identifier

When enabling HTTPS security, some systems allow applications to obtain the SSL / TLS session identifier. Use of the SSL/TLS session identifier is very secure, but many web development languages do not provide robust built-in functionality for this.

### Regenerate SID on each request

A countermeasure against session fixation is to generate a new session identifier (SID) on each request. If this is done, then even though an attacker may trick a user into accepting a known SID, the SID will be invalid when the attacker attempts to re-use the SID. Implementation of such a system is simple, as demonstrated by the following:

- Get previous Session Identifier `OLD_SID` from HTTP request.
- If `OLD_SID` is null, empty, or no session with SID=`OLD_SID` exists, create a new session.
- Generate new session identifier `NEW_SID` with a secure random number generator.
- Let session be identified by SID=`NEW_SID` (and no longer by SID=`OLD_SID`)
- Transmit new SID to client.

Example:

If Mallory successfully tricks Alice into visiting `http://victim.example.com/?SID=I_KNOW_THE_SID`, this HTTP request is sent to `victim.example.com`:

```mw
GET /?SID=I_KNOW_THE_SID HTTP/1.1
Host: victim.example.com
```

`victim.example.com` accepts `SID=I_KNOW_THE_SID`, which would normally be bad. However, `victim.example.com` is secure because it performs session regeneration. `victim.example.com` gets the following response:

```mw
HTTP/1.1 200 OK
Set-Cookie: SID=3134998145AB331F
```

Alice will now use `SID=3134998145AB331F` that is unknown to Mallory, and `SID=I_KNOW_THE_SID` is invalid. Mallory is thus unsuccessful in the session fixation attempt.

Unfortunately session regeneration is not always possible. Problems are known to occur when third-party software such as ActiveX or Java applets are used, and when browser plugins communicate with the server. Third-party software could cause logouts, or the session could be split into two separate sessions.

If the implementation of sessions includes transmitting the SID through GET or POST variables, then this might also render the "back" button in most browsers unusable, as the user would then be using an older, invalid, session identifier from a previous request.

### Accept only server-generated SIDs

One way to improve security is not to accept session identifiers that were not generated by the server. However, as noted above, this does not prevent all session fixation attacks.

```mw
if (!isset($_SESSION['SERVER_GENERATED_SID'])) {
    session_destroy(); // Destroy all data in session
}
session_regenerate_id(); // Generate a new session identifier
$_SESSION['SERVER_GENERATED_SID'] = true;
```

### Logout function

A logout function is useful as it allows users to indicate that a session should not allow further requests. Thus attacks can only be effective while a session is active. Note that the following code performs no Cross-site request forgery checks, potentially allowing an attacker to force users to log out of the web application.

```mw
if (logout) {
    session_destroy(); // Destroy all data in session
}
```

### Time-out old SIDs

This defense is simple to implement and has the advantage of providing a measure of protection against unauthorized users accessing an authorized user's account by using a machine that may have been left unattended.

Store a session variable containing a time stamp of the last access made by that SID. When that SID is used again, compare the current timestamp with the one stored in the session. If the difference is greater than a predefined number, say 5 minutes, destroy the session. Otherwise, update the session variable with the current timestamp.

### Destroy session if Referrer is suspicious

When visiting a page, most web browsers will set the Referrer header – the page that contained the link that you followed to get to this page.

When the user is logged into a site that is not likely to be linked to from outside that site (e.g., banking websites, or webmail), and the site is not the kind of site where users would remain logged in for any great length of time, the Referrer should be from that site. Any other Referrer should be considered suspicious. However, if the originating request is from a HTTPS page, then the referrer will be stripped, so you cannot depend on this security system.

For example, `http://vulnerable.example.com/` could employ the following security check:

```mw
if (strpos($_SERVER['HTTP_REFERER'], 'http://vulnerable.example.com/') !== 0) {
    session_destroy(); // Destroy all data in session
}
session_regenerate_id(); // Generate a new session identifier
```

### Verify that additional information is consistent throughout session

One way to further improve security is to ensure that the user appears to be the same end user (client). This makes it a bit harder to perform session fixation and other attacks.

As more and more networks begin to conform to RFC 3704 and other anti-spoofing practices, the IP address becomes more reliable as a "same source" identifier. Therefore, the security of a web site can be improved by verifying that the source IP address is consistent throughout a session.

This could be performed in this manner:

```mw
if ($_SERVER['REMOTE_ADDR'] != $_SESSION['PREV_REMOTEADDR']) {
    session_destroy(); // Destroy all data in session
}
session_regenerate_id(); // Generate a new session identifier
$_SESSION['PREV_REMOTEADDR'] = $_SERVER['REMOTE_ADDR'];
```

However, there are some points to consider before employing this approach.

- Several users may share one IP address. It is not uncommon for an entire building to share one IP address using NAT.
- One user may have an inconsistent IP address. This is true for users behind proxies (such as AOL customers). It is also true for some mobile/roaming users, as well as users that are behind load balanced Internet connections. Users with IPv6 Privacy Extensions enabled may also change their IPv6 privacy addresses at any time.
- It will not work reliably with dual stack clients as requests will move between IPv4 and IPv6.
- It will not work reliably with mobile users, as mobile users roam between addresses as well.

For some sites, the added security outweighs the lack of convenience, and for others it does not.

#### User Agent

Browsers identify themselves by "User-Agent" HTTP headers. This header does not normally change during use; it would be extremely suspicious if that were to happen. A web application might make use of User-Agent detection in attempt to prevent malicious users from stealing sessions. This however is trivial to bypass, as an attacker can easily capture the victim's user-agent with their own site and then spoof it during the attack. This proposed security system is relying on security through obscurity.

```mw
if ($_SERVER['HTTP_USER_AGENT'] != $_SESSION['PREV_USERAGENT']) {
    session_destroy(); // Destroy all data in session
}
session_regenerate_id(); // Generate a new session identifier
$_SESSION['PREV_USERAGENT'] = $_SERVER['HTTP_USER_AGENT'];
```

However, there are some points to consider before employing this approach.

- Several users may have same browser User Agent in Internet café.
- Several users may have same default browser (ex: Internet Explorer 6 in Windows XP SP3 or mini browser in mobile phone).

But User Agent may change legally in few cases. Following examples are the same users.

- A smartphone whose screen rotated since the last request
  - `Mozilla/5.0 (Linux; U; Android 2.2; en-us; DROID2 Build/VZW) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 854X480 motorola DROID2`
  - `Mozilla/5.0 (Linux; U; Android 2.2; en-us; DROID2 Build/VZW) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 480X854 motorola DROID2`
- Internet Explorer compatibility mode:
  - `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)`
  - `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)`
- A user accessing a web site through a proxy distributed across multiple servers, not all of which are upgraded to the latest version of the proxy software
  - `Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (FlipboardProxy/0.0.5; +http://flipboard.com/browserproxy)`
  - `Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (FlipboardProxy/1.1; +http://flipboard.com/browserproxy)`

## Defense in depth

Defense in depth is to combine several countermeasures. The idea is simple: if one obstacle is trivial to overcome, several obstacles could be very hard to overcome.

A defense in depth strategy could involve:

- Enable HTTPS (to protect against other problems)
- Correct configuration (do not accept external SIDs, set time-out, etc.)
- Perform session_regeneration, support log-out, etc.

HTTP referrers are not passed with SSL/TLS (HTTPS).

The following PHP script demonstrates several such countermeasures combined in a defense in depth manner:

```mw
if (isset($_GET['LOGOUT']) ||
    $_SERVER['REMOTE_ADDR'] !== $_SESSION['PREV_REMOTEADDR'] ||
    $_SERVER['HTTP_USER_AGENT'] !== $_SESSION['PREV_USERAGENT']) {
    session_destroy();
}

session_regenerate_id(); // Generate a new session identifier

$_SESSION['PREV_USERAGENT'] = $_SERVER['HTTP_USER_AGENT'];
$_SESSION['PREV_REMOTEADDR'] = $_SERVER['REMOTE_ADDR'];
```

Note that this code checks the current REMOTE_ADDR (the user's IP address) and User-agent against the REMOTE_ADDR and User-agent of the previous request. This might be inconvenient for some sites as discussed above.
