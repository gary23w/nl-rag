---
title: "Get started"
source: https://docs.soda.io/soda/quick-start-sip.html
domain: soda-data-quality
license: CC-BY-SA-4.0
tags: soda core, data quality testing, data reliability, soda checks language
fetched: 2026-07-02
---

# Get started

For the complete documentation index, see

llms.txt

. This page is also available as

Markdown

.

# Get started

Follow this tutorial to set up and run a simple Soda scan for data quality using example data.

The Soda environment has been updated since this tutorial.

> Refer to for updated tutorials.

Is Soda the data quality testing solution you've been looking for? Take a sip and see! 🫧

Use the example data in this quick tutorial to set up and run a simple Soda scan for data quality.

| 3 minutes | 2 minutes | 5 minutes | 5 minutes

> 💡 For standard set up instructions, access the .
> 
> ✨ Want a total UI experience? Use the out-of-the-box to skip the CLI.

## Set up Soda

This tutorial references a MacOS environment.

1. Check the following prerequisites:

- You have installed Python 3.8, 3.9, or 3.10.
- You have installed Pip 21.0 or greater.
- (Optional) You have installed and have access to , to set up an example data source.

1. Contact us at to get an account set up.
2. In your command-line interface, create a Soda project directory in your local environment, then navigate to the directory.

1. Best practice dictates that you install the Soda using a virtual environment. In your command-line interface, create a virtual environment in the `.venv` directory, then activate the environment.

1. Execute the following command to install the Soda package for PostgreSQL in your virtual environment. The example data is in a PostgreSQL data source, but there are 15+ data sources with which you can connect your own data beyond this tutorial.

1. Validate the installation.

To exit the virtual environment when you are done with this tutorial, use the command `deactivate`.

## Build an example data source

To enable you to take a first sip of Soda, you can use Docker to quickly build an example PostgreSQL data source against which you can run scans for data quality. The example data source contains data for AdventureWorks, an imaginary online e-commerce organization.

- (Optional) Access the repository in GitHub.
- (Optional) Access a quick view of the .

1. Open a new tab in Terminal.
2. If it is not already running, start Docker Desktop.
3. Run the following command in Terminal to set up the prepared example data source.

When the output reads `data system is ready to accept connections`, your data source is set up and you are ready to proceed.

Troubleshoot

**Problem:** When you run `docker-compose up` you get an error that reads `[17168] Failed to execute script docker-compose`.

**Solution:** Start Docker Desktop running.

**Problem:** When you run `docker-compose up` you get an error that reads `Cannot start service soda-adventureworks: Ports are not available: exposing port TCP 0.0.0.0:5432 -> 0.0.0.0:0: listen tcp 0.0.0.0:5432: bind: address already in use`.

**Solution:**1. Execute the command `lsof -i tcp:5432` to print a list of PIDs using the port. 2. Use the PID value to run the following command to free up the port: `kill -9 your_PID_value`. You many need to prepend the commands with `sudo`. 3. Run the `docker run` command again.

Alternatively, you can use your own data for this tutorial. To do so:

1. Skip the steps above involving Docker.
2. Install the Soda Library package that corresponds with your data source, such as `soda-bigquery`, `soda-athena`, etc. See full list.
3. Collect your data source's login credentials that you must provide to Soda so that it can scan your data for quality.
4. Move on to .

## Connect Soda

To connect to a data source such as Snowflake, PostgreSQL, Amazon Athena, or GCP BigQuery, you use a `configuration.yml` file which stores access details for your data source.

This tutorial also instructs you to connect to a Soda Cloud account using API keys that you create and add to the same `configuration.yml` file. Available for free as a 45-day trial, your Soda Cloud account validates your free trial or license, gives you access to visualized scan results, tracks trends in data quality over time, lets you set alert notifications, and much more.

1. In a code editor such as Sublime or Visual Studio Code, create a new file called `configuration.yml` and save it in your `soda_sip` directory.
2. Copy and paste the following connection details into the file. The `data_source` configuration details connect Soda to the example AdventureWorks data source you set up using Docker. If you are using your own data, provide the `data_source` values that correspond with your own data source.
3. In your Soda account, navigate to **your avatar** > **Profile**, then access the **API keys** tab. Click the plus icon to generate new API keys. Copy+paste the `soda_cloud` configuration syntax, including the API keys, into the `configuration.yml` file, as in the example below.
4. Save the `configuration.yml` file and close the API modal in your Soda account.
5. In Terminal, return to the tab in which the virtual environment is active in the `soda_sip` directory. Run the following command to test Soda's connection to the data source. Command:

Output:

## Write some checks and run a scan

1. Create another file in the `soda_sip` directory called `checks.yml`. A check is a test that Soda executes when it scans a dataset in your data source. The `checks.yml` file stores the checks you write using the Soda Checks Language (SodaCL).
2. Open the `checks.yml` file in your code editor, then copy and paste the following checks into the file.

What do these checks do?

- **Ensure values are formatted as email addresses** checks that all entries in the `email_address` column are formatted as `name@domain.extension`. See .
- **Ensure there are no null values in the Last Name column** automatically checks for NULL values in the `last_name` column. See .
- **No duplicate phone numbers** validates that each value in the `phone` column is unique. See .
- **Columns have not been added, removed, or changed** compares the schema of the dataset to the last scan result to determine if any columns were added, deleted, changed data type, or changed index. The first time this check executes, the results show `[NOT EVALUATED]` because there are no previous values to which to compare current results. In other words, this check requires a minimum of two scans to evaluate properly. See .
- **Data in this dataset is less than 7 days old** confirms that the data in the dataset is less than seven days old. See .

1. Save the changes to the `checks.yml` file, then, in Terminal, use the following command to run a scan. A scan is a CLI command which instructs Soda to prepare SQL queries that execute data quality checks on your data source. As input, the command requires:

- `-d` the name of the data source to scan
- `-c` the filepath and name of the `configuration.yml` file
- the filepath and name of the `checks.yml` file Command:

Output:

1. As you can see in the Scan Summary in the command-line output, some checks failed and Soda sent the results to your Cloud account. To access visualized check results and further examine the failed checks, return to your Soda account in your browser and click **Checks**.
2. In the table of checks that Soda displays, you can click the line item for one of the checks that failed to examine the visualized results in a line graph, and to access the failed row samples that Soda automatically collected when it ran the scan and executed the checks. Use the failed row samples, as in the example below, to determine what caused a data quality check to fail.

✨Well done!✨ You've taken the first step towards a future in which you and your colleagues can trust the quality and reliability of your data. Huzzah!

If you are done with the example data, you can delete it from your account to start fresh with your own data.

1. Navigate to **your avatar** > **Data Sources**.
2. In the **Data Sources** tab, click the stacked dots to the right of the `adventureworks` data source, then select **Delete Data Source**.
3. Follow the steps to confirm deletion.
4. Connect to your own data by in your existing `configuration.yml` file. 5. Adjust your `checks.yml` to point to your own dataset in your data source, then adjust the checks to apply to your own data. Go ahead and run a scan!

## Go further

- Get inspired on how to set up Soda to meet your .
- Use check suggestions to quickly get off the ground with basic checks for data quality.
- Learn writing SodaCL checks.
- Read more about in general.
- Learn more about .

## Need help?

- What can Soda do for you? .
- Join the .

Previous

Soda v3 documentation

Next

Get started roadmap

Last updated 1 month ago

Was this helpful?
