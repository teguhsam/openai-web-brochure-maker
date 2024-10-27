# AI-Powered Web Brochure Maker

Sign up for OpenAI
https://platform.openai.com/docs/overview

Sign up for Anthropic
https://www.anthropic.com/

This Python script scrapes a website, extracts useful links, and generates a short brochure about the company in Markdown format. The brochure includes details about the company, such as its culture, customers, and career opportunities, based on the content of relevant pages on the website. Users can choose between OpenAI's GPT model and Anthropic's Claude model to create the brochure, which is displayed in a Markdown format within the Gradio interface.

## Table of Contents

- [AI-Powered Web Brochure Maker](#ai-powered-web-brochure-maker)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example](#example)

## Features

- Web Scraping: Extracts the main text and relevant links from a website.
- Brochure Generation: Uses OpenAI or Anthropic's Claude to summarize and format content into a Markdown brochure.
- Interactive Interface with Gradio: Allows users to input a company name, landing page URL, and select a model (GPT or Claude).
- Markdown Display: The generated brochure is shown in Markdown format directly within the Gradio interface.

## Requirements

- Python 3.6+
- Packages:
  - requests
  - beautifulsoup4
  - python-dotenv
  - openai
  - anthropic
  - gradio

## Installation

Set up your .env file in the project root and add your OpenAI API key and Anthropic API key:

```
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

## Usage

1. Run the script and use the Gradio interface to enter the company name, website URL, and select a model (GPT or Claude).
2. The selected model will generate a brochure based on the website content.
3. The brochure will be displayed in Markdown format directly in the Gradio interface.

### Example

To create a brochure for Morningstar's website, input "Morningstar" as the company name, "https://www.morningstar.ca/ca/" as the URL, and choose a model. Then, run the script. The brochure will be displayed in the Gradio interface in Markdown format.

![Example](output_img.png)
