app_name = "gdrive_notifier"
app_title = "GDrive Notifier"
app_publisher = "Your Company"
app_description = "Notify backup status to Uptime Kuma via Push URL"
app_email = "you@example.com"
app_license = "MIT"

scheduler_events = {
    "daily": [
        "gdrive_notifier.backup_check.check_backup_and_notify"
    ]
}
