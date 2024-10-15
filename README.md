
# Pomodoro App

## Overview

This is a **Pomodoro App** built in Python, which helps users manage their work sessions using the **Pomodoro technique**. The app allows users to set durations for work and break sessions, tag sessions for categorization, track progress using a SQLite database, and export session data as CSV reports.

## Features

- **Work and Break Sessions**: Set the duration for Pomodoro work sessions and break intervals.
- **Session Tracking**: Track session data, including session number and optional tags, using SQLite.
- **CSV Export**: Export daily Pomodoro session data to a CSV file.
- **Timer Countdown**: Visual countdown for work and break sessions using ASCII art.
- **Notifications**: Chime sound notifications at the start and end of sessions.
- **Customizable Sessions**: Add a custom tag to each Pomodoro session for easy categorization.

## Technologies Used

- **Python 3.x**
- **SQLite**: For storing session information.
- **CSV**: For exporting session data.
- **PyFiglet**: For rendering the countdown in a stylish font.
- **Chime**: For sound notifications.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/pomodoro-app.git
   cd pomodoro-app
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scriptsctivate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python pomodoro_app.py
   ```

## Usage

1. Upon running the app, you will be prompted to:
   - Enter the duration of the Pomodoro work session (in minutes).
   - Optionally tag your Pomodoro session.
   - Enter the duration of the break session (in minutes).
   - Enter the number of sessions.

2. The app will start with a visual countdown using ASCII art and provide sound notifications for the start and end of each session and break.

3. After completing all sessions, the app will export the session data to a CSV file, named as `pomodoro_report_YYYY-MM-DD.csv`.

## Example

```bash
$ python pomodoro_app.py
```

You will be prompted for the following inputs:

- Work session duration in Minutes: `25`
- Break session duration in Minutes: `5`
- Number of Pomodoro sessions: `4`
- Tag your Pomodoro session (Optional): `Focus Study`

The app will then start the countdown for 4 Pomodoro sessions, each lasting 25 minutes, followed by a 5-minute break.

## Database

The session data is stored locally in an SQLite database named `pomodoro_sessions.db`. The structure of the `sessions` table is:

| Column         | Type    |
|----------------|---------|
| id             | INTEGER |
| session_date   | TEXT    |
| session_number | INTEGER |
| tag            | TEXT    |

## CSV Report

The CSV report generated contains the following columns:

| ID   | Date       | Session Number | Tag          |
|------|------------|----------------|--------------|
| 1    | 2024-10-15 | 1              | Focus Study  |
| 2    | 2024-10-15 | 2              | Focus Study  |

## Running Tests

The app uses `pytest` for unit testing. To run the tests, simply use:

```bash
pytest
```

Tests are provided for:

- Input validation
- Database initialization
- Session updates
- CSV export

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! If you'd like to contribute, please open a pull request or raise an issue.

---

### Acknowledgments

- This app uses `pyfiglet` for stylish terminal output and `chime` for notification sounds.
