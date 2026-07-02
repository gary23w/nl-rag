---
title: "Waiting Strategies"
source: https://www.selenium.dev/documentation/webdriver/waits/
domain: selenium
license: CC-BY-SA-4.0
tags: selenium webdriver, browser automation, web testing, headless browser
fetched: 2026-07-02
---

# Waiting Strategies

Perhaps the most common challenge for browser automation is ensuring that the web application is in a state to execute a particular Selenium command as desired. The processes often end up in a *race condition* where sometimes the browser gets into the right state first (things work as intended) and sometimes the Selenium code executes first (things do not work as intended). This is one of the primary causes of *flaky tests*.

All navigation commands wait for a specific `readyState` value based on the page load strategy (the default value to wait for is `"complete"`) before the driver returns control to the code. The `readyState` only concerns itself with loading assets defined in the HTML, but loaded JavaScript assets often result in changes to the site, and elements that need to be interacted with may not yet be on the page when the code is ready to execute the next Selenium command.

Similarly, in a lot of single page applications, elements get dynamically added to a page or change visibility based on a click. An element must be both present and displayed on the page in order for Selenium to interact with it.

Take this page for example: https://www.selenium.dev/selenium/web/dynamic.html When the “Add a box!” button is clicked, a “div” element that does not exist is created. When the “Reveal a new input” button is clicked, a hidden text field element is displayed. In both cases the transition takes a couple seconds. If the Selenium code is to click one of these buttons and interact with the resulting element, it will do so before that element is ready and fail.

The first solution many people turn to is adding a sleep statement to pause the code execution for a set period of time. Because the code can’t know exactly how long it needs to wait, this can fail when it doesn’t sleep long enough. Alternately, if the value is set too high and a sleep statement is added in every place it is needed, the duration of the session can become prohibitive.

Selenium provides two different mechanisms for synchronization that are better.

## Implicit waits

Selenium has a built-in way to automatically wait for elements called an *implicit wait*. An implicit wait value can be set either with the timeouts capability in the browser options, or with a driver method (as shown below).

This is a global setting that applies to every element location call for the entire session. The default value is `0`, which means that if the element is not found, it will immediately return an error. If an implicit wait is set, the driver will wait for the duration of the provided value before returning the error. Note that as soon as the element is located, the driver will return the element reference and the code will continue executing, so a larger implicit wait value won’t necessarily increase the duration of the session.

*Warning:* Do not mix implicit and explicit waits. Doing so can cause unpredictable wait times. For example, setting an implicit wait of 10 seconds and an explicit wait of 15 seconds could cause a timeout to occur after 20 seconds.

Solving our example with an implicit wait looks like this:

```java
    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
```

View Complete Code

View on GitHub

##### /examples/java/src/test/java/dev/selenium/waits/WaitsTest.java

```java
package dev.selenium.waits;

import dev.selenium.BaseTest;
import java.time.Duration;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.ElementNotInteractableException;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

public class WaitsTest extends BaseTest {
  @Test
  public void fails() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    Assertions.assertThrows(
        NoSuchElementException.class,
        () -> {
          driver.findElement(By.id("box0"));
        });
  }

  @Test
  public void sleep() throws InterruptedException {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    Thread.sleep(1000);

    WebElement added = driver.findElement(By.id("box0"));

    Assertions.assertEquals("redbox", added.getDomAttribute("class"));
  }

  @Test
  public void implicit() {
    startChromeDriver(new ChromeOptions());

    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    WebElement added = driver.findElement(By.id("box0"));

    Assertions.assertEquals("redbox", added.getDomAttribute("class"));
  }

  @Test
  public void explicit() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    WebElement revealed = driver.findElement(By.id("revealed"));
    driver.findElement(By.id("reveal")).click();

    Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(2));
    wait.until(d -> revealed.isDisplayed());

    revealed.sendKeys("Displayed");
    Assertions.assertEquals("Displayed", revealed.getDomProperty("value"));
  }

  @Test
  public void explicitWithOptions() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    WebElement revealed = driver.findElement(By.id("revealed"));
    driver.findElement(By.id("reveal")).click();

    Wait<WebDriver> wait =
        new FluentWait<>(driver)
            .withTimeout(Duration.ofSeconds(2))
            .pollingEvery(Duration.ofMillis(300))
            .ignoring(ElementNotInteractableException.class);

    wait.until(
        d -> {
          revealed.sendKeys("Displayed");
          return true;
        });

    Assertions.assertEquals("Displayed", revealed.getDomProperty("value"));
  }
}
```

```py
    driver.implicitly_wait(2)
```

View Complete Code

View on GitHub

##### /examples/python/tests/waits/test_waits.py

```py
import pytest
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, 'box0')

def test_sleep(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    time.sleep(2)
    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_implicit(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"

def test_explicit_options(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda _ : revealed.send_keys("Displayed") or True)

    assert revealed.get_property("value") == "Displayed"
```

```cs
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);
```

View Complete Code

View on GitHub

##### /examples/dotnet/SeleniumDocs/Waits/WaitsTest.cs

```cs
using System;
using System.Threading;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;

namespace SeleniumDocs.Waits
{
    [TestClass]
    public class WaitsTest : BaseChromeTest
    {
        [TestMethod]
        public void Fails()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            Assert.ThrowsException<NoSuchElementException>(
                () => driver.FindElement(By.Id("box0"))
            );
        }

        [TestMethod]
        public void Sleep()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            Thread.Sleep(1000);

            IWebElement added = driver.FindElement(By.Id("box0"));

            Assert.AreEqual("redbox", added.GetDomAttribute("class"));
        }

        [TestMethod]
        public void Implicit()
        {
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);
            
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            IWebElement added = driver.FindElement(By.Id("box0"));

            Assert.AreEqual("redbox", added.GetDomAttribute("class"));
        }

        [TestMethod]
        public void Explicit()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            IWebElement revealed = driver.FindElement(By.Id("revealed"));
            driver.FindElement(By.Id("reveal")).Click();

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2));
            wait.Until(d => revealed.Displayed);

            revealed.SendKeys("Displayed");
            Assert.AreEqual("Displayed", revealed.GetDomProperty("value"));
        }

        [TestMethod]
        public void ExplicitOptions()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            IWebElement revealed = driver.FindElement(By.Id("revealed"));
            driver.FindElement(By.Id("reveal")).Click();

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2))
            {
                PollingInterval = TimeSpan.FromMilliseconds(300),
            };
            wait.IgnoreExceptionTypes(typeof(ElementNotInteractableException));

            wait.Until(d => {
                revealed.SendKeys("Displayed");
                return true;
            });

            Assert.AreEqual("input", revealed.TagName);
        }
    }
}
```

```rb
    driver.manage.timeouts.implicit_wait = 2
```

View Complete Code

View on GitHub

##### /examples/ruby/spec/waits/waits_spec.rb

```rb
# frozen_string_literal: true

require 'spec_helper'

RSpec.describe 'Waits' do
  let(:driver) { start_session }

  it 'fails' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    expect {
      driver.find_element(id: 'box0')
    }.to raise_error(Selenium::WebDriver::Error::NoSuchElementError)
  end

  it 'sleeps' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    sleep 1
    added = driver.find_element(id: 'box0')

    expect(added.dom_attribute(:class)).to eq('redbox')
  end

  it 'implicit' do
    driver.manage.timeouts.implicit_wait = 2
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    added = driver.find_element(id: 'box0')

    expect(added.dom_attribute(:class)).to eq('redbox')
  end

  it 'explicit' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    revealed = driver.find_element(id: 'revealed')
    driver.find_element(id: 'reveal').click

    wait = Selenium::WebDriver::Wait.new
    wait.until { revealed.displayed? }

    revealed.send_keys('Displayed')
    expect(revealed.property(:value)).to eq('Displayed')
  end

  it 'options with explicit' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    revealed = driver.find_element(id: 'revealed')
    driver.find_element(id: 'reveal').click

    errors = [Selenium::WebDriver::Error::NoSuchElementError,
              Selenium::WebDriver::Error::ElementNotInteractableError]
    wait = Selenium::WebDriver::Wait.new(timeout: 2,
                                         interval: 0.3,
                                         ignore: errors)

    wait.until { revealed.send_keys('Displayed') || true }

    expect(revealed.property(:value)).to eq('Displayed')
  end
end
```

```js
        await driver.manage().setTimeouts({ implicit: 2000 });
```

View Complete Code

View on GitHub

##### /examples/javascript/test/waits/waits.spec.js

```js
const { By, Browser, until, Builder} = require('selenium-webdriver');
const assert = require("node:assert");

describe('Waits', function () {
    let driver;

    before(async function () {
        driver = new Builder()
          .forBrowser(Browser.CHROME)
          .build();
    });

    after(async () => await driver.quit());

    it('fail', async function () {
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        await driver.findElement(By.id("adder")).click();

        await assert.rejects(async () => {
              await driver.findElement(By.id("box0"))
          },
          Error
        )
    });

    it('sleep', async function () {
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        await driver.findElement(By.id("adder")).click();

        await driver.sleep(2000);
        let added = await driver.findElement(By.id("box0"));

        assert.equal(await added.getAttribute('class'), "redbox")
    });

    it('implicit', async function () {
        await driver.manage().setTimeouts({ implicit: 2000 });
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        await driver.findElement(By.id("adder")).click();

        let added = await driver.findElement(By.id("box0"));

        assert.equal(await added.getAttribute('class'), "redbox")
    });

    it('explicit', async function () {
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        let revealed = await driver.findElement(By.id("revealed"));
        await driver.findElement(By.id("reveal")).click();
        await driver.wait(until.elementIsVisible(revealed), 2000);
        await revealed.sendKeys("Displayed");
        assert.equal(await revealed.getAttribute("value"), "Displayed")
    })
});
```

View Complete Code

View on GitHub

##### examples/kotlin/src/test/kotlin/dev/selenium/waits/WaitsTest.kt

## Explicit waits

*Explicit waits* are loops added to the code that poll the application for a specific condition to evaluate as true before it exits the loop and continues to the next command in the code. If the condition is not met before a designated timeout value, the code will give a timeout error. Since there are many ways for the application not to be in the desired state, explicit waits are a great choice to specify the exact condition to wait for in each place it is needed. Another nice feature is that, by default, the Selenium Wait class automatically waits for the designated element to exist.

This example shows the condition being waited for as a *lambda*. Java also supports Expected Conditions

```java
    Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(2));
    wait.until(d -> revealed.isDisplayed());
```

View Complete Code

View on GitHub

##### /examples/java/src/test/java/dev/selenium/waits/WaitsTest.java

```java
package dev.selenium.waits;

import dev.selenium.BaseTest;
import java.time.Duration;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.ElementNotInteractableException;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

public class WaitsTest extends BaseTest {
  @Test
  public void fails() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    Assertions.assertThrows(
        NoSuchElementException.class,
        () -> {
          driver.findElement(By.id("box0"));
        });
  }

  @Test
  public void sleep() throws InterruptedException {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    Thread.sleep(1000);

    WebElement added = driver.findElement(By.id("box0"));

    Assertions.assertEquals("redbox", added.getDomAttribute("class"));
  }

  @Test
  public void implicit() {
    startChromeDriver(new ChromeOptions());

    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    WebElement added = driver.findElement(By.id("box0"));

    Assertions.assertEquals("redbox", added.getDomAttribute("class"));
  }

  @Test
  public void explicit() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    WebElement revealed = driver.findElement(By.id("revealed"));
    driver.findElement(By.id("reveal")).click();

    Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(2));
    wait.until(d -> revealed.isDisplayed());

    revealed.sendKeys("Displayed");
    Assertions.assertEquals("Displayed", revealed.getDomProperty("value"));
  }

  @Test
  public void explicitWithOptions() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    WebElement revealed = driver.findElement(By.id("revealed"));
    driver.findElement(By.id("reveal")).click();

    Wait<WebDriver> wait =
        new FluentWait<>(driver)
            .withTimeout(Duration.ofSeconds(2))
            .pollingEvery(Duration.ofMillis(300))
            .ignoring(ElementNotInteractableException.class);

    wait.until(
        d -> {
          revealed.sendKeys("Displayed");
          return true;
        });

    Assertions.assertEquals("Displayed", revealed.getDomProperty("value"));
  }
}
```

This example shows the condition being waited for as a *lambda*. Python also supports Expected Conditions

```py
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : revealed.is_displayed())
```

View Complete Code

View on GitHub

##### /examples/python/tests/waits/test_waits.py

```py
import pytest
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, 'box0')

def test_sleep(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    time.sleep(2)
    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_implicit(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"

def test_explicit_options(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda _ : revealed.send_keys("Displayed") or True)

    assert revealed.get_property("value") == "Displayed"
```

```cs
            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2));
            wait.Until(d => revealed.Displayed);
```

View Complete Code

View on GitHub

##### /examples/dotnet/SeleniumDocs/Waits/WaitsTest.cs

```cs
using System;
using System.Threading;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;

namespace SeleniumDocs.Waits
{
    [TestClass]
    public class WaitsTest : BaseChromeTest
    {
        [TestMethod]
        public void Fails()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            Assert.ThrowsException<NoSuchElementException>(
                () => driver.FindElement(By.Id("box0"))
            );
        }

        [TestMethod]
        public void Sleep()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            Thread.Sleep(1000);

            IWebElement added = driver.FindElement(By.Id("box0"));

            Assert.AreEqual("redbox", added.GetDomAttribute("class"));
        }

        [TestMethod]
        public void Implicit()
        {
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);
            
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            IWebElement added = driver.FindElement(By.Id("box0"));

            Assert.AreEqual("redbox", added.GetDomAttribute("class"));
        }

        [TestMethod]
        public void Explicit()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            IWebElement revealed = driver.FindElement(By.Id("revealed"));
            driver.FindElement(By.Id("reveal")).Click();

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2));
            wait.Until(d => revealed.Displayed);

            revealed.SendKeys("Displayed");
            Assert.AreEqual("Displayed", revealed.GetDomProperty("value"));
        }

        [TestMethod]
        public void ExplicitOptions()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            IWebElement revealed = driver.FindElement(By.Id("revealed"));
            driver.FindElement(By.Id("reveal")).Click();

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2))
            {
                PollingInterval = TimeSpan.FromMilliseconds(300),
            };
            wait.IgnoreExceptionTypes(typeof(ElementNotInteractableException));

            wait.Until(d => {
                revealed.SendKeys("Displayed");
                return true;
            });

            Assert.AreEqual("input", revealed.TagName);
        }
    }
}
```

```rb
    wait = Selenium::WebDriver::Wait.new
    wait.until { revealed.displayed? }
```

View Complete Code

View on GitHub

##### /examples/ruby/spec/waits/waits_spec.rb

```rb
# frozen_string_literal: true

require 'spec_helper'

RSpec.describe 'Waits' do
  let(:driver) { start_session }

  it 'fails' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    expect {
      driver.find_element(id: 'box0')
    }.to raise_error(Selenium::WebDriver::Error::NoSuchElementError)
  end

  it 'sleeps' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    sleep 1
    added = driver.find_element(id: 'box0')

    expect(added.dom_attribute(:class)).to eq('redbox')
  end

  it 'implicit' do
    driver.manage.timeouts.implicit_wait = 2
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    added = driver.find_element(id: 'box0')

    expect(added.dom_attribute(:class)).to eq('redbox')
  end

  it 'explicit' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    revealed = driver.find_element(id: 'revealed')
    driver.find_element(id: 'reveal').click

    wait = Selenium::WebDriver::Wait.new
    wait.until { revealed.displayed? }

    revealed.send_keys('Displayed')
    expect(revealed.property(:value)).to eq('Displayed')
  end

  it 'options with explicit' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    revealed = driver.find_element(id: 'revealed')
    driver.find_element(id: 'reveal').click

    errors = [Selenium::WebDriver::Error::NoSuchElementError,
              Selenium::WebDriver::Error::ElementNotInteractableError]
    wait = Selenium::WebDriver::Wait.new(timeout: 2,
                                         interval: 0.3,
                                         ignore: errors)

    wait.until { revealed.send_keys('Displayed') || true }

    expect(revealed.property(:value)).to eq('Displayed')
  end
end
```

JavaScript also supports Expected Conditions

```js
        await driver.wait(until.elementIsVisible(revealed), 2000);
```

View Complete Code

View on GitHub

##### /examples/javascript/test/waits/waits.spec.js

```js
const { By, Browser, until, Builder} = require('selenium-webdriver');
const assert = require("node:assert");

describe('Waits', function () {
    let driver;

    before(async function () {
        driver = new Builder()
          .forBrowser(Browser.CHROME)
          .build();
    });

    after(async () => await driver.quit());

    it('fail', async function () {
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        await driver.findElement(By.id("adder")).click();

        await assert.rejects(async () => {
              await driver.findElement(By.id("box0"))
          },
          Error
        )
    });

    it('sleep', async function () {
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        await driver.findElement(By.id("adder")).click();

        await driver.sleep(2000);
        let added = await driver.findElement(By.id("box0"));

        assert.equal(await added.getAttribute('class'), "redbox")
    });

    it('implicit', async function () {
        await driver.manage().setTimeouts({ implicit: 2000 });
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        await driver.findElement(By.id("adder")).click();

        let added = await driver.findElement(By.id("box0"));

        assert.equal(await added.getAttribute('class'), "redbox")
    });

    it('explicit', async function () {
        await driver.get('https://www.selenium.dev/selenium/web/dynamic.html');
        let revealed = await driver.findElement(By.id("revealed"));
        await driver.findElement(By.id("reveal")).click();
        await driver.wait(until.elementIsVisible(revealed), 2000);
        await revealed.sendKeys("Displayed");
        assert.equal(await revealed.getAttribute("value"), "Displayed")
    })
});
```

View Complete Code

View on GitHub

##### examples/kotlin/src/test/kotlin/dev/selenium/waits/WaitsTest.kt

### Customization

The Wait class can be instantiated with various parameters that will change how the conditions are evaluated.

This can include:

- Changing how often the code is evaluated (polling interval)
- Specifying which exceptions should be handled automatically
- Changing the total timeout length
- Customizing the timeout message

For instance, if the *element not interactable* error is retried by default, then we can add an action on a method inside the code getting executed (we just need to make sure that the code returns `true` when it is successful):

The easiest way to customize Waits in Java is to use the `FluentWait` class:

```java
    Wait<WebDriver> wait =
        new FluentWait<>(driver)
            .withTimeout(Duration.ofSeconds(2))
            .pollingEvery(Duration.ofMillis(300))
            .ignoring(ElementNotInteractableException.class);

    wait.until(
        d -> {
          revealed.sendKeys("Displayed");
          return true;
        });
```

View Complete Code

View on GitHub

##### /examples/java/src/test/java/dev/selenium/waits/WaitsTest.java

```java
package dev.selenium.waits;

import dev.selenium.BaseTest;
import java.time.Duration;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.ElementNotInteractableException;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

public class WaitsTest extends BaseTest {
  @Test
  public void fails() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    Assertions.assertThrows(
        NoSuchElementException.class,
        () -> {
          driver.findElement(By.id("box0"));
        });
  }

  @Test
  public void sleep() throws InterruptedException {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    Thread.sleep(1000);

    WebElement added = driver.findElement(By.id("box0"));

    Assertions.assertEquals("redbox", added.getDomAttribute("class"));
  }

  @Test
  public void implicit() {
    startChromeDriver(new ChromeOptions());

    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    driver.findElement(By.id("adder")).click();

    WebElement added = driver.findElement(By.id("box0"));

    Assertions.assertEquals("redbox", added.getDomAttribute("class"));
  }

  @Test
  public void explicit() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    WebElement revealed = driver.findElement(By.id("revealed"));
    driver.findElement(By.id("reveal")).click();

    Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(2));
    wait.until(d -> revealed.isDisplayed());

    revealed.sendKeys("Displayed");
    Assertions.assertEquals("Displayed", revealed.getDomProperty("value"));
  }

  @Test
  public void explicitWithOptions() {
    startChromeDriver(new ChromeOptions());

    driver.get("https://www.selenium.dev/selenium/web/dynamic.html");
    WebElement revealed = driver.findElement(By.id("revealed"));
    driver.findElement(By.id("reveal")).click();

    Wait<WebDriver> wait =
        new FluentWait<>(driver)
            .withTimeout(Duration.ofSeconds(2))
            .pollingEvery(Duration.ofMillis(300))
            .ignoring(ElementNotInteractableException.class);

    wait.until(
        d -> {
          revealed.sendKeys("Displayed");
          return true;
        });

    Assertions.assertEquals("Displayed", revealed.getDomProperty("value"));
  }
}
```

```py
    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda _ : revealed.send_keys("Displayed") or True)
```

View Complete Code

View on GitHub

##### /examples/python/tests/waits/test_waits.py

```py
import pytest
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_fails(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.ID, 'box0')

def test_sleep(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    time.sleep(2)
    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_implicit(driver):
    driver.implicitly_wait(2)
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.ID, "adder").click()

    added = driver.find_element(By.ID, "box0")

    assert added.get_dom_attribute('class') == "redbox"

def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"

def test_explicit_options(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda _ : revealed.send_keys("Displayed") or True)

    assert revealed.get_property("value") == "Displayed"
```

```cs
            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2))
            {
                PollingInterval = TimeSpan.FromMilliseconds(300),
            };
            wait.IgnoreExceptionTypes(typeof(ElementNotInteractableException));

            wait.Until(d => {
                revealed.SendKeys("Displayed");
                return true;
            });
```

View Complete Code

View on GitHub

##### /examples/dotnet/SeleniumDocs/Waits/WaitsTest.cs

```cs
using System;
using System.Threading;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;

namespace SeleniumDocs.Waits
{
    [TestClass]
    public class WaitsTest : BaseChromeTest
    {
        [TestMethod]
        public void Fails()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            Assert.ThrowsException<NoSuchElementException>(
                () => driver.FindElement(By.Id("box0"))
            );
        }

        [TestMethod]
        public void Sleep()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            Thread.Sleep(1000);

            IWebElement added = driver.FindElement(By.Id("box0"));

            Assert.AreEqual("redbox", added.GetDomAttribute("class"));
        }

        [TestMethod]
        public void Implicit()
        {
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);
            
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            driver.FindElement(By.Id("adder")).Click();

            IWebElement added = driver.FindElement(By.Id("box0"));

            Assert.AreEqual("redbox", added.GetDomAttribute("class"));
        }

        [TestMethod]
        public void Explicit()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            IWebElement revealed = driver.FindElement(By.Id("revealed"));
            driver.FindElement(By.Id("reveal")).Click();

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2));
            wait.Until(d => revealed.Displayed);

            revealed.SendKeys("Displayed");
            Assert.AreEqual("Displayed", revealed.GetDomProperty("value"));
        }

        [TestMethod]
        public void ExplicitOptions()
        {
            driver.Url = "https://www.selenium.dev/selenium/web/dynamic.html";
            IWebElement revealed = driver.FindElement(By.Id("revealed"));
            driver.FindElement(By.Id("reveal")).Click();

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(2))
            {
                PollingInterval = TimeSpan.FromMilliseconds(300),
            };
            wait.IgnoreExceptionTypes(typeof(ElementNotInteractableException));

            wait.Until(d => {
                revealed.SendKeys("Displayed");
                return true;
            });

            Assert.AreEqual("input", revealed.TagName);
        }
    }
}
```

```rb
    errors = [Selenium::WebDriver::Error::NoSuchElementError,
              Selenium::WebDriver::Error::ElementNotInteractableError]
    wait = Selenium::WebDriver::Wait.new(timeout: 2,
                                         interval: 0.3,
                                         ignore: errors)

    wait.until { revealed.send_keys('Displayed') || true }
```

View Complete Code

View on GitHub

##### /examples/ruby/spec/waits/waits_spec.rb

```rb
# frozen_string_literal: true

require 'spec_helper'

RSpec.describe 'Waits' do
  let(:driver) { start_session }

  it 'fails' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    expect {
      driver.find_element(id: 'box0')
    }.to raise_error(Selenium::WebDriver::Error::NoSuchElementError)
  end

  it 'sleeps' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    sleep 1
    added = driver.find_element(id: 'box0')

    expect(added.dom_attribute(:class)).to eq('redbox')
  end

  it 'implicit' do
    driver.manage.timeouts.implicit_wait = 2
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    driver.find_element(id: 'adder').click

    added = driver.find_element(id: 'box0')

    expect(added.dom_attribute(:class)).to eq('redbox')
  end

  it 'explicit' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    revealed = driver.find_element(id: 'revealed')
    driver.find_element(id: 'reveal').click

    wait = Selenium::WebDriver::Wait.new
    wait.until { revealed.displayed? }

    revealed.send_keys('Displayed')
    expect(revealed.property(:value)).to eq('Displayed')
  end

  it 'options with explicit' do
    driver.get 'https://www.selenium.dev/selenium/web/dynamic.html'
    revealed = driver.find_element(id: 'revealed')
    driver.find_element(id: 'reveal').click

    errors = [Selenium::WebDriver::Error::NoSuchElementError,
              Selenium::WebDriver::Error::ElementNotInteractableError]
    wait = Selenium::WebDriver::Wait.new(timeout: 2,
                                         interval: 0.3,
                                         ignore: errors)

    wait.until { revealed.send_keys('Displayed') || true }

    expect(revealed.property(:value)).to eq('Displayed')
  end
end
```

Add Example

View Complete Code

View on GitHub

##### examples/kotlin/src/test/kotlin/dev/selenium/waits/WaitsTest.kt

Last modified October 31, 2025:

Added Kotlin Code Examples (#2499) (e49b07e4f68)
