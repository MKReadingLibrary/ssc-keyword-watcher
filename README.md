# ssc-keyword-watcher

A simple monitor for the keyword `NR13123` on the SSC NR Phase XI results page.  
Built to run every ~2 minutes on Railway's cron job scheduler.

## 🚀 Deploy on Railway

1. **Deploy** this repository to Railway via the “Deploy on Railway” button.
2. In your Railway project, add environment variables:
   - `EMAIL_SENDER`: your Gmail address  
   - `EMAIL_PASSWORD`: your Gmail app password (not login password)
3. Configure the **Cron Schedule**:
