###### WIRIN System Design
API Handling + Request Resolution.  
   
This is the primary repository containing the working files of the system design files of the wirin project.

### Instructions to run : 
**This is a standard flask app, and hence requires all flask modules. Additionally, you will need to install python's datetime module if you don't already have it installed.**

To set up a virtual environment (venv) for your Flask app and install the required dependencies, follow these steps:

# Step 1: Set Up a Virtual Environment

1. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

   This will create a directory named `venv` in your project folder.

2. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

# Step 2: Create `requirements.txt`

Create a `requirements.txt` file in your project's root directory with the following content:

```plaintext
Flask
```

You do not need to add `datetime` or `threading` since they are part of Python's standard library.

# Step 3: Install Dependencies

With the virtual environment activated, run the following command to install all the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

# Step 4: Running the Flask App

To run your Flask app, ensure the virtual environment is activated and then use the following command:

```bash
flask run
```

If you need to specify the path to your Flask app, set the `FLASK_APP` environment variable:

- On Windows:

  ```
  set FLASK_APP=main_app.py
  flask run
  ```

- On macOS/Linux:

  ```
  export FLASK_APP=main_app.py
  flask run
  ```

