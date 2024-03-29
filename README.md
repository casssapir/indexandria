# Indexandria

AI Copilot for Customer Support

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12.2 (or newer)
- pip (usually comes with Python)
- (optional) OpenAI API Key

### Setup

**1. Clone the Repository**

```
git clone https://github.com/casssapir/indexandria
```
**2. Activate the Virtual Environment**

In your IDE or Terminal, navigate to the project directory

```
cd path/to/your/project
```

Create a virtual environment named venv:
```
python3 -m venv venv
```
Activate the Virtual Environment
```
source venv/bin/activate
```

Your command prompt should now begin with ```(venv)``` indicating that you are now operating within the virtual environment.

**3. Install Required Packages**
```
pip install -r requirements.txt
```

**4. Create environment file**

Create a file in the root directory called ```.env```. Using the below template add in your API keys and other details.
```
OPENAI_API_KEY=your_openai_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
```


## Running Indexandria
- start the application
- run scripts
- execute tests

## Contributing
We welcome contributions to Indexandria! Please read our contribution guidelines for more information on how you can contribute to the project.

Make sure to update ```requirements.txt``` with any changes by running 
```
pip freeze > requirements.txt
```
