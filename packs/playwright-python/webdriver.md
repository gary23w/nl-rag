---
title: "Selenium (software)"
source: https://en.wikipedia.org/wiki/WebDriver
domain: playwright-python
license: CC-BY-SA-4.0
tags: python playwright, playwright automation, headless browser python
fetched: 2026-07-02
---

# Selenium (software)

(Redirected from

WebDriver

)

**Selenium** is an open source umbrella project for a range of tools and libraries aimed at supporting browser automation. It provides a playback tool for authoring functional tests across most modern web browsers, without the need to learn a test scripting language (Selenium IDE). It also provides a test domain-specific language (Selenese) to write tests in a number of popular programming languages, including JavaScript (Node.js), C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala. A C++ wrapper exists on its git page, but has not been updated in years. Selenium runs on Windows, Linux, and macOS. It is open-source software released under the Apache License 2.0.

## History

Selenium was originally developed by Jason Huggins in 2004 as an internal tool at ThoughtWorks. Huggins was later joined by other programmers and testers at ThoughtWorks, before Paul Hammant joined the team and steered the development of the second mode of operation that would later become "Selenium Remote Control" (RC). The tool was open sourced that year.

In 2005 Dan Fabulich and Nelson Sproul (with help from Pat Lightbody) made an offer to accept a series of patches that would transform Selenium-RC into what it became best known for. In the same meeting, the steering of Selenium as a project would continue as a committee, with Huggins and Hammant being the ThoughtWorks representatives.

In 2007, Huggins joined Google. Together with others like Jennifer Bevan, he continued with the development and stabilization of Selenium RC. At the same time, Simon Stewart at ThoughtWorks developed a superior browser automation tool called WebDriver. In 2009, after a meeting between the developers at the Google Test Automation Conference, it was decided to merge the two projects, and call the new project Selenium WebDriver, or Selenium 2.0.

In 2008, Philippe Hanrigou (then at ThoughtWorks) made "Selenium Grid", which provides a hub allowing the running of multiple Selenium tests concurrently on any number of local or remote systems, thus minimizing test execution time. Grid offered, as open source, a similar capability to the internal/private Google cloud for Selenium RC. Pat Lightbody had already made a private cloud for "HostedQA" which he went on to sell to Gomez, Inc.

The name Selenium comes from a joke made by Huggins in an email, mocking a competitor named Mercury, saying that mercury poisoning can be cured by taking supplements of the element selenium. The others that received the email took the name and ran with it.

## Components

Selenium is composed of several components with each taking on a specific role in aiding the development of web application test automation.

### Selenium IDE

Selenium IDE is a complete integrated development environment (IDE) for Selenium tests. It is implemented as a Firefox Add-On and as a Chrome Extension. It allows for recording, editing and debugging of functional tests. It was previously known as Selenium Recorder. Selenium-IDE was originally created by Shinya Kasatani and donated to the Selenium project in 2006. Selenium IDE began being actively maintained in 2018.

Scripts may be automatically recorded and edited manually providing autocompletion support and the ability to move commands around quickly. Scripts are recorded in *Selenese*, a special test scripting language for Selenium. Selenese provides commands for performing actions in a browser (click a link, select an option) and for retrieving data from the resulting pages. Selenese serves as the language for composing Selenium Commands, which are utilized in the testing of web applications. These commands, tailored to the HTML tags of UI elements, facilitate the verification of their existence. They guide Selenium in comprehending the specific actions or operations to execute.

### Selenium client API

As an alternative to writing tests in Selenese, tests can also be written in various programming languages. These tests then communicate with Selenium by calling methods in the Selenium Client API. Selenium currently provides client APIs for Java, C#, Ruby, JavaScript, R and Python.

### Selenium Remote Control

Selenium Remote Control (RC) is a server, written in Java, that accepts commands for the browser via HTTP. RC makes it possible to write automated tests for a web application in any programming language, which allows for better integration of Selenium in existing unit test frameworks. To make writing tests easier, Selenium project currently provides client drivers for PHP, Python, Ruby, .NET, Perl and Java. The Java driver can also be used with JavaScript (via the Rhino engine). An instance of selenium RC server is needed to launch html test case - which means that the port should be different for each parallel run. However, for Java/PHP test case only one Selenium RC instance needs to be running continuously.

Selenium Remote Control was a refactoring of Driven Selenium or Selenium B designed by Paul Hammant, credited with Jason as co-creator of Selenium. The original version directly launched a process for the browser in question, from the test language of Java, .NET, Python or Ruby. The wire protocol (called 'Selenese' in its day) was reimplemented in each language port. After the refactor by Dan Fabulich and Nelson Sproul (with help from Pat Lightbody) there was an intermediate daemon process between the driving test script and the browser. The benefits included the ability to drive remote browsers and the reduced need to port every line of code to an increasingly growing set of languages. *Selenium Remote Control* completely took over from the Driven Selenium code-line in 2006. The browser pattern for 'Driven'/'B' and 'RC' was response/request, which subsequently became known as Comet.

Selenium RC served as the flagship testing framework of the entire project of selenium for a long-standing time. Selenium RC is the first and foremost automated web testing tool that enabled users to adopt their preferred programming language.

With the release of Selenium 2, Selenium RC has been officially deprecated in favor of Selenium WebDriver.

### Selenium WebDriver

At the core of Selenium is Selenium WebDriver, an interface to write instructions that work interchangeably across browsers. It is the successor to Selenium RC. Selenium WebDriver accepts commands (sent in Selenese, or via a Client API) and sends them to a browser. This is implemented through a browser-specific browser driver, which sends commands to a browser and retrieves results. Most browser drivers actually launch and access a browser application (such as Firefox, Google Chrome, Internet Explorer, Safari, or Microsoft Edge); there is also an HtmlUnit browser driver, which simulates a browser using the headless browser HtmlUnit. Since Selenium 4 and Google Chrome version 109, headless mode has been supported through a native implementation of the browser, in which Chrome operates without a graphical user interface but with rendering and execution behavior identical to the regular mode.

Unlike in Selenium 1, where the Selenium server was necessary to run tests, Selenium WebDriver does not need a special server to execute tests. Instead, the WebDriver directly starts a browser instance and controls it. However, Selenium Grid can be used with WebDriver to execute tests on remote systems (see below). Where possible, WebDriver uses native operating system level functionality rather than browser-based JavaScript commands to drive the browser. This bypasses problems with subtle differences between native and JavaScript commands, including security restrictions.

As of early 2012, Simon Stewart (inventor of WebDriver), who was then with Google, and David Burns of Mozilla were negotiating with the W3C to make WebDriver an Internet standard. In July 2012, the working draft was released and the recommendation followed in June 2018. Selenium WebDriver (Selenium 2.0) is fully implemented and supported in JavaScript (Node.js), Python, Ruby, Java, Kotlin, and C#. As of 2021, Selenium 4 is a release candidate.

#### Python

```mw
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.remote.webelement import WebElement

if __name__ == "__main__":
    # This example requires Selenium WebDriver 3.13 or newer
    with Firefox() as driver:
        wait: WebDriverWait = WebDriverWait(driver, 10)
        driver.get("https://google.com/ncr")
        driver.find_element(By.NAME, "q").send_keys(f"cheese{Keys.RETURN}")
        first_result: WebElement = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
        print(first_result.get_attribute("textContent"))
```

#### Java

```mw
package org.wikipedia.examples;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import static org.openqa.selenium.support.ui.ExpectedConditions.presenceOfElementLocated;

public class HelloSelenium {
    public static void main(String[] args) {
        try (WebDriver driver = new FirefoxDriver()) {
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10))
            driver.get("https://google.com/ncr");
            driver.findElement(By.name("q")).sendKeys("cheese" + Keys.ENTER);
            WebElement firstResult = wait.until(presenceOfElementLocated(By.cssSelector("h3")));
            System.out.println(firstResult.getAttribute("textContent"));
            driver.quit();
        } catch (Exception e) {
            System.err.printf("Error caught: %s%n", e.getMessage());
        }
    }
}
```

#### C

```mw
namespace Wikipedia.Examples;

using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;

public class HelloSelenium
{
    static void Main(string[] args)
    {
        using (IWebDriver driver = new FirefoxDriver())
        {
            WebDriverWait wait = new(driver, TimeSpan.FromSeconds(10));
            driver.Navigate().GoToUrl("https://www.google.com/");
            driver.FindElement(By.Name("q")).SendKeys($"cheese{Keys.Enter}");
            wait.Until(webDriver => webDriver.FindElement(By.CssSelector("h3")).Displayed);
            IWebElement firstResult = driver.FindElement(By.CssSelector("h3"));
            Console.WriteLine(firstResult.GetAttribute("textContent"));
        }
    }
}
```

### Selenium Grid

Selenium Grid is a server that allows tests to use web browser instances running on remote machines. With Selenium Grid, one server acts as the central hub. Tests contact the hub to obtain access to browser instances. The hub has a list of servers that provide access to browser instances (WebDriver nodes), and lets tests use these instances. Selenium Grid allows running tests in parallel on multiple machines and to manage different browser versions and browser configurations centrally (instead of in each individual test).

The ability to run tests on remote browser instances is useful to spread the load of testing across several machines and to run tests in browsers running on different platforms or operating systems. The latter is particularly useful in cases where not all browsers to be used for testing can run on the same platform.
