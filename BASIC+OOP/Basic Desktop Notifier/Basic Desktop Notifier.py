import getpass
import datetime
from plyer import notification
username=getpass.getuser()
current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
notification.notify(
    title=f"Hello, {username}",
    message=f"Have a good day, the time is: {current_time}",
    app_name='Desktop Notifier',
    timeout=10
)

