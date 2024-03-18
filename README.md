YT link:  ....


# Summarizer and Keyword Extractor App 
## Setup Guide

This guide will help you set up and run the Streamlit application on your local machine.

## Step 1: Obtain API Keys

You will need to obtain the following API keys:

- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`

Once you have your keys, you will need to set them as environment variables. Open a terminal or command prompt and run the following commands:

```bash
export ANTHROPIC_API_KEY=your_anthropic_api_key_here
export OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_anthropic_api_key_here` and `your_openai_api_key_here` with your actual API keys.

## Step 2: Install Dependencies

The application requires certain Python packages to run. These dependencies are listed in a `requirements.txt` file.
Navigate to the root directory of the project in your terminal or command prompt and run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```


## Step 3: Run the Application

After installing the dependencies, you can run the application using Streamlit. In the terminal or command prompt, run the following command:

```bash
streamlit run app.py
```


This command starts the Streamlit server and opens the application in your default web browser.

## Troubleshooting

If you encounter any issues during the setup or while running the application, ensure that:

- You have correctly set the API keys as environment variables.
- All dependencies are installed correctly.
- You are running the commands in the project's root directory.
