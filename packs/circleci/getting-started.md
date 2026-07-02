---
title: "Quickstart guide"
source: https://circleci.com/docs/getting-started/
domain: circleci
license: CC-BY-SA-4.0
tags: circleci pipeline, continuous integration, ci cd pipeline, build automation
fetched: 2026-07-02
---

# Quickstart guide

16 days ago

·

8 min read

Cloud

- View markdown

This quickstart provides a guided tour through setting up a project, collaborating, and tools to iterate on and debug your build configuration. The following sections cover the following:

- Create a project, connecting some existing code to CircleCI.
- Inviting team members to collaborate on your new project.
- Use the VS Code extension to debug and extend your config.
- SSH into a build to debug your project.

If you would rather jump to a full list of CircleCI `config.yml` options, see the Configuration Reference.

## Prerequisites

- A CircleCI account. You can sign up for free.
- A code repository you want to build on CircleCI.

|   | This guide assumes you have Signed Up and connected to GitHub, Bitbucket or GitLab |
|---|---|

**Check your project slug to discover which GitHub integration you have set up:**

1. Head to the CircleCI web app and select your org from the cards on your user homepage.
2. Select **Projects** from the sidebar and locate your project from the list. You can use the search to help.
3. Select the ellipsis menu (Ellipsis menu icon)(Ellipsis menu icon) next to your project and select **Project Settings**. The project slug is listed on the project settings homepage. **GitHub App**: Project slug starts with `circleci` followed by UUIDs. For example, `circleci/34R3kN5RtfEE7v4sa4nWAU/4nYdoKGkb6RXn7JGt8SQtg`. **GitHub OAuth app**: Project slug is human readable. For example, `github/circleci/circleci-demo-workflows`.

For more information about the differences, see the Version Control Systems, Pipeline Types, and Feature Support guide.

## 1. Connect your code

Figure 1. Connect your code

**Create a project, connect your new code repository, and commit a CircleCI configuration file. View your project build in the CircleCI app.**

- GitHub App
- GitLab & Bitbucket Data Center
- GitHub OAuth app & Bitbucket Cloud

(create project)

**Create a project** In the CircleCI web app select your org, then select **Create project**, then follow the instructions in the app.

If you do not see these options select the CircleCI logo in the top bar to get back to your user homepage and check you have the correct org selected.

(setup pipeline)

**Set up a pipeline** Follow the in-app instructions to set up your pipeline including connecting your code, preparing a config file and reviewing triggers.

For a more detailed look at this process see the Create a Project guide.

(commit and run)

**Commit and run** Once you have gone through the pipeline setup process in the app, you have everything you need to commit your config and build. If you already have a config in your repo, you do not need to commit a new one.

Review your project details and select **Commit config and run**.

(pass pipeline)

**Congratulations 🎉** You will soon have a passing pipeline.

In the next sections we will cover ways to modify and debug your config.

(create project)

**Create a project** In the CircleCI web app, select Projects from the sidebar. Select **Create project**, then select the repository you would like to connect from the dropdown.

If you do not see the org selector in the top left corner, navigate back to your user homepage to find the correct organization

(select config gitlab)

**Select a config.yml** In the "Select your config.yml file" modal, select **Fast**, then give your project a name, and select **Create Project**. If you are authenticated through the GitHub App, you also need to set up SSH access for your project at this point.

(change config gitlab)

**CircleCI config editor** You are now in the <a class="no-external-icon" CircleCI config editor, pre-populated with a sample `config.yml` file. You can swap out this config for an alternative by selecting **Change: Hello World**.

(commit run gitlab)

**Commit your config** Select **Commit and Run**. This will create a `.circleci/config.yml` file at the root of your repository on a new branch called `update-circleci-config`.

(pass pipeline)

**Congratulations** 🎉 You will soon have a passing pipeline. If you are happy with this configuration, merge it into your main branch, or continue to make changes.

(set up project)

**Set up a project** In the CircleCI web app select your org, then select **Set up a Project**, then select **Set up Project** next to your project in the list.

If you do not see these options, select the CircleCI logo in the top bar to get back to your user homepage and check you have the correct org selected.

(select config)

**Select a config.yml** In the "Select your config.yml file" modal, select **Faster**, then click **Set Up Project**.

(pass pipeline)

**Congratulations** 🎉 You will soon have a passing pipeline. In the next sections we will cover ways to modify and debug your config.

## 2. Dig into your first pipeline

Figure 2. Dig into your first pipeline

**Explore your passing pipeline and invite your teammates to join you, for free. By collaborating, you can troubleshoot, get pull requests approved, and build and test faster.**

(steps)

**So, what just happened?** Expand your workflow and select a job to view the steps that ran. Use the tabs along the top to access test results, timing data, artifacts, and resource usage metrics.

(expand step)

**View step output** Expand any step to view the build output. You can search, share or download the output for collaboration and debugging. If a step fails, use the Explain This Error button for help.

(invite)

**Invite teammates** Invite teammates to collaborate on your projects. Navigate to   **People** to generate invites and get further instructions. Collaborators can view and follow your projects. Teammates can make a free CircleCI account at any time to view your pipelines, even if they are not committing any code.

## 3. Debug and iterate

Figure 3. Debug and iterate

**Discover CircleCI features to help debug and configure your builds.**

(ssh rerun)

**Rerun with SSH** To access a job’s build environment for troubleshooting, rerun the job with SSH access. The VM remains active for 10 minutes after the pipeline finishes. For full details, see the Debug With SSH page.

(validate config)

**VS Code extension** Using the CircleCI VS Code Extension, validate your CircleCI config file. Get help with troubleshooting config updates and help keeping dependencies up to date.

## Next steps

- CircleCI foundation videos
- Introduction to Configuration
- CircleCI Concepts
- CircleCI Plans Overview
