# GDrive Notifier

Custom ERPNext app that sends push status to Uptime Kuma after daily backup.

## Features

- Monitors private/backups for `.gz` files
- Sends "up" or "down" to a Push URL
- Includes a Doctype UI to set the Push URL

## Setup

1. Install the app:
```bash
bench get-app /path/to/gdrive_notifier_push_ui_fixed.zip
bench --site your-site-name install-app gdrive_notifier
```

2. Open ERPNext > GDrive Notifier Settings and enter your Uptime Kuma Push URL

3. Make sure scheduler is enabled:
```bash
bench --site your-site-name enable-scheduler
```
