# Report Server

Simple Python HTTP server for serving CI/CD reports.

## Features

- Serves reports on port 9898
- Landing page with links to all reports
- Supports multiple report types (test results, lint reports, etc.)

## Usage

```bash
python server.py
```

Access at: http://localhost:9898

## Expected Directory Structure

```
/reports/
├── testresults/
│   └── index.html
├── lint/
│   └── index.html
└── server.py
```

## Used By

This server is designed to be cloned and used in multi-stage Docker builds for serving Android CI reports.