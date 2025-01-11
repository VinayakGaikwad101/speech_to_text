# Speech to Text Project

This project converts live human speech into text and saves it to a text file using the Vosk offline speech recognition library.

## Features

- Supports both Indian English and American English models.
- Recognizes and transcribes live speech.
- Adds a full stop after each recognized segment.
- Allows stopping the recording with the `Ctrl + Q` shortcut.

## Setup

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd speech_to_text_project
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **On Windows:**

     ```bash
     .\venv\Scripts\activate
     ```

   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the script:

   ```bash
   python speech_to_text.py
   ```

2. Choose the model:

   - Enter `1` for Indian English.
   - Enter `2` for American English.

3. Speak into your microphone. The recognized text will be printed to the terminal and saved in `output.txt`.

4. Press `Ctrl + Q` to stop the recording.

5. The audio is saved in the output.txt file in the root directory

## License

This project is licensed under the MIT License. See the LICENSE file for details.

```

```
