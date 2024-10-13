# openai-webpage-summarizer

sign up for OpenAI
https://platform.openai.com/docs/overview

This Python project scrapes a website's content using BeautifulSoup, removes irrelevant tags (like scripts and images), and generates a short summary using the OpenAI API. It is particularly designed for extracting website content, analyzing it, and providing a concise summary in Markdown format.

## Features

- Web scraping: Fetch website content using requests and BeautifulSoup.
- Text processing: Remove unnecessary HTML tags like <script>, <style>, and images to focus on the main text.
- OpenAI API integration: Use OpenAI’s API to summarize the website's contents in a human-readable markdown format.
- Environment variables: Load and manage sensitive API keys using .env file.

## Requirements

- Python 3.6+
- Packages:
  - requests
  - beautifulsoup4
  - python-dotenv
  - openai

## Installation

Set up your .env file in the project root and add your OpenAI API key:
makefile

`OPENAI_API_KEY=your-openai-api-key`
