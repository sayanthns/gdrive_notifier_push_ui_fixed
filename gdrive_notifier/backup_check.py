import frappe
import os
import requests
from datetime import datetime, timedelta

def check_backup_and_notify():
    backup_path = frappe.get_site_path('private', 'backups')
    latest_file = max(
        [os.path.join(backup_path, f) for f in os.listdir(backup_path) if f.endswith('.gz')],
        key=os.path.getctime,
        default=None
    )

    if not latest_file:
        return

    backup_time = datetime.fromtimestamp(os.path.getctime(latest_file))
    time_diff = datetime.now() - backup_time

    webhook_url = frappe.db.get_single_value("GDrive Notifier Settings", "kuma_webhook_url")

    if not webhook_url:
        return

    try:
        if time_diff > timedelta(hours=24):
            message = f"ERP Backup Alert: Last backup was {backup_time.strftime('%Y-%m-%d %H:%M:%S')}"
            requests.post(webhook_url, json={"status": "down", "msg": message})
        else:
            message = f"ERP Backup OK: Last backup was {backup_time.strftime('%Y-%m-%d %H:%M:%S')}"
            requests.post(webhook_url, json={"status": "up", "msg": message})
    except Exception as e:
        frappe.log_error(f"Kuma Push URL failed: {str(e)}", "GDrive Notifier")
