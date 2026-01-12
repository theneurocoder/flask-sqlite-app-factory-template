# Documentation
## Overview
This template provides a minimal, opinionated starting point for building small Flask applications using SQLite. It focuses on clear structure, simple configuration, and a lightweight database setup. It intentionally does not include authentication, migrations, background jobs, or production deployment tooling. The goal is to give you a clean foundation that is easy to understand, modify, and extend, rather than a fully featured application.

## Requirements
The template requires Python 3.10 or newer and pip for dependency management. A virtual environment is strongly recommended to isolate dependencies, but not strictly required. No external database server is needed, as the template uses SQLite.

## Important Note
If `pip`, `flask`, and `pytest` are not available as direct commands on your system, use the module form instead:
- `pip` becomes `python3 -m pip`
- `flask` becomes `python3 -m flask`
- `pytest` becomes `python3 -m pytest`

## Installation
After downloading the template, create and activate a virtual environment, then install the dependencies by running `pip install -r requirements.txt`.

## Testing
This template includes a basic test that verifies app setup and SQLite persistence. To run the test in the shell: `pytest -s`. The test prints a message at each step, ending with `"Test completed."`

## Database Initialization
You can initialize the database manually by running `flask init-db`. This creates the database file defined by `DATABASE` in `config.py` and initializes a `notes` table.

The database can also be initialized automatically at application startup if the database file does not already exist. This is intended for deployments hosted on services with no access to a shell.

Data persistence in production requires mounting a persistent volume and configuring the database path to point to that volume.

## Running the Development Server
### Primary (recommended):
Use `flask run` during development. This respects Flask configuration, environment variables, and CLI commands.

### Alternative:
Use `python3 main.py` as a simple entry point. This runs the server on port 5000. If port 5000 is already in use on your system, update the port value in `main.py` to an available port, for example: `port=5001`.

Once running, the app will be available at `http://127.0.0.1:<port>`, where `<port>` is the port the server is started on. If running on a hosted environment, use the platform-provided preview URL.

## Environment Configuration
Environment-specific settings are managed using environment variables. `.env.example` documents the variables. You must copy or rename this file to `.env` and update the values as needed for your environment. The `.env` file is not committed to version control and is intended for local configuration only.

## Structure
This template is organized to separate configuration, routing, database logic, and templates. Application routes are defined in `routes.py`, database access is handled in `db.py`, and configuration is managed in `config.py`. HTML templates live in the `templates/` directory. This structure is intended to keep concerns isolated and make it clear where new features or files should be added.

## Adding New Features 
To add new features, new routes must be defined in `routes.py`, following the existing patterns. Database changes or new queries must be added in `tables.py`, and new HTML templates must be created in the `templates/` directory. If a feature requires configuration, document the required environment variables in `.env.example` and set their values in `.env`, then access them through `config.py`.

## Notes Example
### Purpose
The notes example is included as a reference implementation that demonstrates how the template is intended to be used. It shows a minimal feature built on top of the core structure, and is meant to be read, modified, or removed.

The example implements basic data creation and retrieval operations for notes, stored in a SQLite table. It demonstrates how routes, database queries, and templates work together within the template's structure.

### How to remove or replace the example
The notes example can be safely deleted once you understand how it works. Remove the notes-related routes in `routes.py`, the `notes` table definition in `tables.py`, and the block for the notes in `index.html`, and the rest of the template will continue to function. Alternatively, you can rename or adapt the existing files and reuse them as the starting point for your own feature.

## What Is Safe to Change
You are expected to modify `routes.py`, `tables.py`, and the files in the `templates/` directory to build your application. You can also update `.env` and extend `.env.example` when adding new configuration. Core wiring files such as `main.py`, `config.py`, and `db.py` should generally be left unchanged unless you understand how they are used by the application.

## License and Support
This template is provided under the included license file and is offered as-is, without guarantees or ongoing support. You are free to modify and use it for your own projects in accordance with the license terms.

Created by TheNeuroCoder. For more information about the developer: [neurocoder.io](https://neurocoder.io)
