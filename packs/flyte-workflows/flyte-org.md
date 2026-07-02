---
title: "Flyte"
source: https://flyte.org/
domain: flyte-workflows
license: CC-BY-SA-4.0
tags: flyte platform, workflow orchestration, machine learning pipelines, kubernetes workflows
fetched: 2026-07-02
---

# Flyte

AI orchestration in pure Python. Open source and trusted by leading AI labs and Fortune 500 companies.

Try Flyte Devbox

Demo Flyte 2 in browser

Flyte 2 is available today locally. For distributed execution, try Flyte 1.

Copied to clipboard!

```python
"""Run durable agents with full observability"""

import random

import flyte
from agents import Agent, Runner
from flyteplugins.openai.agents import function_tool

env = flyte.TaskEnvironment(
    name="openai_agents_tools",
    resources=flyte.Resources(cpu=1, memory="250Mi"),
    image=flyte.Image.from_debian_base().with_pip_packages(
        "flyte", "flyteplugins-openai", "openai-agents",
    ),
    secrets=flyte.Secret("OPENAI_API_KEY", as_env_var="OPENAI_API_KEY"),
)

@function_tool
@env.task
async def get_weather(city: str) -> dict:
    """Get random weather data."""
    low = random.randint(-5, 25)
    high = low + random.randint(3, 10)
    conditions = random.choice([
        "Sunny", "Partly cloudy", "Overcast", "Light rain",
        "Heavy rain", "Thunderstorms", "Snowy", "Foggy",
        "Windy", "Sunny with wind", "Clear skies", "Hail",
    ])
    return {"city":city, "temperature_range": f"{low}-{high}C", "conditions": conditions}

agent = Agent(
    name="Weather agent",
    instructions="You are a helpful weather agent.",
    tools=[get_weather],
)

@env.task
async def main() -> str:
    result = await Runner.run(agent, input="What's the weather in Tokyo?")
    print(result.final_output)
    return result.final_output

#flyte run openai_agent.py agent --request "What is the weather in Tokyo, Japan?"
```

Copied to clipboard!

```python
"""Run high-throughout inference for generative AI."""
  
import base64
import torch

import flyte
import flyte.io
import flyte.report

env = flyte.TaskEnvironment(
    name="stable-diffusion",
    image=(
        flyte.Image.from_debian_base()
        .with_commands(["pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124"])
        .with_requirements("requirements.txt")
    ),
    resources=flyte.Resources(cpu=2, memory="8Gi", gpu=1),
)

@env.task(report=True)
async def generate(prompt: str, steps: int = 30) -> flyte.io.File:
    """Generate an image from a text prompt using Stable Diffusion."""
    from diffusers import AutoPipelineForText2Image

    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sdxl-turbo",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        variant="fp16" if device == "cuda" else None,
    ).to(device)

    image = pipe(prompt, num_inference_steps=steps, guidance_scale=0.0).images[0]

    path = "/tmp/output.png"
    image.save(path)

    with open(path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    await flyte.report.replace.aio(
        f"<h2>Stable Diffusion</h2>"
        f"<p><b>Prompt:</b> {prompt}</p>"
        f'<img src="data:image/png;base64,{img_b64}" style="max-width:512px" />'
    )
    await flyte.report.flush.aio()

    return await flyte.io.File.from_local(path)

#flyte run stable_diffusion.py generate --prompt "a cat astronaut floating in space, digital art"
```

Copied to clipboard!

```python
"""Run data ETL jobs at scale with modern frameworks."""
  
import duckdb
import pandas as pd

import flyte
import flyte.report

env = flyte.TaskEnvironment(
    name="duckdb-etl",
    image=flyte.Image.from_debian_base().with_pip_packages("duckdb", "pandas", "pyarrow"),
    resources=flyte.Resources(cpu=1, memory="1Gi"),
)

SAMPLE_CSV = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

@env.task
async def extract() -> pd.DataFrame:
    """Load raw data from a CSV source."""
    df = duckdb.sql(f"SELECT * FROM read_csv_auto('{SAMPLE_CSV}')").df()
    print(f"Extracted {len(df)} rows")
    return df

@env.task
async def transform(raw: pd.DataFrame) -> pd.DataFrame:
    """Aggregate survival stats by passenger class using DuckDB SQL."""
    summary = duckdb.sql("""
        SELECT
            Pclass AS passenger_class,
            COUNT(*) AS total,
            SUM(Survived) AS survived,
            ROUND(AVG(Survived) * 100, 1) AS survival_rate,
            ROUND(AVG(Fare), 2) AS avg_fare
        FROM raw
        GROUP BY Pclass
        ORDER BY Pclass
    """).df()
    print(summary.to_string(index=False))
    return summary

@env.task(report=True)
async def pipeline() -> pd.DataFrame:
    """Extract → Transform pipeline."""
    raw = await extract()
    summary = await transform(raw)

    await flyte.report.replace.aio(
        f"<h2>DuckDB ETL Results</h2>"
        f"<p>Processed {len(raw)} rows into {len(summary)} groups</p>"
        f"<h3>Survival by Passenger Class</h3>"
        f"{summary.to_html(index=False)}"
    )
    await flyte.report.flush.aio()

    return summary

#flyte run duckdb_etl.py pipeline
```

Trusted by thousands of AI builders

## Introducing Flyte 2

The most intuitive, developer-loved way to orchestrate AI workflows in open source. Now available for local execution.

### AI orchestration & runtime

Dynamically orchestrate complex, long-running, and agentic workflows with autoscaling and infrastructure awareness.

### Author in pure Python

Write workflows in actual Python, no need to learn a DSL. Write, test, and version workflows locally, then run them at scale.

### Durable by default

Build fault-tolerant, resilient workflows that retry automatically, pick up where they leave off, and make failures inconsequential.

## Choose your engine

### Flyte 2 OSS

Build durable AI/ML pipelines and agents with OSS.

Open-source

Build and scale dynamic AI/ML workflows using Flyte’s open-source platform and community.

Infra-aware orchestration

Author in pure Python to provision and scale resources for workflows.

Dynamic workflow execution

Workflows can make on-the-fly decisions at runtime with real-time logic, conditions, and retries.

Self-healing workflows

Workflows can autonomously recover from failures and continue where they left off.

Run locally

Test and debug tasks in your local environment using the same Python SDK that runs in production on Kubernetes.

Try now

### Union.ai

The enterprise Flyte platform. Build scalable AI and agents in your cloud.

Everything in Flyte 2 OSS, plus:

Massive scale at 50k+ actions/run

Massive scale and ultra-low latency to accelerate AI from experiment to production

Orchestrate, train, and serve

Orchestrate, deploy, and optimize AI/ML systems one unified platform.

Real-time inference

Serve performant agents and models with sub-second latency.

Live remote debugger

Debug remote tasks, line-by-line, on the actual infrastructure where your tasks run.

Reusable, warm-start containers

Achieve task startup time of <100ms by eliminating cold starts.

Observability

Get visibility into resource usage, data lineage, and versioning.

White-glove support

Get dedicated help from a team of expert AI engineers.

Try for free

Features

## Make your AI, ML, and agentic workflows fly.

Build dynamic, self-healing workflows in open source. Our infra-aware platform orchestrates data, models, & compute.

### Build in pure Python

Author dynamic, production workflows in pure Python. No DSL required.

Learn more

### Iterate intelligently

Develop and debug locally before deploying to production.

Learn more

### Recover & reproduce

Built-in caching and versioning ensure fast, repeatable runs.

Learn more

### Visualize

Render plots and visualize data with reports.

Learn more

### Deploy

Promote workflows to cloud or on-prem without infra complexities.

Learn more

### Adapt at runtime

Build truly agentic workflows with stateful execution with automatic failure recovery.

Learn more

### Scale

Autoscale compute dynamically to match workload demand.

Learn more

Integrations

## Expand your workflows with powerful integrations.

### Apache Spark

Run Spark jobs on ephemeral clusters.

### BigQuery

Query a BigQuery table.

### PyTorch Elastic v1

Pytorch-native multi-node distributed training.

### Ray

Connect to Ray cluster to perform distributed model training and hyperparameter tuning.

### Snowflake

Query a Snowflake service.

### Weights & Biases v1

Best in class ML/AI experiment- and inference-time tracking.

Explore Integrations

Community

## Ask questions, share ideas, and get advice.

Explore Community

Events

## Join us for events, workshops, and trainings.

Resources

## See the latest docs and articles.

### Spotify cuts quarterly forecast time in half with Flyte

Read case study ↗

### Wayve accelerates autonomous driving R&D with Flyte’s scalable orchestration

Read case study ↗

### Cradle accelerates ML development for protein design with Flyte

Read case study ↗

### Warner Bros. Discovery accelerates ML workflow delivery and reduces costs with Flyte

Read case study ↗

### Kineo accelerates AI delivery and cuts orchestration costs with Flyte

Read case study ↗

### MethaneSAT uses Flyte to orchestrate global methane reduction from space

Read case study ↗

### See Inside Your AI Tasks: Function-Level Visibility with Traces

Read article ↗

### Flyte MCP: give your local coding agent control-plane superpowers

Read article ↗

### Long horizon Agents on a Durable AI Runtime

Read article ↗

### Breach! How AI stacks are compromising data security.

Read article ↗

### Fan Out Tasks Like a Pro with Map Tasks

Read article ↗

### Use Cache to Stop re-running work in your pipelines

Read article ↗
